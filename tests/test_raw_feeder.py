from __future__ import annotations

import io
import os
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from paper_research_agent.core.config import Settings
from paper_research_agent.core.models import DiscoverIntent, PaperRecord
from paper_research_agent.discover import RawFeederService
from paper_research_agent.feeder_store import ProjectPaths
from paper_research_agent.main import run_cli


class FakeCollector:
    def __init__(self) -> None:
        self.calls: list[tuple[str, int | None]] = []

    async def collect_records_for_query_specs(
        self,
        query_specs,
        stage_name: str,
        max_results_per_source: int | None,
        from_year: int | None,
    ):
        self.calls.append((stage_name, len(query_specs)))
        records = [
            PaperRecord(
                title="BrepGPT: Autoregressive B-rep Generation",
                source="arXiv",
                summary="An abstract about direct B-rep generation.",
                authors=["Author A"],
                published="2025-01-01",
                url="https://arxiv.org/abs/2501.12345",
                pdf_url="https://arxiv.org/pdf/2501.12345.pdf",
                doi="",
                source_rank=1,
                matched_query="brep generation",
                query_stage=stage_name,
            ),
            PaperRecord(
                title="BrepGPT: Autoregressive B-rep Generation",
                source="OpenAlex",
                summary="A duplicate abstract from OpenAlex.",
                authors=["Author B"],
                published="2025-01-01",
                url="https://openalex.org/W123456789",
                pdf_url="",
                doi="10.1145/example",
                source_rank=2,
                matched_query="brep generation",
                query_stage=stage_name,
            ),
            PaperRecord(
                title="Diffusion Models for CAD Reconstruction",
                source="Crossref / CAD Journal",
                summary="A second paper with useful abstract evidence.",
                authors=["Author C"],
                published="2024-01-01",
                url="https://example.com/cad-paper",
                pdf_url="",
                doi="10.1000/cad-paper",
                source_rank=1,
                matched_query="cad reconstruction diffusion",
                query_stage=stage_name,
            ),
        ]
        executed = [
            {
                "query": str(item["query"]),
                "sources": [str(item["source"])],
                "stage": stage_name,
                "notes": "Executed during test discovery.",
            }
            for item in query_specs
        ]
        return records, [], executed


class FakeApp:
    def __init__(self, *_args, **_kwargs) -> None:
        self.closed = False

    async def discover(self, *, project_slug: str, query: str, top_k: int = 5):
        batch = type(
            "Batch",
            (),
            {
                "selected_count": 1,
                "written_files": [type("Item", (), {"path": f"projects/{project_slug}/raw/papers/metadata/demo.md"})()],
            },
        )()
        return batch, Path(f"projects/{project_slug}/.feeder/batches/demo.json")

    async def close(self) -> None:
        self.closed = True


