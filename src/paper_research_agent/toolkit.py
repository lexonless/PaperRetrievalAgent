from __future__ import annotations

import asyncio
import json
import re
import xml.etree.ElementTree as ET
from io import BytesIO
from typing import Any

import httpx
from autogen_core.models import SystemMessage, UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient

from .config import Settings
from .models import PaperRecord
from .normalization import normalize_string_list, normalize_text

DEFAULT_SOURCE_ORDER = ("arXiv", "Crossref", "OpenAlex")
PRIMARY_STAGE = "primary"
TOPIC_FALLBACK_STAGE = "topic_fallback"

HARD_NOISE_PHRASES = (
    "decision letter",
    "editorial",
    "correction",
    "erratum",
    "table of contents",
    "front matter",
    "preface",
    "call for papers",
)

REVIEW_ARTICLE_PHRASES = (
    "systematic review",
    "survey",
    "review",
    "overview",
    "survey and outlook",
)

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "highly",
    "how",
    "in",
    "into",
    "is",
    "latest",
    "learning",
    "method",
    "methods",
    "model",
    "models",
    "of",
    "on",
    "or",
    "paper",
    "papers",
    "recent",
    "relevant",
    "research",
    "task",
    "tasks",
    "that",
    "the",
    "their",
    "then",
    "to",
    "using",
    "via",
    "what",
    "where",
    "with",
}

RERANK_SYSTEM_MESSAGE = """You are a scholarly retrieval reranking model.

You receive a search task and a small batch of candidate papers.
Judge each paper independently using only the provided evidence.

Output requirements:
- Return exactly one JSON object and nothing else.
- Do not use markdown code fences.
- Use the provided paper_id values unchanged.

Judgment rules:
- relevance measures topical closeness to the user request: high, medium, or low.
- task_fit measures whether the paper is directly doing the requested task or only loosely/partially related:
  - direct: substantially addresses the user's requested task
  - related: meaningfully relevant, but not an exact task match
  - weak: only weakly related or mostly off-target
- verification measures how reliable the judgment is from the current evidence only:
  - strong: the provided abstract or PDF text clearly supports the judgment
  - partial: some support exists, but important ambiguity remains
  - weak: current evidence is too thin to trust strongly

Important constraints:
- Do not require any specific wording from the paper.
- Do not assume every task has a strict input/output template.
- Prefer recall-friendly judgments: if a paper might still be useful, choose related rather than weak.
- Only use weak when the paper is clearly loose, generic, or off-target for the requested task.

Required JSON schema:
{
  "papers": [
    {
      "paper_id": "p0",
      "relevance": "high" | "medium" | "low",
      "task_fit": "direct" | "related" | "weak",
      "verification": "strong" | "partial" | "weak",
      "score": 0-100,
      "reason": "short evidence-based explanation"
    }
  ]
}
"""

MAX_RERANK_CANDIDATES = 24
RERANK_BATCH_SIZE = 6


