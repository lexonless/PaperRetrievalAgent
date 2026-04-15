from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from ..core.config import Settings
from ..core.llm import build_chat_model, build_rerank_chat_model, coerce_model, invoke_structured_output
from ..core.models import RetrievalOutput
from ..core.models import ResearchNoteOutput
from ..core.models import ReviewOutput
from ..core.models import TaskInterpretation
from ..core.models import TaskQueryIRUpdate
from ..core.models import TaskQueryPlan
from ..core.models import TimeRangeResolution
from ..core.models import TraceEvent
from ..core.normalization import normalize_string_list, normalize_text
from ..core.state import ResearchProjectState
from ..project.reporting import build_trace_payload, render_research_note_markdown, summarize_manifest_sources
from ..project.store import append_run_record
from ..project.store import build_timestamped_filename
from ..project.store import discover_local_pdfs
from ..project.store import ensure_project_paths
from ..project.store import load_manifest
from ..project.store import merge_manifest_sources
from ..project.store import persist_manifest
from ..project.store import write_json
from ..retrieval.query_planning import apply_query_ir_update
from ..retrieval.query_planning import build_query_plan
from ..retrieval.toolkit import PaperSearchToolkit


YEAR_TOKEN_PATTERN = re.compile(r"\b(?:19|20)\d{2}\b")
VENUE_TOKEN_PATTERN = re.compile(r"\b(?:cvpr|iccv|eccv|siggraph|neurips|nips|iclr|aaai)\b", re.IGNORECASE)
MAX_REVIEW_REVISIONS = 3
GENERIC_SEMANTIC_TERM_PATTERNS = {
    "geometric deep learning",
    "3d shape reconstruction",
    "cad reconstruction",
}


TASK_INTERPRETATION_SYSTEM_MESSAGE_TEMPLATE = """You are the task interpretation agent for a project-centered research assistant.

Today is {today}.
For year-bucketed planning, resolve relative time expressions against today's date.
If runtime notes already resolve a time window, treat them as authoritative.

Your job:
1. Interpret the research task and produce a retrieval-ready task interpretation.
2. Return only these top-level fields:
   - intent
   - query_plan
   - hard_requirements
3. intent must contain:
   - topic
   - goal
   - time_range
   - must_include
   - must_exclude
4. query_plan must contain:
   - query_ir
   - rendered_queries
   - primary_queries
   - semantic_core_terms
5. query_ir must contain:
   - topic_phrases
   - method_terms
   - optional_terms
   - excluded_terms
   - alias_groups
5. hard_requirements must contain:
   - minimum_paper_count
   - maximum_paper_count
   - required_paper_types
   - forbidden_paper_types
   - required_source_families
6. Extract any explicit output-count or paper-type constraints from the user request into hard_requirements.
7. If the user asks for a range like "8-10 papers", set minimum_paper_count=8 and maximum_paper_count=10.
8. primary_queries should be high-quality search queries, not natural-language summaries.
9. query_ir should capture the stable retrieval semantics, not source-specific syntax.
10. Keep rendered_queries, primary_queries, and semantic_core_terms lightweight. The program may normalize or rerender them.
11. must_include and must_exclude are user-facing hard constraints, not retrieval metadata.
12. If reviewer feedback exists, use failure_reasons and reformulation_advice to revise the interpretation.
13. Do not repeat weak prior query patterns from the previous interpretation.
14. Avoid venue names and explicit year tokens in query_ir, primary_queries, and semantic_core_terms.
15. topic_phrases, method_terms, and optional_terms are ordered lists, not unordered bags of terms.
16. Put the most essential, highest-precision, and most discriminative concepts first in each ordered list.
17. Earlier items are treated as higher-priority during query rendering.
18. Precision queries are built from the earliest positive groups.
19. Recall queries use only the earliest broad but still task-faithful groups.
"""