class RawFeederTests(unittest.IsolatedAsyncioTestCase):
    async def test_discover_generates_raw_files_batch_and_log(self) -> None:
        fake_root = Path(os.getcwd()) / "projects" / "demo-project"
        fake_paths = ProjectPaths(
            root_dir=fake_root,
            project_file=fake_root / "project.md",
            raw_dir=fake_root / "raw",
            papers_dir=fake_root / "raw" / "papers",
            paper_metadata_dir=fake_root / "raw" / "papers" / "metadata",
            paper_fulltext_dir=fake_root / "raw" / "papers" / "fulltext",
            paper_page_images_dir=fake_root / "raw" / "papers" / "page_images",
            papers_pdf_dir=fake_root / "raw" / "papers_pdf",
            feeder_dir=fake_root / ".feeder",
            batches_dir=fake_root / ".feeder" / "batches",
            log_path=fake_root / ".feeder" / "log.md",
        )
        written_markdown: dict[str, str] = {}
        batch_writes: list[tuple[str, dict]] = []
        log_calls: list[str] = []

        def _capture_write_raw_paper(path: Path, content: str) -> None:
            written_markdown[str(path)] = content

        def _capture_persist_batch(paths: ProjectPaths, batch) -> Path:
            batch_writes.append((str(paths.batches_dir), batch.model_dump()))
            return paths.batches_dir / f"{batch.batch_id}.json"

        def _capture_append_log(paths: ProjectPaths, *, batch, batch_path: Path) -> None:
            log_calls.append(f"{paths.log_path}:{batch_path}")

        with (
            patch("paper_research_agent.discover.ensure_project_paths", return_value=fake_paths),
            patch("paper_research_agent.discover.write_raw_paper", side_effect=_capture_write_raw_paper),
            patch("paper_research_agent.discover.persist_batch", side_effect=_capture_persist_batch),
            patch("paper_research_agent.discover.append_log", side_effect=_capture_append_log),
            patch.object(RawFeederService, "_download_pdf", side_effect=_fake_download_pdf),
            patch.object(RawFeederService, "_process_pdf_with_docling", side_effect=_fake_process_pdf_with_docling),
        ):
            service = RawFeederService(
                settings=_build_settings(),
                output_root=str(fake_root.parent),
                source_collector=FakeCollector(),
                intent_resolver=_fake_intent_resolver,
            )
            batch, batch_path = await service.discover(
                project_slug="demo-project",
                query="recent papers on direct brep generation",
                top_k=2,
            )
            await service.close()

            self.assertEqual(batch.selected_count, 2)
            self.assertEqual(len(written_markdown), 2)
            self.assertTrue(batch_path.name.endswith(".json"))
            self.assertEqual(len(batch_writes), 1)
            self.assertEqual(len(log_calls), 1)
            self.assertTrue(
                any("raw source material" in content.lower() for content in written_markdown.values())
            )
            self.assertEqual(len({item.slug for item in batch.written_files}), 2)
            self.assertTrue(any(item.pdf_downloaded for item in batch.written_files))
            self.assertTrue(any(item.fulltext_extracted for item in batch.written_files))
            self.assertTrue(any(item.page_images_exported for item in batch.written_files))
            normalized_paths = [path.replace("\\", "/") for path in written_markdown]
            self.assertTrue(any("/raw/papers/metadata/" in path and path.endswith(".md") for path in normalized_paths))
            self.assertTrue(any((fake_paths.paper_fulltext_dir / f"{item.slug}.md").exists() for item in batch.written_files))
            self.assertTrue(any((fake_paths.paper_page_images_dir / item.slug / "page-001.png").exists() for item in batch.written_files))

    def test_cli_discover_prints_summary(self) -> None:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = run_cli(
                ["discover", "--project", "demo", "--query", "papers on brep generation", "--top-k", "1"],
                app_factory=lambda settings, output_root: FakeApp(settings, output_root),
                settings=_build_settings(),
            )

        self.assertEqual(exit_code, 0)
        output = stdout.getvalue()
        self.assertIn("Project: demo", output)
        self.assertIn("Selected raw papers: 1", output)


async def _fake_intent_resolver(query: str, project_context: str) -> DiscoverIntent:
    _ = query, project_context
    return DiscoverIntent(
        topic="direct brep generation",
        must_include=["diffusion"],
        must_exclude=["mesh reconstruction"],
        source_hints=["arXiv", "OpenAlex", "Crossref"],
        primary_queries=[
            "direct brep generation diffusion",
            "cad reconstruction diffusion",
        ],
    )


async def _fake_download_pdf(*args, **kwargs) -> bytes:
    pdf_url = kwargs.get("pdf_url") or args[-1]
    return f"fake pdf bytes from {pdf_url}".encode("utf-8")


def _fake_process_pdf_with_docling(*args, **kwargs) -> dict[str, object]:
    fulltext_path = kwargs.get("fulltext_path") or args[1]
    page_image_dir = kwargs.get("page_image_dir") or args[2]
    Path(fulltext_path).parent.mkdir(parents=True, exist_ok=True)
    Path(fulltext_path).write_text("# Introduction\n\nStructured full text.", encoding="utf-8")
    Path(page_image_dir).mkdir(parents=True, exist_ok=True)
    (Path(page_image_dir) / "page-001.png").write_bytes(b"fake image")
    return {
        "fulltext_extracted": True,
        "local_fulltext_path": str(fulltext_path),
        "page_images_exported": True,
        "local_page_image_dir": str(page_image_dir),
        "pdf_error": "",
    }


def _build_settings() -> Settings:
    return Settings(
        model_provider="glm",
        model_api_key="test-key",
        model_base_url="https://example.com",
        model_name="test-model",
        default_headers=None,
        rerank_model_api_key="test-key",
        rerank_model_base_url="https://example.com",
        rerank_model_name="test-model",
        rerank_default_headers=None,
        request_timeout=30.0,
        max_results_per_source=5,
        docling_accelerator="AUTO",
        docling_ocr_backend="torch",
    )


if __name__ == "__main__":
    unittest.main()
