from __future__ import annotations

import asyncio
import time
import unittest
from pathlib import Path
from types import SimpleNamespace

from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage
from fastapi.testclient import TestClient

from paper_research_agent.web import PaperAgentWebService, create_app


class FakeApplication:
    def __init__(self, items: list[object] | None = None, error: Exception | None = None) -> None:
        self.items = items if items is not None else [TaskResult(messages=[], stop_reason="done")]
        self.error = error
        self.closed = False
        self.queries: list[str] = []

    async def run_stream(self, query: str):
        self.queries.append(query)

        async def generator():
            for item in self.items:
                await asyncio.sleep(0.01)
                yield item

        if self.error is not None:
            raise self.error
        return generator()

    async def close(self) -> None:
        self.closed = True


class WebAppTests(unittest.TestCase):
    def test_index_page_loads(self) -> None:
        service = PaperAgentWebService(app_factory=FakeApplication)
        client = TestClient(create_app(service=service))
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Recent steps", response.text)

    def test_create_job_rejects_blank_query(self) -> None:
        service = PaperAgentWebService(app_factory=FakeApplication)
        client = TestClient(create_app(service=service))
        response = client.post("/api/jobs", json={"query": "   "})
        self.assertEqual(response.status_code, 422)

    def test_get_job_returns_404_for_unknown_id(self) -> None:
        service = PaperAgentWebService(app_factory=FakeApplication)
        client = TestClient(create_app(service=service))
        response = client.get("/api/jobs/missing")
        self.assertEqual(response.status_code, 404)

    def test_job_snapshot_contains_phase_and_events(self) -> None:
        fake_app = FakeApplication(
            items=[
                TextMessage(source="PlannerAgent", content='{"topic":"t"}'),
                TextMessage(source="RetrievalAgent", content='{"papers":[]}'),
                TextMessage(source="ReviewerAgent", content='{"decision":"REVISE"}'),
                TextMessage(source="WriterAgent", content='{"report_title":"done"}'),
                TaskResult(messages=[], stop_reason="done"),
            ]
        )

        def fake_save(task_result: object, query: str, output_dir: str = "reports") -> SimpleNamespace:
            return SimpleNamespace(
                report_path=Path(output_dir) / "user_reports" / "result.md",
                report_content=(
                    "# Final Notes\n\n"
                    "## Query Understanding\n\n"
                    "This part should not be rendered.\n\n"
                    "## Candidate Papers\n\n"
                    "- alpha\n- beta\n"
                ),
            )

        service = PaperAgentWebService(
            output_dir="tmp-reports",
            app_factory=lambda: fake_app,
            report_saver=fake_save,
            html_renderer=lambda markdown: "<h1>Final Notes</h1><ul><li>alpha</li><li>beta</li></ul>",
        )
        client = TestClient(create_app(service=service))

        create_response = client.post("/api/jobs", json={"query": "recent papers"})
        self.assertEqual(create_response.status_code, 202)

        final_payload = self._wait_for_terminal_status(client, create_response.json()["job_id"])
        self.assertEqual(final_payload["status"], "succeeded")
        self.assertEqual(final_payload["phase"], "completed")
        self.assertIn("<h1>Final Notes</h1>", final_payload["result_html"])
        self.assertIn("## Query Understanding", final_payload["result_markdown"])
        self.assertNotIn("Query Understanding", final_payload["result_html"])
        self.assertGreaterEqual(len(final_payload["events"]), 4)
        self.assertEqual(final_payload["events"][-1]["phase"], "completed")
        self.assertIn(
            "Retrieval agent returned structured candidate papers.",
            [event["summary"] for event in final_payload["events"]],
        )
        self.assertNotIn("{", [event["summary"] for event in final_payload["events"]])
        self.assertTrue(fake_app.closed)

    def test_job_failure_sets_failed_status(self) -> None:
        fake_app = FakeApplication(error=RuntimeError("boom"))
        service = PaperAgentWebService(
            app_factory=lambda: fake_app,
            report_saver=lambda *args, **kwargs: None,
            html_renderer=lambda markdown: markdown,
        )
        client = TestClient(create_app(service=service))

        create_response = client.post("/api/jobs", json={"query": "test failure"})
        self.assertEqual(create_response.status_code, 202)

        final_payload = self._wait_for_terminal_status(client, create_response.json()["job_id"])
        self.assertEqual(final_payload["status"], "failed")
        self.assertEqual(final_payload["phase"], "failed")
        self.assertEqual(final_payload["error"], "boom")
        self.assertTrue(fake_app.closed)

    def test_events_endpoint_starts_with_snapshot(self) -> None:
        fake_app = FakeApplication(items=[TaskResult(messages=[], stop_reason="done")])

        def fake_save(task_result: object, query: str, output_dir: str = "reports") -> SimpleNamespace:
            return SimpleNamespace(
                report_path=Path(output_dir) / "user_reports" / "result.md",
                report_content="# Final Notes\n\n## Candidate Papers\n\n- alpha\n",
            )

        service = PaperAgentWebService(
            output_dir="tmp-reports",
            app_factory=lambda: fake_app,
            report_saver=fake_save,
            html_renderer=lambda markdown: "<h1>Final Notes</h1>",
        )
        client = TestClient(create_app(service=service))

        create_response = client.post("/api/jobs", json={"query": "recent papers"})
        job_id = create_response.json()["job_id"]

        with client.stream("GET", f"/api/jobs/{job_id}/events") as response:
            self.assertEqual(response.status_code, 200)
            chunks = []
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
        for _ in range(120):
            response = client.get(f"/api/jobs/{job_id}")
            self.assertEqual(response.status_code, 200)
            payload = response.json()
            if payload["status"] in {"succeeded", "failed"}:
                return payload
            time.sleep(0.02)
        self.fail("Job did not reach a terminal state in time.")


if __name__ == "__main__":
    unittest.main()
