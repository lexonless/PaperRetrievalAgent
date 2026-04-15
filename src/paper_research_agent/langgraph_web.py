from __future__ import annotations

import argparse
import asyncio
import json
import queue
import threading
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from uuid import uuid4

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .app import ResearchAssistantApplication
from .core.config import Settings
from .core.models import ResearchNoteOutput
from .project.reporting import render_markdown_to_safe_html, render_research_note_markdown

MAX_JOB_EVENTS = 50

PHASE_BY_STEP = {
    "prepare_run_context": "preparing",
    "task_interpretation_node": "planning",
    "retrieval_node": "retrieving",
    "reviewer_node": "reviewing",
    "validate_review_gate_node": "reviewing",
    "generate_research_note": "writing",
    "persist_project_artifacts": "persisting",
}


def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


@dataclass(slots=True)
class LangGraphProgressEvent:
    index: int
    timestamp: str
    phase: str
    step: str
    event_type: str
    summary: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "phase": self.phase,
            "step": self.step,
            "event_type": self.event_type,
            "summary": self.summary,
        }


@dataclass(slots=True)
class LangGraphJobRecord:
    job_id: str
    query: str
    project_slug: str
    pdf_dir: str
    status: str
    phase: str
    created_at: str
    started_at: str | None = None
    finished_at: str | None = None
    latest_message: str = ""
    current_trace_index: int = 0
    event_index: int = 0
    events: list[LangGraphProgressEvent] = field(default_factory=list)
    artifacts: dict[str, str] = field(default_factory=dict)
    stop_reason: str = ""
    result_markdown: str | None = None
    result_html: str | None = None
    error: str | None = None


class LangGraphJobCreateRequest(BaseModel):
    query: str
    project_slug: str
    pdf_dir: str = ""


