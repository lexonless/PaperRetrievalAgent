from __future__ import annotations

import asyncio
import time
import unittest

from fastapi.testclient import TestClient

from paper_research_agent.langgraph_web import LangGraphWebService, create_app


def _build_state(
    *,
    project_slug: str,
    query: str,
    trace_events: list[dict],
    stop_reason: str = "",
    note_output: dict | None = None,
    note_path: str = "",
    artifacts: dict[str, str] | None = None,
) -> dict:
    return {
        "project": {"slug": project_slug},
        "request": {"raw_query": query},
        "retrieval": {"revision_count": 0, "forced_write": False},
        "note": {
            "research_note_output": note_output,
            "note_path": note_path,
        },
        "run": {
            "trace_events": trace_events,
            "artifacts": artifacts or {},
            "stop_reason": stop_reason,
            "errors": [],
        },
    }


class FakeResearchApplication:
    def __init__(self, states: list[dict] | None = None, error: Exception | None = None) -> None:
        self.states = states or []
        self.error = error
        self.closed = False
        self.calls: list[tuple[str, str, str]] = []

    async def run_stream(self, *, project_slug: str, task: str, pdf_dir: str = ""):
        self.calls.append((project_slug, task, pdf_dir))

        async def generator():
            for state in self.states:
                await asyncio.sleep(0.01)
                yield state

        if self.error is not None:
            raise self.error
        return generator()

    async def close(self) -> None:
        self.closed = True


