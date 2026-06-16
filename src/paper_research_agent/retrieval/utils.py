from __future__ import annotations

import re

from ..core.normalization import normalize_text


DEFAULT_SOURCE_ORDER = ("arXiv", "Crossref", "OpenAlex")


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