QUERY_REWRITE_SYSTEM_MESSAGE_TEMPLATE = """You are the query rewrite agent for a project-centered research assistant.

Today is {today}.
For year-bucketed planning, resolve relative time expressions against today's date only if needed for query wording.

Your job:
1. Revise only the query plan after a failed retrieval-review cycle.
2. Return only these top-level fields:
   - topic_phrases
   - method_terms
   - optional_terms
   - excluded_terms
   - alias_groups
3. Return only the query IR update fields that need to change. Leave untouched fields as null or omit them.
4. Keep the existing task intent and hard requirements unchanged. Do not reinterpret the task.
4. Use the previous failed query plan, the actual executed queries, and the reviewer failure_reasons and reformulation_advice.
5. Make targeted fixes to the queries instead of regenerating a brand-new task interpretation.
6. Replace weak or failed query patterns with sharper alternatives; do not simply restate them.
7. Focus on fixing the query IR buckets that caused failure.
8. Avoid venue names and explicit year tokens in all rewritten fields.
9. excluded_terms should contain concepts to suppress in retrieval, not source-specific boolean syntax.
10. topic_phrases, method_terms, and optional_terms are ordered lists, not unordered bags of terms.
11. Reorder surviving terms by expected retrieval value when necessary.
12. Move sharper, more discriminative terms earlier; move weaker or broader terms later.
13. Earlier items are treated as higher-priority during query rendering.
14. Precision queries are built from the earliest positive groups, and recall queries use only the earliest broad but still task-faithful groups.
"""


RETRIEVAL_SYSTEM_MESSAGE = """You are the retrieval agent for a research assistant.

Your job:
1. Use the available retrieval tool to execute the latest task interpretation.
2. Do not invent or override query strings. Execute the task interpretation's query plan as-is.
3. Prefer a single call to retrieve_candidates_from_plan.
4. Do not fabricate metadata or final notes.
5. Return tool output as the canonical retrieval result.
"""


REVIEWER_SYSTEM_MESSAGE_TEMPLATE = """You are the quality gate for a research assistant.

Today is {today}. Use the task interpretation's resolved time range as the reference window.

Return PASS only when the retrieval result is credibly useful for follow-on research notes.
If evidence is thin, missing, or inconsistent, return REVISE with concrete next actions.
Evaluate the retrieval against the interpreted goal, required inclusions, required exclusions, resolved time range, and hard_requirements.
Treat hard_requirements as binding. If the user explicitly requested a minimum number of papers, do not return PASS unless the retrieval credibly supports that minimum.
If required_paper_types or forbidden_paper_types are present, explicitly assess whether the retained papers satisfy them.
If the decision is REVISE, populate:
- failure_reasons: concise statements of what went wrong
- reformulation_advice: concrete guidance for the next interpretation cycle, especially query and semantic-term improvements
If the decision is PASS, keep failure_reasons and reformulation_advice empty unless a minor caution is essential.
The run may revise at most {MAX_REVIEW_REVISIONS} times before it must continue with explicit limitations.
"""


RESEARCH_NOTE_SYSTEM_MESSAGE = """You are drafting a project-centered research note.

Use the project context, retrieval output, and review outcome to produce a concise but useful research note draft.

Rules:
- If review passed, treat the core papers as reasonably credible.
- If review did not pass or the revision budget was exhausted, explicitly frame the note as tentative and list limitations.
- Respect hard_requirements from the task interpretation. If a minimum paper count is specified and retrieval supports it, include at least that many papers across core_papers and supporting_papers.
- Do not fabricate citations or evidence.
- Keep the note useful for continued research work on this project.
"""


@dataclass(slots=True)
class GraphResources:
    settings: Settings
    output_root: Path
    toolkit: PaperSearchToolkit
    task_interpretation_model: Any
    retrieval_model: Any
    reviewer_model: Any
    note_model: Any
    retrieval_tool: Any
    revision_budget: int = MAX_REVIEW_REVISIONS


def create_resources(settings: Settings, *, output_root: str) -> GraphResources:
    from langchain_core.tools import StructuredTool

    toolkit = PaperSearchToolkit(settings, rerank_model_client=build_rerank_chat_model(settings))
    retrieval_tool = StructuredTool.from_function(
        coroutine=toolkit.retrieve_candidates_from_plan,
        name="retrieve_candidates_from_plan",
        description=(
            "Run the current task interpretation and return ranked paper candidates. "
            "Supported args: top_k, max_results_per_source."
        ),
    )
    return GraphResources(
        settings=settings,
        output_root=Path(output_root),
        toolkit=toolkit,
        task_interpretation_model=build_chat_model(settings, temperature=0.1),
        retrieval_model=build_chat_model(settings, temperature=0.1),
        reviewer_model=build_chat_model(settings, temperature=0.0),
        note_model=build_chat_model(settings, temperature=0.2),
        retrieval_tool=retrieval_tool,
    )


