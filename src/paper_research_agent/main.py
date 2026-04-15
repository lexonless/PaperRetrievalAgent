from __future__ import annotations

import argparse
import asyncio
from collections.abc import Callable

from .core.config import Settings


AppFactory = Callable[[Settings, str], object]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Raw feeder for LLM Wiki source materials.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover_parser = subparsers.add_parser(
        "discover",
        help="Discover papers from a natural-language query and materialize them into raw markdown.",
    )
    discover_parser.add_argument("--project", type=str, required=True, help="Project slug used for the feeder workspace.")
    discover_parser.add_argument("--query", type=str, required=True, help="Natural-language query for paper discovery.")
    discover_parser.add_argument("--top-k", type=int, default=5, help="Maximum number of raw paper files to write.")
    discover_parser.add_argument(
        "--output-dir",
        type=str,
        default="projects",
        help="Root directory for project raw outputs.",
    )
    return parser.parse_args(argv)


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

    resolved_settings = settings or Settings.from_env()
    factory = app_factory or (lambda configured_settings, configured_output: RawFeederApplication(configured_settings, output_root=configured_output))
    app = factory(resolved_settings, output_dir)

    try:
        batch, batch_path = await app.discover(project_slug=project_slug, query=query, top_k=top_k)
        print(f"\nProject: {project_slug}")
        print(f"Query: {query}")
        print(f"Batch: {batch_path}")
        print(f"Selected raw papers: {batch.selected_count}")
        for item in batch.written_files:
            print(f"- {item.path}")
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
    asyncio.run(
        run_once(
            project_slug=args.project.strip(),
            query=args.query.strip(),
            top_k=args.top_k,
            output_dir=args.output_dir.strip(),
            app_factory=app_factory,
            settings=settings,
        )
    )
    return 0


def main() -> None:
    raise SystemExit(run_cli())


if __name__ == "__main__":
    main()
