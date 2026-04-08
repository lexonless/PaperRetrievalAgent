from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import ThoughtEvent, ToolCallExecutionEvent, ToolCallRequestEvent

from .normalization import normalize_string_list


@dataclass(slots=True)
class SavedReport:
    report_path: Path
    report_content: str
    debug_path: Path
    debug_content: str


def save_markdown_report(task_result: TaskResult, query: str, output_dir: str = "reports") -> SavedReport:
    base_path = Path(output_dir)
    report_dir = base_path / "user_reports"
    debug_dir = base_path / "debug_traces"
    report_dir.mkdir(parents=True, exist_ok=True)
    debug_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = _slugify(query)[:60] or "query"
    report_path = report_dir / f"{timestamp}-{slug}.md"
    debug_path = debug_dir / f"{timestamp}-{slug}.md"

    report_content = format_final_report_as_markdown(task_result, query)
    debug_content = format_debug_trace_as_markdown(task_result, query)
    report_path.write_text(report_content, encoding="utf-8")
    debug_path.write_text(debug_content, encoding="utf-8")

    return SavedReport(
        report_path=report_path,
        report_content=report_content,
        debug_path=debug_path,
        debug_content=debug_content,
    )


def format_final_report_as_markdown(task_result: TaskResult, query: str) -> str:
    lines: list[str] = [f"**Generated At:** {datetime.now().isoformat(timespec='seconds')}"]
    if task_result.stop_reason:
        lines.append(f"**Stop Reason:** {task_result.stop_reason}")

    final_message = _latest_message_from_source(task_result, "WriterAgent")
    final_payload = _try_parse_json_content(getattr(final_message, "content", "")) if final_message is not None else None
    final_content = _stringify_content(getattr(final_message, "content", "")) if final_message is not None else ""

    if final_message is None:
        latest_reviewer = _latest_message_from_source(task_result, "ReviewerAgent")
        latest_retrieval = _latest_message_from_source(task_result, "RetrievalAgent")
        latest_planner = _latest_message_from_source(task_result, "PlannerAgent")
        latest_review_payload = _try_parse_json_content(getattr(latest_reviewer, "content", "")) if latest_reviewer is not None else None
        latest_review_decision = ""
        if isinstance(latest_review_payload, dict):
            latest_review_decision = str(latest_review_payload.get("decision", "")).upper()

        lines.extend(
            [
                "",
                "_No final writer report was produced before the run stopped._",
                "",
                "## Run Status",
                "",
                f"- Latest reviewer decision: `{latest_review_decision or 'UNKNOWN'}`",
                f"- Latest retrieval available: `{'yes' if latest_retrieval is not None else 'no'}`",
                f"- Latest planner available: `{'yes' if latest_planner is not None else 'no'}`",
            ]
        )
        return "\n".join(lines).rstrip() + "\n"

    rendered_report = _render_writer_payload_as_markdown(final_payload) if isinstance(final_payload, dict) else ""
    lines.extend(["", rendered_report or final_content or "_No final response was returned._"])
    return "\n".join(lines).rstrip() + "\n"