def build_research_assistant_graph(resources: GraphResources):
    from langgraph.graph import END, START, StateGraph

    retrieval_subgraph = build_paper_retrieval_subgraph(resources)

    builder = StateGraph(ResearchProjectState)
    builder.add_node("prepare_run_context", _make_prepare_run_context_node(resources))
    builder.add_node("paper_retrieval_subgraph", retrieval_subgraph)
    builder.add_node("generate_research_note", _make_generate_research_note_node(resources))
    builder.add_node("persist_project_artifacts", _make_persist_project_artifacts_node(resources))

    builder.add_edge(START, "prepare_run_context")
    builder.add_edge("prepare_run_context", "paper_retrieval_subgraph")
    builder.add_edge("paper_retrieval_subgraph", "generate_research_note")
    builder.add_edge("generate_research_note", "persist_project_artifacts")
    builder.add_edge("persist_project_artifacts", END)
    return builder.compile()


def build_paper_retrieval_subgraph(resources: GraphResources):
    from langgraph.graph import END, START, StateGraph

    builder = StateGraph(ResearchProjectState)
    builder.add_node("task_interpretation_node", _make_task_interpretation_node(resources))
    builder.add_node("retrieval_node", _make_retrieval_node(resources))
    builder.add_node("reviewer_node", _make_reviewer_node(resources))
    builder.add_node("validate_review_gate_node", _make_validate_review_gate_node(resources))

    builder.add_edge(START, "task_interpretation_node")
    builder.add_edge("task_interpretation_node", "retrieval_node")
    builder.add_edge("retrieval_node", "reviewer_node")
    builder.add_edge("reviewer_node", "validate_review_gate_node")
    builder.add_conditional_edges(
        "validate_review_gate_node",
        _next_after_review_validation,
        {
            "task_interpretation_node": "task_interpretation_node",
            END: END,
        },
    )
    return builder.compile()


def _make_prepare_run_context_node(resources: GraphResources):
    async def prepare_run_context(state: ResearchProjectState) -> dict[str, Any]:
        raw_query = state["request"]["raw_query"]
        project_slug = state["project"]["slug"]
        pdf_dir = state["project"].get("pdf_dir", "")
        project_paths = ensure_project_paths(resources.output_root, project_slug)
        manifest = load_manifest(project_paths.manifest_path, project_slug)
        local_pdf_paths = discover_local_pdfs(project_paths=project_paths, pdf_dir=pdf_dir)
        manifest = merge_manifest_sources(manifest, local_pdf_paths)
        resources.toolkit.set_local_pdf_paths(local_pdf_paths)

        prepared_query, time_resolution, runtime_notes = _prepare_task(raw_query)
        run = dict(state["run"])
        run["trace_events"] = _append_trace(
            state,
            step="prepare_run_context",
            event_type="state_update",
            message="Initialized project paths, manifest, and runtime search context.",
            payload={
                "project_root": str(project_paths.root_dir),
                "local_pdf_count": len(local_pdf_paths),
            },
        )
        return {
            "project": {
                **state["project"],
                "root_dir": str(project_paths.root_dir),
                "project_file": str(project_paths.project_file),
                "source_manifest": manifest.model_dump(),
                "local_pdf_paths": local_pdf_paths,
                "pdf_dir": pdf_dir,
            },
            "request": {
                **state["request"],
                "prepared_query": prepared_query,
                "time_resolution": time_resolution,
                "runtime_notes": runtime_notes,
            },
            "run": run,
        }

    return prepare_run_context


