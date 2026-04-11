from __future__ import annotations

from typing import Any, TypedDict
from uuid import uuid4


class ProjectState(TypedDict):
    slug: str
    root_dir: str
    project_file: str
    source_manifest: dict[str, Any]
    local_pdf_paths: list[str]
    pdf_dir: str


class RequestState(TypedDict):
    raw_query: str
    prepared_query: str
    time_resolution: dict[str, Any]
    runtime_notes: list[str]


class RetrievalState(TypedDict):
    task_interpretation: dict[str, Any] | None
    retrieval_output: dict[str, Any] | None
    review_output: dict[str, Any] | None
    revision_count: int
    forced_write: bool


class NoteState(TypedDict):
    research_note_output: dict[str, Any] | None
    note_path: str


class RunState(TypedDict):
    run_id: str
    trace_events: list[dict[str, Any]]
    artifacts: dict[str, str]
    stop_reason: str
    errors: list[str]


class ResearchProjectState(TypedDict):
    project: ProjectState
    request: RequestState
    retrieval: RetrievalState
    note: NoteState
    run: RunState


def create_initial_state(
    *,
    project_slug: str,
    query: str,
) -> ResearchProjectState:
    return {
        "project": {
            "slug": project_slug,
            "root_dir": "",
            "project_file": "",
            "source_manifest": {},
            "local_pdf_paths": [],
            "pdf_dir": "",
        },
        "request": {
            "raw_query": query,
            "prepared_query": "",
            "time_resolution": {},
            "runtime_notes": [],
        },
        "retrieval": {
            "task_interpretation": None,
            "retrieval_output": None,
            "review_output": None,
            "revision_count": 0,
            "forced_write": False,
        },
        "note": {
            "research_note_output": None,
            "note_path": "",
        },
        "run": {
            "run_id": uuid4().hex,
            "trace_events": [],
            "artifacts": {},
            "stop_reason": "",
            "errors": [],
        },
    }
