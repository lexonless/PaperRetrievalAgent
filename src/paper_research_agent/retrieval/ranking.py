from __future__ import annotations

import json
import re
from typing import Any

from ..core.models import PaperRecord, RerankBatchTrace, RerankTrace
from ..core.normalization import normalize_string_list, normalize_text
from .utils import (
    EVIDENCE_LEVEL_RANK,
    EVIDENCE_SUFFICIENCY_RANK,
    HARD_NOISE_PHRASES,
    PRIMARY_STAGE,
    REVIEW_ARTICLE_PHRASES,
    TASK_FIT_RANK,
    TIME_RANGE_STATUS_RANK,
    TOPICAL_RELEVANCE_RANK,
    TOPIC_FALLBACK_STAGE,
    VERIFICATION_STATUS_RANK,
    extract_match_tokens,
    normalize_pdf_url,
    extract_year,
    pick_better_enum,
)

RERANK_SYSTEM_MESSAGE = """You are a scholarly retrieval reranking model.

You receive a search task and a small batch of candidate papers.
Judge each paper independently using only the provided evidence.

Output requirements:
- Return exactly one JSON object and nothing else.
- Do not use markdown code fences.
- Use the provided paper_id values unchanged.
- The top-level JSON object must have exactly one key: "papers".
- "papers" must be a JSON array, not an object keyed by paper_id.
- Each array item must be an object with exactly these keys:
  - "paper_id"
  - "topical_relevance"
  - "task_fit"
  - "evidence_sufficiency"
  - "reason"
- Do not use alternative keys such as "reasoning".

Required output shape:
{
  "papers": [
    {
      "paper_id": "p0",
      "topical_relevance": "high",
      "task_fit": "direct",
      "evidence_sufficiency": "strong",
      "reason": "..."
    }
  ]
}

Judgment rules:
- topical_relevance measures topical closeness to the user request: high, medium, or low.
- task_fit measures whether the paper is directly doing the requested task or only loosely/partially related:
  - direct: substantially addresses the user's requested task
  - related: meaningfully relevant, but not an exact task match
  - weak: only weakly related or mostly off-target
- evidence_sufficiency measures how reliable the judgment is from the current evidence only:
  - strong: the provided abstract or PDF text clearly supports the judgment
  - partial: some support exists, but important ambiguity remains
  - weak: current evidence is too thin to trust strongly

Important constraints:
- Do not require any specific wording from the paper.
- Do not assume every task has a strict input/output template.
- Prefer recall-friendly judgments: if a paper might still be useful, choose related rather than weak.
- Only use weak when the paper is clearly loose, generic, or off-target for the requested task.
"""

MAX_RERANK_CANDIDATES = 24
RERANK_BATCH_SIZE = 6