def _make_task_interpretation_node(resources: GraphResources):
    async def task_interpretation_node(state: ResearchProjectState) -> dict[str, Any]:
        previous_task_interpretation_payload = state["retrieval"]["task_interpretation"] or {}
        review_feedback_payload = state["retrieval"]["review_output"] or {}
        retrieval_output_payload = state["retrieval"]["retrieval_output"] or {}
        revision_count = state["retrieval"]["revision_count"]
        task_input = {
            "project_slug": state["project"]["slug"],
            "query": state["request"]["raw_query"],
            "prepared_query": state["request"]["prepared_query"],
            "time_resolution": state["request"]["time_resolution"],
            "runtime_notes": state["request"]["runtime_notes"],
            "revision_count": revision_count,
            "previous_task_interpretation": previous_task_interpretation_payload,
            "review_feedback": review_feedback_payload,
            "local_source_hints": summarize_manifest_sources(state["project"]["source_manifest"]),
        }

        if _should_target_query_rewrite(revision_count, previous_task_interpretation_payload):
            previous_task_interpretation = TaskInterpretation.model_validate(previous_task_interpretation_payload)
            rewrite_input = {
                "project_slug": state["project"]["slug"],
                "query": state["request"]["raw_query"],
                "prepared_query": state["request"]["prepared_query"],
                "revision_count": revision_count,
                "intent": previous_task_interpretation.intent.model_dump(),
                "hard_requirements": previous_task_interpretation.hard_requirements.model_dump(),
                "previous_query_plan": previous_task_interpretation.query_plan.model_dump(),
                "failed_queries": _collect_failed_queries(
                    previous_task_interpretation_payload,
                    retrieval_output_payload,
                ),
                "review_feedback": review_feedback_payload,
                "local_source_hints": summarize_manifest_sources(state["project"]["source_manifest"]),
            }
            rewritten_query_ir_update = await invoke_structured_output(
                model=resources.task_interpretation_model,
                schema=TaskQueryIRUpdate,
                system_prompt=QUERY_REWRITE_SYSTEM_MESSAGE_TEMPLATE.format(today=date.today().isoformat()),
                user_prompt=json.dumps(rewrite_input, ensure_ascii=False, indent=2),
            )
            rewritten_query_ir = apply_query_ir_update(
                previous_task_interpretation.query_plan.query_ir,
                rewritten_query_ir_update,
            )
            task_interpretation = previous_task_interpretation.model_copy(
                update={
                    "query_plan": build_query_plan(
                        previous_task_interpretation.query_plan.model_copy(update={"query_ir": rewritten_query_ir})
                    )
                }
            )
        else:
            task_interpretation = await invoke_structured_output(
                model=resources.task_interpretation_model,
                schema=TaskInterpretation,
                system_prompt=TASK_INTERPRETATION_SYSTEM_MESSAGE_TEMPLATE.format(today=date.today().isoformat()),
                user_prompt=json.dumps(task_input, ensure_ascii=False, indent=2),
            )
        task_interpretation = _clean_task_interpretation_output(task_interpretation)
        return {
            "retrieval": {
                **state["retrieval"],
                "task_interpretation": task_interpretation.model_dump(),
            },
            "run": {
                **state["run"],
                "trace_events": _append_trace(
                    state,
                    step="task_interpretation_node",
                    event_type="structured_output",
                    message="Task interpretation produced structured intent and query planning output.",
                    payload={
                        "query_count": len(task_interpretation.query_plan.primary_queries),
                        "semantic_core_term_count": len(task_interpretation.query_plan.semantic_core_terms),
                        "minimum_paper_count": task_interpretation.hard_requirements.minimum_paper_count,
                        "maximum_paper_count": task_interpretation.hard_requirements.maximum_paper_count,
                        "revision_count": state["retrieval"]["revision_count"],
                    },
                ),
            },
        }

    return task_interpretation_node