class LangGraphWebService:
    def __init__(
        self,
        *,
        output_dir: str = "projects",
        app_factory: Callable[[], ResearchAssistantApplication] | None = None,
        markdown_renderer: Callable[[str], str] | None = None,
        pdf_dir_selector: Callable[[], str] | None = None,
    ) -> None:
        self.output_dir = output_dir
        self.app_factory = app_factory or self._build_application
        self.markdown_renderer = markdown_renderer or (
            lambda markdown: render_markdown_to_safe_html(markdown, strip_query_metadata=True)
        )
        self.pdf_dir_selector = pdf_dir_selector or self._select_pdf_dir_native
        self.jobs: dict[str, LangGraphJobRecord] = {}
        self._jobs_lock = threading.Lock()
        self._threads: set[threading.Thread] = set()
        self._subscribers: dict[str, list[queue.Queue[dict[str, Any]]]] = {}

    def _build_application(self) -> ResearchAssistantApplication:
        return ResearchAssistantApplication(Settings.from_env(), output_root=self.output_dir)

    def _select_pdf_dir_native(self) -> str:
        try:
            import tkinter as tk
            from tkinter import filedialog
        except Exception as exc:  # pragma: no cover - environment dependent
            raise RuntimeError("Native folder picker is unavailable in this environment.") from exc

        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        try:
            selected = filedialog.askdirectory(title="Select PDF directory")
        finally:
            root.destroy()
        return str(Path(selected).resolve()) if selected else ""

    def select_pdf_dir(self) -> str:
        return self.pdf_dir_selector()

    def create_job(self, query: str, project_slug: str, pdf_dir: str = "") -> LangGraphJobRecord:
        clean_query = query.strip()
        clean_slug = project_slug.strip()
        clean_pdf_dir = pdf_dir.strip()
        if not clean_query:
            raise ValueError("Query must not be empty.")
        if not clean_slug:
            raise ValueError("Project slug must not be empty.")

        job = LangGraphJobRecord(
            job_id=str(uuid4()),
            query=clean_query,
            project_slug=clean_slug,
            pdf_dir=clean_pdf_dir,
            status="queued",
            phase="queued",
            created_at=_now_iso(),
            latest_message="Waiting to start.",
        )
        with self._jobs_lock:
            self.jobs[job.job_id] = job
            self._subscribers[job.job_id] = []
        return job

    def schedule_job(self, job_id: str) -> None:
        thread = threading.Thread(target=self._run_job_in_thread, args=(job_id,), daemon=True)
        self._threads.add(thread)
        thread.start()

    def _run_job_in_thread(self, job_id: str) -> None:
        try:
            asyncio.run(self.run_job(job_id))
        finally:
            self._threads = {thread for thread in self._threads if thread.is_alive()}

    async def run_job(self, job_id: str) -> None:
        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.status = "running"
            job.phase = "preparing"
            job.started_at = _now_iso()
            job.latest_message = "Preparing project context and runtime inputs."
            progress_payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "progress", progress_payload)
        self._append_event(
            job_id,
            phase="preparing",
            step="system",
            event_type="status",
            summary="Preparing project context and runtime inputs.",
        )

        app = self.app_factory()
        final_state: dict[str, Any] | None = None
        try:
            stream = await app.run_stream(
                project_slug=job.project_slug,
                task=job.query,
                pdf_dir=job.pdf_dir,
            )
            async for state in stream:
                final_state = state
                self._ingest_state(job_id, state)

            if final_state is None:
                raise RuntimeError("The graph did not produce a final state.")

            self._complete_job(job_id, final_state)
        except Exception as exc:
            self._mark_failed(job_id, str(exc) or exc.__class__.__name__)
        finally:
            await app.close()

    def _ingest_state(self, job_id: str, state: dict[str, Any]) -> None:
        run = state.get("run", {}) if isinstance(state, dict) else {}
        trace_events = run.get("trace_events", []) if isinstance(run, dict) else []

        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            already_seen = job.current_trace_index

        new_events = trace_events[already_seen:]
        for raw_event in new_events:
            if not isinstance(raw_event, dict):
                continue
            step = str(raw_event.get("step", "")).strip() or "graph"
            event_type = str(raw_event.get("event_type", "")).strip() or "update"
            message = str(raw_event.get("message", "")).strip() or "Graph emitted an update."
            phase = self._phase_for_trace(step=step, stop_reason=str(run.get("stop_reason", "")).strip())
            self._append_event(
                job_id,
                phase=phase,
                step=step,
                event_type=event_type,
                summary=message,
                timestamp=str(raw_event.get("timestamp", "")).strip() or None,
            )

        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.current_trace_index = len(trace_events)
            job.artifacts = self._build_artifacts(state)
            job.stop_reason = str(run.get("stop_reason", "")).strip()
            if job.events:
                latest_event = job.events[-1]
                job.phase = latest_event.phase
                job.latest_message = latest_event.summary
            payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "progress", payload)

    def _complete_job(self, job_id: str, state: dict[str, Any]) -> None:
        note_payload = (state.get("note", {}) or {}).get("research_note_output")
        if not note_payload:
            raise RuntimeError("The graph completed without a research note output.")

        note_output = ResearchNoteOutput.model_validate(note_payload)
        query = (state.get("request", {}) or {}).get("raw_query", "")
        project_slug = (state.get("project", {}) or {}).get("slug", "")
        result_markdown = render_research_note_markdown(note_output, project_slug=project_slug, query=query)
        result_html = self.markdown_renderer(result_markdown)
        artifacts = self._build_artifacts(state)
        stop_reason = str((state.get("run", {}) or {}).get("stop_reason", "")).strip()

        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.status = "succeeded"
            job.phase = "completed"
            job.finished_at = _now_iso()
            job.latest_message = "Research note is ready."
            job.result_markdown = result_markdown
            job.result_html = result_html
            job.artifacts = artifacts
            job.stop_reason = stop_reason
            job.error = None
            job.event_index += 1
            completed_event = LangGraphProgressEvent(
                index=job.event_index,
                timestamp=_now_iso(),
                phase="completed",
                step="complete",
                event_type="status",
                summary="Research note is ready.",
            )
            job.events.append(completed_event)
            if len(job.events) > MAX_JOB_EVENTS:
                job.events = job.events[-MAX_JOB_EVENTS:]
            complete_payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "event", completed_event.as_dict())
        self._broadcast(job_id, "complete", complete_payload)

    def _mark_failed(self, job_id: str, error_message: str) -> None:
        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.status = "failed"
            job.phase = "failed"
            job.finished_at = _now_iso()
            job.latest_message = error_message
            job.error = error_message
            job.event_index += 1
            failed_event = LangGraphProgressEvent(
                index=job.event_index,
                timestamp=_now_iso(),
                phase="failed",
                step="error",
                event_type="error",
                summary=error_message,
            )
            job.events.append(failed_event)
            if len(job.events) > MAX_JOB_EVENTS:
                job.events = job.events[-MAX_JOB_EVENTS:]
            payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "event", failed_event.as_dict())
        self._broadcast(job_id, "error", payload)

    def _append_event(
        self,
        job_id: str,
        *,
        phase: str,
        step: str,
        event_type: str,
        summary: str,
        timestamp: str | None = None,
    ) -> None:
        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.event_index += 1
            event = LangGraphProgressEvent(
                index=job.event_index,
                timestamp=timestamp or _now_iso(),
                phase=phase,
                step=step,
                event_type=event_type,
                summary=summary,
            )
            job.events.append(event)
            if len(job.events) > MAX_JOB_EVENTS:
                job.events = job.events[-MAX_JOB_EVENTS:]
            payload = event.as_dict()

        self._broadcast(job_id, "event", payload)

    def _phase_for_trace(self, *, step: str, stop_reason: str) -> str:
        if step == "validate_review_gate_node" and stop_reason == "review_passed":
            return "writing"
        return PHASE_BY_STEP.get(step, "running")

    def _build_artifacts(self, state: dict[str, Any]) -> dict[str, str]:
        run_artifacts = (state.get("run", {}) or {}).get("artifacts", {}) or {}
        note_path = str((state.get("note", {}) or {}).get("note_path", "")).strip()
        artifacts = {
            key: str(value)
            for key, value in run_artifacts.items()
            if str(value).strip()
        }
        if note_path and "note_path" not in artifacts:
            artifacts["note_path"] = note_path
        return artifacts

    def _snapshot_payload_locked(self, job: LangGraphJobRecord) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "job_id": job.job_id,
            "query": job.query,
            "project_slug": job.project_slug,
            "pdf_dir": job.pdf_dir,
            "status": job.status,
            "phase": job.phase,
            "created_at": job.created_at,
            "started_at": job.started_at,
            "finished_at": job.finished_at,
            "latest_message": job.latest_message,
            "current_trace_index": job.current_trace_index,
            "events": [event.as_dict() for event in job.events],
            "artifacts": job.artifacts,
            "stop_reason": job.stop_reason,
        }
        if job.status == "succeeded":
            payload["result_markdown"] = job.result_markdown
            payload["result_html"] = job.result_html
        elif job.status == "failed":
            payload["error"] = job.error
        return payload

    def get_job_payload(self, job_id: str) -> dict[str, Any]:
        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                raise KeyError(job_id)
            return self._snapshot_payload_locked(job)

    def subscribe(self, job_id: str) -> queue.Queue[dict[str, Any]]:
        listener: queue.Queue[dict[str, Any]] = queue.Queue()
        with self._jobs_lock:
            if job_id not in self.jobs:
                raise KeyError(job_id)
            self._subscribers.setdefault(job_id, []).append(listener)
            snapshot = self._snapshot_payload_locked(self.jobs[job_id])
        listener.put({"event": "snapshot", "data": snapshot})
        return listener

    def unsubscribe(self, job_id: str, listener: queue.Queue[dict[str, Any]]) -> None:
        with self._jobs_lock:
            listeners = self._subscribers.get(job_id)
            if listeners is None:
                return
            self._subscribers[job_id] = [item for item in listeners if item is not listener]

    def _broadcast(self, job_id: str, event_name: str, data: dict[str, Any]) -> None:
        with self._jobs_lock:
            listeners = list(self._subscribers.get(job_id, []))
        for listener in listeners:
            listener.put({"event": event_name, "data": data})

    async def event_stream(self, job_id: str, request: Request) -> AsyncGenerator[str, None]:
        listener = self.subscribe(job_id)
        try:
            while True:
                if await request.is_disconnected():
                    break
                try:
                    message = await asyncio.to_thread(listener.get, True, 0.5)
                except queue.Empty:
                    continue
                yield self._format_sse(message["event"], message["data"])
                if message["event"] in {"complete", "error"}:
                    break
        finally:
            self.unsubscribe(job_id, listener)

    def _format_sse(self, event_name: str, data: dict[str, Any]) -> str:
        return f"event: {event_name}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

    async def shutdown(self) -> None:
        self._threads = {thread for thread in self._threads if thread.is_alive()}


