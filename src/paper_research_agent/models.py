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


class TaskQueryPlan(BaseModel):
    primary_queries: list[str] = Field(default_factory=list)
    semantic_core_terms: list[str] = Field(default_factory=list)


class TaskInterpretation(BaseModel):
    intent: TaskIntent = Field(default_factory=TaskIntent)
    query_plan: TaskQueryPlan = Field(default_factory=TaskQueryPlan)


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


class RetrievalOutput(BaseModel):
    sources_used: list[str] = Field(default_factory=list)
    queries_executed: list[QueryExecution] = Field(default_factory=list)
    papers: list[PaperCandidate] = Field(default_factory=list)
    dedup_notes: list[str] = Field(default_factory=list)
    missing_metadata: list[str] = Field(default_factory=list)
    coverage_gaps: list[str] = Field(default_factory=list)
    source_errors: list[dict[str, str]] = Field(default_factory=list)
    rerank_trace: RerankTrace = Field(default_factory=RerankTrace)


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
