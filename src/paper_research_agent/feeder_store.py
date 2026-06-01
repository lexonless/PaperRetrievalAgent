from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core.models import PaperDict


@dataclass(slots=True)
class ProjectPaths:
    root_dir: Path
    project_file: Path
    raw_dir: Path
    papers_dir: Path
    paper_metadata_dir: Path
    paper_fulltext_dir: Path
    paper_page_images_dir: Path
    papers_pdf_dir: Path
    feeder_dir: Path
    batches_dir: Path
    log_path: Path


def ensure_project_paths(project_root: Path, slug: str) -> ProjectPaths:
    project_root = project_root.resolve()
    root_dir = (project_root / slug).resolve()
    raw_dir = root_dir / "raw"
    papers_dir = raw_dir / "papers"
    paper_metadata_dir = papers_dir / "metadata"
    paper_fulltext_dir = papers_dir / "fulltext"
    paper_page_images_dir = papers_dir / "page_images"
    papers_pdf_dir = raw_dir / "papers_pdf"
    feeder_dir = root_dir / ".feeder"
    batches_dir = feeder_dir / "batches"
    for path in (
        root_dir,
        raw_dir,
        papers_dir,
        paper_metadata_dir,
        paper_fulltext_dir,
        paper_page_images_dir,
        papers_pdf_dir,
        feeder_dir,
        batches_dir,
    ):
        path.mkdir(parents=True, exist_ok=True)

    project_file = root_dir / "project.md"
    if not project_file.exists():
        project_file.write_text(
            (
                f"# {slug}\n\n"
                "Project context for raw paper discovery.\n"
                "Describe the topic, constraints, and what should or should not enter raw/.\n"
            ),
            encoding="utf-8",
        )

    return ProjectPaths(
        root_dir=root_dir,
        project_file=project_file,
        raw_dir=raw_dir,
        papers_dir=papers_dir,
        paper_metadata_dir=paper_metadata_dir,
        paper_fulltext_dir=paper_fulltext_dir,
        paper_page_images_dir=paper_page_images_dir,
        papers_pdf_dir=papers_pdf_dir,
        feeder_dir=feeder_dir,
        batches_dir=batches_dir,
        log_path=feeder_dir / "log.md",
    )


def list_batches(project_root: Path, slug: str) -> list[Path]:
    batches_dir = (project_root.resolve() / slug / ".feeder" / "batches")
    if not batches_dir.is_dir():
        return []
    batch_files = sorted(
        batches_dir.glob("*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return batch_files


def load_batch_json(batch_path: Path) -> dict[str, Any]:
    return json.loads(batch_path.read_text(encoding="utf-8"))


_YAML_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_metadata_papers(project_root: Path, slug: str) -> list[PaperDict]:
    metadata_dir = (project_root.resolve() / slug / "raw" / "papers" / "metadata")
    if not metadata_dir.is_dir():
        return []

    papers: list[PaperDict] = []
    for md_file in sorted(metadata_dir.glob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        m = _YAML_FRONTMATTER_RE.match(content)
        if not m:
            continue

        yaml_text = m.group(1)
        body_text = content[m.end():]
        frontmatter = _parse_simple_yaml(yaml_text)
        abstract = _extract_abstract(body_text)
        paper = _frontmatter_to_paper_dict(frontmatter, abstract=abstract)
        if paper.title:
            papers.append(paper)

    return papers


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    current_key: str | None = None
    current_list: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if not line.startswith(" ") and not line.startswith("\t") and ":" in stripped:
            if current_key and current_list:
                result[current_key] = current_list
                current_list = []
            raw_key = stripped.split(":", 1)[0].strip()
            raw_val = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            current_key = raw_key
            if raw_val:
                result[current_key] = raw_val
            else:
                result[current_key] = ""
        elif current_key and stripped.startswith("- "):
            item = stripped[2:].strip().strip('"').strip("'")
            current_list.append(item)

    if current_key and current_list:
        result[current_key] = current_list

    return result


def _frontmatter_to_paper_dict(fm: dict[str, Any], *, abstract: str = "") -> PaperDict:
    authors = fm.get("authors", [])
    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(",") if a.strip()]
    return PaperDict(
        title=fm.get("title", ""),
        authors=authors,
        year=_parse_year(fm.get("year", "")),
        source=fm.get("source_family", ""),
        doi=fm.get("doi", ""),
        url=fm.get("canonical_url", ""),
        pdf_url=fm.get("pdf_url", ""),
        pdf_status=fm.get("pdf_download_status", "pending"),
        evidence_snippets=[abstract] if abstract else [],
    )


def _parse_year(value: Any) -> int:
    if isinstance(value, int):
        return value if value > 1900 else 0
    if isinstance(value, str):
        try:
            y = int(value.strip())
            return y if y > 1900 else 0
        except (ValueError, TypeError):
            pass
    return 0


_BODY_ABSTRACT_RE = re.compile(r"## Abstract\s*\n+(.*?)(?:\n## |\n---|\Z)", re.DOTALL)


def _extract_abstract(text: str) -> str:
    m = _BODY_ABSTRACT_RE.search(text)
    if m:
        return m.group(1).strip()
    return ""


def get_project_query(project_root: Path, slug: str) -> str:
    batches = list_batches(project_root, slug)
    for batch_path in batches:
        try:
            data = load_batch_json(batch_path)
            query = data.get("query", "")
            if query:
                return query
        except Exception:
            continue
    return ""


def get_project_decomposition(project_root: Path, slug: str) -> dict[str, Any] | None:
    batches = list_batches(project_root, slug)
    for batch_path in batches:
        try:
            data = load_batch_json(batch_path)
            decomp = data.get("query_decomposition")
            if decomp:
                return decomp
        except Exception:
            continue
    return None


def get_project_review_stats(project_root: Path, slug: str) -> dict[str, Any]:
    batches = list_batches(project_root, slug)
    stats: dict[str, Any] = {}
    for batch_path in batches:
        try:
            data = load_batch_json(batch_path)
            stats.setdefault("candidate_count", data.get("candidate_count", 0))
            stats.setdefault("selected_count", data.get("selected_count", 0))
        except Exception:
            continue
    return stats


def get_project_convergence_status(project_root: Path, slug: str) -> bool | None:
    batches = list_batches(project_root, slug)
    for batch_path in batches:
        try:
            data = load_batch_json(batch_path)
            converged = data.get("converged")
            if isinstance(converged, bool):
                return converged
        except Exception:
            continue
    return None