class PaperSearchToolkit:
    def __init__(
        self,
        settings: Settings,
        rerank_model_client: OpenAIChatCompletionClient | None = None,
    ) -> None:
        self._settings = settings
        self._latest_retrieval_request: dict[str, Any] | None = None
        self._rerank_model_client = rerank_model_client
        self._client = httpx.AsyncClient(
            timeout=settings.request_timeout,
            headers={
                "User-Agent": "paper-retrieval-agent/0.1 (+AutoGen starter)",
                "Accept": "*/*",
            },
            follow_redirects=True,
        )

    async def close(self) -> None:
        await self._client.aclose()

    def set_latest_retrieval_request(self, payload: dict[str, Any]) -> None:
        self._latest_retrieval_request = payload

    def clear_latest_retrieval_request(self) -> None:
        self._latest_retrieval_request = None

    async def retrieve_candidates_from_plan(
        self,
        top_k: int = 10,
        max_results_per_source: int | None = None,
        query: str = "",
    ) -> str:
        """High-level retrieval tool for agents.

        Allowed parameters:
        - top_k: number of final candidates to keep
        - max_results_per_source: raw recall limit per source
        - query: optional retrieval query override while still inheriting planner query planning
        """
        retrieval_request = self._latest_retrieval_request
        if not isinstance(retrieval_request, dict):
            return json.dumps(
                {
                    "error": "No retrieval request is available yet.",
                    "hint": "Run PlannerAgent first so the team can prepare the latest retrieval request.",
                },
                ensure_ascii=False,
                indent=2,
            )

        override_query = normalize_text(query)
        retrieval_plan = self._build_retrieval_plan(retrieval_request, override_query)
        if not retrieval_plan:
            return json.dumps(
                {
                    "error": "The latest retrieval request did not provide a usable query.",
                    "request_excerpt": retrieval_request,
                },
                ensure_ascii=False,
                indent=2,
            )

        all_records: list[PaperRecord] = []
        all_source_errors: list[dict[str, str]] = []
        executed_query_specs: list[dict[str, Any]] = []
        from_year = retrieval_request.get("from_year") if isinstance(retrieval_request.get("from_year"), int) else None
        end_year = retrieval_request.get("end_year") if isinstance(retrieval_request.get("end_year"), int) else None

        for stage_name, query_specs in retrieval_plan:
            if not query_specs:
                continue

            records, source_errors, executed_specs = await self._collect_records_for_query_specs(
                query_specs=query_specs,
                stage_name=stage_name,
                max_results_per_source=max_results_per_source,
                from_year=from_year,
            )
            all_records.extend(records)
            all_source_errors.extend(source_errors)
            executed_query_specs.extend(executed_specs)

            context = self._build_retrieval_context(retrieval_request, executed_query_specs)
            provisional_papers, _, _ = self._prepare_ranked_papers(
                records=all_records,
                from_year=from_year,
                end_year=end_year,
                context=context,
            )
            if not self._should_expand_queries(provisional_papers):
                break

        planner_query_source = retrieval_request.get("planner_query_source")
        if not isinstance(planner_query_source, dict):
            planner_query_source = {}
        planner_query_source = dict(planner_query_source)
        planner_query_source["effective_query"] = executed_query_specs[0]["query"] if executed_query_specs else ""
        planner_query_source["used_override_query"] = bool(override_query)
        planner_query_source["executed_queries"] = [item["query"] for item in executed_query_specs]
        planner_query_source["fallback_used"] = any(
            str(item.get("stage", "")).strip().lower().startswith(TOPIC_FALLBACK_STAGE)
            for item in executed_query_specs
        )

        context = self._build_retrieval_context(retrieval_request, executed_query_specs)
        papers, retrieval_duplicate_count, raw_source_families = self._prepare_ranked_papers(
            records=all_records,
            from_year=from_year,
            end_year=end_year,
            context=context,
        )
        papers = await self._rerank_with_model(papers, retrieval_request)
        papers = await self._verify_promising_candidates(papers, context)
        papers = self._score_filter_sort_papers(papers, context)
        papers = papers[: max(1, min(top_k, 50))]

        retrieval_payload = self._build_retrieval_payload(
            papers=papers,
            raw_source_families=raw_source_families,
            retrieval_duplicate_count=retrieval_duplicate_count,
            source_errors=all_source_errors,
            executed_query_specs=executed_query_specs,
            planner_query_source=planner_query_source,
        )
        return json.dumps(retrieval_payload, ensure_ascii=False, indent=2)

    def _build_retrieval_plan(
        self,
        retrieval_request: dict[str, Any],
        override_query: str,
    ) -> list[tuple[str, list[str]]]:
        primary_queries = normalize_string_list(retrieval_request.get("planned_queries"))
        fallback_queries = normalize_string_list(retrieval_request.get("fallback_queries"))

        if override_query:
            primary_queries = normalize_string_list([override_query, *primary_queries])

        if not primary_queries and fallback_queries:
            primary_queries = [fallback_queries[0]]
            fallback_queries = fallback_queries[1:]

        primary_query_texts = set(primary_queries)
        ordered_fallbacks = [
            query for query in fallback_queries
            if query and query not in primary_query_texts
        ]

        retrieval_plan: list[tuple[str, list[str]]] = [(PRIMARY_STAGE, primary_queries)]
        for index, query in enumerate(ordered_fallbacks[:3], start=1):
            retrieval_plan.append((f"{TOPIC_FALLBACK_STAGE}_{index}", [query]))
        return retrieval_plan

    async def _collect_records_for_query_specs(
        self,
        query_specs: list[str],
        stage_name: str,
        max_results_per_source: int | None,
        from_year: int | None,
    ) -> tuple[list[PaperRecord], list[dict[str, str]], list[dict[str, Any]]]:
        records: list[PaperRecord] = []
        source_errors: list[dict[str, str]] = []
        executed_specs: list[dict[str, Any]] = []

        for query_text in query_specs:
            query = normalize_text(query_text)
            if not query:
                continue
            query_records, query_errors = await self._collect_all_source_records(
                query=query,
                stage_name=stage_name,
                max_results_per_source=max_results_per_source,
                from_year=from_year,
            )
            records.extend(query_records)
            source_errors.extend(query_errors)
            executed_specs.append(
                {
                    "query": query,
                    "sources": list(DEFAULT_SOURCE_ORDER),
                    "stage": stage_name,
                }
            )

        return records, source_errors, executed_specs

    async def _collect_all_source_records(
        self,
        query: str,
        stage_name: str,
        max_results_per_source: int | None = None,
        from_year: int | None = None,
    ) -> tuple[list[PaperRecord], list[dict[str, str]]]:
        selected_sources = list(DEFAULT_SOURCE_ORDER)
        tasks: list[tuple[str, Any]] = []
        for source_name in selected_sources:
            if source_name == "arXiv":
                tasks.append(("arXiv", self._search_arxiv_records(query, max_results=max_results_per_source)))
            elif source_name == "Crossref":
                tasks.append(("Crossref", self._search_crossref_records(query, max_results=max_results_per_source, from_year=from_year)))
            elif source_name == "OpenAlex":
                tasks.append(("OpenAlex", self._search_openalex_records(query, max_results=max_results_per_source, from_year=from_year)))

        rendered_results = await asyncio.gather(*(task for _, task in tasks), return_exceptions=True)

        records: list[PaperRecord] = []
        source_errors: list[dict[str, str]] = []
        for (source_name, _), rendered in zip(tasks, rendered_results, strict=False):
            if isinstance(rendered, Exception):
                source_errors.append(
                    {
                        "source": source_name,
                        "error": str(rendered),
                        "query": query,
                    }
                )
                continue

            for record in rendered:
                records.append(
                    PaperRecord(
                        title=record.title,
                        source=record.source,
                        summary=record.summary,
                        authors=record.authors,
                        published=record.published,
                        url=record.url,
                        pdf_url=record.pdf_url,
                        doi=record.doi,
                        source_rank=record.source_rank,
                        matched_query=query,
                        query_stage=stage_name,
                    )
                )
        return records, source_errors

    def _prepare_ranked_papers(
        self,
        records: list[PaperRecord],
        from_year: int | None,
        end_year: int | None,
        context: dict[str, Any],
    ) -> tuple[list[dict[str, Any]], int, set[str]]:
        papers: list[dict[str, Any]] = []
        raw_source_families: set[str] = set()
        for record in records:
            title = normalize_text(record.title)
            source = normalize_text(record.source)
            if not title or not source:
                continue

            lowered_source = source.lower()
            if lowered_source.startswith("arxiv"):
                raw_source_families.add("arXiv")
            elif lowered_source.startswith("crossref"):
                raw_source_families.add("Crossref")
            elif lowered_source.startswith("openalex"):
                raw_source_families.add("OpenAlex")
            else:
                raw_source_families.add(source)
            published = normalize_text(record.published)
            year = self._extract_year(published)
            summary = normalize_text(record.summary)

            evidence_level = "abstract" if summary else "title_only"
            verification_status = "partial" if summary else "weak"

            time_range_status = "unknown"
            if year is not None:
                in_lower_bound = not isinstance(from_year, int) or year >= from_year
                in_upper_bound = end_year is None or year <= end_year
                time_range_status = "in_range" if in_lower_bound and in_upper_bound else "out_of_range"

            papers.append(
                {
                    "title": title,
                    "source": source,
                    "year": year if year is not None else "",
                    "date": published,
                    "url": normalize_text(record.url),
                    "doi": normalize_text(record.doi),
                    "_pdf_url": self._normalize_pdf_url(record.pdf_url or record.url),
                    "authors": [
                        normalize_text(author)
                        for author in record.authors[:8]
                        if normalize_text(author)
                    ],
                    "verification_status": verification_status,
                    "evidence_level": evidence_level,
                    "time_range_status": time_range_status,
                    "evidence_snippets": [summary] if summary else [],
                    "_matched_queries": [record.matched_query] if record.matched_query else [],
                    "_source_ranks": [record.source_rank] if record.source_rank else [],
                    "_query_stages": [record.query_stage] if record.query_stage else [],
                    "_retrieval_score": 0,
                }
            )

        papers, retrieval_duplicate_count = self._deduplicate_retrieval_papers(papers)
        papers = self._score_filter_sort_papers(papers, context)
        return papers, retrieval_duplicate_count, raw_source_families

    def _build_retrieval_context(
        self,
        retrieval_request: dict[str, Any],
        executed_query_specs: list[dict[str, Any]],
    ) -> dict[str, Any]:
        query_phrases: list[str] = []
        for item in executed_query_specs:
            query = normalize_text(item.get("query", ""))
            if query:
                query_phrases.append(query)

        topic = normalize_text(retrieval_request.get("topic", ""))
        user_intent = normalize_text(retrieval_request.get("user_intent", ""))
        focus_areas = normalize_string_list(retrieval_request.get("focus_areas"))
        exclude_areas = normalize_string_list(retrieval_request.get("exclude_areas"))

        query_phrases.extend(focus_areas)
        if topic:
            query_phrases.append(topic)

        combined_text = " ".join([topic, user_intent, *query_phrases]).lower()
        allow_review_articles = any(term in combined_text for term in REVIEW_ARTICLE_PHRASES)

        return {
            "query_phrases": list(dict.fromkeys(query_phrases)),
            "query_tokens": self._extract_match_tokens([*query_phrases, topic, user_intent]),
            "exclude_phrases": normalize_string_list(exclude_areas, for_matching=True),
            "allow_review_articles": allow_review_articles,
        }

    def _should_expand_queries(self, papers: list[dict[str, Any]]) -> bool:
        supported_evidence_count = self._count_supported_evidence(papers)
        return len(papers) < 15 or supported_evidence_count < 5

    def _count_supported_evidence(self, papers: list[dict[str, Any]]) -> int:
        count = 0
        for paper in papers:
            if not isinstance(paper, dict):
                continue
            verification_status = str(paper.get("verification_status", "")).strip().lower()
            evidence_level = str(paper.get("evidence_level", "")).strip().lower()
            evidence_snippets = paper.get("evidence_snippets")
            if (
                verification_status in {"partial", "verified"}
                and evidence_level in {"abstract", "excerpt"}
                and isinstance(evidence_snippets, list)
                and any(normalize_text(item) for item in evidence_snippets)
            ):
                count += 1
        return count

    async def _rerank_with_model(
        self,
        papers: list[dict[str, Any]],
        retrieval_request: dict[str, Any],
    ) -> list[dict[str, Any]]:
        if self._rerank_model_client is None or len(papers) < 2:
            return papers

        updated_papers = [dict(paper) for paper in papers]
        candidate_limit = min(len(updated_papers), MAX_RERANK_CANDIDATES)
        if candidate_limit <= 1:
            return updated_papers

        candidate_items = [
            (index, updated_papers[index])
            for index in range(candidate_limit)
        ]
        judgments_by_paper_id: dict[str, dict[str, Any]] = {}

        for start in range(0, len(candidate_items), RERANK_BATCH_SIZE):
            batch = candidate_items[start : start + RERANK_BATCH_SIZE]
            if not batch:
                continue
            try:
                batch_judgments = await self._judge_rerank_batch(retrieval_request, batch)
            except Exception:
                continue
            for judgment in batch_judgments:
                paper_id = normalize_text(judgment.get("paper_id", ""))
                if paper_id:
                    judgments_by_paper_id[paper_id] = judgment

        if not judgments_by_paper_id:
            return updated_papers

        for index, paper in candidate_items:
            paper_id = f"p{index}"
            judgment = judgments_by_paper_id.get(paper_id)
            if judgment is None:
                continue
            updated_papers[index] = self._apply_rerank_judgment(paper, judgment)

        updated_papers.sort(key=self._retrieval_paper_sort_key)
        return updated_papers

    async def _judge_rerank_batch(
        self,
        retrieval_request: dict[str, Any],
        batch: list[tuple[int, dict[str, Any]]],
    ) -> list[dict[str, Any]]:
        if self._rerank_model_client is None or not batch:
            return []

        task_payload = {
            "topic": normalize_text(retrieval_request.get("topic", "")),
            "user_intent": normalize_text(retrieval_request.get("user_intent", "")),
            "focus_areas": normalize_string_list(retrieval_request.get("focus_areas")),
            "exclude_areas": normalize_string_list(retrieval_request.get("exclude_areas")),
            "time_range": {
                "from_year": retrieval_request.get("from_year") if isinstance(retrieval_request.get("from_year"), int) else "",
                "end_year": retrieval_request.get("end_year") if isinstance(retrieval_request.get("end_year"), int) else "",
            },
            "papers": [
                {
                    "paper_id": f"p{index}",
                    "title": normalize_text(paper.get("title", "")),
                    "year": paper.get("year") if isinstance(paper.get("year"), int) else "",
                    "source": normalize_text(paper.get("source", "")),
                    "matched_queries": [
                        normalize_text(item)
                        for item in paper.get("_matched_queries", []) or []
                        if normalize_text(item)
                    ],
                    "evidence_level": normalize_text(paper.get("evidence_level", "")),
                    "evidence_text": self._build_rerank_evidence_text(paper),
                }
                for index, paper in batch
            ],
        }

        result = await self._rerank_model_client.create(
            [
                SystemMessage(content=RERANK_SYSTEM_MESSAGE),
                UserMessage(content=json.dumps(task_payload, ensure_ascii=False), source="user"),
            ],
            json_output=True,
        )
        return self._parse_rerank_response(result.content)

    def _build_rerank_evidence_text(self, paper: dict[str, Any]) -> str:
        evidence_snippets = paper.get("evidence_snippets")
        snippets: list[str] = []
        if isinstance(evidence_snippets, list):
            for item in evidence_snippets:
                cleaned = normalize_text(item)
                if cleaned:
                    snippets.append(cleaned)
        evidence_text = snippets[0] if snippets else ""
        if not evidence_text:
            evidence_text = normalize_text(paper.get("title", ""))
        evidence_level = normalize_text(paper.get("evidence_level", ""), for_matching=True)
        if evidence_level == "abstract":
            return evidence_text
        return evidence_text[:900]

    def _parse_rerank_response(self, raw_content: Any) -> list[dict[str, Any]]:
        if isinstance(raw_content, str):
            cleaned = raw_content.strip()
            if cleaned.startswith("```"):
                cleaned = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", cleaned)
                cleaned = re.sub(r"\s*```$", "", cleaned)
            cleaned = cleaned.strip()
            if not cleaned:
                return []
            try:
                payload = json.loads(cleaned)
            except json.JSONDecodeError:
                return []
        elif isinstance(raw_content, dict):
            payload = raw_content
        else:
            return []

        if not isinstance(payload, dict):
            return []
        items = payload.get("papers")
        if not isinstance(items, list):
            return []

        normalized: list[dict[str, Any]] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            paper_id = normalize_text(item.get("paper_id", ""))
            if not paper_id:
                continue
            relevance = self._normalize_enum_value(str(item.get("relevance", "") or ""), {"high", "medium", "low"}, "low")
            task_fit = self._normalize_enum_value(str(item.get("task_fit", "") or ""), {"direct", "related", "weak"}, "weak")
            verification = self._normalize_enum_value(str(item.get("verification", "") or ""), {"strong", "partial", "weak"}, "weak")
            score = item.get("score")
            if not isinstance(score, int):
                try:
                    score = int(score)
                except (TypeError, ValueError):
                    score = 0
            reason = normalize_text(item.get("reason", ""))
            normalized.append(
                {
                    "paper_id": paper_id,
                    "relevance": relevance,
                    "task_fit": task_fit,
                    "verification": verification,
                    "score": max(0, min(score, 100)),
                    "reason": reason,
                }
            )
        return normalized

    def _apply_rerank_judgment(
        self,
        paper: dict[str, Any],
        judgment: dict[str, Any],
    ) -> dict[str, Any]:
        updated = dict(paper)
        updated["_rerank_relevance"] = self._normalize_enum_value(
            str(judgment.get("relevance", "") or ""),
            {"high", "medium", "low"},
            "low",
        )
        updated["_rerank_task_fit"] = self._normalize_enum_value(
            str(judgment.get("task_fit", "") or ""),
            {"direct", "related", "weak"},
            "weak",
        )
        updated["_rerank_verification"] = self._normalize_enum_value(
            str(judgment.get("verification", "") or ""),
            {"strong", "partial", "weak"},
            "weak",
        )
        score = judgment.get("score")
        if not isinstance(score, int):
            try:
                score = int(score)
            except (TypeError, ValueError):
                score = 0
        updated["_rerank_score"] = max(0, min(score, 100))
        updated["_rerank_reason"] = normalize_text(judgment.get("reason", ""))
        return updated

    def _normalize_enum_value(self, value: str, allowed: set[str], default: str) -> str:
        normalized = normalize_text(value, for_matching=True)
        return normalized if normalized in allowed else default

    def _build_retrieval_payload(
        self,
        papers: list[dict[str, Any]],
        raw_source_families: set[str],
        retrieval_duplicate_count: int,
        source_errors: list[dict[str, str]] | None,
        executed_query_specs: list[dict[str, Any]],
        planner_query_source: dict[str, Any] | None,
    ) -> dict[str, Any]:
        coverage_gaps: list[str] = []
        normalized_source_errors = source_errors if isinstance(source_errors, list) else []
        for item in normalized_source_errors:
            if not isinstance(item, dict):
                continue
            source_name = normalize_text(item.get("source", ""))
            error_text = normalize_text(item.get("error", ""))
            if source_name:
                coverage_gaps.append(f"{source_name} retrieval failed: {error_text}")

        if len(papers) < 5:
            coverage_gaps.append("Fewer than 5 candidate papers were retained after staged retrieval, deduplication, and noise filtering.")

        supported_evidence_count = self._count_supported_evidence(papers)
        if supported_evidence_count < 3:
            coverage_gaps.append("Fewer than 3 candidates currently have non-weak evidence suitable for a confident PASS.")

        return {
            "sources_used": sorted(raw_source_families),
            "queries_executed": [
                {
                    "query": item["query"],
                    "sources": item["sources"],
                    "notes": (
                        "Planner query executed in the primary retrieval phase."
                        if str(item.get("stage", "")).strip().lower() == PRIMARY_STAGE
                        else "Fallback query executed because earlier retrieval remained sparse."
                        if str(item.get("stage", "")).strip().lower().startswith(TOPIC_FALLBACK_STAGE)
                        else "Derived from the latest planner payload."
                    ),
                }
                for item in executed_query_specs
            ],
            "papers": [self._strip_internal_paper_fields(paper) for paper in papers],
            "dedup_notes": [
                f"Retrieved papers were deduplicated by DOI, URL, or normalized title; {retrieval_duplicate_count} duplicate entries were merged."
            ],
            "missing_metadata": [
                "Title-only candidates remain weak until abstract or excerpt evidence is available."
            ],
            "coverage_gaps": coverage_gaps,
            "source_errors": normalized_source_errors,
            "planner_query_source": planner_query_source if isinstance(planner_query_source, dict) else {},
        }

    def _strip_internal_paper_fields(self, paper: dict[str, Any]) -> dict[str, Any]:
        return {
            key: value
            for key, value in paper.items()
            if not key.startswith("_")
        }

    def _score_filter_sort_papers(
        self,
        papers: list[dict[str, Any]],
        context: dict[str, Any],
    ) -> list[dict[str, Any]]:
        scored_papers: list[dict[str, Any]] = []
        for paper in papers:
            scored = self._apply_relevance_scoring(paper, context)
            if scored is None:
                continue
            scored_papers.append(scored)

        scored_papers.sort(key=self._retrieval_paper_sort_key)
        return scored_papers

    def _apply_relevance_scoring(
        self,
        paper: dict[str, Any],
        context: dict[str, Any],
    ) -> dict[str, Any] | None:
        title_text = normalize_text(paper.get("title", ""), for_matching=True)
        evidence_snippets = paper.get("evidence_snippets")
        evidence_parts: list[str] = []
        if isinstance(evidence_snippets, list):
            for item in evidence_snippets:
                cleaned = normalize_text(item)
                if cleaned:
                    evidence_parts.append(cleaned)
        evidence_text = normalize_text(" ".join(evidence_parts), for_matching=True)
        combined_text = " ".join(part for part in [title_text, evidence_text] if part).strip()

        if not combined_text:
            return None

        query_phrases = [
            normalize_text(item, for_matching=True)
            for item in paper.get("_matched_queries", []) or context.get("query_phrases", [])
            if normalize_text(item, for_matching=True)
        ]
        query_phrases = list(dict.fromkeys(query_phrases))
        query_tokens = set(context.get("query_tokens", []))

        title_phrase_hits = [phrase for phrase in query_phrases if phrase and phrase in title_text]
        evidence_phrase_hits = [phrase for phrase in query_phrases if phrase and phrase in evidence_text and phrase not in title_phrase_hits]

        title_tokens = set(title_text.split())
        evidence_tokens = set(evidence_text.split())
        title_token_hits = sorted(query_tokens.intersection(title_tokens))
        evidence_token_hits = sorted(query_tokens.intersection(evidence_tokens) - set(title_token_hits))
        exclude_hits = [
            phrase for phrase in context.get("exclude_phrases", [])
            if phrase and phrase in combined_text
        ]

        if any(phrase in combined_text for phrase in HARD_NOISE_PHRASES):
            return None

        if (
            not context.get("allow_review_articles", False)
            and any(phrase in title_text for phrase in REVIEW_ARTICLE_PHRASES)
        ):
            return None

        positive_signal_count = len(title_phrase_hits) + len(evidence_phrase_hits) + len(title_token_hits) + len(evidence_token_hits)
        if exclude_hits and positive_signal_count < 3:
            return None

        title_signal_count = len(title_phrase_hits) + len(title_token_hits)
        evidence_signal_count = len(evidence_phrase_hits) + len(evidence_token_hits)
        score = 0
        score += min(len(title_phrase_hits), 1) * 4
        score += min(len(evidence_phrase_hits), 1) * 3
        score += min(len(title_token_hits), 3)
        score += min(len(evidence_token_hits), 3)

        source_ranks = [
            value for value in paper.get("_source_ranks", [])
            if isinstance(value, int) and value > 0
        ]
        if source_ranks:
            score += max(0, 3 - min(source_ranks) // 5)

        query_stages = [str(item).strip().lower() for item in paper.get("_query_stages", []) if str(item).strip()]
        if PRIMARY_STAGE in query_stages:
            score += 1
        elif any(stage.startswith(TOPIC_FALLBACK_STAGE) for stage in query_stages):
            score += 0

        evidence_level = str(paper.get("evidence_level", "")).strip().lower()
        if evidence_level in {"abstract", "excerpt"}:
            score += 2

        time_range_status = str(paper.get("time_range_status", "")).strip().lower()
        if time_range_status == "in_range":
            score += 2
        elif time_range_status == "out_of_range":
            score -= 4

        if exclude_hits:
            score -= 4

        updated = dict(paper)
        updated["_retrieval_score"] = score
        return updated

    async def _verify_promising_candidates(
        self,
        papers: list[dict[str, Any]],
        context: dict[str, Any],
    ) -> list[dict[str, Any]]:
        updated_papers = [dict(paper) for paper in papers]
        verification_targets: list[int] = []
        for index, paper in enumerate(updated_papers[:15]):
            if len(verification_targets) >= 8:
                break
            if not self._resolve_pdf_url(paper):
                continue
            evidence_level = str(paper.get("evidence_level", "")).strip().lower()
            rerank_task_fit = str(paper.get("_rerank_task_fit", "")).strip().lower()
            rerank_relevance = str(paper.get("_rerank_relevance", "")).strip().lower()
            rerank_verification = str(paper.get("_rerank_verification", "")).strip().lower()
            rerank_score = int(paper.get("_rerank_score", 0))
            retrieval_score = int(paper.get("_retrieval_score", 0))

            should_verify = False
            if evidence_level == "title_only":
                should_verify = retrieval_score >= 6 or (
                    rerank_task_fit in {"direct", "related"} and rerank_score >= 60
                )
            elif evidence_level == "abstract":
                should_verify = (
                    rerank_task_fit in {"direct", "related"}
                    and rerank_relevance in {"high", "medium"}
                    and rerank_verification in {"weak", "partial"}
                    and rerank_score >= 70
                )

            if not should_verify:
                continue
            verification_targets.append(index)

        for index in verification_targets:
            paper = updated_papers[index]
            pdf_url = self._resolve_pdf_url(paper)
            if not pdf_url:
                continue
            try:
                pdf_text = await self._fetch_pdf_text(url=pdf_url, max_chars=2500)
            except Exception:
                continue
            if not pdf_text:
                continue

            evidence_snippets: list[str] = []
            existing_snippets = paper.get("evidence_snippets")
            if isinstance(existing_snippets, list):
                for item in existing_snippets:
                    normalized = normalize_text(item)
                    if normalized and normalized not in evidence_snippets:
                        evidence_snippets.append(normalized[:800])
                    if len(evidence_snippets) >= 1:
                        break
            normalized_pdf_text = normalize_text(pdf_text)
            if normalized_pdf_text:
                if normalized_pdf_text not in evidence_snippets:
                    evidence_snippets.append(normalized_pdf_text[:800])
            else:
                evidence_snippets.append(pdf_text[:800])
            paper["evidence_snippets"] = evidence_snippets[:2]
            paper["evidence_level"] = "excerpt"
            rescored = self._apply_relevance_scoring(paper, context)
            if rescored is None:
                paper["verification_status"] = "weak"
                paper["_retrieval_score"] = -100
                continue

            signal_strength = int(rescored.get("_retrieval_score", 0))
            rerank_task_fit = str(rescored.get("_rerank_task_fit", "")).strip().lower()
            rerank_relevance = str(rescored.get("_rerank_relevance", "")).strip().lower()
            verified_threshold = 14 if rerank_task_fit == "direct" and rerank_relevance == "high" else 16
            rescored["verification_status"] = "verified" if signal_strength >= verified_threshold else "partial"
            updated_papers[index] = rescored

        return updated_papers

    async def _fetch_pdf_text(self, url: str, max_chars: int = 1800) -> str:
        try:
            from pypdf import PdfReader
        except ImportError:
            return ""

        response = await self._client.get(url)
        response.raise_for_status()
        content = response.content
        content_type = str(response.headers.get("content-type", "")).lower()
        if b"%PDF" not in content[:8] and "application/pdf" not in content_type:
            return ""

        try:
            reader = PdfReader(BytesIO(content))
        except Exception:
            return ""

        chunks: list[str] = []
        remaining = max_chars
        for page in reader.pages[:3]:
            if remaining <= 0:
                break
            try:
                page_text = page.extract_text() or ""
            except Exception:
                continue
            normalized = normalize_text(page_text)
            if not normalized:
                continue
            snippet = normalized[:remaining]
            if snippet:
                chunks.append(snippet)
                remaining -= len(snippet)
        return normalize_text(" ".join(chunks))[:max_chars]

    def _resolve_pdf_url(self, paper: dict[str, Any]) -> str:
        preferred = self._normalize_pdf_url(str(paper.get("_pdf_url", "") or ""))
        if preferred:
            return preferred

        url = normalize_text(paper.get("url", ""))
        return self._normalize_pdf_url(url)

    def _normalize_pdf_url(self, url: str) -> str:
        normalized = normalize_text(url)
        if not normalized:
            return ""
        lowered = normalized.lower()
        if lowered.endswith(".pdf") or ".pdf?" in lowered:
            return normalized
        if "arxiv.org/abs/" in lowered:
            return self._derive_arxiv_pdf_url(normalized)
        return ""

    def _derive_arxiv_pdf_url(self, url: str) -> str:
        normalized = normalize_text(url)
        if not normalized:
            return ""
        match = re.search(r"(https?://arxiv\.org/)(abs|pdf)/([^?#]+)", normalized, re.IGNORECASE)
        if not match:
            return ""
        identifier = match.group(3)
        if identifier.lower().endswith(".pdf"):
            identifier = identifier[:-4]
        return f"{match.group(1)}pdf/{identifier}.pdf"

    def _deduplicate_retrieval_papers(self, papers: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
        best_by_key: dict[str, dict[str, Any]] = {}
        duplicate_count = 0
        for paper in papers:
            key = self._retrieval_paper_dedup_key(paper)
            existing = best_by_key.get(key)
            if existing is None:
                best_by_key[key] = paper
                continue
            duplicate_count += 1
            best_by_key[key] = self._merge_retrieval_papers(existing, paper)
        deduped = list(best_by_key.values())
        return deduped, duplicate_count

    def _retrieval_paper_dedup_key(self, paper: dict[str, Any]) -> str:
        doi = normalize_text(paper.get("doi", ""), for_matching=True)
        if doi:
            return f"doi:{doi}"
        url = normalize_text(paper.get("url", ""), for_matching=True)
        if url:
            url = re.sub(r"v\d+$", "", url)
            return f"url:{url}"
        title = normalize_text(paper.get("title", ""), for_matching=True)
        return f"title:{title}"

    def _merge_retrieval_papers(self, left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
        primary = left if self._retrieval_paper_quality_score(left) >= self._retrieval_paper_quality_score(right) else right
        secondary = right if primary is left else left
        merged = dict(primary)

        if not merged.get("url") and secondary.get("url"):
            merged["url"] = secondary["url"]
        if not merged.get("_pdf_url") and secondary.get("_pdf_url"):
            merged["_pdf_url"] = secondary["_pdf_url"]
        if not merged.get("doi") and secondary.get("doi"):
            merged["doi"] = secondary["doi"]
        if not merged.get("date") and secondary.get("date"):
            merged["date"] = secondary["date"]
        if not merged.get("year") and secondary.get("year"):
            merged["year"] = secondary["year"]

        primary_authors = merged.get("authors") if isinstance(merged.get("authors"), list) else []
        secondary_authors = secondary.get("authors") if isinstance(secondary.get("authors"), list) else []
        merged["authors"] = list(
            dict.fromkeys(
                [normalize_text(author) for author in [*primary_authors, *secondary_authors] if normalize_text(author)]
            )
        )

        primary_snippets = merged.get("evidence_snippets") if isinstance(merged.get("evidence_snippets"), list) else []
        secondary_snippets = secondary.get("evidence_snippets") if isinstance(secondary.get("evidence_snippets"), list) else []
        merged["evidence_snippets"] = list(
            dict.fromkeys(
                [normalize_text(snippet) for snippet in [*primary_snippets, *secondary_snippets] if normalize_text(snippet)]
            )
        )[:2]

        sources = [
            normalize_text(source)
            for source in [merged.get("source", ""), secondary.get("source", "")]
            if normalize_text(source)
        ]
        merged["source"] = " | ".join(dict.fromkeys(sources))

        matched_queries = [
            normalize_text(query)
            for query in [*(merged.get("_matched_queries", []) or []), *(secondary.get("_matched_queries", []) or [])]
            if normalize_text(query)
        ]
        merged["_matched_queries"] = list(dict.fromkeys(matched_queries))

        source_ranks = [
            rank for rank in [*(merged.get("_source_ranks", []) or []), *(secondary.get("_source_ranks", []) or [])]
            if isinstance(rank, int) and rank > 0
        ]
        merged["_source_ranks"] = source_ranks

        query_stages = [
            normalize_text(stage)
            for stage in [*(merged.get("_query_stages", []) or []), *(secondary.get("_query_stages", []) or [])]
            if normalize_text(stage)
        ]
        merged["_query_stages"] = list(dict.fromkeys(query_stages))

        merged["verification_status"] = self._better_verification_status(
            str(merged.get("verification_status", "")),
            str(secondary.get("verification_status", "")),
        )
        merged["evidence_level"] = self._better_evidence_level(
            str(merged.get("evidence_level", "")),
            str(secondary.get("evidence_level", "")),
        )
        merged["time_range_status"] = self._better_time_range_status(
            str(merged.get("time_range_status", "")),
            str(secondary.get("time_range_status", "")),
        )
        return merged

    def _retrieval_paper_quality_score(self, paper: dict[str, Any]) -> tuple[int, int, int, int, int]:
        verification_rank = {"weak": 0, "partial": 1, "verified": 2}
        evidence_rank = {"title_only": 0, "abstract": 1, "excerpt": 2}
        return (
            verification_rank.get(str(paper.get("verification_status", "")).strip().lower(), -1),
            evidence_rank.get(str(paper.get("evidence_level", "")).strip().lower(), -1),
            1 if paper.get("doi") else 0,
            1 if paper.get("url") else 0,
            len(paper.get("authors", [])) if isinstance(paper.get("authors"), list) else 0,
        )

    def _retrieval_paper_sort_key(self, paper: dict[str, Any]) -> tuple[int, int, int, int, int, int, int, int, str]:
        rerank_relevance_rank = {"low": 0, "medium": 1, "high": 2}
        rerank_task_fit_rank = {"weak": 0, "related": 1, "direct": 2}
        rerank_verification_rank = {"weak": 0, "partial": 1, "strong": 2}
        verification_rank = {"weak": 0, "partial": 1, "verified": 2}
        evidence_rank = {"title_only": 0, "abstract": 1, "excerpt": 2}
        year_value = paper.get("year")
        year = year_value if isinstance(year_value, int) else 0
        return (
            -rerank_task_fit_rank.get(str(paper.get("_rerank_task_fit", "")).strip().lower(), 0),
            -rerank_relevance_rank.get(str(paper.get("_rerank_relevance", "")).strip().lower(), 0),
            -rerank_verification_rank.get(str(paper.get("_rerank_verification", "")).strip().lower(), 0),
            -int(paper.get("_rerank_score", 0)),
            -int(paper.get("_retrieval_score", 0)),
            -verification_rank.get(str(paper.get("verification_status", "")).strip().lower(), -1),
            -evidence_rank.get(str(paper.get("evidence_level", "")).strip().lower(), -1),
            -year,
            normalize_text(paper.get("title", "")),
        )

    def _better_verification_status(self, left: str, right: str) -> str:
        rank = {"weak": 0, "partial": 1, "verified": 2}
        left_value = left.strip().lower()
        right_value = right.strip().lower()
        return left_value if rank.get(left_value, -1) >= rank.get(right_value, -1) else right_value

    def _better_evidence_level(self, left: str, right: str) -> str:
        rank = {"title_only": 0, "abstract": 1, "excerpt": 2}
        left_value = left.strip().lower()
        right_value = right.strip().lower()
        return left_value if rank.get(left_value, -1) >= rank.get(right_value, -1) else right_value

    def _better_time_range_status(self, left: str, right: str) -> str:
        rank = {"unknown": 0, "out_of_range": 1, "in_range": 2}
        left_value = left.strip().lower()
        right_value = right.strip().lower()
        return left_value if rank.get(left_value, -1) >= rank.get(right_value, -1) else right_value

    async def _search_arxiv_records(self, query: str, max_results: int | None = None) -> list[PaperRecord]:
        limit = self._resolve_limit(max_results)
        response = await self._client.get(
            "http://export.arxiv.org/api/query",
            params={
                "search_query": f"all:{query}",
                "start": 0,
                "max_results": limit,
                "sortBy": "relevance",
                "sortOrder": "descending",
            },
        )
        response.raise_for_status()

        root = ET.fromstring(response.text)
        namespace = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", namespace)

        records: list[PaperRecord] = []
        for rank, entry in enumerate(entries, start=1):
            authors = [
                author.findtext("atom:name", default="", namespaces=namespace).strip()
                for author in entry.findall("atom:author", namespace)
            ]
            title = entry.findtext("atom:title", default="", namespaces=namespace).strip()
            summary = entry.findtext("atom:summary", default="", namespaces=namespace).strip()
            published = entry.findtext("atom:published", default="", namespaces=namespace).strip()
            url = entry.findtext("atom:id", default="", namespaces=namespace).strip()
            pdf_url = ""
            for link in entry.findall("atom:link", namespace):
                href = normalize_text(link.attrib.get("href", ""))
                title_attr = normalize_text(link.attrib.get("title", "")).lower()
                type_attr = normalize_text(link.attrib.get("type", "")).lower()
                if title_attr == "pdf" or type_attr == "application/pdf" or href.lower().endswith(".pdf"):
                    pdf_url = href
                    break
            pdf_url = self._normalize_pdf_url(pdf_url) or self._derive_arxiv_pdf_url(url)
            records.append(
                PaperRecord(
                    title=normalize_text(title),
                    source="arXiv",
                    summary=normalize_text(summary),
                    authors=[author for author in authors if author],
                    published=published,
                    url=url,
                    pdf_url=pdf_url,
                    source_rank=rank,
                )
            )
        return records

    async def _search_crossref_records(
        self,
        query: str,
        max_results: int | None = None,
        from_year: int | None = None,
    ) -> list[PaperRecord]:
        limit = self._resolve_limit(max_results)
        params: dict[str, Any] = {
            "query": query,
            "rows": limit,
            "select": "title,author,DOI,URL,published-print,published-online,issued,container-title,abstract,link",
        }
        if from_year is not None:
            params["filter"] = f"from-pub-date:{from_year}-01-01"

        response = await self._client.get("https://api.crossref.org/works", params=params)
        response.raise_for_status()
        payload = response.json()
        items = payload.get("message", {}).get("items", [])

        records: list[PaperRecord] = []
        for rank, item in enumerate(items, start=1):
            title_list = item.get("title") or []
            title = title_list[0].strip() if title_list else "Untitled"
            authors: list[str] = []
            for author in item.get("author", []):
                given = (author.get("given") or "").strip()
                family = (author.get("family") or "").strip()
                full_name = " ".join(part for part in [given, family] if part)
                if full_name:
                    authors.append(full_name)

            venue_list = item.get("container-title") or []
            venue = venue_list[0].strip() if venue_list else "Crossref"
            published = self._extract_crossref_date(item)
            abstract = normalize_text(item.get("abstract", ""))
            pdf_url = self._extract_crossref_pdf_url(item)
            records.append(
                PaperRecord(
                    title=normalize_text(title),
                    source=f"Crossref / {venue}",
                    summary=abstract,
                    authors=authors,
                    published=published,
                    url=(item.get("URL") or "").strip(),
                    pdf_url=pdf_url,
                    doi=(item.get("DOI") or "").strip(),
                    source_rank=rank,
                )
            )
        return records

    async def _search_openalex_records(
        self,
        query: str,
        max_results: int | None = None,
        from_year: int | None = None,
    ) -> list[PaperRecord]:
        limit = self._resolve_limit(max_results)
        params: dict[str, Any] = {
            "search": query,
            "per-page": limit,
            "sort": "relevance_score:desc",
            "select": ",".join(
                [
                    "display_name",
                    "authorships",
                    "publication_year",
                    "publication_date",
                    "ids",
                    "doi",
                    "primary_location",
                    "abstract_inverted_index",
                    "type",
                ]
            ),
        }
        if from_year is not None:
            params["filter"] = f"from_publication_date:{from_year}-01-01"

        response = await self._client.get("https://api.openalex.org/works", params=params)
        response.raise_for_status()
        payload = response.json()
        items = payload.get("results", [])

        records: list[PaperRecord] = []
        for rank, item in enumerate(items, start=1):
            title = normalize_text(item.get("display_name", "") or "Untitled")
            authorships = item.get("authorships") or []
            authors: list[str] = []
            for authorship in authorships:
                if not isinstance(authorship, dict):
                    continue
                author = authorship.get("author") or {}
                if not isinstance(author, dict):
                    continue
                name = normalize_text(author.get("display_name", ""))
                if name:
                    authors.append(name)

            published = normalize_text(
                item.get("publication_date")
                or str(item.get("publication_year") or "")
            )
            ids = item.get("ids") or {}
            primary_location = item.get("primary_location") or {}
            landing_page = ""
            pdf_url = ""
            if isinstance(primary_location, dict):
                landing_page = normalize_text(primary_location.get("landing_page_url", ""))
                pdf_url = self._normalize_pdf_url(primary_location.get("pdf_url", "") or "")
            if isinstance(ids, dict):
                landing_page = landing_page or normalize_text(ids.get("openalex", ""))

            doi = normalize_text(item.get("doi", ""))
            if doi.startswith("https://doi.org/"):
                doi = doi.removeprefix("https://doi.org/")
            summary = self._reconstruct_openalex_abstract(item.get("abstract_inverted_index"))
            records.append(
                PaperRecord(
                    title=title,
                    source="OpenAlex",
                    summary=summary,
                    authors=authors,
                    published=published,
                    url=landing_page,
                    pdf_url=pdf_url,
                    doi=doi,
                    source_rank=rank,
                )
            )
        return records

    def _extract_match_tokens(self, phrases: list[str]) -> list[str]:
        tokens: list[str] = []
        for phrase in phrases:
            normalized = normalize_text(phrase, for_matching=True)
            if not normalized:
                continue
            for token in normalized.split():
                if token in STOPWORDS:
                    continue
                if len(token) >= 3 or token in {"3d", "cad", "ai"}:
                    tokens.append(token)
        return list(dict.fromkeys(tokens))

    def _resolve_limit(self, max_results: int | None) -> int:
        if max_results is None:
            return self._settings.max_results_per_source
        return max(1, min(max_results, 20))

    def _extract_crossref_date(self, item: dict[str, Any]) -> str:
        for field_name in ("published-print", "published-online", "issued"):
            field = item.get(field_name)
            if not field:
                continue
            parts = field.get("date-parts", [])
            if not parts or not parts[0]:
                continue
            return "-".join(str(part) for part in parts[0])
        return ""

    def _extract_crossref_pdf_url(self, item: dict[str, Any]) -> str:
        links = item.get("link")
        if not isinstance(links, list):
            return ""
        for link in links:
            if not isinstance(link, dict):
                continue
            content_type = normalize_text(link.get("content-type", "")).lower()
            candidate = self._normalize_pdf_url(
                str(link.get("URL") or link.get("url") or "")
            )
            if candidate and (content_type == "application/pdf" or candidate.lower().endswith(".pdf")):
                return candidate
        return ""

    def _reconstruct_openalex_abstract(self, abstract_inverted_index: Any) -> str:
        if not isinstance(abstract_inverted_index, dict):
            return ""
        positions: dict[int, str] = {}
        for token, token_positions in abstract_inverted_index.items():
            if not isinstance(token, str) or not isinstance(token_positions, list):
                continue
            for pos in token_positions:
                if isinstance(pos, int):
                    positions[pos] = token
        if not positions:
            return ""
        ordered_tokens = [positions[pos] for pos in sorted(positions)]
        return normalize_text(" ".join(ordered_tokens))

    def _extract_year(self, published: str) -> int | None:
        match = re.search(r"\b(19|20)\d{2}\b", published or "")
        if not match:
            return None
        return int(match.group(0))
