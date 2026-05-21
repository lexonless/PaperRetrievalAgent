from __future__ import annotations

import re
from typing import Any
from collections import defaultdict

from ..core.models import PaperRecord
from ..core.normalization import normalize_text
from .utils import extract_year, normalize_pdf_url


class PaperRankingEngine:
    def __init__(self) -> None:
        pass

    def prepare_agent_candidates(
        self, records: list[PaperRecord], *, matched_query: str
    ) -> list[dict[str, Any]]:
        papers: list[dict[str, Any]] = []
        for record in records:
            title = normalize_text(record.title)
            source = normalize_text(record.source)
            if not title or not source:
                continue
            published = normalize_text(record.published)
            year = extract_year(published)
            summary = normalize_text(record.summary)
            evidence_level = "abstract" if summary else "title_only"
            papers.append(
                {
                    "title": title,
                    "source": source,
                    "year": year if year is not None else "",
                    "date": published,
                    "url": normalize_text(record.url),
                    "doi": normalize_text(record.doi),
                    "authors": [normalize_text(a) for a in record.authors[:8] if normalize_text(a)],
                    "evidence_level": evidence_level,
                    "evidence_snippets": [summary] if summary else [],
                    "_matched_queries": [matched_query],
                    "_source_ranks": [record.source_rank] if record.source_rank else [],
                    "_query_stages": [record.query_stage] if record.query_stage else [],
                    "_openalex_id": record.openalex_id,
                    "_cited_by_count": record.cited_by_count,
                    "pdf_status": "pending",
                    "pdf_url": "",
                    "pdf_urls": [],
                    "local_path": "",
                }
            )
        papers, _ = self._deduplicate_retrieval_papers(papers)
        papers.sort(key=lambda p: -(p.get("year") if isinstance(p.get("year"), int) else 0))
        return papers

    def prepare_ranked_papers(
        self, records: list[PaperRecord], from_year: int | None, end_year: int | None, context: dict[str, Any]
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
                    "authors": [normalize_text(a) for a in record.authors[:8] if normalize_text(a)],
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
        return papers, retrieval_duplicate_count, raw_source_families

    def _deduplicate_retrieval_papers(self, papers: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
        # 1. 初始化并查集：每个论文的初始父节点是自己
        parent = {i: i for i in range(len(papers))}

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # 2. 建立特征到索引的映射
        indices = {"doi": {}, "url": {}, "title": {}}
        
        # 3. 第一阶段：寻找所有重复关联（连通图）
        for i, paper in enumerate(papers):
            key = self._retrieval_paper_dedup_key(paper)
            for field in ["doi", "url", "title"]:
                val = key.get(field)
                if val:
                    if val in indices[field]:
                        union(i, indices[field][val])  # 发现重复，合并节点
                    else:
                        indices[field][val] = i

        # 4. 第二阶段：将归属于同一组的论文合并
        groups_dict = defaultdict(list)
        for i, paper in enumerate(papers):
            root = find(i)
            groups_dict[root].append(paper)

        merged_groups = []
        for group_papers in groups_dict.values():
            # 以组内第一篇为基础，合并其他篇
            merged_paper = group_papers[0]
            for other in group_papers[1:]:
                merged_paper = self._merge_retrieval_papers(merged_paper, other)
            merged_groups.append(merged_paper)

        duplicate_count = len(papers) - len(merged_groups)
        return merged_groups, duplicate_count

    @staticmethod
    def _retrieval_paper_dedup_key(paper: dict[str, Any]) -> dict[str, str]:
        doi = normalize_text(paper.get("doi", ""), for_matching=True)
        url = normalize_text(paper.get("url", ""), for_matching=True)
        if url:
            url = re.sub(r"v\d+$", "", url)
        title = normalize_text(paper.get("title", ""), for_matching=True)
        return {"doi": doi, "url": url, "title": title}

    def _merge_retrieval_papers(self, left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
        merged = dict(left)
        for key in ("url", "doi", "date", "year", "pdf_url"):
            if not merged.get(key) and right.get(key):
                merged[key] = right[key]
        if right.get("pdf_status") == "available" and merged.get("pdf_status") != "available":
            merged["pdf_status"] = "available"
            merged["pdf_url"] = right.get("pdf_url", merged.get("pdf_url", ""))
            merged["pdf_urls"] = right.get("pdf_urls", merged.get("pdf_urls", []))
        merged["authors"] = list(dict.fromkeys([
            normalize_text(a) for a in [*(merged.get("authors", []) or []), *(right.get("authors", []) or [])] if normalize_text(a)
        ]))
        merged["evidence_snippets"] = list(dict.fromkeys([
            normalize_text(s) for s in [*(merged.get("evidence_snippets", []) or []), *(right.get("evidence_snippets", []) or [])] if normalize_text(s)
        ]))[:2]
        merged["source"] = " | ".join(dict.fromkeys([
            normalize_text(s) for s in [merged.get("source", ""), right.get("source", "")] if normalize_text(s)
        ]))
        merged["_matched_queries"] = list(dict.fromkeys([
            normalize_text(q) for q in [*(merged.get("_matched_queries", []) or []), *(right.get("_matched_queries", []) or [])] if normalize_text(q)
        ]))
        merged["_source_ranks"] = [rank for rank in [*(merged.get("_source_ranks", []) or []), *(right.get("_source_ranks", []) or [])] if isinstance(rank, int) and rank > 0]
        merged["_query_stages"] = list(dict.fromkeys([
            normalize_text(stage) for stage in [*(merged.get("_query_stages", []) or []), *(right.get("_query_stages", []) or [])] if normalize_text(stage)
        ]))
        return merged
