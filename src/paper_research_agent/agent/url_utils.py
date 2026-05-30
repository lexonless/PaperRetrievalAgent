from __future__ import annotations

import re
from typing import Any

from ..core.models import PaperDict
from ..core.normalization import normalize_text


_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", re.IGNORECASE)


def extract_direct_pdf_urls(paper: PaperDict) -> list[str]:
    source = normalize_text(paper.source, for_matching=True)
    oa_id = paper.openalex_id
    url = normalize_text(paper.url)
    doi = normalize_text(paper.doi)
    paper_pdf = normalize_text(paper.pdf_url)
    urls: list[str] = []

    if paper_pdf:
        urls.append(paper_pdf)

    if "openalex" in source and oa_id:
        mirror = f"https://content.openalex.org/works/{oa_id}.pdf"
        if mirror not in urls:
            urls.append(mirror)

    if "arxiv" in source or "arxiv.org" in url:
        match = _ARXIV_ID_RE.search(url)
        if match:
            arxiv_url = f"https://arxiv.org/pdf/{match.group(1).removesuffix('.pdf')}.pdf"
            if arxiv_url not in urls:
                urls.append(arxiv_url)

    if doi.startswith("10.48550/"):
        arxiv_id = doi.split("/", 1)[1].removeprefix("arxiv.")
        if arxiv_id:
            arxiv_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            if arxiv_url not in urls:
                urls.append(arxiv_url)

    if doi.startswith("10.1145/"):
        acm_url = f"https://dl.acm.org/doi/pdf/{doi}"
        if acm_url not in urls:
            urls.append(acm_url)

    return urls


def sort_pdf_urls(urls: list[str]) -> list[str]:
    def _priority(u: str) -> int:
        lowered = u.lower()
        if "arxiv.org/pdf/" in lowered:
            return 0
        if "content.openalex.org" in lowered:
            return 3
        if "dl.acm.org" in lowered or "ieeexplore.ieee.org" in lowered or "link.springer.com" in lowered or "sciencedirect.com" in lowered:
            return 4
        return 1

    deduped: list[str] = []
    seen: set[str] = set()
    for u in urls:
        key = u.rstrip("/")
        if key not in seen:
            seen.add(key)
            deduped.append(u)
    return sorted(deduped, key=_priority)


def url_source_label(url: str) -> str:
    lowered = url.lower()
    if "arxiv.org" in lowered:
        return "arXiv"
    if "content.openalex.org" in lowered:
        return "OpenAlex mirror"
    if "dl.acm.org" in lowered:
        return "ACM DL"
    if "ieeexplore.ieee.org" in lowered:
        return "IEEE Xplore"
    if "link.springer.com" in lowered:
        return "Springer"
    if "sciencedirect.com" in lowered:
        return "ScienceDirect"
    return "other"


def extract_http_status(exc: Exception) -> int:
    if hasattr(exc, "response"):
        resp = getattr(exc, "response", None)
        if resp is not None:
            return getattr(resp, "status_code", 0)
    req_exc = getattr(exc, "request", None)
    if req_exc is not None:
        return getattr(req_exc, "status_code", 0)
    return 0
