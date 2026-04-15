from __future__ import annotations

import re
from pathlib import Path

from .core.normalization import normalize_text


ARXIV_ID_PATTERN = re.compile(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", re.IGNORECASE)


def build_raw_paper_slug(paper: dict) -> str:
    doi = normalize_text(paper.get("doi", ""), for_matching=True)
    if doi:
        return _slugify(f"doi-{doi}", max_length=90)

    for candidate in (
        normalize_text(paper.get("url", "")),
        normalize_text(paper.get("_pdf_url", "")),
    ):
        match = ARXIV_ID_PATTERN.search(candidate)
        if match:
            identifier = match.group(1).removesuffix(".pdf")
            return _slugify(f"arxiv-{identifier}", max_length=90)

    title = normalize_text(paper.get("title", "paper"))
    return _slugify(title, max_length=90) or "paper"


def render_raw_paper_markdown(
    paper: dict,
    *,
    project_slug: str,
    user_query: str,
    generated_at: str,
    local_pdf_path: str = "",
    local_fulltext_path: str = "",
    local_page_image_dir: str = "",
    pdf_download_status: str = "not_attempted",
    pdf_error: str = "",
) -> str:
    title = normalize_text(paper.get("title", "")) or "Untitled Paper"
    authors = [normalize_text(author) for author in paper.get("authors", []) if normalize_text(author)]
    source_family = _resolve_source_family(normalize_text(paper.get("source", "")))
    canonical_url = normalize_text(paper.get("url", "")) or normalize_text(paper.get("_pdf_url", ""))
    doi = normalize_text(paper.get("doi", ""))
    pdf_url = normalize_text(paper.get("_pdf_url", ""))
    summary = normalize_text((paper.get("evidence_snippets") or [""])[0])
    if not summary:
        summary = "_No abstract or summary was available from the discovery sources._"
    matched_queries = [normalize_text(item) for item in paper.get("_matched_queries", []) if normalize_text(item)]
    arxiv_id = _extract_arxiv_id(canonical_url or pdf_url)
    lines = [
        "---",
        f'title: "{_escape_yaml(title)}"',
        "type: raw_source",
        "source_kind: paper",
        f'project: "{_escape_yaml(project_slug)}"',
        f'generated_at: "{generated_at}"',
        f'feeder: "raw-feeder-v1"',
        f'source_family: "{_escape_yaml(source_family)}"',
        f'year: "{_escape_yaml(str(paper.get("year", "")))}"',
        f'date: "{_escape_yaml(normalize_text(paper.get("date", "")))}"',
        f'canonical_url: "{_escape_yaml(canonical_url)}"',
        f'doi: "{_escape_yaml(doi)}"',
            f'pdf_url: "{_escape_yaml(pdf_url)}"',
            f'local_pdf_path: "{_escape_yaml(local_pdf_path)}"',
            f'local_fulltext_path: "{_escape_yaml(local_fulltext_path)}"',
            f'local_page_image_dir: "{_escape_yaml(local_page_image_dir)}"',
            f'pdf_download_status: "{_escape_yaml(pdf_download_status)}"',
            "authors:",
    ]
    if authors:
        lines.extend([f'  - "{_escape_yaml(author)}"' for author in authors])
    else:
        lines.append('  - ""')
    lines.extend(
        [
            "matched_queries:",
            *([f'  - "{_escape_yaml(item)}"' for item in matched_queries] or ['  - ""']),
            "provenance:",
            f'  fetched_at: "{generated_at}"',
            '  fetched_by: "raw-feeder-v1"',
            f'  source_family: "{_escape_yaml(source_family)}"',
            f'  canonical_url: "{_escape_yaml(canonical_url)}"',
            f'  doi: "{_escape_yaml(doi)}"',
            f'  arxiv_id: "{_escape_yaml(arxiv_id)}"',
            "---",
            "",
            f"# Raw Source Material: {title}",
            "",
            "This file is raw source material prepared for downstream wiki ingestion.",
            "It is not a wiki page and should not be treated as a synthesized conclusion.",
            "",
            "## Bibliographic Metadata",
            "",
            f"- Source family: `{source_family}`",
            f"- Authors: {', '.join(authors) if authors else '_Unknown_'}",
            f"- Year: {normalize_text(str(paper.get('year', ''))) or '_Unknown_'}",
            f"- Date: {normalize_text(paper.get('date', '')) or '_Unknown_'}",
            f"- Canonical URL: {canonical_url or '_Unavailable_'}",
            f"- DOI: {doi or '_Unavailable_'}",
            f"- PDF URL: {pdf_url or '_Unavailable_'}",
            f"- Local PDF: {local_pdf_path or '_Unavailable_'}",
            f"- Local converted markdown: {local_fulltext_path or '_Unavailable_'}",
            f"- Local page images: {local_page_image_dir or '_Unavailable_'}",
            f"- PDF download status: `{pdf_download_status}`",
            "",
            "## Abstract",
            "",
            summary,
            "",
            "## Discovery Context",
            "",
            f"- User query: {user_query}",
            f"- Matched queries: {', '.join(matched_queries) if matched_queries else '_Unavailable_'}",
            f"- Retrieval evidence level: {normalize_text(paper.get('evidence_level', '')) or '_unknown_'}",
            f"- Eligibility score: {paper.get('eligibility_score', 0)}",
            "",
            "## Provenance",
            "",
            f"- fetched_at: `{generated_at}`",
            "- fetched_by: `raw-feeder-v1`",
            f"- source_family: `{source_family}`",
            f"- canonical_url: {canonical_url or '_Unavailable_'}",
            f"- doi: {doi or '_Unavailable_'}",
            f"- arXiv id: {arxiv_id or '_Unavailable_'}",
        ]
    )
    if pdf_error:
        lines.extend(["", "## PDF Processing Notes", "", f"- {pdf_error}"])
    return "\n".join(lines).rstrip() + "\n"


def write_raw_paper(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_text_artifact(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _extract_arxiv_id(value: str) -> str:
    match = ARXIV_ID_PATTERN.search(value)
    if not match:
        return ""
    return match.group(1).removesuffix(".pdf")


def _resolve_source_family(source: str) -> str:
    lowered = source.lower()
    if lowered.startswith("arxiv"):
        return "arXiv"
    if lowered.startswith("crossref"):
        return "Crossref"
    if lowered.startswith("openalex"):
        return "OpenAlex"
    return source or "Unknown"


def _slugify(value: str, *, max_length: int) -> str:
    normalized = normalize_text(value, for_matching=True)
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    if not normalized:
        return ""
    if len(normalized) > max_length:
        normalized = normalized[:max_length].rstrip("-")
    return normalized


def _escape_yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')
