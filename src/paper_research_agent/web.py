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
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import (
    ModelClientStreamingChunkEvent,
    TextMessage,
    ThoughtEvent,
    ToolCallExecutionEvent,
    ToolCallRequestEvent,
    ToolCallSummaryMessage,
)
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .app import PaperSearchApplication
from .config import Settings
from .reporting import render_markdown_to_safe_html, save_markdown_report

MAX_JOB_EVENTS = 50


def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


@dataclass(slots=True)
class ProgressEvent:
    index: int
    timestamp: str
    phase: str
    agent: str
    kind: str
    summary: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "phase": self.phase,
            "agent": self.agent,
            "kind": self.kind,
            "summary": self.summary,
        }


@dataclass(slots=True)
class JobRecord:
    job_id: str
    query: str
    status: str
    phase: str
    created_at: str
    started_at: str | None = None
    finished_at: str | None = None
    current_agent: str | None = None
    latest_message: str = ""
    event_index: int = 0
    events: list[ProgressEvent] = field(default_factory=list)
    result_markdown: str | None = None
    result_html: str | None = None
    report_path: str | None = None
    error: str | None = None


class JobCreateRequest(BaseModel):
    query: str


class PaperAgentWebService:
    def __init__(
        self,
        *,
        output_dir: str = "reports",
        app_factory: Callable[[], PaperSearchApplication] | None = None,
        report_saver: Callable[..., Any] = save_markdown_report,
        html_renderer: Callable[[str], str] = render_markdown_to_safe_html,
    ) -> None:
        self.output_dir = output_dir
        self.app_factory = app_factory or self._build_application
        self.report_saver = report_saver
        self.html_renderer = html_renderer
        self.jobs: dict[str, JobRecord] = {}
        self._jobs_lock = threading.Lock()
        self._threads: set[threading.Thread] = set()
        self._subscribers: dict[str, list[queue.Queue[dict[str, Any]]]] = {}

    def _build_application(self) -> PaperSearchApplication:
        return PaperSearchApplication(Settings.from_env())

    def create_job(self, query: str) -> JobRecord:
        clean_query = query.strip()
        if not clean_query:
            raise ValueError("Query must not be empty.")

        job = JobRecord(
            job_id=str(uuid4()),
            query=clean_query,
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
        thread = threading.Thread(
            target=self._run_job_in_thread,
            args=(job_id,),
            daemon=True,
        )
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
            job.phase = "planning"
            job.started_at = _now_iso()
            job.current_agent = "PlannerAgent"
            job.latest_message = "Planner is building the search plan."
            progress_payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "progress", progress_payload)
        self._append_progress_event(
            job_id,
            phase="planning",
            agent="PlannerAgent",
            kind="status",
            summary="Planner started building the search plan.",
        )

        app = self.app_factory()
        try:
            stream = await app.run_stream(job.query)
            async for item in stream:
                if isinstance(item, TaskResult):
                    await self._complete_job(job_id, item)
                    return
                self._record_stream_item(job_id, item)
        except Exception as exc:
            self._mark_failed(job_id, str(exc) or exc.__class__.__name__)
        finally:
            await app.close()

    async def _complete_job(self, job_id: str, task_result: TaskResult) -> None:
        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            query = job.query
            job.phase = "writing"
            job.current_agent = "WriterAgent"
            job.latest_message = "Writer is finalizing notes."
            progress_payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "progress", progress_payload)
        self._append_progress_event(
            job_id,
            phase="writing",
            agent="WriterAgent",
            kind="status",
            summary="Writer is finalizing the notes.",
        )

        saved_report = self.report_saver(task_result, query, output_dir=self.output_dir)
        result_markdown = saved_report.report_content
        result_html = self.html_renderer(result_markdown)

        with self._jobs_lock:
            current = self.jobs.get(job_id)
            if current is None:
                return
            current.status = "succeeded"
            current.phase = "completed"
            current.finished_at = _now_iso()
            current.current_agent = "WriterAgent"
            current.latest_message = "Run completed."
            current.result_markdown = result_markdown
            current.result_html = result_html
            current.report_path = str(Path(saved_report.report_path).resolve())
            current.error = None
            current.event_index += 1
            completed_event = ProgressEvent(
                index=current.event_index,
                timestamp=_now_iso(),
                phase="completed",
                agent="WriterAgent",
                kind="status",
                summary="Run completed and notes are ready.",
            )
            current.events.append(completed_event)
            if len(current.events) > MAX_JOB_EVENTS:
                current.events = current.events[-MAX_JOB_EVENTS:]
            complete_payload = self._snapshot_payload_locked(current)

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
            failed_event = ProgressEvent(
                index=job.event_index,
                timestamp=_now_iso(),
                phase="failed",
                agent=job.current_agent or "system",
                kind="error",
                summary=error_message,
            )
            job.events.append(failed_event)
            if len(job.events) > MAX_JOB_EVENTS:
                job.events = job.events[-MAX_JOB_EVENTS:]
            payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "event", failed_event.as_dict())
        self._broadcast(job_id, "error", payload)

    def _record_stream_item(self, job_id: str, item: Any) -> None:
        if isinstance(item, ModelClientStreamingChunkEvent):
            return
        if isinstance(item, ThoughtEvent):
            return

        summary_info = self._summarize_stream_item(item)
        if summary_info is None:
            return

        phase, agent, kind, summary = summary_info
        self._append_progress_event(job_id, phase=phase, agent=agent, kind=kind, summary=summary)

        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.phase = phase
            job.current_agent = agent or job.current_agent
            job.latest_message = summary
            payload = self._snapshot_payload_locked(job)

        self._broadcast(job_id, "progress", payload)

    def _append_progress_event(
        self,
        job_id: str,
        *,
        phase: str,
        agent: str,
        kind: str,
        summary: str,
    ) -> None:
        with self._jobs_lock:
            job = self.jobs.get(job_id)
            if job is None:
                return
            job.event_index += 1
            event = ProgressEvent(
                index=job.event_index,
                timestamp=_now_iso(),
                phase=phase,
                agent=agent,
                kind=kind,
                summary=summary,
            )
            job.events.append(event)
            if len(job.events) > MAX_JOB_EVENTS:
                job.events = job.events[-MAX_JOB_EVENTS:]
            event_payload = event.as_dict()

        self._broadcast(job_id, "event", event_payload)

    def _summarize_stream_item(self, item: Any) -> tuple[str, str, str, str] | None:
        source = getattr(item, "source", "") or "system"
        if source == "user":
            return None
        phase = self._phase_for_source(item)

        if isinstance(item, ToolCallRequestEvent):
            names = [getattr(call, "name", "tool") for call in getattr(item, "content", [])]
            summary = f"{source} requested tool calls: {', '.join(names) or 'tool'}."
            return phase, source, "tool_request", summary

        if isinstance(item, ToolCallExecutionEvent):
            names = [getattr(result, "name", "tool") for result in getattr(item, "content", [])]
            summary = f"{source} executed tool calls: {', '.join(names) or 'tool'}."
            return phase, source, "tool_execution", summary

        if isinstance(item, ToolCallSummaryMessage):
            content = getattr(item, "content", "")
            text = self._structured_message_summary(source, content) or self._first_line(content)
            summary = text or f"{source} completed a tool-assisted step."
            return phase, source, "tool_summary", summary

        if isinstance(item, TextMessage):
            summary = self._summarize_text_message(item)
            if summary:
                return phase, source, "message", summary
            return None

        content = getattr(item, "content", "")
        if isinstance(content, str) and content.strip():
            return phase, source, "message", self._first_line(content)
        return None

    def _summarize_text_message(self, message: TextMessage) -> str:
        source = getattr(message, "source", "") or "system"
        content = getattr(message, "content", "")
        structured_summary = self._structured_message_summary(source, content)
        if structured_summary:
            return structured_summary
        first_line = self._first_line(content)

        if source == "PlannerAgent":
            return "Planner updated the search plan."
        if source == "RetrievalAgent":
            return "Retrieval agent updated the candidate set."
        if source == "ReviewerAgent":
            upper = str(content).upper()
            if '"DECISION": "REVISE"' in upper or '"DECISION":"REVISE"' in upper:
                return "Reviewer requested revisions."
            if '"DECISION": "PASS"' in upper or '"DECISION":"PASS"' in upper:
                return "Reviewer approved the current results."
            return "Reviewer updated the quality review."
        if source == "WriterAgent":
            return "Writer updated the final notes."
        return first_line or f"{source} sent an update."

    def _phase_for_source(self, item: Any) -> str:
        source = getattr(item, "source", "") or ""
        if source == "PlannerAgent":
            return "planning"
        if source == "RetrievalAgent":
            return "retrieving"
        if source == "ReviewerAgent":
            return "reviewing"
        if source == "WriterAgent":
            return "writing"
        return "running"

    def _first_line(self, content: Any) -> str:
        if isinstance(content, str):
            stripped = content.strip()
        else:
            stripped = str(content).strip()
        if not stripped:
            return ""
        return stripped.splitlines()[0][:180]

    def _structured_message_summary(self, source: str, content: Any) -> str | None:
        if not isinstance(content, str):
            return None

        stripped = content.strip()
        if not stripped or stripped[0] not in "{[":
            return None

        if source == "PlannerAgent":
            return "Planner returned a structured search plan."
        if source == "RetrievalAgent":
            return "Retrieval agent returned structured candidate papers."
        if source == "ReviewerAgent":
            upper = stripped.upper()
            if '"DECISION": "REVISE"' in upper or '"DECISION":"REVISE"' in upper:
                return "Reviewer returned a structured revise decision."
            if '"DECISION": "PASS"' in upper or '"DECISION":"PASS"' in upper:
                return "Reviewer returned a structured pass decision."
            return "Reviewer returned a structured review."
        if source == "WriterAgent":
            return "Writer returned structured final notes."
        return "Structured message received."

    def _snapshot_payload_locked(self, job: JobRecord) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "job_id": job.job_id,
            "status": job.status,
            "phase": job.phase,
            "query": job.query,
            "created_at": job.created_at,
            "started_at": job.started_at,
            "finished_at": job.finished_at,
            "current_agent": job.current_agent,
            "latest_message": job.latest_message,
            "event_index": job.event_index,
            "events": [event.as_dict() for event in job.events],
        }
        if job.status == "succeeded":
            payload.update(
                {
                    "result_markdown": job.result_markdown,
                    "result_html": job.result_html,
                    "report_path": job.report_path,
                }
            )
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
        serialized = json.dumps(data, ensure_ascii=False)
        return f"event: {event_name}\ndata: {serialized}\n\n"

    async def shutdown(self) -> None:
        self._threads = {thread for thread in self._threads if thread.is_alive()}


