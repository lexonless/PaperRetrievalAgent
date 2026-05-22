from __future__ import annotations

import argparse
import asyncio
import logging
from collections.abc import Callable
from pathlib import Path

from .core.config import Settings


AppFactory = Callable[[Settings, str], object]


def _setup_logging(output_dir: str, project_slug: str) -> None:
    log_dir = Path(output_dir) / project_slug / ".feeder"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "agent.log"
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(name)s] %(levelname)s: %(message)s", datefmt="%H:%M:%S")
    fh = logging.FileHandler(str(log_path), encoding="utf-8")
    fh.setFormatter(fmt)
    root.addHandler(fh)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Paper discovery agent with LLM tool calling.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover_parser = subparsers.add_parser(
        "discover",
        help="Discover papers from a natural-language query and materialize them into raw markdown.",
    )
    discover_parser.add_argument("--project", type=str, required=True, help="Project slug used for the work directory.")
    query_group = discover_parser.add_mutually_exclusive_group(required=True)
    query_group.add_argument("--query", type=str, help="Natural-language query for paper discovery.")
    query_group.add_argument("--query-txt", type=str, dest="query_txt", help="Path to a .txt file containing the query.")
    discover_parser.add_argument("--top-k", type=int, default=5, help="Maximum number of raw paper files to write.")
    discover_parser.add_argument(
        "--output-dir",
        type=str,
        default="projects",
        help="Root directory for project outputs.",
    )
    return parser.parse_args(argv)


def _resolve_query(args: argparse.Namespace) -> str:
    if args.query:
        return args.query.strip()
    path = Path(args.query_txt)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"query-txt file not found: {args.query_txt}")
    for enc in ("utf-8", "utf-16", "gbk"):
        try:
            return path.read_text(encoding=enc).strip()
        except (UnicodeDecodeError, UnicodeError):
            continue
    raise argparse.ArgumentTypeError(f"Failed to decode query-txt file: {args.query_txt}")


async def run_once(
    *,
    project_slug: str,
    query: str,
    top_k: int,
    output_dir: str,
    app_factory: AppFactory | None = None,
    settings: Settings | None = None,
) -> None:
    from .app import RawFeederApplication

    _setup_logging(output_dir, project_slug)
    resolved_settings = settings or Settings.from_env()
    factory = app_factory or (lambda configured_settings, configured_output: RawFeederApplication(configured_settings, output_root=configured_output))
    app = factory(resolved_settings, output_dir)

    try:
        batch, batch_path = await app.discover(project_slug=project_slug, query=query, top_k=top_k)
        print(f"\nProject: {project_slug}")
        print(f"Query: {query}")
        print(f"Batch: {batch_path}")
        selected = batch.get("selected_count", 0) if isinstance(batch, dict) else getattr(batch, "selected_count", 0)
        written = batch.get("written_files", []) if isinstance(batch, dict) else getattr(batch, "written_files", [])
        print(f"Selected raw papers: {selected}")
        for item in written:
            path = item.get("path", "") if isinstance(item, dict) else getattr(item, "path", "")
            print(f"- {path}")
    finally:
        await app.close()


def run_cli(
    argv: list[str] | None = None,
    *,
    app_factory: AppFactory | None = None,
    settings: Settings | None = None,
) -> int:
    args = parse_args(argv)
    if args.command != "discover":
        raise ValueError(f"Unsupported command: {args.command}")
    query = _resolve_query(args)
    asyncio.run(
        run_once(
            project_slug=args.project.strip(),
            query=query,
            top_k=args.top_k,
            output_dir=args.output_dir.strip(),
            app_factory=app_factory,
            settings=settings,
        )
    )
    return 0


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s", datefmt="%H:%M:%S")
    raise SystemExit(run_cli())


if __name__ == "__main__":
    main()
