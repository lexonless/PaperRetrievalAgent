from __future__ import annotations

import re
from collections import defaultdict

from ..core.models import PaperDict
from ..core.normalization import normalize_text
from .utils import extract_year


class PaperRankingEngine:
    def __init__(self) -> None:
        pass

    def prepare_agent_candidates(
        self, records: list[PaperDict], *, matched_query: str
    ) -> list[PaperDict]:
        papers: list[PaperDict] = []
        for record in records:
            title = normalize_text(record.title)
            source = normalize_text(record.source)
            if not title or not source:
                continue
            published = normalize_text(record.date)
            year = extract_year(published)
            summary = normalize_text(record.evidence_snippets[0] if record.evidence_snippets else "")
            evidence_level = "abstract" if summary else "title_only"
            papers.append(
                PaperDict(
                    title=title,
                    source=source,
                    year=year if year is not None else 0,
                    date=published,
                    url=normalize_text(record.url),
                    doi=normalize_text(record.doi),
                    authors=[normalize_text(a) for a in record.authors[:8] if normalize_text(a)],
                    evidence_level=evidence_level,
                    evidence_snippets=[summary] if summary else [],
                    matched_queries=[matched_query],
                    source_ranks=[record.source_rank] if record.source_rank else [],
                    query_stages=[record.query_stage] if record.query_stage else [],
                    openalex_id=record.openalex_id,
                    cited_by_count=record.cited_by_count,
                    pdf_status="pending",
                )
            )
        papers, _ = self._deduplicate_retrieval_papers(papers)
        papers.sort(key=lambda p: -p.year if p.year else 0)
        return papers

    def _deduplicate_retrieval_papers(self, papers: list[PaperDict]) -> tuple[list[PaperDict], int]:
        parent = {i: i for i in range(len(papers))}

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        indices = {"doi": {}, "url": {}, "title": {}}

        for i, paper in enumerate(papers):
            key = self._retrieval_paper_dedup_key(paper)
            for field in ["doi", "url", "title"]:
                val = key.get(field)
                if val:
                    if val in indices[field]:
                        union(i, indices[field][val])
                    else:
                        indices[field][val] = i

        groups_dict = defaultdict(list)
        for i, paper in enumerate(papers):
            root = find(i)
            groups_dict[root].append(paper)

        merged_groups = []
        for group_papers in groups_dict.values():
            merged_paper = group_papers[0]
            for other in group_papers[1:]:
                merged_paper = self._merge_retrieval_papers(merged_paper, other)
            merged_groups.append(merged_paper)

        duplicate_count = len(papers) - len(merged_groups)
        return merged_groups, duplicate_count

    @staticmethod
    def _retrieval_paper_dedup_key(paper: PaperDict) -> dict[str, str]:
        doi = normalize_text(paper.doi, for_matching=True)
        url = normalize_text(paper.url, for_matching=True)
        if url:
            url = re.sub(r"v\d+$", "", url)
        title = normalize_text(paper.title, for_matching=True)
        return {"doi": doi, "url": url, "title": title}

    def _merge_retrieval_papers(self, left: PaperDict, right: PaperDict) -> PaperDict:
        merged = left.model_copy()
        for key in ("url", "doi", "date", "year", "pdf_url"):
            if not getattr(merged, key, None) and getattr(right, key, None):
                setattr(merged, key, getattr(right, key, None))
        if right.pdf_status == "available" and merged.pdf_status != "available":
            merged.pdf_status = "available"
            merged.pdf_url = right.pdf_url or merged.pdf_url
            merged.pdf_urls = right.pdf_urls or merged.pdf_urls
        merged.authors = list(dict.fromkeys([
            normalize_text(a) for a in [*merged.authors, *right.authors] if normalize_text(a)
        ]))
        merged.evidence_snippets = list(dict.fromkeys([
            normalize_text(s) for s in [*merged.evidence_snippets, *right.evidence_snippets] if normalize_text(s)
        ]))[:2]
        merged.source = " | ".join(dict.fromkeys([
            normalize_text(s) for s in [merged.source, right.source] if normalize_text(s)
        ]))
        merged.matched_queries = list(dict.fromkeys([
            normalize_text(q) for q in [*merged.matched_queries, *right.matched_queries] if normalize_text(q)
        ]))
        merged.source_ranks = [rank for rank in [*merged.source_ranks, *right.source_ranks] if isinstance(rank, int) and rank > 0]
        merged.query_stages = list(dict.fromkeys([
            normalize_text(stage) for stage in [*merged.query_stages, *right.query_stages] if normalize_text(stage)
        ]))
        return merged