def create_app(
    *,
    output_dir: str = "projects",
    service: LangGraphWebService | None = None,
) -> FastAPI:
    static_dir = Path(__file__).resolve().parent / "langgraph_web_static"
    web_service = service or LangGraphWebService(output_dir=output_dir)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        yield
        await web_service.shutdown()

    app = FastAPI(title="LangGraph Research Assistant Web", version="0.1.0", lifespan=lifespan)
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/", response_class=FileResponse)
    async def index() -> FileResponse:
        return FileResponse(static_dir / "index.html")

    @app.post("/api/jobs", status_code=202)
    async def create_job_endpoint(payload: LangGraphJobCreateRequest) -> dict[str, str]:
        try:
            job = web_service.create_job(payload.query, payload.project_slug, payload.pdf_dir)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        web_service.schedule_job(job.job_id)
        return {
            "job_id": job.job_id,
            "status": job.status,
            "poll_url": f"/api/jobs/{job.job_id}",
            "events_url": f"/api/jobs/{job.job_id}/events",
        }

    @app.post("/api/select-pdf-dir")
    async def select_pdf_dir_endpoint() -> dict[str, str]:
        try:
            selected = await asyncio.to_thread(web_service.select_pdf_dir)
        except RuntimeError as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        return {"pdf_dir": selected}

    @app.get("/api/jobs/{job_id}")
    async def get_job_endpoint(job_id: str) -> dict[str, Any]:
        try:
            return web_service.get_job_payload(job_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=f"Unknown job id: {job_id}") from exc

    @app.get("/api/jobs/{job_id}/events")
    async def get_job_events(job_id: str, request: Request) -> StreamingResponse:
        try:
            web_service.get_job_payload(job_id)
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=f"Unknown job id: {job_id}") from exc
        return StreamingResponse(web_service.event_stream(job_id, request), media_type="text/event-stream")

    return app


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the LangGraph research assistant web server.")
    parser.add_argument("--host", default="127.0.0.1", help="Host used to bind the web server.")
    parser.add_argument("--port", type=int, default=8004, help="Port used to bind the web server.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="projects",
        help="Project library root directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    uvicorn.run(create_app(output_dir=args.output_dir), host=args.host, port=args.port)
