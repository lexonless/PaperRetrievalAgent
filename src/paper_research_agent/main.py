from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from .config import Settings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the LangGraph research assistant.")
    parser.add_argument("--project", type=str, required=True, help="Project slug used for the project library.")
    parser.add_argument("--query", type=str, help="Run a single research query.")
    parser.add_argument("--query-file", type=str, help="Path to a text file containing the query prompt.")
    parser.add_argument("--pdf-dir", type=str, default="", help="Optional directory containing local PDF sources.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="projects",
        help="Project library root directory.",
    )
    parser.add_argument(
        "--no-stream",
        action="store_true",
        help="Disable progress streaming and only print final artifact paths.",
    )
    return parser.parse_args()


async def run_once(
    *,
    project_slug: str,
    query: str,
    pdf_dir: str,
    output_dir: str,
    stream: bool,
) -> None:
    from .app import ResearchAssistantApplication

    settings = Settings.from_env()
    app = ResearchAssistantApplication(settings, output_root=output_dir)

    try:
        final_state: dict | None = None
        if stream:
            async for update in await app.run_stream(project_slug=project_slug, task=query, pdf_dir=pdf_dir):
                final_state = update
                stop_reason = update.get("run", {}).get("stop_reason", "")
                revision_count = update.get("retrieval", {}).get("revision_count", 0)
                print(f"[graph] stop_reason={stop_reason or 'running'} revision_count={revision_count}")
        else:
            final_state = await app.run(project_slug=project_slug, task=query, pdf_dir=pdf_dir)

        if final_state is None:
            raise RuntimeError("The graph did not produce a final state.")
        artifacts = final_state.get("run", {}).get("artifacts", {})
        print(f"\nProject: {project_slug}")
        print(f"Note: {artifacts.get('note_path', '')}")
        print(f"Retrieval JSON: {artifacts.get('retrieval_path', '')}")
        print(f"Trace JSON: {artifacts.get('trace_path', '')}")
        stop_reason = final_state.get("run", {}).get("stop_reason", "")
        if stop_reason:
            print(f"Stop reason: {stop_reason}")
    finally:
        await app.close()


def main() -> None:
    args = parse_args()
    query = _resolve_query(args)
    asyncio.run(
        run_once(
            project_slug=args.project.strip(),
            query=query,
            pdf_dir=args.pdf_dir.strip(),
            output_dir=args.output_dir.strip(),
            stream=not args.no_stream,
        )
    )


def _resolve_query(args: argparse.Namespace) -> str:
    if args.query and args.query_file:
        raise ValueError("Use either --query or --query-file, not both.")
    if args.query:
        return args.query.strip()
    if args.query_file:
        query_path = Path(args.query_file)
        content = query_path.read_text(encoding="utf-8").strip()
        if not content:
            raise ValueError(f"Query file is empty: {query_path}")
        return content
    raise ValueError("Provide either --query or --query-file.")


if __name__ == "__main__":
    main()
