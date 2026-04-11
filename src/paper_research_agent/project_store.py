from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .models import ManifestRunRecord, ProjectSourceItem, ProjectSourceManifest
from .normalization import normalize_text


@dataclass(slots=True)
class ProjectPaths:
    root_dir: Path
    project_file: Path
    source_dir: Path
    notes_dir: Path
    retrieval_dir: Path
    traces_dir: Path
    manifest_path: Path


def ensure_project_paths(project_root: Path, slug: str) -> ProjectPaths:
    root_dir = project_root / slug
    source_dir = root_dir / "sources"
    notes_dir = root_dir / "notes"
    retrieval_dir = root_dir / "retrieval"
    traces_dir = root_dir / "traces"
    for path in (root_dir, source_dir, notes_dir, retrieval_dir, traces_dir):
        path.mkdir(parents=True, exist_ok=True)

    project_file = root_dir / "project.md"
    if not project_file.exists():
        project_file.write_text(
            f"# {slug}\n\nProject context, hypotheses, and working notes live here.\n",
            encoding="utf-8",
        )

    manifest_path = source_dir / "manifest.json"
    return ProjectPaths(
        root_dir=root_dir,
        project_file=project_file,
        source_dir=source_dir,
        notes_dir=notes_dir,
        retrieval_dir=retrieval_dir,
        traces_dir=traces_dir,
        manifest_path=manifest_path,
    )


def load_manifest(manifest_path: Path, project_slug: str) -> ProjectSourceManifest:
    if manifest_path.exists():
        try:
            return ProjectSourceManifest.model_validate_json(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return ProjectSourceManifest(project_slug=project_slug, generated_at=_timestamp())


def discover_local_pdfs(*, project_paths: ProjectPaths, pdf_dir: str = "") -> list[str]:
    candidates: list[Path] = []
    if pdf_dir:
        requested_dir = Path(pdf_dir).expanduser()
        if requested_dir.exists():
            candidates.extend(requested_dir.rglob("*.pdf"))

    default_pdf_dir = project_paths.source_dir / "pdfs"
    if default_pdf_dir.exists():
        candidates.extend(default_pdf_dir.rglob("*.pdf"))

    normalized_paths: list[str] = []
    seen: set[str] = set()
    for path in candidates:
        resolved = str(path.resolve())
        if resolved not in seen:
            seen.add(resolved)
            normalized_paths.append(resolved)
    return normalized_paths


def merge_manifest_sources(
    manifest: ProjectSourceManifest,
    local_pdf_paths: list[str],
) -> ProjectSourceManifest:
    existing_by_path = {item.path: item for item in manifest.sources}
    for pdf_path in local_pdf_paths:
        path_obj = Path(pdf_path)
        title = normalize_text(path_obj.stem.replace("_", " ").replace("-", " "))
        modified_at = ""
        try:
            modified_at = datetime.fromtimestamp(path_obj.stat().st_mtime).isoformat(timespec="seconds")
        except OSError:
            pass
        existing_by_path[pdf_path] = ProjectSourceItem(
            path=pdf_path,
            kind="pdf",
            title=title or path_obj.name,
            modified_at=modified_at,
        )

    manifest.sources = sorted(existing_by_path.values(), key=lambda item: item.path.lower())
    manifest.generated_at = _timestamp()
    return manifest


def persist_manifest(manifest_path: Path, manifest: ProjectSourceManifest) -> None:
    manifest_path.write_text(manifest.model_dump_json(indent=2), encoding="utf-8")


def append_run_record(
    manifest: ProjectSourceManifest,
    *,
    run_id: str,
    query: str,
    note_path: str,
    retrieval_path: str,
    trace_path: str,
) -> ProjectSourceManifest:
    manifest.run_history.append(
        ManifestRunRecord(
            run_id=run_id,
            query=query,
            generated_at=_timestamp(),
            note_path=note_path,
            retrieval_path=retrieval_path,
            trace_path=trace_path,
        )
    )
    manifest.generated_at = _timestamp()
    return manifest


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_timestamped_filename(prefix: str, suffix: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{timestamp}-{prefix}{suffix}"


def _timestamp() -> str:
    return datetime.now().isoformat(timespec="seconds")
