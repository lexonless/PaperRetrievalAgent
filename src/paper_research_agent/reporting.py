from __future__ import annotations

from datetime import datetime
from typing import Any

from .models import ResearchNoteOutput
from .normalization import normalize_string_list, normalize_text


def render_research_note_markdown(note: ResearchNoteOutput, *, project_slug: str, query: str) -> str:
    lines: list[str] = [
        f"# {note.note_title}",
        "",
        f"**Project:** `{project_slug}`",
        f"**Query:** {query}",
        f"**Generated At:** {datetime.now().isoformat(timespec='seconds')}",
        "",
    ]

    if note.project_focus:
        lines.extend(["## Project Focus", "", note.project_focus, ""])
    if note.retrieval_assessment:
        lines.extend(["## Retrieval Assessment", "", note.retrieval_assessment, ""])

    lines.extend(_render_list_section("## Search Scope", note.search_scope))
    lines.extend(["## Core Papers", ""])
    lines.extend(_render_paper_entries(note.core_papers, empty_message="_No core papers were selected._"))
    lines.extend(["", "## Supporting Papers", ""])
    lines.extend(_render_paper_entries(note.supporting_papers, empty_message="_No supporting papers were added._"))
    lines.append("")
    lines.extend(_render_list_section("## Local Context", note.local_context))
    lines.extend(_render_list_section("## Key Observations", note.key_observations))
    lines.extend(_render_list_section("## Open Questions", note.open_questions))
    lines.extend(_render_list_section("## Limitations", note.limitations))
    lines.extend(_render_list_section("## Next Steps", note.next_steps))
    return "\n".join(lines).rstrip() + "\n"


def build_trace_payload(state: dict[str, Any]) -> dict[str, Any]:
    project = state.get("project", {})
    request = state.get("request", {})
    retrieval = state.get("retrieval", {})
    note = state.get("note", {})
    run = state.get("run", {})
    return {
        "project_slug": project.get("slug", ""),
        "query": request.get("raw_query", ""),
        "prepared_query": request.get("prepared_query", ""),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "run_id": run.get("run_id", ""),
        "revision_count": retrieval.get("revision_count", 0),
        "forced_write": retrieval.get("forced_write", False),
        "stop_reason": run.get("stop_reason", ""),
        "artifacts": run.get("artifacts", {}),
        "errors": run.get("errors", []),
        "events": run.get("trace_events", []),
        "task_interpretation": retrieval.get("task_interpretation") or {},
        "final_state_summary": {
            "task_interpretation_present": retrieval.get("task_interpretation") is not None,
            "retrieval_present": retrieval.get("retrieval_output") is not None,
            "review_present": retrieval.get("review_output") is not None,
            "note_present": note.get("research_note_output") is not None,
        },
    }


def summarize_manifest_sources(manifest: dict[str, Any], *, max_items: int = 5) -> list[str]:
    sources = manifest.get("sources", []) if isinstance(manifest, dict) else []
    summaries: list[str] = []
    for item in sources[:max_items]:
        if not isinstance(item, dict):
            continue
        title = normalize_text(item.get("title", "")) or normalize_text(item.get("path", ""))
        if title:
            summaries.append(title)
    return summaries


def _render_list_section(header: str, items: Any) -> list[str]:
    lines = [header, ""]
    normalized_items = normalize_string_list(items)
    if not normalized_items:
        lines.extend(["_None._", ""])
        return lines
    lines.extend([f"- {item}" for item in normalized_items])
    lines.append("")
    return lines


def _render_paper_entries(items: list[Any], *, empty_message: str) -> list[str]:
    if not items:
        return [empty_message]

    lines: list[str] = []
    for index, item in enumerate(items, start=1):
        title = normalize_text(getattr(item, "title", "")) or f"Untitled Paper {index}"
        year = getattr(item, "year", "")
        source = normalize_text(getattr(item, "source", ""))
        link = normalize_text(getattr(item, "link", ""))
        contribution_summary = normalize_text(getattr(item, "contribution_summary", ""))
        relevance_note = normalize_text(getattr(item, "relevance_note", ""))
        evidence_note = normalize_text(getattr(item, "evidence_note", ""))

        heading = f"### {index}. {title}"
        if isinstance(year, int):
            heading += f" ({year})"
        elif str(year).strip():
            heading += f" ({year})"
        lines.extend([heading, ""])
        if source:
            lines.append(f"- **Source:** `{source}`")
        if link:
            lines.append(f"- **Link:** {link}")
        if contribution_summary:
            lines.append(f"- **Contribution:** {contribution_summary}")
        if relevance_note:
            lines.append(f"- **Why It Matters:** {relevance_note}")
        if evidence_note:
            lines.append(f"- **Evidence:** {evidence_note}")
        lines.append("")

    return lines[:-1] if lines and lines[-1] == "" else lines
