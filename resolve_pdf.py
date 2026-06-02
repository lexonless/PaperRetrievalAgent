#!/usr/bin/env python
"""Standalone DOI → PDF URL resolver.

Usage:
    python resolve_pdf.py 10.1109/icra55743.2025.11128271
    python resolve_pdf.py 10.1109/icra55743.2025.11128271 10.1115/1.4070890
"""

from __future__ import annotations

import asyncio
import os
import re
import sys

import httpx

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from paper_research_agent.agent.pdf import PdfUrlResolver
from paper_research_agent.agent.url_utils import sort_pdf_urls, url_source_label
from paper_research_agent.core.config import Settings

_HEADERS = {
    "User-Agent": "paper-discovery-agent/0.1 (doi pdf resolver)",
    "Accept": "*/*",
}


async def _resolve(dois: list[str], *, settings: Settings) -> dict[str, list[str]]:
    async with httpx.AsyncClient(headers=_HEADERS, follow_redirects=True, timeout=30) as client:
        resolver = PdfUrlResolver(settings, client)

        oa_by_doi, s2_by_doi, cr_by_doi = await asyncio.gather(
            resolver._batch_fetch_openalex_by_doi(dois),
            resolver._batch_fetch_s2_by_doi(dois),
            resolver._resolve_crossref_batch(dois),
        )

        result: dict[str, list[str]] = {}
        for doi in dois:
            doi_lower = doi.lower()
            urls: list[str] = []
            for mapping in (oa_by_doi, s2_by_doi, cr_by_doi):
                for u in mapping.get(doi_lower, []):
                    if u and u not in urls:
                        urls.append(u)
            if urls:
                result[doi_lower] = sort_pdf_urls(urls)

        if settings.unpaywall_email:
            upw_by_doi = await resolver._resolve_unpaywall_batch(dois)
            for doi in dois:
                doi_lower = doi.lower()
                for u in upw_by_doi.get(doi_lower, []):
                    if u and u not in result.get(doi_lower, []):
                        result.setdefault(doi_lower, []).append(u)
                if doi_lower in result:
                    result[doi_lower] = sort_pdf_urls(result[doi_lower])

        return result


def _build_settings(email: str) -> Settings:
    return Settings(
        model_api_key="",
        model_base_url="https://example.com",
        model_name="",
        default_headers=None,
        rerank_model_api_key="",
        rerank_model_base_url="https://example.com",
        rerank_model_name="",
        rerank_default_headers=None,
        cross_encoder_model="BAAI/bge-reranker-base",
        cross_encoder_device="cpu",
        cross_encoder_batch_size=32,
        cross_encoder_max_length=512,
        request_timeout=30.0,
        max_output_tokens=4096,
        max_results_per_source=10,
        http_proxy="",
        openalex_api_key=os.getenv("OPENALEX_API_KEY", ""),
        unpaywall_email=email,
        pdf_extractor="docling",
    )


def main(argv: list[str] | None = None) -> None:

    args = argv or sys.argv[1:]
    email: str = ""
    dois_args: list[str] = []

    i = 0
    while i < len(args):
        if args[i] in ("--email", "-e") and i + 1 < len(args):
            email = args[i + 1].strip()
            i += 2
        elif args[i].startswith("--email="):
            email = args[i].split("=", 1)[1].strip()
            i += 1
        else:
            dois_args.append(args[i])
            i += 1

    if not email:
        email = os.getenv("UNPAYWALL_EMAIL", "").strip()

    if not dois_args:
        print("Usage: python resolve_pdf.py [--email user@example.com] <doi> [doi...]", file=sys.stderr)
        sys.exit(1)

    dois: list[str] = []
    for arg in dois_args:
        doi = arg.strip().lower()
        doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi)
        if doi.startswith("10."):
            dois.append(doi)
        else:
            print(f"Skipping invalid DOI: {arg}", file=sys.stderr)

    if not dois:
        print("No valid DOIs provided.", file=sys.stderr)
        sys.exit(1)

    settings = _build_settings(email)
    result = asyncio.run(_resolve(dois, settings=settings))

    for doi, urls in result.items():
        print(f"\n{doi}")
        print(f"  {'─' * 60}")
        if urls:
            for i, u in enumerate(urls, 1):
                label = url_source_label(u)
                print(f"  [{i}] {label:20s}  {u}")
        else:
            print("  (no PDF URLs found)")
        print()


if __name__ == "__main__":
    main()
