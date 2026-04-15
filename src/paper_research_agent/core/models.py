from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

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


class QueryAliasGroup(BaseModel):
    canonical: str = ""
    aliases: list[str] = Field(default_factory=list)


class TaskQueryIR(BaseModel):
    topic_phrases: list[str] = Field(default_factory=list)
    method_terms: list[str] = Field(default_factory=list)
    optional_terms: list[str] = Field(default_factory=list)
    excluded_terms: list[str] = Field(default_factory=list)
    alias_groups: list[QueryAliasGroup] = Field(default_factory=list)


class TaskQueryIRUpdate(BaseModel):
    topic_phrases: list[str] | None = None
    method_terms: list[str] | None = None
    optional_terms: list[str] | None = None
    excluded_terms: list[str] | None = None
    alias_groups: list[QueryAliasGroup] | None = None


class SourceQuerySpec(BaseModel):
    source: Literal["arXiv", "Crossref", "OpenAlex"]
    query: str
    purpose: Literal["precision", "recall"] = "precision"
    stage: str = "primary"
    notes: str = ""


class TaskQueryPlan(BaseModel):
    query_ir: TaskQueryIR = Field(default_factory=TaskQueryIR)
    rendered_queries: list[SourceQuerySpec] = Field(default_factory=list)
    primary_queries: list[str] = Field(default_factory=list)
    semantic_core_terms: list[str] = Field(default_factory=list)


class DiscoverIntent(BaseModel):
    topic: str = ""
    must_include: list[str] = Field(default_factory=list)
    must_exclude: list[str] = Field(default_factory=list)
    domain_terms: list[str] = Field(default_factory=list)
    negative_domains: list[str] = Field(default_factory=list)
    source_hints: list[str] = Field(default_factory=list)
    primary_queries: list[str] = Field(default_factory=list)
    start_year: int | None = None
    end_year: int | None = None


class DiscoverReview(BaseModel):
    decision: Literal["PASS", "RETRY"] = "PASS"
    review_summary: str = ""
    failure_reasons: list[str] = Field(default_factory=list)
    query_adjustments: list[str] = Field(default_factory=list)
    domain_drift_detected: bool = False


class QueryExecution(BaseModel):
    query: str
    sources: list[str] = Field(default_factory=list)
    notes: str


class RerankBatchTrace(BaseModel):
    batch_index: int
    paper_ids: list[str] = Field(default_factory=list)
    status: Literal["success", "empty", "error", "skipped"]
    parsed_judgment_count: int = 0
    raw_response_preview: str = ""
    error: str = ""


class RerankTrace(BaseModel):
    attempted: bool = False
    skipped_reason: str = ""
    candidate_count: int = 0
    batch_size: int = 0
    batch_count: int = 0
    successful_batches: int = 0
    empty_batches: int = 0
    failed_batches: int = 0
    judgment_count: int = 0
    judged_paper_ids: list[str] = Field(default_factory=list)
    batches: list[RerankBatchTrace] = Field(default_factory=list)


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


class DiscoverBatch(BaseModel):
    batch_id: str
    project_slug: str
    query: str
    generated_at: str
    project_context_used: bool = False
    discover_intent: DiscoverIntent
    attempt_count: int = 1
    review_decision: Literal["PASS", "RETRY"] = "PASS"
    review_summary: str = ""
    executed_queries: list[QueryExecution] = Field(default_factory=list)
    retrieved_record_count: int = 0
    candidate_count: int = 0
    selected_count: int = 0
    written_files: list[RawPaperArtifact] = Field(default_factory=list)
    source_errors: list[dict[str, str]] = Field(default_factory=list)
