from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class PaperRecord:
    title: str
    source: str
    summary: str = ""
    authors: list[str] = field(default_factory=list)
    published: str = ""
    url: str = ""
    pdf_url: str = ""
    doi: str = ""
    source_rank: int = 0
    matched_query: str = ""
    query_stage: str = ""
