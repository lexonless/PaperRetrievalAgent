from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool

from .agent.reader import read_papers
from .core.config import Settings
from .core.llm import build_chat_model
from .feeder_store import (
    list_batches,
    load_batch_json,
    parse_metadata_papers,
)
from .materializer import write_text_artifact
from .synthesis.engine import SynthesisEngine, build_synthesis_context

logger = logging.getLogger(__name__)

ORCHESTRATOR_SYSTEM_PROMPT = """You are an academic research assistant. Based on the user's needs, autonomously decide which tools to call to complete the task.

## Available Tools

1. **discover_papers**: Search for academic papers. Takes a research topic as input, returns search result summary. May only be called once.
2. **synthesize_report**: Generate a Chinese research report from existing paper data. Requires paper data in the project directory.
3. **get_project_status**: Check the current project status (paper count, batch info, whether a report already exists, etc.).
4. **read_papers**: Read downloaded PDF papers and return structured understanding (problem statement, method, contributions, results, limitations). Can read a single paper or all papers in the project.

## Decision Rules

- User wants to **research a new topic** → first call get_project_status, if no data then discover_papers, then synthesize_report
- User **already has paper data, needs a report** → first call get_project_status to confirm data exists, then synthesize_report
- User **asks about project progress** → only call get_project_status

## Notes

- discover_papers iterates internally until convergence; only call it once
- synthesize_report works regardless of whether discover_papers converged.
  If converged=false, the report will honestly note limitations and research
  gaps. Papers found are still valuable — generate the report with available data.
- Provide a brief summary to the user at the end.
"""


def _build_discover_papers_tool(settings: Settings, output_root: str) -> Any:
    @tool
    async def discover_papers(query: str, project: str) -> str:
        """Search academic papers and download PDFs. Provide a research query and project name; searches across arXiv/Crossref/OpenAlex.

        Args:
            query: Research question or search keywords (required)
            project: Project name/slug (required)
        """
        from .agent import PaperDiscoveryAgent

        agent = PaperDiscoveryAgent(settings, output_root=output_root)
        try:
            batch, batch_path = await agent.discover(
                project_slug=project, query=query
            )
            return _format_discover_result(batch, batch_path, project, Path(output_root).resolve())
        finally:
            await agent.close()

    return discover_papers


def _format_discover_result(batch: dict, batch_path: Path, project: str, root: Path) -> str:
    rows: list[str] = []

    selected = batch.get("selected_count", 0)
    candidates = batch.get("candidate_count", 0)

    rows.append("Search results:")
    rows.append(f"  Candidates: {candidates} → Retained: {selected}")
    rows.append(f"  Batch: {batch_path}")

    iterations = batch.get("iterations", 0)
    converged = batch.get("converged", False)
    if iterations:
        rows.append(f"  Internal iterations: {iterations}/3 rounds, converged: {'Yes' if converged else 'No'}")

    review_log = batch.get("review_log") or []
    if review_log:
        for rl in review_log:
            rows.append(f"    Round {rl.get('iteration', '?')}: reviewed {rl.get('reviewed_count', 0)} papers, "
                        f"converged={rl.get('converged', False)}, "
                        f"reason=\"{rl.get('convergence_reason', '')}\"")
    else:
        rows.append("    (No LLM review; insufficient papers or low scores)")

    executed = batch.get("executed_queries") or []
    if executed:
        rows.append("  Search directions:")
        seen_directions: set[str] = set()
        for eq in executed:
            q = eq.get("query", "")
            purpose = eq.get("purpose", "")
            direction = f"\"{q}\"" + (f" ({purpose})" if purpose else "")
            if direction not in seen_directions:
                seen_directions.add(direction)
                rows.append(f"    - {direction}")

    total_papers = len(parse_metadata_papers(root, project))
    rows.append(f"")
    rows.append(f"Cumulative project paper count: {total_papers}")

    suggestion = _build_suggestion(converged, total_papers, iterations)
    rows.append(f"Suggestion: {suggestion}")

    return "\n".join(rows)


def _build_suggestion(converged: bool, total_papers: int, iterations: int) -> str:
    if converged and total_papers >= 3:
        return "Search converged. Recommend calling synthesize_report to generate report."
    if not converged and iterations >= 6:
        return "Maximum iterations reached. Recommend calling synthesize_report to generate report."
    if total_papers < 3:
        return "Too few papers. Suggest trying a different angle."
    return "Ready to call synthesize_report."


