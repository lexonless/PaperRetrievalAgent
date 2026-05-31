from __future__ import annotations

from pydantic import BaseModel, Field, field_validator

from .normalization import normalize_text


def paper_key(paper: PaperDict) -> str:
    """Generate a stable unique key for paper deduplication, preferring OpenAlex ID > DOI > title."""
    oa_id = normalize_text(paper.openalex_id, for_matching=True)
    if oa_id:
        return f"oa:{oa_id}"
    doi = normalize_text(paper.doi, for_matching=True)
    if doi:
        return f"doi:{doi}"
    title = normalize_text(paper.title, for_matching=True)
    return f"title:{title}" if title else f"unknown_{id(paper)}"


class PaperDict(BaseModel):
    """Unified paper representation used throughout the agent pipeline."""
    model_config = {"extra": "allow"}

    # ── basic metadata ──
    title: str = ""
    source: str = ""
    year: int = 0
    date: str = ""
    url: str = ""
    doi: str = ""
    pdf_url: str = ""

    # ── authors / content ──
    authors: list[str] = Field(default_factory=list)
    evidence_snippets: list[str] = Field(default_factory=list)
    evidence_level: str = "abstract"

    # ── source tracking ──
    source_rank: int = 0
    matched_query: str = ""
    query_stage: str = ""
    openalex_id: str = ""
    cited_by_count: int = 0
    matched_queries: list[str] = Field(default_factory=list)
    source_ranks: list[int] = Field(default_factory=list)
    query_stages: list[str] = Field(default_factory=list)

    # ── scoring ──
    relevance_score: int = 0
    ce_score: float = 0.0
    ce_mapped_score: int = 0
    llm_overall: int = 0
    llm_reason: str = ""

    # ── PDF ──
    pdf_status: str = "pending"
    pdf_urls: list[str] = Field(default_factory=list)
    local_path: str = ""

    # ── output materialization ──
    slug: str = ""
    path: str = ""
    pdf_downloaded: bool = False
    pdf_error: str = ""

    # ── internal tracking ──
    graph_seed: str = ""


class QueryDecomposition(BaseModel):
    core_techs: list[str] = Field(default_factory=list)
    application_domains: list[str] = Field(default_factory=list)
    key_metrics: list[str] = Field(default_factory=list)
    expanded_terms: list[str] = Field(default_factory=list)
    desired_paper_count: int = 5
    year_from: int | None = None
    year_to: int | None = None

    @field_validator("expanded_terms", mode="before")
    @classmethod
    def _flatten_expanded_terms(cls, v: object) -> list[str]:
        if isinstance(v, dict):
            result: list[str] = []
            for key, terms in v.items():
                result.append(str(key))
                if isinstance(terms, list):
                    for term in terms:
                        result.append(str(term))
            return result
        return v  # type: ignore[return-value]


class ReviewResult(BaseModel):
    converged: bool = False
    convergence_reason: str = ""
    refined_query: str = ""