def _make_retrieval_node(resources: GraphResources):
    async def retrieval_node(state: ResearchProjectState) -> dict[str, Any]:
        from langchain_core.messages import HumanMessage, SystemMessage

        task_interpretation = _resolve_task_interpretation_for_execution(
            state["retrieval"]["task_interpretation"] or {},
            state["request"]["time_resolution"],
        )
        resources.toolkit.set_latest_task_interpretation(task_interpretation.model_dump())
        prompt_payload = {
            "prepared_query": state["request"]["prepared_query"],
            "task_interpretation": task_interpretation.model_dump(),
            "local_pdf_count": len(state["project"]["local_pdf_paths"]),
            "local_source_hints": summarize_manifest_sources(state["project"]["source_manifest"]),
        }
        bound_model = resources.retrieval_model.bind_tools([resources.retrieval_tool])
        raw_result: Any = None
        tool_call_payloads: list[dict[str, Any]] = []

        try:
            response = await bound_model.ainvoke(
                [
                    SystemMessage(content=RETRIEVAL_SYSTEM_MESSAGE),
                    HumanMessage(content=json.dumps(prompt_payload, ensure_ascii=False, indent=2)),
                ]
            )
            tool_calls = getattr(response, "tool_calls", []) or []
            for tool_call in tool_calls:
                if tool_call.get("name") != resources.retrieval_tool.name:
                    continue
                args = _sanitize_retrieval_tool_args(tool_call.get("args", {}) or {})
                tool_call_payloads.append({"name": tool_call.get("name", ""), "args": args})
                raw_result = await resources.retrieval_tool.ainvoke(args)
            if raw_result is None:
                raw_result = getattr(response, "content", response)
            retrieval_output = coerce_model(RetrievalOutput, raw_result)
            run = {
                **state["run"],
                "trace_events": _append_trace(
                    state,
                    step="retrieval_node",
                    event_type="tool_result",
                    message="Retrieval node produced candidate papers.",
                    payload={
                        "tool_calls": tool_call_payloads,
                        "paper_count": len(retrieval_output.papers),
                        "source_count": len(retrieval_output.sources_used),
                        "local_library_debug": {
                            "scanned_count": retrieval_output.local_library_debug.scanned_count,
                            "missing_count": retrieval_output.local_library_debug.missing_count,
                            "read_error_count": retrieval_output.local_library_debug.read_error_count,
                            "empty_text_count": retrieval_output.local_library_debug.empty_text_count,
                            "token_miss_count": retrieval_output.local_library_debug.token_miss_count,
                            "candidate_count": retrieval_output.local_library_debug.candidate_count,
                            "retained_count": retrieval_output.local_library_debug.retained_count,
                        },
                        "rerank_trace": {
                            "attempted": retrieval_output.rerank_trace.attempted,
                            "skipped_reason": retrieval_output.rerank_trace.skipped_reason,
                            "candidate_count": retrieval_output.rerank_trace.candidate_count,
                            "batch_count": retrieval_output.rerank_trace.batch_count,
                            "successful_batches": retrieval_output.rerank_trace.successful_batches,
                            "empty_batches": retrieval_output.rerank_trace.empty_batches,
                            "failed_batches": retrieval_output.rerank_trace.failed_batches,
                            "judgment_count": retrieval_output.rerank_trace.judgment_count,
                        },
                    },
                ),
            }
            return {
                "retrieval": {
                    **state["retrieval"],
                    "task_interpretation": task_interpretation.model_dump(),
                    "retrieval_output": retrieval_output.model_dump(),
                },
                "run": run,
            }
        except Exception as exc:
            fallback_output = RetrievalOutput(
                sources_used=[],
                queries_executed=[],
                papers=[],
                dedup_notes=[],
                missing_metadata=[],
                coverage_gaps=[f"Retrieval failed before completing the tool workflow: {exc}"],
                source_errors=[{"source": "retrieval_node", "error": str(exc), "query": state["request"]["raw_query"]}],
            )
            run = {
                **state["run"],
                "errors": [*state["run"]["errors"], str(exc)],
                "trace_events": _append_trace(
                    state,
                    step="retrieval_node",
                    event_type="error",
                    message="Retrieval node failed and emitted a fallback empty retrieval output.",
                    payload={"error": str(exc)},
                ),
            }
            return {
                "retrieval": {
                    **state["retrieval"],
                    "task_interpretation": task_interpretation.model_dump(),
                    "retrieval_output": fallback_output.model_dump(),
                },
                "run": run,
            }

    return retrieval_node


def _make_reviewer_node(resources: GraphResources):
    async def reviewer_node(state: ResearchProjectState) -> dict[str, Any]:
        review_input = {
            "prepared_query": state["request"]["prepared_query"],
            "task_interpretation": state["retrieval"]["task_interpretation"] or {},
            "retrieval_output": state["retrieval"]["retrieval_output"] or {},
            "revision_count": state["retrieval"]["revision_count"],
        }
        review_output = await invoke_structured_output(
            model=resources.reviewer_model,
            schema=ReviewOutput,
            system_prompt=REVIEWER_SYSTEM_MESSAGE_TEMPLATE.format(
                today=date.today().isoformat(),
                MAX_REVIEW_REVISIONS=resources.revision_budget,
            ),
            user_prompt=json.dumps(review_input, ensure_ascii=False, indent=2),
        )
        return {
            "retrieval": {
                **state["retrieval"],
                "review_output": review_output.model_dump(),
            },
            "run": {
                **state["run"],
                "trace_events": _append_trace(
                    state,
                    step="reviewer_node",
                    event_type="structured_output",
                    message="Reviewer returned a structured quality decision.",
                    payload={
                        "decision": review_output.decision,
                        "failure_reason_count": len(review_output.failure_reasons),
                        "reformulation_advice_count": len(review_output.reformulation_advice),
                    },
                ),
            },
        }

    return reviewer_node


