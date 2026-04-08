from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from autogen_agentchat.ui import Console

from .app import PaperSearchApplication
from .config import Settings
from .reporting import save_markdown_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the AutoGen paper retrieval agent.")
    parser.add_argument("--query", type=str, help="Run a single paper-search query.")
    parser.add_argument(
        "--query-file",
        type=str,
        help="Path to a text file containing the query prompt.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="Directory used to save markdown reports.",
    )
    return parser.parse_args()


async def run_once(query: str, output_dir: str) -> None:
    settings = Settings.from_env()
    app = PaperSearchApplication(settings)

    try:
        task_result = await Console(await app.run_stream(query))
        report = save_markdown_report(task_result, query, output_dir=output_dir)
        print(f"\nUser markdown saved to: {report.report_path}")
        print(f"Debug trace saved to: {report.debug_path}")
    finally:
        await app.close()


async def run_interactive(output_dir: str) -> None:
    settings = Settings.from_env()
    app = PaperSearchApplication(settings)

    print("Paper Retrieval Agent")
    print("Type your query. Enter 'exit' to quit.")

    try:
        while True:
            query = input("\n>>> ").strip()
            if not query:
                continue
            if query.lower() in {"exit", "quit"}:
                break
            task_result = await Console(await app.run_stream(query))
            report = save_markdown_report(task_result, query, output_dir=output_dir)
            print(f"\nUser markdown saved to: {report.report_path}")
            print(f"Debug trace saved to: {report.debug_path}")
    finally:
        await app.close()


def main() -> None:
    args = parse_args()
    query = _resolve_query(args)
    if query is not None:
        asyncio.run(run_once(query, args.output_dir))
        return
    asyncio.run(run_interactive(args.output_dir))


def _resolve_query(args: argparse.Namespace) -> str | None:
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
    return None


if __name__ == "__main__":
    main()