class PaperRankingEngine:
    def __init__(self, rerank_model_client: Any | None = None) -> None:
        self._rerank_model_client = rerank_model_client
        self._last_rerank_trace = RerankTrace(skipped_reason="Rerank has not run yet.")

    def build_retrieval_context(self, task_interpretation: dict[str, Any], executed_query_specs: list[dict[str, Any]]) -> dict[str, Any]:
        query_phrases: list[str] = []
        for item in executed_query_specs:
            query = normalize_text(item.get("query", ""))
            if query:
                query_phrases.append(query)
        intent = task_interpretation.get("intent", {}) if isinstance(task_interpretation, dict) else {}
        query_plan = task_interpretation.get("query_plan", {}) if isinstance(task_interpretation, dict) else {}
        topic = normalize_text(intent.get("topic", ""))
        goal = normalize_text(intent.get("goal", ""))
        semantic_core_terms = normalize_string_list(query_plan.get("semantic_core_terms"))
        must_include = normalize_string_list(intent.get("must_include"))
        must_exclude = normalize_string_list(intent.get("must_exclude"))
        query_phrases.extend(semantic_core_terms)
        query_phrases.extend(must_include)
        if topic:
            query_phrases.append(topic)
        combined_text = " ".join([topic, goal, *query_phrases]).lower()
        allow_review_articles = any(term in combined_text for term in REVIEW_ARTICLE_PHRASES)
        return {
            "query_phrases": list(dict.fromkeys(query_phrases)),
            "query_tokens": extract_match_tokens([*query_phrases, topic, goal]),
            "exclude_phrases": normalize_string_list(must_exclude, for_matching=True),
            "allow_review_articles": allow_review_articles,
        }

    def prepare_ranked_papers(self, records: list[PaperRecord], from_year: int | None, end_year: int | None, context: dict[str, Any]) -> tuple[list[dict[str, Any]], int, set[str]]:
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
            year = extract_year(published)
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
                    "_pdf_url": normalize_pdf_url(record.pdf_url or record.url),
                    "authors": [normalize_text(author) for author in record.authors[:8] if normalize_text(author)],
                    "eligibility_score": 0,
                    "eligible": False,
                    "topical_relevance": "low",
                    "task_fit": "weak",
                    "evidence_sufficiency": "weak",
                    "rank_reason": "",
                    "verification_status": verification_status,
                    "evidence_level": evidence_level,
                    "time_range_status": time_range_status,
                    "evidence_snippets": [summary] if summary else [],
                    "_matched_queries": [record.matched_query] if record.matched_query else [],
                    "_source_ranks": [record.source_rank] if record.source_rank else [],
                    "_query_stages": [record.query_stage] if record.query_stage else [],
                }
            )
        papers, retrieval_duplicate_count = self._deduplicate_retrieval_papers(papers)
        papers = self._apply_eligibility_filter(papers, context)
        return papers, retrieval_duplicate_count, raw_source_families

    def should_expand_queries(self, papers: list[dict[str, Any]]) -> bool:
        summary = self.summarize_candidate_pool(papers)
        return summary["eligible_count"] < 15 or summary["task_fit_count"] < 5 or summary["supported_count"] < 5

    async def rerank_with_model(self, papers: list[dict[str, Any]], task_interpretation: dict[str, Any]) -> list[dict[str, Any]]:
        if self._rerank_model_client is None:
            self._last_rerank_trace = RerankTrace(
                attempted=False,
                skipped_reason="No rerank model client is configured.",
                candidate_count=len(papers),
            )
            return papers
        if len(papers) < 2:
            self._last_rerank_trace = RerankTrace(
                attempted=False,
                skipped_reason="Fewer than 2 candidates were available for reranking.",
                candidate_count=len(papers),
            )
            return papers
        updated_papers = [dict(paper) for paper in papers]
        candidate_items = [(index, updated_papers[index]) for index in range(min(len(updated_papers), MAX_RERANK_CANDIDATES))]
        judgments_by_paper_id: dict[str, dict[str, Any]] = {}
        batch_traces: list[RerankBatchTrace] = []
        for start in range(0, len(candidate_items), RERANK_BATCH_SIZE):
            batch = candidate_items[start : start + RERANK_BATCH_SIZE]
            if not batch:
                continue
            try:
                batch_judgments, batch_trace = await self._judge_rerank_batch(task_interpretation, batch, start // RERANK_BATCH_SIZE)
            except Exception as exc:
                batch_traces.append(
                    RerankBatchTrace(
                        batch_index=start // RERANK_BATCH_SIZE,
                        paper_ids=[f"p{index}" for index, _ in batch],
                        status="error",
                        error=str(exc),
                    )
                )
                continue
            batch_traces.append(batch_trace)
            for judgment in batch_judgments:
                paper_id = normalize_text(judgment.get("paper_id", ""))
                if paper_id:
                    judgments_by_paper_id[paper_id] = judgment
        self._last_rerank_trace = RerankTrace(
            attempted=True,
            candidate_count=len(candidate_items),
            batch_size=RERANK_BATCH_SIZE,
            batch_count=len(batch_traces),
            successful_batches=sum(1 for item in batch_traces if item.status == "success"),
            empty_batches=sum(1 for item in batch_traces if item.status == "empty"),
            failed_batches=sum(1 for item in batch_traces if item.status == "error"),
            judgment_count=len(judgments_by_paper_id),
            judged_paper_ids=sorted(judgments_by_paper_id.keys()),
            batches=batch_traces,
        )
        if not judgments_by_paper_id:
            return self.finalize_ranked_papers(updated_papers)
        for index, paper in candidate_items:
            judgment = judgments_by_paper_id.get(f"p{index}")
            if judgment is not None:
                updated_papers[index] = self._apply_rerank_judgment(paper, judgment)
        return self.finalize_ranked_papers(updated_papers)

    def get_last_rerank_trace(self) -> dict[str, Any]:
        return self._last_rerank_trace.model_dump()

    def build_retrieval_payload(self, papers: list[dict[str, Any]], raw_source_families: set[str], retrieval_duplicate_count: int, source_errors: list[dict[str, str]] | None, executed_query_specs: list[dict[str, Any]], local_library_debug: dict[str, Any] | None = None) -> dict[str, Any]:
        coverage_gaps: list[str] = []
        normalized_source_errors = source_errors if isinstance(source_errors, list) else []
        normalized_local_library_debug = self._finalize_local_library_debug(local_library_debug, papers)
        for item in normalized_source_errors:
            if isinstance(item, dict) and normalize_text(item.get("source", "")):
                coverage_gaps.append(f"{normalize_text(item.get('source', ''))} retrieval failed: {normalize_text(item.get('error', ''))}")
        summary = self.summarize_candidate_pool(papers)
        if summary["eligible_count"] < 5:
            coverage_gaps.append("Fewer than 5 eligible papers were retained after staged retrieval and filtering.")
        if summary["task_fit_count"] < 5:
            coverage_gaps.append("Fewer than 5 candidates were rated as direct or related to the task.")
        if summary["supported_count"] < 3:
            coverage_gaps.append("Fewer than 3 candidates currently have partial or verified evidence support.")
        if summary["verified_count"] < 1:
            coverage_gaps.append("No candidate reached verified status from excerpt-backed evidence.")
        if len(raw_source_families) < 2:
            coverage_gaps.append("Retrieved candidates do not cover at least two distinct source families.")
        return {
            "sources_used": sorted(raw_source_families),
            "queries_executed": [
                {
                    "query": item["query"],
                    "sources": item["sources"],
                    "notes": "Primary query executed from the latest task interpretation." if str(item.get("stage", "")).strip().lower() == PRIMARY_STAGE else "Semantic core term expansion executed because earlier retrieval remained sparse." if str(item.get("stage", "")).strip().lower().startswith(TOPIC_FALLBACK_STAGE) else "Derived from the latest task interpretation.",
                }
                for item in executed_query_specs
            ],
            "papers": [{key: value for key, value in paper.items() if not key.startswith("_")} for paper in papers],
            "dedup_notes": [f"Retrieved papers were deduplicated by DOI, URL, or normalized title; {retrieval_duplicate_count} duplicate entries were merged."],
            "missing_metadata": ["Title-only candidates remain weak until abstract or excerpt evidence is available."],
            "coverage_gaps": coverage_gaps,
            "source_errors": normalized_source_errors,
            "rerank_trace": self.get_last_rerank_trace(),
            "local_library_debug": normalized_local_library_debug,
        }

    def _finalize_local_library_debug(self, local_library_debug: dict[str, Any] | None, papers: list[dict[str, Any]]) -> dict[str, Any]:
        debug = dict(local_library_debug or {})
        entries = [dict(item) for item in debug.get("entries", []) if isinstance(item, dict)]
        final_local_papers: dict[str, dict[str, Any]] = {}
        for index, paper in enumerate(papers, start=1):
            if normalize_text(paper.get("source", "")).lower() != "locallibrary":
                continue
            path = normalize_text(paper.get("url", ""))
            if not path:
                continue
            final_local_papers[path] = {
                "retained_in_final": True,
                "final_rank": index,
                "eligible": bool(paper.get("eligible")),
                "eligibility_score": int(paper.get("eligibility_score", 0)),
                "verification_status": normalize_text(paper.get("verification_status", "")),
            }

        retained_count = 0
        for entry in entries:
            path = normalize_text(entry.get("path", ""))
            final_info = final_local_papers.get(path)
            if final_info is None:
                entry["retained_in_final"] = False
                continue
            retained_count += 1
            entry.update(final_info)

        debug["entries"] = entries
        debug["scanned_count"] = int(debug.get("scanned_count", 0))
        debug["missing_count"] = int(debug.get("missing_count", 0))
        debug["read_error_count"] = int(debug.get("read_error_count", 0))
        debug["empty_text_count"] = int(debug.get("empty_text_count", 0))
        debug["token_miss_count"] = int(debug.get("token_miss_count", 0))
        debug["candidate_count"] = int(debug.get("candidate_count", 0))
        debug["retained_count"] = retained_count
        return debug

    def finalize_ranked_papers(self, papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
        for paper in papers:
            if not normalize_text(paper.get("rank_reason", "")):
                paper["rank_reason"] = self._build_default_rank_reason(paper)
            self.apply_verification_constraints(paper)
        papers.sort(key=self.retrieval_paper_sort_key)
        return papers

    def score_eligibility(self, paper: dict[str, Any], context: dict[str, Any]) -> dict[str, Any] | None:
        title_text = normalize_text(paper.get("title", ""), for_matching=True)
        evidence_parts = [normalize_text(item) for item in (paper.get("evidence_snippets") or []) if normalize_text(item)]
        evidence_text = normalize_text(" ".join(evidence_parts), for_matching=True)
        combined_text = " ".join(part for part in [title_text, evidence_text] if part).strip()
        if not combined_text:
            return None
        query_phrases = [normalize_text(item, for_matching=True) for item in paper.get("_matched_queries", []) or context.get("query_phrases", []) if normalize_text(item, for_matching=True)]
        query_phrases = list(dict.fromkeys(query_phrases))
        query_tokens = set(context.get("query_tokens", []))
        title_phrase_hits = [phrase for phrase in query_phrases if phrase and phrase in title_text]
        evidence_phrase_hits = [phrase for phrase in query_phrases if phrase and phrase in evidence_text and phrase not in title_phrase_hits]
        title_tokens = set(title_text.split())
        evidence_tokens = set(evidence_text.split())
        title_token_hits = sorted(query_tokens.intersection(title_tokens))
        evidence_token_hits = sorted(query_tokens.intersection(evidence_tokens) - set(title_token_hits))
        exclude_hits = [phrase for phrase in context.get("exclude_phrases", []) if phrase and phrase in combined_text]
        if any(phrase in combined_text for phrase in HARD_NOISE_PHRASES):
            return None
        if not context.get("allow_review_articles", False) and any(phrase in title_text for phrase in REVIEW_ARTICLE_PHRASES):
            return None
        positive_signal_count = len(title_phrase_hits) + len(evidence_phrase_hits) + len(title_token_hits) + len(evidence_token_hits)
        if exclude_hits and positive_signal_count < 3:
            return None
        score = 0
        score += min(len(title_phrase_hits), 1) * 4
        score += min(len(evidence_phrase_hits), 1) * 3
        score += min(len(title_token_hits), 3)
        score += min(len(evidence_token_hits), 3)
        source_ranks = [value for value in paper.get("_source_ranks", []) if isinstance(value, int) and value > 0]
        if source_ranks:
            score += max(0, 3 - min(source_ranks) // 5)
        query_stages = [str(item).strip().lower() for item in paper.get("_query_stages", []) if str(item).strip()]
        if PRIMARY_STAGE in query_stages:
            score += 1
        if str(paper.get("evidence_level", "")).strip().lower() in {"abstract", "excerpt"}:
            score += 1
        time_range_status = str(paper.get("time_range_status", "")).strip().lower()
        if time_range_status == "in_range":
            score += 2
        elif time_range_status == "out_of_range":
            score -= 2
        if paper.get("doi") or paper.get("url"):
            score += 1
        if exclude_hits:
            score -= 4
        updated = dict(paper)
        updated["eligibility_score"] = max(0, min(score, 10))
        updated["eligible"] = updated["eligibility_score"] >= 4
        if not updated.get("rank_reason"):
            updated["rank_reason"] = self._build_default_rank_reason(updated)
        return updated

    def summarize_candidate_pool(self, papers: list[dict[str, Any]]) -> dict[str, int]:
        summary = {"eligible_count": 0, "task_fit_count": 0, "supported_count": 0, "verified_count": 0}
        for paper in papers:
            if not isinstance(paper, dict):
                continue
            if paper.get("eligible"):
                summary["eligible_count"] += 1
            if str(paper.get("task_fit", "")).strip().lower() in {"direct", "related"}:
                summary["task_fit_count"] += 1
            if self._has_supported_evidence(paper):
                summary["supported_count"] += 1
            if str(paper.get("verification_status", "")).strip().lower() == "verified":
                summary["verified_count"] += 1
        return summary

    def retrieval_paper_sort_key(self, paper: dict[str, Any]) -> tuple[int, int, int, int, int, str]:
        year_value = paper.get("year")
        year = year_value if isinstance(year_value, int) else 0
        return (-TASK_FIT_RANK.get(str(paper.get("task_fit", "")).strip().lower(), 0), -TOPICAL_RELEVANCE_RANK.get(str(paper.get("topical_relevance", "")).strip().lower(), 0), -VERIFICATION_STATUS_RANK.get(str(paper.get("verification_status", "")).strip().lower(), -1), -int(paper.get("eligibility_score", 0)), -year, normalize_text(paper.get("title", "")))

    def apply_verification_constraints(self, paper: dict[str, Any]) -> None:
        evidence_level = str(paper.get("evidence_level", "")).strip().lower()
        evidence_sufficiency = str(paper.get("evidence_sufficiency", "")).strip().lower()
        task_fit = str(paper.get("task_fit", "")).strip().lower()
        topical_relevance = str(paper.get("topical_relevance", "")).strip().lower()
        if evidence_level == "title_only":
            paper["verification_status"] = "weak"
        elif evidence_level == "abstract":
            paper["verification_status"] = "verified" if evidence_sufficiency == "strong" and task_fit == "direct" and topical_relevance == "high" else "partial"
        elif evidence_level == "excerpt":
            paper["verification_status"] = "verified" if task_fit == "direct" and topical_relevance == "high" and evidence_sufficiency in {"strong", "partial"} else "partial"
        else:
            paper["verification_status"] = "weak"

    async def _judge_rerank_batch(self, task_interpretation: dict[str, Any], batch: list[tuple[int, dict[str, Any]]], batch_index: int) -> tuple[list[dict[str, Any]], RerankBatchTrace]:
        from langchain_core.messages import HumanMessage, SystemMessage

        intent = task_interpretation.get("intent", {}) if isinstance(task_interpretation, dict) else {}
        query_plan = task_interpretation.get("query_plan", {}) if isinstance(task_interpretation, dict) else {}
        time_range = intent.get("time_range", {}) if isinstance(intent, dict) else {}

        result = await self._rerank_model_client.ainvoke(
            [
                SystemMessage(content=RERANK_SYSTEM_MESSAGE),
                HumanMessage(
                    content=json.dumps(
                        {
                            "topic": normalize_text(intent.get("topic", "")),
                            "goal": normalize_text(intent.get("goal", "")),
                            "must_include": normalize_string_list(intent.get("must_include")),
                            "must_exclude": normalize_string_list(intent.get("must_exclude")),
                            "semantic_core_terms": normalize_string_list(query_plan.get("semantic_core_terms")),
                            "time_range": {
                                "from_year": time_range.get("start_year") if isinstance(time_range.get("start_year"), int) else "",
                                "end_year": time_range.get("end_year") if isinstance(time_range.get("end_year"), int) else "",
                            },
                            "papers": [
                                {
                                    "paper_id": f"p{index}",
                                    "title": normalize_text(paper.get("title", "")),
                                    "year": paper.get("year") if isinstance(paper.get("year"), int) else "",
                                    "source": normalize_text(paper.get("source", "")),
                                    "matched_queries": [normalize_text(item) for item in paper.get("_matched_queries", []) or [] if normalize_text(item)],
                                    "evidence_level": normalize_text(paper.get("evidence_level", "")),
                                    "evidence_text": self._build_rerank_evidence_text(paper),
                                }
                                for index, paper in batch
                            ],
                        },
                        ensure_ascii=False,
                    )
                ),
            ]
        )
        raw_content = getattr(result, "content", result)
        batch_judgments = self._parse_rerank_response(raw_content)
        return (
            batch_judgments,
            RerankBatchTrace(
                batch_index=batch_index,
                paper_ids=[f"p{index}" for index, _ in batch],
                status="success" if batch_judgments else "empty",
                parsed_judgment_count=len(batch_judgments),
                raw_response_preview=self._build_raw_response_preview(raw_content),
            ),
        )

    def _build_rerank_evidence_text(self, paper: dict[str, Any]) -> str:
        snippets = [normalize_text(item) for item in paper.get("evidence_snippets", []) if normalize_text(item)]
        evidence_text = snippets[0] if snippets else normalize_text(paper.get("title", ""))
        return evidence_text if normalize_text(paper.get("evidence_level", ""), for_matching=True) == "abstract" else evidence_text[:900]

    def _parse_rerank_response(self, raw_content: Any) -> list[dict[str, Any]]:
        if isinstance(raw_content, str):
            cleaned = raw_content.strip()
            if cleaned.startswith("```"):
                cleaned = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", cleaned)
                cleaned = re.sub(r"\s*```$", "", cleaned)
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
        items = payload.get("papers") if isinstance(payload, dict) else None
        if not isinstance(items, list):
            return []
        normalized: list[dict[str, Any]] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            paper_id = normalize_text(item.get("paper_id", ""))
            if not paper_id:
                continue
            normalized.append(
                {
                    "paper_id": paper_id,
                    "topical_relevance": self._normalize_enum_value(str(item.get("topical_relevance", "") or ""), {"high", "medium", "low"}, "low"),
                    "task_fit": self._normalize_enum_value(str(item.get("task_fit", "") or ""), {"direct", "related", "weak"}, "weak"),
                    "evidence_sufficiency": self._normalize_enum_value(str(item.get("evidence_sufficiency", "") or ""), {"strong", "partial", "weak"}, "weak"),
                    "reason": normalize_text(item.get("reason", "")),
                }
            )
        return normalized

    def _build_raw_response_preview(self, raw_content: Any) -> str:
        if isinstance(raw_content, str):
            return raw_content.strip()[:500]
        if isinstance(raw_content, dict):
            try:
                return json.dumps(raw_content, ensure_ascii=False)[:500]
            except TypeError:
                return str(raw_content)[:500]
        return str(raw_content)[:500]

    def _apply_rerank_judgment(self, paper: dict[str, Any], judgment: dict[str, Any]) -> dict[str, Any]:
        updated = dict(paper)
        updated["topical_relevance"] = self._normalize_enum_value(str(judgment.get("topical_relevance", "") or ""), {"high", "medium", "low"}, "low")
        updated["task_fit"] = self._normalize_enum_value(str(judgment.get("task_fit", "") or ""), {"direct", "related", "weak"}, "weak")
        updated["evidence_sufficiency"] = self._normalize_enum_value(str(judgment.get("evidence_sufficiency", "") or ""), {"strong", "partial", "weak"}, "weak")
        updated["rank_reason"] = normalize_text(judgment.get("reason", ""))
        return updated

    def _normalize_enum_value(self, value: str, allowed: set[str], default: str) -> str:
        normalized = normalize_text(value, for_matching=True)
        return normalized if normalized in allowed else default

    def _has_supported_evidence(self, paper: dict[str, Any]) -> bool:
        return bool(paper.get("eligible")) and str(paper.get("verification_status", "")).strip().lower() in {"partial", "verified"} and str(paper.get("evidence_level", "")).strip().lower() in {"abstract", "excerpt"} and isinstance(paper.get("evidence_snippets"), list) and any(normalize_text(item) for item in paper.get("evidence_snippets", []))

    def _build_default_rank_reason(self, paper: dict[str, Any]) -> str:
        if not paper.get("eligible"):
            return "The candidate did not meet the retrieval eligibility threshold."
        task_fit = str(paper.get("task_fit", "")).strip().lower()
        topical_relevance = str(paper.get("topical_relevance", "")).strip().lower()
        evidence_level = str(paper.get("evidence_level", "")).strip().lower()
        parts = ["Directly addresses the task." if task_fit == "direct" else "Meaningfully related to the task." if task_fit == "related" else "Only weakly connected to the task."]
        parts.append("Topically very close to the request." if topical_relevance == "high" else "Topically relevant to the request." if topical_relevance == "medium" else "Topical match is limited.")
        parts.append("Backed by a document excerpt." if evidence_level == "excerpt" else "Backed by abstract-level evidence." if evidence_level == "abstract" else "Only title-level evidence is available.")
        return " ".join(parts)

    def _apply_eligibility_filter(self, papers: list[dict[str, Any]], context: dict[str, Any]) -> list[dict[str, Any]]:
        eligible_papers = []
        for paper in papers:
            scored = self.score_eligibility(paper, context)
            if scored is not None and scored.get("eligible"):
                eligible_papers.append(scored)
        eligible_papers.sort(key=self.retrieval_paper_sort_key)
        return eligible_papers

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
        return list(best_by_key.values()), duplicate_count

    def _retrieval_paper_dedup_key(self, paper: dict[str, Any]) -> str:
        doi = normalize_text(paper.get("doi", ""), for_matching=True)
        if doi:
            return f"doi:{doi}"
        url = normalize_text(paper.get("url", ""), for_matching=True)
        if url:
            return f"url:{re.sub(r'v\\d+$', '', url)}"
        return f"title:{normalize_text(paper.get('title', ''), for_matching=True)}"

    def _merge_retrieval_papers(self, left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
        primary = left if self._retrieval_paper_quality_score(left) >= self._retrieval_paper_quality_score(right) else right
        secondary = right if primary is left else left
        merged = dict(primary)
        for key in ("url", "doi", "date", "year"):
            if not merged.get(key) and secondary.get(key):
                merged[key] = secondary[key]
        if not merged.get("_pdf_url") and secondary.get("_pdf_url"):
            merged["_pdf_url"] = secondary["_pdf_url"]
        merged["authors"] = list(dict.fromkeys([normalize_text(a) for a in [*(merged.get("authors", []) or []), *(secondary.get("authors", []) or [])] if normalize_text(a)]))
        merged["evidence_snippets"] = list(dict.fromkeys([normalize_text(s) for s in [*(merged.get("evidence_snippets", []) or []), *(secondary.get("evidence_snippets", []) or [])] if normalize_text(s)]))[:2]
        merged["source"] = " | ".join(dict.fromkeys([normalize_text(s) for s in [merged.get("source", ""), secondary.get("source", "")] if normalize_text(s)]))
        merged["_matched_queries"] = list(dict.fromkeys([normalize_text(q) for q in [*(merged.get("_matched_queries", []) or []), *(secondary.get("_matched_queries", []) or [])] if normalize_text(q)]))
        merged["_source_ranks"] = [rank for rank in [*(merged.get("_source_ranks", []) or []), *(secondary.get("_source_ranks", []) or [])] if isinstance(rank, int) and rank > 0]
        merged["_query_stages"] = list(dict.fromkeys([normalize_text(stage) for stage in [*(merged.get("_query_stages", []) or []), *(secondary.get("_query_stages", []) or [])] if normalize_text(stage)]))
        merged["verification_status"] = pick_better_enum(str(merged.get("verification_status", "")), str(secondary.get("verification_status", "")), VERIFICATION_STATUS_RANK)
        merged["evidence_level"] = pick_better_enum(str(merged.get("evidence_level", "")), str(secondary.get("evidence_level", "")), EVIDENCE_LEVEL_RANK)
        merged["time_range_status"] = pick_better_enum(str(merged.get("time_range_status", "")), str(secondary.get("time_range_status", "")), TIME_RANGE_STATUS_RANK)
        merged["eligibility_score"] = max(int(merged.get("eligibility_score", 0)), int(secondary.get("eligibility_score", 0)))
        merged["eligible"] = bool(merged.get("eligible")) or bool(secondary.get("eligible"))
        merged["task_fit"] = pick_better_enum(str(merged.get("task_fit", "")), str(secondary.get("task_fit", "")), TASK_FIT_RANK)
        merged["topical_relevance"] = pick_better_enum(str(merged.get("topical_relevance", "")), str(secondary.get("topical_relevance", "")), TOPICAL_RELEVANCE_RANK)
        merged["evidence_sufficiency"] = pick_better_enum(str(merged.get("evidence_sufficiency", "")), str(secondary.get("evidence_sufficiency", "")), EVIDENCE_SUFFICIENCY_RANK)
        if not normalize_text(merged.get("rank_reason", "")):
            merged["rank_reason"] = normalize_text(secondary.get("rank_reason", ""))
        return merged

    def _retrieval_paper_quality_score(self, paper: dict[str, Any]) -> tuple[int, int, int, int, int]:
        return (
            VERIFICATION_STATUS_RANK.get(str(paper.get("verification_status", "")).strip().lower(), -1),
            EVIDENCE_LEVEL_RANK.get(str(paper.get("evidence_level", "")).strip().lower(), -1),
            TASK_FIT_RANK.get(str(paper.get("task_fit", "")).strip().lower(), -1),
            TOPICAL_RELEVANCE_RANK.get(str(paper.get("topical_relevance", "")).strip().lower(), -1),
            int(paper.get("eligibility_score", 0)),
        )