class LangGraphWebTests(unittest.TestCase):
    def test_index_page_loads(self) -> None:
        service = LangGraphWebService(app_factory=FakeResearchApplication)
        client = TestClient(create_app(service=service))
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Project Slug", response.text)

    def test_create_job_rejects_blank_fields(self) -> None:
        service = LangGraphWebService(app_factory=FakeResearchApplication)
        client = TestClient(create_app(service=service))
        response = client.post("/api/jobs", json={"project_slug": "", "query": "   ", "pdf_dir": ""})
        self.assertEqual(response.status_code, 422)

    def test_select_pdf_dir_returns_chosen_path(self) -> None:
        service = LangGraphWebService(
            app_factory=FakeResearchApplication,
            pdf_dir_selector=lambda: r"D:\papers\medical",
        )
        client = TestClient(create_app(service=service))
        response = client.post("/api/select-pdf-dir")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["pdf_dir"], r"D:\papers\medical")

    def test_job_snapshot_contains_langgraph_progress(self) -> None:
        query = "find papers on multimodal segmentation"
        trace_events_1 = [
            {
                "timestamp": "2026-04-13T10:00:00",
                "step": "prepare_run_context",
                "event_type": "state_update",
                "message": "Initialized project paths, manifest, and runtime search context.",
                "payload": {},
            }
        ]
        trace_events_2 = trace_events_1 + [
            {
                "timestamp": "2026-04-13T10:00:02",
                "step": "task_interpretation_node",
                "event_type": "structured_output",
                "message": "Task interpretation produced structured intent and query planning output.",
                "payload": {},
            },
            {
                "timestamp": "2026-04-13T10:00:05",
                "step": "retrieval_node",
                "event_type": "tool_result",
                "message": "Retrieval node produced candidate papers.",
                "payload": {},
            },
            {
                "timestamp": "2026-04-13T10:00:08",
                "step": "reviewer_node",
                "event_type": "structured_output",
                "message": "Reviewer returned a structured quality decision.",
                "payload": {},
            },
            {
                "timestamp": "2026-04-13T10:00:10",
                "step": "generate_research_note",
                "event_type": "structured_output",
                "message": "Generated the final project research note.",
                "payload": {},
            },
            {
                "timestamp": "2026-04-13T10:00:12",
                "step": "persist_project_artifacts",
                "event_type": "artifact",
                "message": "Persisted project artifacts and updated the source manifest.",
                "payload": {},
            },
        ]

        note_output = {
            "note_title": "Medical Vision Note",
            "project_focus": "Focus on multimodal fusion for segmentation.",
            "retrieval_assessment": "The retrieval covered the main recent directions.",
            "search_scope": ["Recent multimodal medical segmentation work"],
            "core_papers": [
                {
                    "title": "Paper A",
                    "year": 2025,
                    "source": "arXiv",
                    "link": "https://example.com/a",
                    "contribution_summary": "A multimodal segmentation method.",
                    "relevance_note": "Directly targets the project task.",
                    "evidence_note": "Abstract and retrieval evidence align.",
                }
            ],
            "supporting_papers": [],
            "local_context": [],
            "key_observations": ["Fusion quality is central."],
            "open_questions": [],
            "limitations": [],
            "next_steps": ["Read the strongest fusion papers closely."],
        }

        fake_app = FakeResearchApplication(
            states=[
                _build_state(project_slug="med-vision", query=query, trace_events=trace_events_1),
                _build_state(
                    project_slug="med-vision",
                    query=query,
                    trace_events=trace_events_2,
                    stop_reason="completed",
                    note_output=note_output,
                    note_path="projects/med-vision/notes/note.md",
                    artifacts={
                        "note_path": "projects/med-vision/notes/note.md",
                        "retrieval_path": "projects/med-vision/retrieval/retrieval.json",
                        "trace_path": "projects/med-vision/traces/trace.json",
                    },
                ),
            ]
        )
        service = LangGraphWebService(output_dir="projects", app_factory=lambda: fake_app)
        client = TestClient(create_app(service=service))

        create_response = client.post(
            "/api/jobs",
            json={"project_slug": "med-vision", "query": query, "pdf_dir": "D:\\papers"},
        )
        self.assertEqual(create_response.status_code, 202)

        final_payload = self._wait_for_terminal_status(client, create_response.json()["job_id"])
        self.assertEqual(final_payload["status"], "succeeded")
        self.assertEqual(final_payload["phase"], "completed")
        self.assertEqual(final_payload["project_slug"], "med-vision")
        self.assertIn("Retrieval node produced candidate papers.", [event["summary"] for event in final_payload["events"]])
        self.assertIn("projects/med-vision/notes/note.md", final_payload["artifacts"]["note_path"])
        self.assertIn("# Medical Vision Note", final_payload["result_markdown"])
        self.assertIn("**Query:**", final_payload["result_markdown"])
        self.assertNotIn("**Query:**", final_payload["result_html"])
        self.assertTrue(fake_app.closed)
        self.assertEqual(fake_app.calls[0], ("med-vision", query, "D:\\papers"))

    def test_job_failure_sets_failed_status(self) -> None:
        fake_app = FakeResearchApplication(error=RuntimeError("graph boom"))
        service = LangGraphWebService(app_factory=lambda: fake_app)
        client = TestClient(create_app(service=service))

        create_response = client.post(
            "/api/jobs",
            json={"project_slug": "med-vision", "query": "test failure", "pdf_dir": ""},
        )
        self.assertEqual(create_response.status_code, 202)

        final_payload = self._wait_for_terminal_status(client, create_response.json()["job_id"])
        self.assertEqual(final_payload["status"], "failed")
        self.assertEqual(final_payload["phase"], "failed")
        self.assertEqual(final_payload["error"], "graph boom")
        self.assertTrue(fake_app.closed)

    def test_events_endpoint_starts_with_snapshot(self) -> None:
        note_output = {
            "note_title": "Quick Note",
            "project_focus": "",
            "retrieval_assessment": "",
            "search_scope": [],
            "core_papers": [],
            "supporting_papers": [],
            "local_context": [],
            "key_observations": [],
            "open_questions": [],
            "limitations": [],
            "next_steps": [],
        }
        fake_app = FakeResearchApplication(
            states=[
                _build_state(
                    project_slug="demo",
                    query="quick query",
                    trace_events=[
                        {
                            "timestamp": "2026-04-13T10:00:00",
                            "step": "prepare_run_context",
                            "event_type": "state_update",
                            "message": "Initialized project paths, manifest, and runtime search context.",
                            "payload": {},
                        }
                    ],
                    stop_reason="completed",
                    note_output=note_output,
                    artifacts={"note_path": "projects/demo/notes/note.md"},
                )
            ]
        )
        service = LangGraphWebService(app_factory=lambda: fake_app)
        client = TestClient(create_app(service=service))

        create_response = client.post(
            "/api/jobs",
            json={"project_slug": "demo", "query": "quick query", "pdf_dir": ""},
        )
        job_id = create_response.json()["job_id"]

        with client.stream("GET", f"/api/jobs/{job_id}/events") as response:
            self.assertEqual(response.status_code, 200)
            chunks: list[str] = []
            for text in response.iter_text():
                if text:
                    chunks.append(text)
                joined = "".join(chunks)
                if "event: snapshot" in joined and ("event: complete" in joined or "event: error" in joined):
                    break

        joined = "".join(chunks)
        self.assertIn("event: snapshot", joined)
        self.assertTrue("event: complete" in joined or "event: error" in joined)

    def _wait_for_terminal_status(self, client: TestClient, job_id: str) -> dict:
        for _ in range(150):
            response = client.get(f"/api/jobs/{job_id}")
            self.assertEqual(response.status_code, 200)
            payload = response.json()
            if payload["status"] in {"succeeded", "failed"}:
                return payload
            time.sleep(0.02)
        self.fail("Job did not reach a terminal state in time.")


if __name__ == "__main__":
    unittest.main()
