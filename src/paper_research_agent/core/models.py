from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

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


class TimeRangeResolution(BaseModel):
    start_year: int | None = None
    end_year: int | None = None
    is_explicit: bool = False
    original_expression: str = ""
    resolution_basis_date: str = ""
    resolved_by_rule: str = ""


class TaskIntent(BaseModel):
    topic: str = ""
    goal: str = ""
    time_range: TimeRangeResolution = Field(default_factory=TimeRangeResolution)
    must_include: list[str] = Field(default_factory=list)
    must_exclude: list[str] = Field(default_factory=list)


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


class TaskHardRequirements(BaseModel):
    minimum_paper_count: int = Field(default=0, ge=0, le=50)
    maximum_paper_count: int | None = Field(default=None, ge=1, le=50)
    required_paper_types: list[str] = Field(default_factory=list)
    forbidden_paper_types: list[str] = Field(default_factory=list)
    required_source_families: list[str] = Field(default_factory=list)


class TaskInterpretation(BaseModel):
    intent: TaskIntent = Field(default_factory=TaskIntent)
    query_plan: TaskQueryPlan = Field(default_factory=TaskQueryPlan)
    hard_requirements: TaskHardRequirements = Field(default_factory=TaskHardRequirements)


class QueryExecution(BaseModel):
    query: str
    sources: list[str] = Field(default_factory=list)
    notes: str


class PaperCandidate(BaseModel):
    title: str
    source: str
    year: int | str = ""
    date: str = ""
    url: str = ""
    doi: str = ""
    authors: list[str] = Field(default_factory=list)
    eligibility_score: int = Field(ge=0, le=10)
    eligible: bool
    topical_relevance: Literal["high", "medium", "low"]
    task_fit: Literal["direct", "related", "weak"]
    evidence_sufficiency: Literal["strong", "partial", "weak"]
    verification_status: Literal["verified", "partial", "weak"]
    evidence_level: Literal["abstract", "excerpt", "title_only"]
    time_range_status: Literal["in_range", "out_of_range", "unknown"]
    rank_reason: str = ""
    evidence_snippets: list[str] = Field(default_factory=list)


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


class LocalPdfDebugEntry(BaseModel):
    path: str
    title: str = ""
    status: Literal["missing_file", "read_error", "empty_text", "token_miss", "candidate_added"]
    extracted_chars: int = 0
    matched_token_count: int = 0
    matched_tokens: list[str] = Field(default_factory=list)
    error: str = ""
    retained_in_final: bool = False
    final_rank: int | None = None
    eligible: bool | None = None
    eligibility_score: int | None = None
    verification_status: str = ""


class LocalLibraryDebug(BaseModel):
    scanned_count: int = 0
    missing_count: int = 0
    read_error_count: int = 0
    empty_text_count: int = 0
    token_miss_count: int = 0
    candidate_count: int = 0
    retained_count: int = 0
    entries: list[LocalPdfDebugEntry] = Field(default_factory=list)


class RetrievalOutput(BaseModel):
    sources_used: list[str] = Field(default_factory=list)
    queries_executed: list[QueryExecution] = Field(default_factory=list)
    papers: list[PaperCandidate] = Field(default_factory=list)
    dedup_notes: list[str] = Field(default_factory=list)
    missing_metadata: list[str] = Field(default_factory=list)
    coverage_gaps: list[str] = Field(default_factory=list)
    source_errors: list[dict[str, str]] = Field(default_factory=list)
    rerank_trace: RerankTrace = Field(default_factory=RerankTrace)
    local_library_debug: LocalLibraryDebug = Field(default_factory=LocalLibraryDebug)


class ReviewRequirement(BaseModel):
    passed: bool
    reason: str


class ReviewScores(BaseModel):
    coverage_score: int = Field(ge=0, le=2)
    relevance_score: int = Field(ge=0, le=2)
    metadata_score: int = Field(ge=0, le=2)
    diversity_score: int = Field(ge=0, le=2)
    evidence_score: int = Field(ge=0, le=2)


class ReviewHardRequirements(BaseModel):
    source_coverage: ReviewRequirement
    candidate_depth: ReviewRequirement
    relevance: ReviewRequirement
    metadata: ReviewRequirement
    query_fit: ReviewRequirement
    core_method_fit: ReviewRequirement
    time_consistency: ReviewRequirement
    gaps: ReviewRequirement


class ReviewOutput(BaseModel):
    decision: Literal["PASS", "REVISE"]
    review_summary: str
    scores: ReviewScores
    hard_requirements: ReviewHardRequirements
    key_risks: list[str] = Field(default_factory=list)
    next_actions: list[str] = Field(default_factory=list)
    failure_reasons: list[str] = Field(default_factory=list)
    reformulation_advice: list[str] = Field(default_factory=list)


class NotePaperEntry(BaseModel):
    title: str
    year: int | str = ""
    source: str = ""
    link: str = ""
    contribution_summary: str = ""
    relevance_note: str = ""
    evidence_note: str = ""


class ResearchNoteOutput(BaseModel):
    note_title: str
    project_focus: str
    retrieval_assessment: str
    search_scope: list[str] = Field(default_factory=list)
    core_papers: list[NotePaperEntry] = Field(default_factory=list)
    supporting_papers: list[NotePaperEntry] = Field(default_factory=list)
    local_context: list[str] = Field(default_factory=list)
    key_observations: list[str] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    next_steps: list[str] = Field(default_factory=list)


class TraceEvent(BaseModel):
    timestamp: str
    step: str
    event_type: str
    message: str
    payload: dict[str, Any] = Field(default_factory=dict)


class ProjectSourceItem(BaseModel):
    path: str
    kind: Literal["pdf", "note"] = "pdf"
    title: str = ""
    tags: list[str] = Field(default_factory=list)
    modified_at: str = ""
    excerpt: str = ""


class ManifestRunRecord(BaseModel):
    run_id: str
    query: str
    generated_at: str
    note_path: str = ""
    retrieval_path: str = ""
    trace_path: str = ""


class ProjectSourceManifest(BaseModel):
    version: int = 1
    project_slug: str
    generated_at: str = ""
    sources: list[ProjectSourceItem] = Field(default_factory=list)
    run_history: list[ManifestRunRecord] = Field(default_factory=list)