def _make_validate_review_gate_node(resources: GraphResources):
    async def validate_review_gate_node(state: ResearchProjectState) -> dict[str, Any]:
        retrieval_output = RetrievalOutput.model_validate(state["retrieval"]["retrieval_output"] or {})
        review_output = ReviewOutput.model_validate(state["retrieval"]["review_output"] or {})
        task_interpretation = TaskInterpretation.model_validate(state["retrieval"]["task_interpretation"] or {})
        is_pass = _review_passes_programmatic_validation(review_output, retrieval_output, task_interpretation)
        revision_count = state["retrieval"]["revision_count"]
        forced_write = False
        stop_reason = "review_passed"
        message = "Review gate passed."

        if not is_pass:
            revision_count += 1
            if revision_count >= resources.revision_budget:
                forced_write = True
                stop_reason = "review_budget_exhausted"
                message = "Review gate failed and the revision budget was exhausted."
            else:
                stop_reason = "review_requested_revision"
                message = "Review gate requested another revision cycle."

        return {
            "retrieval": {
                **state["retrieval"],
                "revision_count": revision_count,
                "forced_write": forced_write,
            },
            "run": {
                **state["run"],
                "stop_reason": stop_reason,
                "trace_events": _append_trace(
                    state,
                    step="validate_review_gate_node",
                    event_type="decision",
                    message=message,
                    payload={
                        "decision": review_output.decision,
                        "validated_pass": is_pass,
                        "revision_count": revision_count,
                        "forced_write": forced_write,
                    },
                ),
            },
        }

    return validate_review_gate_node


def _make_generate_research_note_node(resources: GraphResources):
    async def generate_research_note(state: ResearchProjectState) -> dict[str, Any]:
        project_file = Path(state["project"]["project_file"])
        project_context = ""
        if project_file.exists():
            project_context = project_file.read_text(encoding="utf-8")

        note_input = {
            "project_slug": state["project"]["slug"],
            "query": state["request"]["raw_query"],
            "prepared_query": state["request"]["prepared_query"],
            "project_context": project_context,
            "source_manifest_summary": summarize_manifest_sources(state["project"]["source_manifest"], max_items=8),
            "task_interpretation": state["retrieval"]["task_interpretation"] or {},
            "retrieval_output": state["retrieval"]["retrieval_output"] or {},
            "review_output": state["retrieval"]["review_output"] or {},
            "forced_write": state["retrieval"]["forced_write"],
            "stop_reason": state["run"]["stop_reason"],
        }
        note_output = await invoke_structured_output(
            model=resources.note_model,
            schema=ResearchNoteOutput,
            system_prompt=RESEARCH_NOTE_SYSTEM_MESSAGE,
            user_prompt=json.dumps(note_input, ensure_ascii=False, indent=2),
        )
        return {
            "note": {
                **state["note"],
                "research_note_output": note_output.model_dump(),
            },
            "run": {
                **state["run"],
                "trace_events": _append_trace(
                    state,
                    step="generate_research_note",
                    event_type="structured_output",
                    message="Generated a structured research note draft.",
                    payload={
                        "core_paper_count": len(note_output.core_papers),
                        "supporting_paper_count": len(note_output.supporting_papers),
                    },
                ),
            },
        }

    return generate_research_note


def _make_persist_project_artifacts_node(resources: GraphResources):
    async def persist_project_artifacts(state: ResearchProjectState) -> dict[str, Any]:
        project_paths = ensure_project_paths(resources.output_root, state["project"]["slug"])
        note_output = ResearchNoteOutput.model_validate(state["note"]["research_note_output"] or {})

        note_filename = build_timestamped_filename("research-note", ".md")
        retrieval_filename = build_timestamped_filename("retrieval", ".json")
        trace_filename = build_timestamped_filename("trace", ".json")
        note_path = project_paths.notes_dir / note_filename
        retrieval_path = project_paths.retrieval_dir / retrieval_filename
        trace_path = project_paths.traces_dir / trace_filename

        note_markdown = render_research_note_markdown(
            note_output,
            project_slug=state["project"]["slug"],
            query=state["request"]["raw_query"],
        )
        note_path.write_text(note_markdown, encoding="utf-8")
        write_json(
            retrieval_path,
            {
                "query": state["request"]["raw_query"],
                "prepared_query": state["request"]["prepared_query"],
                "task_interpretation": state["retrieval"]["task_interpretation"] or {},
                "retrieval_output": state["retrieval"]["retrieval_output"] or {},
                "review_output": state["retrieval"]["review_output"] or {},
            },
        )

        manifest = merge_manifest_sources(
            load_manifest(project_paths.manifest_path, state["project"]["slug"]),
            state["project"]["local_pdf_paths"],
        )

        updated_state = {
            **state,
            "note": {
                **state["note"],
                "note_path": str(note_path),
            },
            "run": {
                **state["run"],
                "artifacts": {
                    **state["run"]["artifacts"],
                    "note_path": str(note_path),
                    "retrieval_path": str(retrieval_path),
                    "trace_path": str(trace_path),
                },
                "stop_reason": state["run"]["stop_reason"] or "completed",
            },
        }
        trace_payload = build_trace_payload(updated_state)
        write_json(trace_path, trace_payload)

        manifest = append_run_record(
            manifest,
            run_id=state["run"]["run_id"],
            query=state["request"]["raw_query"],
            note_path=str(note_path),
            retrieval_path=str(retrieval_path),
            trace_path=str(trace_path),
        )
        persist_manifest(project_paths.manifest_path, manifest)

        return {
            "project": {
                **state["project"],
                "root_dir": str(project_paths.root_dir),
                "source_manifest": manifest.model_dump(),
            },
            "note": {
                **state["note"],
                "note_path": str(note_path),
            },
            "run": {
                **updated_state["run"],
                "trace_events": _append_trace(
                    updated_state,
                    step="persist_project_artifacts",
                    event_type="artifact",
                    message="Persisted project artifacts and updated the source manifest.",
                    payload={
                        "note_path": str(note_path),
                        "retrieval_path": str(retrieval_path),
                        "trace_path": str(trace_path),
                    },
                ),
            },
        }

    return persist_project_artifacts


