from __future__ import annotations

import unittest

from paper_research_agent.core.config import Settings
from paper_research_agent.core.models import PaperRecord
from paper_research_agent.retrieval.ranking import PaperRankingEngine
from paper_research_agent.retrieval.sources import PaperSourceCollector
from paper_research_agent.retrieval.utils import DEFAULT_SOURCE_ORDER


class RetrievalSourcesTests(unittest.IsolatedAsyncioTestCase):
    def test_default_source_order_matches_three_sources(self) -> None:
        self.assertEqual(DEFAULT_SOURCE_ORDER, ("arXiv", "Crossref", "OpenAlex"))

    async def test_collect_records_for_query_specs_reports_all_four_sources(self) -> None:
        collector = PaperSourceCollector(settings=self._build_settings(), client=object())

        async def fake_collect_all_source_records(
            query: str,
            stage_name: str,
            max_results_per_source: int | None = None,
            from_year: int | None = None,
            target_source: str = "",
        ) -> tuple[list[PaperRecord], list[dict[str, str]]]:
            return [], []

        collector.collect_all_source_records = fake_collect_all_source_records  # type: ignore[method-assign]
        _, _, executed_specs = await collector.collect_records_for_query_specs(
            query_specs=["graph rag"],
            stage_name="primary",
            max_results_per_source=5,
            from_year=2021,
        )

        self.assertEqual(len(executed_specs), 1)
        self.assertEqual(executed_specs[0]["sources"], ["arXiv", "Crossref", "OpenAlex"])

    async def test_collect_records_for_source_specific_specs_reports_single_source(self) -> None:
        collector = PaperSourceCollector(settings=self._build_settings(), client=object())

        async def fake_collect_all_source_records(
            query: str,
            stage_name: str,
            max_results_per_source: int | None = None,
            from_year: int | None = None,
            target_source: str = "",
        ) -> tuple[list[PaperRecord], list[dict[str, str]]]:
            self.assertEqual(target_source, "arXiv")
            return [], []

        collector.collect_all_source_records = fake_collect_all_source_records  # type: ignore[method-assign]
        _, _, executed_specs = await collector.collect_records_for_query_specs(
            query_specs=[{"query": "all:\"graph rag\"", "source": "arXiv", "purpose": "precision", "stage": "primary", "notes": "arXiv query"}],
            stage_name="primary",
            max_results_per_source=5,
            from_year=2021,
        )

        self.assertEqual(len(executed_specs), 1)
        self.assertEqual(executed_specs[0]["sources"], ["arXiv"])

    async def test_arxiv_structured_query_is_not_prefixed_twice(self) -> None:
        client = _FakeHttpClient()
        collector = PaperSourceCollector(settings=self._build_settings(), client=client)

        await collector.search_arxiv_records('all:"graph rag" AND all:retrieval', max_results=3)

        self.assertEqual(client.last_params["search_query"], 'all:"graph rag" AND all:retrieval')

    def test_ranking_recognizes_openalex_source_family(self) -> None:
        engine = PaperRankingEngine()
        papers, duplicate_count, raw_source_families = engine.prepare_ranked_papers(
            records=[
                PaperRecord(
                    title="Adapter Tuning for Retrieval",
                    source="OpenAlex",
                    summary="A retrieval paper with enough evidence for eligibility.",
                    authors=["A. Author"],
                    published="2024-12-01",
                    url="https://openalex.org/W1234567890",
                    doi="10.1000/example",
                    source_rank=1,
                    matched_query="adapter tuning retrieval",
                    query_stage="primary",
                )
            ],
            from_year=2020,
            end_year=2026,
            context={
                "query_phrases": ["adapter tuning retrieval"],
                "query_tokens": ["adapter", "tuning", "retrieval"],
                "exclude_phrases": [],
                "allow_review_articles": False,
            },
        )

        self.assertEqual(duplicate_count, 0)
        self.assertEqual(raw_source_families, {"OpenAlex"})
        self.assertEqual(len(papers), 1)

    def test_dedup_merges_same_doi(self) -> None:
        engine = PaperRankingEngine()
        papers, duplicate_count, _ = engine.prepare_ranked_papers(
            records=[
                PaperRecord(
                    title="BrepGPT",
                    source="arXiv",
                    summary="Abstract from arXiv.",
                    authors=["Author A"],
                    published="2025-11-27",
                    url="http://arxiv.org/abs/2511.22171v1",
                    doi="10.1145/example",
                    source_rank=1,
                    matched_query="b-rep generation",
                    query_stage="primary",
                ),
                PaperRecord(
                    title="BrepGPT",
                    source="OpenAlex",
                    summary="Abstract from OpenAlex.",
                    authors=["Author B"],
                    published="2025-11-27",
                    url="https://openalex.org/W1234567890",
                    doi="10.1145/example",
                    source_rank=2,
                    matched_query="b-rep generation",
                    query_stage="primary",
                ),
            ],
            from_year=2021,
            end_year=2026,
            context={
                "query_phrases": ["b-rep generation"],
                "query_tokens": ["brep", "generation"],
                "exclude_phrases": [],
                "allow_review_articles": False,
            },
        )

        self.assertEqual(duplicate_count, 1)
        self.assertEqual(len(papers), 1)
        self.assertIn("arXiv", papers[0]["source"])
        self.assertIn("OpenAlex", papers[0]["source"])

    def test_dedup_merges_by_title_when_one_has_doi_and_other_has_url(self) -> None:
        engine = PaperRankingEngine()
        papers, duplicate_count, _ = engine.prepare_ranked_papers(
            records=[
                PaperRecord(
                    title="BrepGPT: Autoregressive B-rep Generation",
                    source="arXiv",
                    summary="Abstract from arXiv.",
                    authors=["Author A"],
                    published="2025-11-27",
                    url="http://arxiv.org/abs/2511.22171v1",
                    doi="",
                    source_rank=1,
                    matched_query="brep",
                    query_stage="primary",
                ),
                PaperRecord(
                    title="BrepGPT: Autoregressive B-rep Generation",
                    source="OpenAlex",
                    summary="Abstract from OpenAlex.",
                    authors=["Author B"],
                    published="2025-11-27",
                    url="https://openalex.org/W1234567890",
                    doi="10.1145/example",
                    source_rank=2,
                    matched_query="brep",
                    query_stage="primary",
                ),
            ],
            from_year=2021,
            end_year=2026,
            context={
                "query_phrases": ["brep"],
                "query_tokens": ["brep", "generation"],
                "exclude_phrases": [],
                "allow_review_articles": False,
            },
        )

        self.assertEqual(duplicate_count, 1)
        self.assertEqual(len(papers), 1)

    def test_dedup_falls_back_to_title_when_no_doi_or_url(self) -> None:
        engine = PaperRankingEngine()
        papers, duplicate_count, _ = engine.prepare_ranked_papers(
            records=[
                PaperRecord(
                    title="BrepGPT",
                    source="arXiv",
                    summary="Abstract.",
                    authors=["Author A"],
                    published="2025-01-01",
                    url="",
                    doi="",
                    source_rank=1,
                    matched_query="brep",
                    query_stage="primary",
                ),
                PaperRecord(
                    title="BrepGPT",
                    source="OpenAlex",
                    summary="Abstract.",
                    authors=["Author B"],
                    published="2025-01-01",
                    url="",
                    doi="",
                    source_rank=2,
                    matched_query="brep",
                    query_stage="primary",
                ),
            ],
            from_year=2021,
            end_year=2026,
            context={
                "query_phrases": ["brep"],
                "query_tokens": ["brep"],
                "exclude_phrases": [],
                "allow_review_articles": False,
            },
        )

        self.assertEqual(duplicate_count, 1)
        self.assertEqual(len(papers), 1)

    def _build_settings(self) -> Settings:
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
            max_results_per_source=10,
            docling_accelerator="AUTO",
            docling_ocr_backend="torch",
            unpaywall_email="",
        )


if __name__ == "__main__":
    unittest.main()


class _FakeHttpResponse:
    def __init__(self) -> None:
        self.text = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"></feed>"""

    def raise_for_status(self) -> None:
        return None


class _FakeHttpClient:
    def __init__(self) -> None:
        self.last_params: dict[str, object] = {}

    async def get(self, _url: str, params: dict[str, object]):
        self.last_params = dict(params)
        return _FakeHttpResponse()
