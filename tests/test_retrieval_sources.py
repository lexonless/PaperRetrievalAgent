from __future__ import annotations

import unittest

from paper_research_agent.core.config import Settings
from paper_research_agent.core.models import PaperDict
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
            year_from: int | None = None,
            year_to: int | None = None,
            target_source: str = "",
        ) -> tuple[list[PaperDict], list[dict[str, str]]]:
            return [], []

        collector.collect_all_source_records = fake_collect_all_source_records  # type: ignore[method-assign]
        _, _, executed_specs = await collector.collect_records_for_query_specs(
            query_specs=["graph rag"],
            stage_name="primary",
            max_results_per_source=5,
            year_from=2021,
        )

        self.assertEqual(len(executed_specs), 1)
        self.assertEqual(executed_specs[0]["sources"], ["arXiv", "Crossref", "OpenAlex"])

    async def test_collect_records_for_source_specific_specs_reports_single_source(self) -> None:
        collector = PaperSourceCollector(settings=self._build_settings(), client=object())

        async def fake_collect_all_source_records(
            query: str,
            stage_name: str,
            max_results_per_source: int | None = None,
            year_from: int | None = None,
            year_to: int | None = None,
            target_source: str = "",
        ) -> tuple[list[PaperDict], list[dict[str, str]]]:
            self.assertEqual(target_source, "arXiv")
            return [], []

        collector.collect_all_source_records = fake_collect_all_source_records  # type: ignore[method-assign]
        _, _, executed_specs = await collector.collect_records_for_query_specs(
            query_specs=[{"query": "all:\"graph rag\"", "source": "arXiv", "purpose": "precision", "stage": "primary", "notes": "arXiv query"}],
            stage_name="primary",
            max_results_per_source=5,
            year_from=2021,
        )

        self.assertEqual(len(executed_specs), 1)
        self.assertEqual(executed_specs[0]["sources"], ["arXiv"])

    async def test_arxiv_structured_query_is_not_prefixed_twice(self) -> None:
        client = _FakeHttpClient()
        collector = PaperSourceCollector(settings=self._build_settings(), client=client)

        await collector.search_arxiv_records('all:"graph rag" AND all:retrieval', max_results=3)

        self.assertEqual(client.last_params["search_query"], 'all:"graph rag" AND all:retrieval')

    def _build_settings(self) -> Settings:
        return Settings(
            model_api_key="test-key",
            model_base_url="https://example.com",
            model_name="test-model",
            default_headers=None,
            rerank_model_api_key="test-key",
            rerank_model_base_url="https://example.com",
            rerank_model_name="test-model",
            rerank_default_headers=None,
            cross_encoder_model="BAAI/bge-reranker-base",
            cross_encoder_device="cpu",
            cross_encoder_batch_size=32,
            cross_encoder_max_length=512,
            request_timeout=30.0,
            max_output_tokens=4096,
            max_results_per_source=10,
            http_proxy="",
            openalex_api_key="",
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
