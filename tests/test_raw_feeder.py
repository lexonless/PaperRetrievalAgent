from __future__ import annotations

import io
import os
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from paper_research_agent.core.config import Settings
from paper_research_agent.core.models import PaperDict
from paper_research_agent.feeder_store import ProjectPaths
from paper_research_agent.main import run_cli


class FakeCollector:
    def __init__(self) -> None:
        self.calls: list[str] = []

    async def collect_all_source_records(
        self, query: str, stage_name: str,
        max_results_per_source: int | None = None,
        from_year: int | None = None,
        target_source: str = "",
    ) -> tuple[list[PaperDict], list[dict[str, str]]]:
        self.calls.append(query)
        return [
            PaperDict(title="Direct B-Rep Generation with Diffusion Models", source="arXiv",
                        evidence_snippets=["We propose a novel diffusion-based approach for direct B-Rep generation."],
                        authors=["Author A"], date="2025-03-15",
                        url="https://arxiv.org/abs/2503.12345",
                        pdf_url="https://arxiv.org/pdf/2503.12345.pdf",
                        source_rank=1, matched_query=query, query_stage=stage_name),
            PaperDict(title="CAD Reconstruction via Neural Implicit Representations",
                        source="Crossref / CAD Journal",
                        evidence_snippets=["A method for reconstructing CAD models."],
                        authors=["Author C"], date="2024-06-01",
                        url="https://example.com/cad-recon", doi="10.1000/cad-recon",
                        source_rank=1, matched_query=query, query_stage=stage_name),
        ], []

    async def fetch_references(self, openalex_id: str, top_k: int = 5) -> list[PaperDict]:
        return []

    async def fetch_citations(self, openalex_id: str, top_k: int = 5) -> list[PaperDict]:
        return []


class FakeLLM:
    def __init__(self) -> None:
        self.call_count = 0

    def bind_tools(self, tools: list): return self

    async def ainvoke(self, messages):
        return type("R", (), {"content": "", "tool_calls": []})()

    def with_structured_output(self, schema):
        return _FakeStructuredLLM(schema)


class _FakeStructuredLLM:
    def __init__(self, schema) -> None:
        self._schema = schema
        self._call_count = 0

    async def ainvoke(self, messages):
        from paper_research_agent.core.models import QueryDecomposition
        name = getattr(self._schema, "__name__", str(self._schema))
        self._call_count += 1

        if "QueryDecomposition" in name:
            return QueryDecomposition(
                core_techs=["diffusion model", "brep"],
                application_domains=["CAD", "geometric modeling"],
                key_metrics=["reconstruction quality"],
                expanded_terms=["boundary representation", "DDPM"],
            )
        if "RerankResult" in name:
            papers = _extract_papers(messages)
            return {"papers": [
                {"paper_key": p.get("paper_key", "title:test"), "relevance": 4,
                 "reason": "Relevant."} for p in papers
            ]}
        if "JudgeResult" in name:
            return {"converged": True, "reason": "Good coverage."}
        if "RewriteResult" in name:
            return {"refined_query": "diffusion brep cad generation"}
        return None


def _extract_papers(messages) -> list[dict]:
    import json as _json
    try:
        text = ""
        for msg in [messages] if not isinstance(messages, list) else messages:
            c = getattr(msg, "content", str(msg))
            text = c if isinstance(c, str) else " ".join(
                i.get("text", "") if isinstance(i, dict) else str(i)
                for i in (c if isinstance(c, list) else [])
            )
        return _json.loads(text).get("papers", []) if text else []
    except Exception:
        return [{"paper_key": "title:fallback"}]


class FakeApp:
    async def discover(self, *, project_slug, query):
        return (
            {"selected_count": 1, "written_files": [
                {"path": f"projects/{project_slug}/raw/papers/metadata/demo.md"}
            ]},
            Path(f"projects/{project_slug}/.feeder/batches/demo.json"),
        )
    async def close(self): pass


class AgentTests(unittest.IsolatedAsyncioTestCase):
    async def test_agent_searches_and_materializes_papers(self):
        from paper_research_agent.agent import PaperDiscoveryAgent
        from paper_research_agent.agent.pdf import PdfDownloader
        from paper_research_agent.retrieval.ranking import PaperRankingEngine

        fake_root = Path(os.getcwd()) / "projects" / "demo-agent-test"
        fake_paths = ProjectPaths(
            root_dir=fake_root, project_file=fake_root / "project.md",
            raw_dir=fake_root / "raw", papers_dir=fake_root / "raw" / "papers",
            paper_metadata_dir=fake_root / "raw" / "papers" / "metadata",
            paper_fulltext_dir=fake_root / "raw" / "papers" / "fulltext",
            paper_page_images_dir=fake_root / "raw" / "papers" / "page_images",
            papers_pdf_dir=fake_root / "raw" / "papers_pdf",
            feeder_dir=fake_root / ".feeder",
            batches_dir=fake_root / ".feeder" / "batches",
            log_path=fake_root / ".feeder" / "log.md",
        )
        written_md: dict[str, str] = {}

        def _capture(path: Path, content: str):
            written_md[str(path)] = content

        with (
            patch("paper_research_agent.agent.engine.ensure_project_paths", return_value=fake_paths),
            patch("paper_research_agent.agent.engine.write_raw_paper", side_effect=_capture),
            patch.object(PdfDownloader, "_fetch", side_effect=lambda s, u: b"fake"),
        ):
            agent = PaperDiscoveryAgent(
                settings=_build_settings(), output_root=str(fake_root.parent),
                source_collector=FakeCollector(), ranking_engine=PaperRankingEngine(),
            )
            agent._llm = FakeLLM()
            batch_data, batch_path = await agent.discover(
                project_slug="demo-agent-test",
                query="recent papers on direct brep generation",
            )
            await agent.close()

        self.assertEqual(batch_data["selected_count"], 2)
        self.assertEqual(len(written_md), 2)
        self.assertTrue(batch_path.name.endswith(".json"))
        self.assertTrue(any("raw source material" in v.lower() for v in written_md.values()))
        self.assertGreaterEqual(batch_data["candidate_count"], 1)

    def test_cli_discover_prints_summary(self):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = run_cli(
                ["discover", "--project", "demo", "--query", "papers on brep"],
                app_factory=lambda s, o: FakeApp(), settings=_build_settings(),
            )
        self.assertEqual(exit_code, 0)
        self.assertIn("Project: demo", stdout.getvalue())
        self.assertIn("Selected raw papers: 1", stdout.getvalue())


def _build_settings():
    return Settings(
        model_api_key="t", model_base_url="https://x.com",
        model_name="m", default_headers=None,
        rerank_model_api_key="t", rerank_model_base_url="https://x.com",
        rerank_model_name="m", rerank_default_headers=None,
        cross_encoder_model="BAAI/bge-reranker-base",
        cross_encoder_device="cpu", cross_encoder_batch_size=32,
        cross_encoder_max_length=512,
        request_timeout=30.0, max_output_tokens=4096,
        max_results_per_source=5, http_proxy="", openalex_api_key="",
        unpaywall_email="",
    )


if __name__ == "__main__":
    unittest.main()
