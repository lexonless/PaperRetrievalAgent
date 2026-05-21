from __future__ import annotations

from dataclasses import dataclass, field

from pydantic import BaseModel, Field


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
    openalex_id: str = ""
    cited_by_count: int = 0


class RawPaperArtifact(BaseModel):
    slug: str
    title: str
    path: str
    source_family: str
    canonical_url: str = ""
    doi: str = ""
    pdf_url: str = ""
    pdf_downloaded: bool = False
    local_pdf_path: str = ""
    fulltext_extracted: bool = False
    local_fulltext_path: str = ""
    page_images_exported: bool = False
    local_page_image_dir: str = ""
    pdf_error: str = ""


class QueryDecomposition(BaseModel):
    core_techs: list[str] = Field(default_factory=list)
    application_domains: list[str] = Field(default_factory=list)
    key_metrics: list[str] = Field(default_factory=list)
    expanded_terms: list[str] = Field(default_factory=list)
    excluded_terms: list[str] = Field(default_factory=list)
