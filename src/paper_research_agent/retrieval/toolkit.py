from __future__ import annotations

import json
from typing import Any

import httpx

from ..core.config import Settings
from .ranking import PaperRankingEngine
from .sources import PaperSourceCollector
from .verification import PaperVerificationEngine


class PaperSearchToolkit:
    def __init__(self, settings: Settings, rerank_model_client: Any | None = None) -> None:
        self._settings = settings
        self._latest_task_interpretation: dict[str, Any] | None = None
        self._client = httpx.AsyncClient(
            timeout=settings.request_timeout,
            headers={
                "User-Agent": "paper-retrieval-agent/0.1 (+LangGraph research assistant)",
                "Accept": "*/*",
            },
            follow_redirects=True,
        )
        self._sources = PaperSourceCollector(settings, self._client)
        self._ranking = PaperRankingEngine(rerank_model_client=rerank_model_client)
        self._verification = PaperVerificationEngine(
            self._client,
            score_eligibility=self._ranking.score_eligibility,
            finalize_ranked_papers=self._ranking.finalize_ranked_papers,
        )

    async def close(self) -> None:
        await self._client.aclose()

    def set_latest_task_interpretation(self, payload: dict[str, Any]) -> None:
        self._latest_task_interpretation = payload

    def clear_latest_task_interpretation(self) -> None:
        self._latest_task_interpretation = None

    def set_local_pdf_paths(self, paths: list[str]) -> None:
        self._sources.set_local_pdf_paths(paths)

    def clear_local_pdf_paths(self) -> None:
        self._sources.clear_local_pdf_paths()

    async def retrieve_candidates_from_plan(
        self,
        top_k: int = 10,
        max_results_per_source: int | None = None,
    ) -> str:
        task_interpretation = self._latest_task_interpretation
        if not isinstance(task_interpretation, dict):
            return json.dumps(
                {
                    "error": "No task interpretation is available yet.",
                    "hint": "Run task interpretation first so the workflow can prepare the latest retrieval input.",
                },
                ensure_ascii=False,
                indent=2,
            )

        retrieval_plan = self._sources.build_retrieval_plan(task_interpretation)
        if not retrieval_plan:
            return json.dumps(
                {
                    "error": "The latest task interpretation did not provide a usable query.",
                    "request_excerpt": task_interpretation,
                },
                ensure_ascii=False,
                indent=2,
            )

        all_records = []
        all_source_errors = []
        executed_query_specs = []
        intent = task_interpretation.get("intent", {}) if isinstance(task_interpretation, dict) else {}
        time_range = intent.get("time_range", {}) if isinstance(intent, dict) else {}
        from_year = time_range.get("start_year") if isinstance(time_range.get("start_year"), int) else None
        end_year = time_range.get("end_year") if isinstance(time_range.get("end_year"), int) else None

        for stage_name, query_specs in retrieval_plan:
            if not query_specs:
                continue
            records, source_errors, executed_specs = await self._sources.collect_records_for_query_specs(
                query_specs=query_specs,
                stage_name=stage_name,
                max_results_per_source=max_results_per_source,
                from_year=from_year,
            )
            all_records.extend(records)
            all_source_errors.extend(source_errors)
            executed_query_specs.extend(executed_specs)
            context = self._ranking.build_retrieval_context(task_interpretation, executed_query_specs)
            provisional_papers, _, _ = self._ranking.prepare_ranked_papers(
                records=all_records,
                from_year=from_year,
                end_year=end_year,
                context=context,
            )
            if not self._ranking.should_expand_queries(provisional_papers):
                break

        context = self._ranking.build_retrieval_context(task_interpretation, executed_query_specs)
        local_records, local_errors, local_library_debug = await self._sources.collect_local_pdf_records(
            task_interpretation=task_interpretation,
            context=context,
        )
        all_records.extend(local_records)
        all_source_errors.extend(local_errors)

        papers, retrieval_duplicate_count, raw_source_families = self._ranking.prepare_ranked_papers(
            records=all_records,
            from_year=from_year,
            end_year=end_year,
            context=context,
        )
        papers = await self._ranking.rerank_with_model(papers, task_interpretation)
        papers = await self._verification.verify_promising_candidates(papers, context)
        papers.sort(key=self._ranking.retrieval_paper_sort_key)
        papers = papers[: max(1, min(top_k, 50))]

        payload = self._ranking.build_retrieval_payload(
            papers=papers,
            raw_source_families=raw_source_families,
            retrieval_duplicate_count=retrieval_duplicate_count,
            source_errors=all_source_errors,
            executed_query_specs=executed_query_specs,
            local_library_debug=local_library_debug,
        )
        return json.dumps(payload, ensure_ascii=False, indent=2)