def _next_after_review_validation(state: ResearchProjectState):
    from langgraph.graph import END

    stop_reason = state["run"]["stop_reason"]
    if stop_reason == "review_passed":
        return END
    if state["retrieval"]["forced_write"]:
        return END
    return "task_interpretation_node"


def _prepare_task(task: str) -> tuple[str, dict[str, Any], list[str]]:
    today = date.today()
    notes = [
        f"Today's date for this run is {today.isoformat()}.",
        "Resolve all explicit and relative time expressions from the user request yourself. Do not rely on pre-resolved time windows.",
    ]
    runtime_context = "\n".join(notes)
    return f"{task}\n\n[Runtime Search Context]\n{runtime_context}", {}, notes


def _append_trace(
    state: ResearchProjectState | dict[str, Any],
    *,
    step: str,
    event_type: str,
    message: str,
    payload: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    run = state.get("run", {}) if isinstance(state, dict) else {}
    trace_events = list(run.get("trace_events", []))
    trace_events.append(
        TraceEvent(
            timestamp=datetime.now().isoformat(timespec="seconds"),
            step=step,
            event_type=event_type,
            message=message,
            payload=payload or {},
        ).model_dump()
    )
    return trace_events


def _resolve_task_interpretation_for_execution(
    task_interpretation_payload: dict[str, Any],
    time_resolution: dict[str, Any],
) -> TaskInterpretation:
    task_interpretation = TaskInterpretation.model_validate(task_interpretation_payload or {})
    resolved_time_range = TimeRangeResolution.model_validate(time_resolution or {})
    if resolved_time_range.start_year is None and resolved_time_range.end_year is None:
        return task_interpretation
    intent = task_interpretation.intent.model_copy(update={"time_range": resolved_time_range})
    return task_interpretation.model_copy(update={"intent": intent})


def _should_target_query_rewrite(revision_count: int, previous_task_interpretation_payload: dict[str, Any]) -> bool:
    if revision_count <= 0:
        return False
    if not isinstance(previous_task_interpretation_payload, dict) or not previous_task_interpretation_payload:
        return False
    query_plan = previous_task_interpretation_payload.get("query_plan", {})
    if not isinstance(query_plan, dict):
        return False
    return bool(query_plan.get("primary_queries") or query_plan.get("semantic_core_terms"))


def _collect_failed_queries(
    previous_task_interpretation_payload: dict[str, Any],
    retrieval_output_payload: dict[str, Any],
) -> dict[str, Any]:
    previous_task_interpretation = TaskInterpretation.model_validate(previous_task_interpretation_payload or {})
    retrieval_output = RetrievalOutput.model_validate(retrieval_output_payload or {})
    planned_primary_queries = list(previous_task_interpretation.query_plan.primary_queries)
    planned_semantic_core_terms = list(previous_task_interpretation.query_plan.semantic_core_terms)
    executed_queries = [
        {
            "query": item.query,
            "sources": list(item.sources),
            "notes": item.notes,
        }
        for item in retrieval_output.queries_executed
        if normalize_text(item.query)
    ]
    return {
        "planned_primary_queries": planned_primary_queries,
        "planned_semantic_core_terms": planned_semantic_core_terms,
        "all_failed_queries": list(
            dict.fromkeys(
                [
                    *planned_primary_queries,
                    *planned_semantic_core_terms,
                    *[item["query"] for item in executed_queries],
                ]
            )
        ),
        "executed_queries": executed_queries,
    }


def _clean_task_interpretation_output(task_interpretation: TaskInterpretation) -> TaskInterpretation:
    return task_interpretation.model_copy(update={"query_plan": build_query_plan(task_interpretation.query_plan)})


def _clean_primary_queries(values: list[str]) -> list[str]:
    cleaned: list[str] = []
    for value in normalize_string_list(values):
        query = YEAR_TOKEN_PATTERN.sub(" ", value)
        query = VENUE_TOKEN_PATTERN.sub(" ", query)
        query = normalize_text(query)
        if not query:
            continue
        if len(query.split()) < 3:
            continue
        cleaned.append(query)
    return list(dict.fromkeys(cleaned))[:8]


def _clean_semantic_core_terms(values: list[str]) -> list[str]:
    cleaned: list[str] = []
    for value in normalize_string_list(values):
        term = YEAR_TOKEN_PATTERN.sub(" ", value)
        term = VENUE_TOKEN_PATTERN.sub(" ", term)
        term = normalize_text(term)
        if not term:
            continue
        if len(term.split()) > 5:
            continue
        if normalize_text(term, for_matching=True) in GENERIC_SEMANTIC_TERM_PATTERNS:
            continue
        cleaned.append(term)
    return list(dict.fromkeys(cleaned))[:8]


def _sanitize_retrieval_tool_args(args: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(args, dict):
        return {}
    sanitized: dict[str, Any] = {}
    top_k = args.get("top_k")
    max_results_per_source = args.get("max_results_per_source")
    if isinstance(top_k, int):
        sanitized["top_k"] = top_k
    if isinstance(max_results_per_source, int):
        sanitized["max_results_per_source"] = max_results_per_source
    return sanitized


def _review_passes_programmatic_validation(
    review: ReviewOutput,
    retrieval: RetrievalOutput | None,
    task_interpretation: TaskInterpretation | None,
) -> bool:
    if review.decision != "PASS":
        return False

    score_values = [
        review.scores.coverage_score,
        review.scores.relevance_score,
        review.scores.metadata_score,
        review.scores.diversity_score,
        review.scores.evidence_score,
    ]
    if any(value == 0 for value in score_values):
        return False
    if sum(score_values) < 8:
        return False

    requirements = review.hard_requirements
    requirement_items = [
        requirements.source_coverage,
        requirements.candidate_depth,
        requirements.relevance,
        requirements.metadata,
        requirements.query_fit,
        requirements.core_method_fit,
        requirements.time_consistency,
        requirements.gaps,
    ]
    if any(item.passed is not True for item in requirement_items):
        return False

    if retrieval is None:
        return False
    return _retrieval_supports_pass(retrieval, task_interpretation)


def _retrieval_supports_pass(retrieval: RetrievalOutput, task_interpretation: TaskInterpretation | None) -> bool:
    distinct_sources = {source.strip() for source in retrieval.sources_used if source.strip()}
    if len(distinct_sources) < 2:
        return False
    if len(retrieval.papers) < 5:
        return False

    eligible_count = 0
    task_fit_count = 0
    in_range_count = 0
    supported_evidence_count = 0
    verified_count = 0
    for paper in retrieval.papers:
        if paper.eligible:
            eligible_count += 1
        if paper.task_fit in {"direct", "related"}:
            task_fit_count += 1
        if paper.time_range_status == "in_range":
            in_range_count += 1
        if (
            paper.verification_status in {"partial", "verified"}
            and paper.evidence_level in {"abstract", "excerpt"}
            and any(normalize_text(item) for item in paper.evidence_snippets)
        ):
            supported_evidence_count += 1
        if paper.verification_status == "verified":
            verified_count += 1

        if paper.evidence_level == "title_only" and paper.evidence_snippets:
            return False
        if paper.evidence_level == "title_only" and paper.verification_status != "weak":
            return False

    if eligible_count < 5:
        return False
    if task_fit_count < 5:
        return False
    if in_range_count < 5:
        return False
    if supported_evidence_count < 3:
        return False
    if verified_count < 1:
        return False
    hard_requirements = task_interpretation.hard_requirements if task_interpretation is not None else None
    minimum_paper_count = hard_requirements.minimum_paper_count if hard_requirements is not None else 0
    if minimum_paper_count > 0 and task_fit_count < minimum_paper_count:
        return False
    return True
