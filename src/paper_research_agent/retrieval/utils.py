from __future__ import annotations

import re

from ..core.normalization import normalize_text


DEFAULT_SOURCE_ORDER = ("arXiv", "Crossref", "OpenAlex")
PRIMARY_STAGE = "primary"
TOPIC_FALLBACK_STAGE = "topic_fallback"

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
    "not",
    "andnot",
    "all",
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

TASK_FIT_RANK = {"weak": 0, "related": 1, "direct": 2}
TOPICAL_RELEVANCE_RANK = {"low": 0, "medium": 1, "high": 2}
EVIDENCE_SUFFICIENCY_RANK = {"weak": 0, "partial": 1, "strong": 2}
VERIFICATION_STATUS_RANK = {"weak": 0, "partial": 1, "verified": 2}
EVIDENCE_LEVEL_RANK = {"title_only": 0, "abstract": 1, "excerpt": 2}
TIME_RANGE_STATUS_RANK = {"unknown": 0, "out_of_range": 1, "in_range": 2}


def derive_arxiv_pdf_url(url: str) -> str:
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


def normalize_pdf_url(url: str) -> str:
    normalized = normalize_text(url)
    if not normalized:
        return ""
    lowered = normalized.lower()
    if lowered.endswith(".pdf") or ".pdf?" in lowered:
        return normalized
    if "arxiv.org/abs/" in lowered:
        return derive_arxiv_pdf_url(normalized)
    return ""


def extract_year(published: str) -> int | None:
    match = re.search(r"\b(19|20)\d{2}\b", published or "")
    if not match:
        return None
    return int(match.group(0))


def extract_match_tokens(phrases: list[str]) -> list[str]:
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


def pick_better_enum(left: str, right: str, rank: dict[str, int]) -> str:
    left_value = left.strip().lower()
    right_value = right.strip().lower()
    return left_value if rank.get(left_value, -1) >= rank.get(right_value, -1) else right_value
