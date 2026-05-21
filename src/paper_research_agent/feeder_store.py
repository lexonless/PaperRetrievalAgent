from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil


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


def ensure_project_paths(project_root: Path, slug: str, *, reset_existing: bool = False) -> ProjectPaths:
    project_root = project_root.resolve()
    root_dir = (project_root / slug).resolve()
    if reset_existing and root_dir.exists():
        _reset_project_root(project_root, root_dir)
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


def _reset_project_root(project_root: Path, root_dir: Path) -> None:
    try:
        root_dir.relative_to(project_root)
    except ValueError as exc:
        raise ValueError(f"Refusing to delete project outside project root: {root_dir}") from exc
    shutil.rmtree(root_dir)