def _build_synthesize_report_tool(settings: Settings, output_root: str) -> Any:
    @tool
    async def synthesize_report(project: str) -> str:
        """Generate a research report from existing paper data.

        Works regardless of search convergence status — when data is
        partial or unconverged, the report will honestly note limitations
        and research gaps. The report is saved as project/report.md.

        Args:
            project: Project name/slug (required)
        """
        root = Path(output_root).resolve()
        ctx = build_synthesis_context(root, project)
        papers = ctx["papers"]
        if not papers:
            return f"No paper data found in project {project}. Please use discover_papers first."

        await read_papers(project=project, paper_slug="", output_dir=output_root)
        logger.info("synthesize_report: pre-read completed for project=%s", project)

        engine = SynthesisEngine(settings)
        report = await engine.synthesize(
            papers=papers,
            query=ctx["query"] or "Unspecified query",
            project_slug=project,
            output_root=output_root,
            decomposition=ctx["decomposition"],
            review_stats=ctx["review_stats"],
            converged=ctx.get("converged"),
        )

        report_dir = root / project
        report_dir.mkdir(parents=True, exist_ok=True)
        report_path = report_dir / "report.md"
        write_text_artifact(report_path, report)

        return (
            f"Research report generated.\n"
            f"- Report path: {report_path}\n"
            f"- Papers cited: {len(papers)}\n"
            f"- Report length: {len(report)} chars"
        )

    return synthesize_report


def _build_get_project_status_tool(output_root: str) -> Any:
    @tool
    def get_project_status(project: str) -> str:
        """Check the current project status. Returns paper count, batch list, whether a report already exists, etc.

        Args:
            project: Project name/slug (required)
        """
        root = Path(output_root).resolve()
        project_dir = root / project
        if not project_dir.is_dir():
            return f"Project {project} does not exist. Create the project first."

        papers = parse_metadata_papers(root, project)
        batches = list_batches(root, project)
        report_exists = (project_dir / "report.md").is_file()

        lines = [
            f"Project {project} status:",
            f"- Paper metadata files: {len(papers)}",
            f"- Batch records: {len(batches)}",
            f"- Research report: {'Exists' if report_exists else 'Not generated'}",
        ]

        if batches:
            latest = batches[0]
            lines.append(f"- Latest batch: {latest.name}")
            try:
                data = load_batch_json(latest)
                lines.append(f"- Latest batch query: {data.get('query', 'Unknown')}")
            except Exception:
                pass

        return "\n".join(lines)

    return get_project_status


class ResearchOrchestrator:
    def __init__(self, settings: Settings, *, output_root: str = "projects") -> None:
        self._settings = settings
        self._output_root = output_root
        self._llm = build_chat_model(settings, temperature=0.1)
        self._tools = [
            _build_discover_papers_tool(settings, output_root),
            _build_synthesize_report_tool(settings, output_root),
            _build_get_project_status_tool(output_root),
            read_papers,
        ]
        self._tool_map = {t.name: t for t in self._tools}

    async def plan(self, user_query: str, project_slug: str) -> str:
        llm_with_tools = self._llm.bind_tools(self._tools)

        messages = [
            SystemMessage(content=ORCHESTRATOR_SYSTEM_PROMPT),
            HumanMessage(content=f"Project: {project_slug}\n\nUser needs: {user_query}"),
        ]

        final_answer = ""
        max_steps = 5
        discover_called = False
        for _step in range(max_steps):
            response = await llm_with_tools.ainvoke(messages)
            messages.append(response)

            tool_calls: list[dict] = getattr(response, "tool_calls", None) or []

            text_content = response.content if hasattr(response, "content") and isinstance(response.content, str) else ""
            if tool_calls:
                pass
            elif text_content.strip():
                final_answer = text_content.strip()
                break
            else:
                break

            for tc in tool_calls:
                name = tc.get("name", "")
                args = tc.get("args", {})
                tool_id = tc.get("id", "")

                if name == "discover_papers":
                    if discover_called:
                        tool_result = (
                            "discover_papers has already been called; the search is complete. "
                            "Please call synthesize_report directly to generate the report."
                        )
                        messages.append(ToolMessage(content=tool_result, tool_call_id=tool_id))
                        continue
                    discover_called = True

                project_value = args.get("project") or args.get("project_slug") or project_slug
                if name == "discover_papers":
                    args = {
                        "query": args.get("query", ""),
                        "project": project_value,
                    }
                elif name == "synthesize_report":
                    args = {"project": project_value}
                elif name == "get_project_status":
                    args = {"project": project_value}
                elif name == "read_papers":
                    args = {"project": project_value, "paper_slug": args.get("paper_slug", "")}

                logger.info("agent: calling tool %s for project=%s", name, project_value)
                print(f"  [Agent] Calling tool: {name}")

                if name not in self._tool_map:
                    result_text = f"Unknown tool: {name}"
                else:
                    try:
                        result_text = await self._tool_map[name].ainvoke(args)
                        if isinstance(result_text, list):
                            result_text = json.dumps(result_text, ensure_ascii=False)
                    except Exception as exc:
                        result_text = f"Tool execution failed: {exc}"
                        logger.warning("tool %s failed: %s", name, exc)

                print(f"  [Agent] Result: {result_text}")
                messages.append(ToolMessage(content=str(result_text)[:6000], tool_call_id=tool_id))
        else:
            if not final_answer:
                final_answer = "Task complete."

        return final_answer