def create_app(
    *,
    output_dir: str = "reports",
    service: PaperAgentWebService | None = None,
) -> FastAPI:
    static_dir = Path(__file__).resolve().parent / "web_static"
    web_service = service or PaperAgentWebService(output_dir=output_dir)

    @asynccontextmanager
    async def lifespan(_: FastAPI):
        yield
        await web_service.shutdown()

    app = FastAPI(title="Paper Retrieval Agent Web", version="0.1.0", lifespan=lifespan)
    app.state.paper_agent_service = web_service
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/", response_class=FileResponse)
    async def index() -> FileResponse:
        return FileResponse(static_dir / "index.html")

    @app.post("/api/jobs", status_code=202)
    async def create_job_endpoint(payload: JobCreateRequest) -> dict[str, str]:
        query = payload.query.strip()
        if not query:
            raise HTTPException(status_code=422, detail="Query must not be empty.")
        job = web_service.create_job(query)
        web_service.schedule_job(job.job_id)
        return {
            "job_id": job.job_id,
            "status": job.status,
            "poll_url": f"/api/jobs/{job.job_id}",
            "events_url": f"/api/jobs/{job.job_id}/events",
        }

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
        stream = web_service.event_stream(job_id, request)
        return StreamingResponse(stream, media_type="text/event-stream")

    return app


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Paper Retrieval Agent web server.")
    parser.add_argument("--host", default="127.0.0.1", help="Host used to bind the web server.")
    parser.add_argument("--port", type=int, default=8000, help="Port used to bind the web server.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="Directory used to save markdown reports.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    uvicorn.run(
        create_app(output_dir=args.output_dir),
        host=args.host,
        port=args.port,
    )