def format_debug_trace_as_markdown(task_result: TaskResult, query: str) -> str:
    review_decisions = _collect_review_decisions(task_result)
    tool_activity = _collect_tool_activity(task_result)
    planner_outputs = _collect_structured_outputs(task_result, "PlannerAgent")
    retrieval_outputs = _collect_structured_outputs(task_result, "RetrievalAgent")

    lines: list[str] = [
        "# Paper Search Debug Trace",
        "",
        f"**Query:** {query}",
        f"**Generated At:** {datetime.now().isoformat(timespec='seconds')}",
    ]
    if task_result.stop_reason:
        lines.append(f"**Stop Reason:** {task_result.stop_reason}")

    lines.extend(
        [
            "",
            "## Run Summary",
            "",
            f"- Stop reason: `{task_result.stop_reason or 'unknown'}`",
            f"- Total messages: `{len(task_result.messages)}`",
            f"- Planner JSON messages: `{len(planner_outputs)}`",
            f"- Retrieval JSON messages: `{len(retrieval_outputs)}`",
            f"- Review decisions seen: `{len(review_decisions)}`",
            f"- Tool activity events: `{len(tool_activity)}`",
            "",
            "## Planner Outputs",
            "",
        ]
    )

    if planner_outputs:
        for item in planner_outputs:
            lines.extend(
                [
                    f"### Planner Output {item['index']}",
                    "",
                    f"- Topic: `{item['summary']}`",
                    "",
                    "```json",
                    item["content"],
                    "```",
                    "",
                ]
            )
    else:
        lines.extend(["_No planner JSON outputs found._", ""])

    lines.extend(
        [
            "## Retrieval Outputs",
            "",
        ]
    )

    if retrieval_outputs:
        for item in retrieval_outputs:
            lines.extend(
                [
                    f"### Retrieval Output {item['index']}",
                    "",
                    f"- Summary: {item['summary']}",
                    "",
                    "```json",
                    item["content"],
                    "```",
                    "",
                ]
            )
    else:
        lines.extend(["_No retrieval JSON outputs found._", ""])

    lines.extend(
        [
            "## Review Decisions",
            "",
        ]
    )

    if review_decisions:
        for item in review_decisions:
            lines.extend(
                [
                    f"### Review {item['index']}",
                    "",
                    f"- Source: `{item['source']}`",
                    f"- Decision: `{item['decision']}`",
                    "",
                    "```text",
                    item["content"],
                    "```",
                    "",
                ]
            )
    else:
        lines.extend(["_No review decision messages found._", ""])

    lines.extend(["## Tool Activity", ""])
    if tool_activity:
        for item in tool_activity:
            lines.extend(
                [
                    f"### Tool Event {item['index']}",
                    "",
                    f"- Source: `{item['source']}`",
                    f"- Type: `{item['event_type']}`",
                    f"- Summary: {item['summary']}",
                    "",
                    "```text",
                    item["content"],
                    "```",
                    "",
                ]
            )
    else:
        lines.extend(["_No tool activity events found._", ""])

    lines.extend(["## Message Trace", ""])
    for index, message in enumerate(task_result.messages, start=1):
        source = getattr(message, "source", "unknown")
        message_type = type(message).__name__
        content = _stringify_content(getattr(message, "content", ""))
        extra = _message_extra_summary(message)
        lines.extend(
            [
                f"### Message {index}",
                "",
                f"- Source: `{source}`",
                f"- Type: `{message_type}`",
                f"- Summary: {extra}",
                "",
                "```text",
                content or "<empty>",
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _stringify_content(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, (list, tuple)):
        return "\n".join(_stringify_content(item) for item in content if item is not None).strip()
    if isinstance(content, dict):
        return json.dumps(content, ensure_ascii=False, indent=2)
    return str(content).strip()


def _slugify(value: str) -> str:
    normalized = re.sub(r"\s+", "-", value.strip().lower())
    normalized = re.sub(r"[^a-z0-9\-_]+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    return normalized


def _collect_review_decisions(task_result: TaskResult) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for index, message in enumerate(task_result.messages, start=1):
        source = getattr(message, "source", "")
        if source != "ReviewerAgent":
            continue
        content = _stringify_content(getattr(message, "content", ""))
        decision = "UNKNOWN"
        payload = _try_parse_json_content(getattr(message, "content", ""))
        if isinstance(payload, dict):
            decision = str(payload.get("decision", "UNKNOWN")).upper()
        items.append(
            {
                "index": str(index),
                "source": source,
                "decision": decision,
                "content": content or "<empty>",
            }
        )
    return items


def _collect_tool_activity(task_result: TaskResult) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for index, message in enumerate(task_result.messages, start=1):
        if isinstance(message, ToolCallRequestEvent):
            summary = _summarize_tool_request(message)
        elif isinstance(message, ToolCallExecutionEvent):
            summary = _summarize_tool_execution(message)
        else:
            continue
        items.append(
            {
                "index": str(index),
                "source": getattr(message, "source", "unknown"),
                "event_type": type(message).__name__,
                "summary": summary,
                "content": _stringify_content(getattr(message, "content", "")) or "<empty>",
            }
        )
    return items


def _message_extra_summary(message: Any) -> str:
    if isinstance(message, ToolCallRequestEvent):
        return _summarize_tool_request(message)
    if isinstance(message, ToolCallExecutionEvent):
        return _summarize_tool_execution(message)
    if isinstance(message, ThoughtEvent):
        return "Agent thought/reasoning event"
    if getattr(message, "source", "") == "ReviewerAgent":
        payload = _try_parse_json_content(getattr(message, "content", ""))
        if isinstance(payload, dict):
            decision = str(payload.get("decision", "UNKNOWN")).upper()
            scores = payload.get("scores", {})
            if isinstance(scores, dict):
                total = sum(value for value in scores.values() if isinstance(value, int))
                return f"Structured review decision: {decision}, total_score={total}"
            return f"Structured review decision: {decision}"
    if getattr(message, "source", "") == "PlannerAgent":
        payload = _try_parse_json_message(message)
        if isinstance(payload, dict):
            topic = str(payload.get("topic", "unknown"))
            queries = payload.get("queries", [])
            query_count = len(queries) if isinstance(queries, list) else 0
            time_range = payload.get("time_range", {})
            if isinstance(time_range, dict):
                start_year = time_range.get("start_year", "?")
                end_year = time_range.get("end_year", "?")
                return f"Structured planner output: topic={topic}, queries={query_count}, years={start_year}-{end_year}"
            return f"Structured planner output: topic={topic}, queries={query_count}"
    if getattr(message, "source", "") == "RetrievalAgent":
        payload = _try_parse_json_message(message)
        if isinstance(payload, dict):
            papers = payload.get("papers", [])
            paper_count = len(papers) if isinstance(papers, list) else 0
            sources = payload.get("sources_used", [])
            source_count = len(sources) if isinstance(sources, list) else 0
            supported_evidence_count = _count_supported_evidence_candidates(payload)
            in_range_count = _count_in_range_papers(payload)
            return (
                f"Structured retrieval output: papers={paper_count}, sources={source_count}, "
                f"supported_evidence={supported_evidence_count}, in_range={in_range_count}"
            )
    content = _stringify_content(getattr(message, "content", ""))
    single_line = content.splitlines()[0] if content else "No content"
    return single_line[:120]


def _summarize_tool_request(message: ToolCallRequestEvent) -> str:
    names = [getattr(call, "name", "unknown_tool") for call in message.content]
    return f"Requested {len(names)} tool call(s): {', '.join(names)}"


def _summarize_tool_execution(message: ToolCallExecutionEvent) -> str:
    names = [getattr(result, "name", "unknown_tool") for result in message.content]
    return f"Executed {len(names)} tool call(s): {', '.join(names)}"


def _try_parse_json_message(message: Any) -> dict | None:
    return _try_parse_json_content(getattr(message, "content", ""))


def _try_parse_json_content(content: Any) -> dict | None:
    if isinstance(content, dict):
        return content
    if not isinstance(content, str):
        return None
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def _latest_message_from_source(task_result: TaskResult, source_name: str) -> Any | None:
    for message in reversed(task_result.messages):
        if getattr(message, "source", "") == source_name:
            return message
    return None


def _render_writer_payload_as_markdown(payload: dict[str, Any]) -> str:
    title = str(payload.get("report_title", "")).strip() or "Paper Search Report"
    report_type = str(payload.get("report_type", "")).strip().lower()
    query_understanding = str(payload.get("query_understanding", "")).strip()
    candidate_intro = str(payload.get("candidate_section_intro", "")).strip()

    lines: list[str] = [f"# {title}", ""]

    if query_understanding:
        lines.extend(["## Query Understanding", "", query_understanding, ""])

    lines.extend(_render_list_section("## Search Strategy", payload.get("search_strategy")))

    lines.extend(["## Candidate Papers", ""])
    if candidate_intro:
        lines.extend([candidate_intro, ""])

    if report_type == "failure":
        lines.extend(["### Verified Candidates", ""])
        lines.extend(_render_candidate_list(payload.get("verified_candidates"), empty_message="_None._"))
        lines.extend(["", "### Unverified Leads", ""])
        lines.extend(_render_candidate_list(payload.get("unverified_leads"), empty_message="_None._"))
        lines.append("")
    else:
        lines.extend(_render_candidate_list(payload.get("candidate_papers"), empty_message="_No candidate papers were provided._"))
        lines.append("")

    lines.extend(_render_list_section("## Notes and Gaps", payload.get("notes_and_gaps")))
    lines.extend(_render_list_section("## Recommended Next Steps", payload.get("recommended_next_steps")))
    return "\n".join(lines).rstrip()


def _render_list_section(header: str, items: Any) -> list[str]:
    lines = [header, ""]
    normalized_items = normalize_string_list(items)
    if not normalized_items:
        lines.extend(["_None._", ""])
        return lines
    lines.extend([f"- {item}" for item in normalized_items])
    lines.append("")
    return lines


def _render_candidate_list(items: Any, *, empty_message: str) -> list[str]:
    if not isinstance(items, list) or not items:
        return [empty_message]

    lines: list[str] = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            continue
        title = str(item.get("title", "")).strip() or f"Untitled Candidate {index}"
        year = item.get("year")
        source = str(item.get("source", "")).strip()
        link = str(item.get("link", "")).strip()
        summary = str(item.get("summary", "")).strip()
        why_included = str(item.get("why_included", "")).strip()

        title_line = f"### {index}. {title}"
        if isinstance(year, int):
            title_line += f" ({year})"
        lines.extend([title_line, ""])

        metadata_parts: list[str] = []
        if source:
            metadata_parts.append(f"**Source:** `{source}`")
        if link:
            metadata_parts.append(f"**Link:** [Open paper]({link})")
        if metadata_parts:
            lines.extend([f"- {part}" for part in metadata_parts])
        if summary:
            lines.append(f"- **Summary:** {summary}")
        if why_included:
            lines.append(f"- **Why Included:** {why_included}")
        lines.append("")

    return lines[:-1] if lines and lines[-1] == "" else lines
def _collect_structured_outputs(task_result: TaskResult, source_name: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for index, message in enumerate(task_result.messages, start=1):
        if getattr(message, "source", "") != source_name:
            continue
        payload = _try_parse_json_message(message)
        if payload is None:
            continue
        summary = _structured_summary(source_name, payload)
        items.append(
            {
                "index": str(index),
                "summary": summary,
                "content": json.dumps(payload, ensure_ascii=False, indent=2),
            }
        )
    return items


def _structured_summary(source_name: str, payload: dict) -> str:
    if source_name == "PlannerAgent":
        topic = str(payload.get("topic", "unknown"))
        queries = payload.get("queries", [])
        query_count = len(queries) if isinstance(queries, list) else 0
        time_range = payload.get("time_range", {})
        if isinstance(time_range, dict):
            start_year = time_range.get("start_year", "?")
            end_year = time_range.get("end_year", "?")
            return f"{topic} ({query_count} queries, {start_year}-{end_year})"
        return f"{topic} ({query_count} queries)"
    if source_name == "RetrievalAgent":
        papers = payload.get("papers", [])
        sources = payload.get("sources_used", [])
        paper_count = len(papers) if isinstance(papers, list) else 0
        source_count = len(sources) if isinstance(sources, list) else 0
        supported_evidence_count = _count_supported_evidence_candidates(payload)
        in_range_count = _count_in_range_papers(payload)
        return f"{paper_count} papers from {source_count} sources, supported_evidence={supported_evidence_count}, in_range={in_range_count}"
    return "Structured output"


def _count_supported_evidence_candidates(payload: dict) -> int:
    papers = payload.get("papers", [])
    if not isinstance(papers, list):
        return 0
    count = 0
    for paper in papers:
        if not isinstance(paper, dict):
            continue
        verification_status = str(paper.get("verification_status", "")).strip().lower()
        evidence_level = str(paper.get("evidence_level", "")).strip().lower()
        time_range_status = str(paper.get("time_range_status", "")).strip().lower()
        evidence_snippets = paper.get("evidence_snippets")
        if (
            verification_status in {"verified", "partial"}
            and evidence_level in {"abstract", "excerpt"}
            and time_range_status == "in_range"
            and isinstance(evidence_snippets, list)
            and any(str(item).strip() for item in evidence_snippets)
        ):
            count += 1
    return count


def _count_in_range_papers(payload: dict) -> int:
    papers = payload.get("papers", [])
    if not isinstance(papers, list):
        return 0
    count = 0
    for paper in papers:
        if not isinstance(paper, dict):
            continue
        if str(paper.get("time_range_status", "")).strip().lower() == "in_range":
            count += 1
    return count
