from __future__ import annotations

import asyncio
import logging
import re
from pathlib import Path
from typing import Any

import httpx

from ..core.config import Settings
from ..core.models import PaperDict
from ..core.normalization import normalize_text
from .url_utils import extract_direct_pdf_urls, extract_http_status, sort_pdf_urls, url_source_label

logger = logging.getLogger(__name__)


class PdfUrlResolver:
    _OPENALEX_DOI_BATCH_SIZE = 25
    _S2_BATCH_SIZE = 100
    _crossref_semaphore: asyncio.Semaphore | None = None
    _unpaywall_semaphore: asyncio.Semaphore | None = None

    def __init__(self, settings: Settings, client: httpx.AsyncClient | None) -> None:
        self._settings = settings
        self._client = client

    async def resolve_pdf_urls(self, papers: list[PaperDict]) -> None:
        if self._client is None:
            return

        paper_infos: list[tuple[int, str, list[str]]] = []
        all_dois: list[str] = []

        for idx, paper in enumerate(papers):
            if paper.pdf_status == "available":
                continue
            urls = extract_direct_pdf_urls(paper)
            doi = normalize_text(paper.doi)
            if doi and doi.startswith("10.") and doi not in all_dois:
                all_dois.append(doi)
            paper_infos.append((idx, doi, urls))

        logger.info("pdf resolve: %s papers, %s unique DOIs", len(paper_infos), len(all_dois))

        oa_by_doi: dict[str, list[str]] = {}
        s2_by_doi: dict[str, list[str]] = {}
        cr_by_doi: dict[str, list[str]] = {}

        if all_dois:
            logger.info("pdf resolve: querying OpenAlex + Semantic Scholar + Crossref in parallel")
            oa_by_doi, s2_by_doi, cr_by_doi = await asyncio.gather(
                self._batch_fetch_openalex_by_doi(all_dois),
                self._batch_fetch_s2_by_doi(all_dois),
                self._resolve_crossref_batch(all_dois),
            )
            logger.info(
                "pdf resolve: OA=%s S2=%s Crossref=%s (of %s DOIs)",
                len(oa_by_doi), len(s2_by_doi), len(cr_by_doi), len(all_dois),
            )

        upw_dois: list[str] = []

        for idx, doi, layer1_urls in paper_infos:
            paper = papers[idx]
            all_urls: list[str] = list(layer1_urls)

            if doi:
                for u in oa_by_doi.get(doi, []):
                    if u and u not in all_urls:
                        all_urls.append(u)
                for u in s2_by_doi.get(doi, []):
                    if u and u not in all_urls:
                        all_urls.append(u)
                for u in cr_by_doi.get(doi, []):
                    if u and u not in all_urls:
                        all_urls.append(u)

            if all_urls:
                paper.pdf_urls = sort_pdf_urls(all_urls)
                paper.pdf_url = paper.pdf_urls[0]
                paper.pdf_status = "available"
            elif doi and doi.startswith("10."):
                upw_dois.append(doi)

        if upw_dois and self._settings.unpaywall_email:
            logger.info("pdf resolve: querying Unpaywall for %s unresolved DOIs", len(upw_dois))
            upw_by_doi = await self._resolve_unpaywall_batch(upw_dois)
            logger.info("pdf resolve: Unpaywall found %s URLs", len(upw_by_doi))
            for idx, doi, _layer1_urls in paper_infos:
                if doi and doi in upw_by_doi:
                    paper = papers[idx]
                    all_urls = list(paper.pdf_urls)
                    for u in upw_by_doi.get(doi, []):
                        if u and u not in all_urls:
                            all_urls.append(u)
                    if all_urls:
                        paper.pdf_urls = sort_pdf_urls(all_urls)
                        paper.pdf_url = paper.pdf_urls[0]
                        paper.pdf_status = "available"

        available = sum(1 for p in papers if p.pdf_status == "available")
        logger.info("pdf resolve: %s/%s papers got PDF URLs", available, len(papers))

    async def _batch_fetch_openalex_by_doi(self, dois: list[str]) -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        failed: list[str] = []

        for batch_start in range(0, len(dois), self._OPENALEX_DOI_BATCH_SIZE):
            batch = dois[batch_start:batch_start + self._OPENALEX_DOI_BATCH_SIZE]
            filter_value = "doi:" + "|".join(batch)
            try:
                response = await self._client.get(
                    "https://api.openalex.org/works",
                    params={"filter": filter_value, "per_page": str(len(batch) * 2)},
                    timeout=15,
                )
                response.raise_for_status()
                data = response.json()
                for work in data.get("results") or []:
                    work_doi = self._extract_doi_from_openalex(work)
                    urls = self._extract_openalex_pdf_urls(work)
                    if work_doi and urls:
                        result[work_doi] = urls
            except Exception as exc:
                logger.debug("OpenAlex batch failed (%s): %s", len(batch), exc)
                failed.extend(batch)

        for doi in failed:
            if doi in result:
                continue
            try:
                work = await asyncio.to_thread(self._fetch_openalex_work_via_pyalex, doi)
                if work is None:
                    continue
                urls = self._extract_openalex_pdf_urls(work)
                if urls:
                    result[doi.lower()] = urls
            except Exception as exc:
                logger.debug("OpenAlex individual fallback failed for %s: %s", doi, exc)

        return result

    @staticmethod
    def _fetch_openalex_work_via_pyalex(doi: str) -> dict | None:
        from pyalex import Works

        try:
            work = Works()["doi:" + doi]
            return dict(work) if work else None
        except Exception:
            return None

    @staticmethod
    def _extract_doi_from_openalex(work: dict) -> str:
        raw = normalize_text(work.get("doi", "") or "")
        return raw.lower().lstrip("https://doi.org/")

    @staticmethod
    def _extract_openalex_pdf_urls(work: dict) -> list[str]:
        urls: list[str] = []

        all_locations: list[dict] = []
        pl = work.get("primary_location")
        if isinstance(pl, dict):
            all_locations.append(pl)
        locs = work.get("locations")
        if isinstance(locs, list):
            all_locations.extend(locs)

        for loc in all_locations:
            if not isinstance(loc, dict):
                continue
            landing = normalize_text(loc.get("landing_page_url", "") or "")
            pdf = normalize_text(loc.get("pdf_url", "") or "")
            candidate = pdf or landing
            if not candidate:
                continue
            if "arxiv.org" in candidate.lower():
                if candidate not in urls:
                    urls.insert(0, candidate)
            elif candidate.lower().endswith(".pdf") and candidate not in urls:
                urls.append(candidate)

        oa_id = work.get("id", "").rsplit("/", 1)[-1] if work.get("id") else ""
        if oa_id and oa_id.startswith("W"):
            mirror = f"https://content.openalex.org/works/{oa_id}.pdf"
            if mirror not in urls:
                urls.append(mirror)
        return urls

    async def _batch_fetch_s2_by_doi(self, dois: list[str]) -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        failed: list[str] = []

        for batch_start in range(0, len(dois), self._S2_BATCH_SIZE):
            batch = dois[batch_start:batch_start + self._S2_BATCH_SIZE]
            ids = [f"DOI:{d}" for d in batch]
            batch_ok = False
            for attempt in range(2):
                try:
                    response = await self._client.post(
                        "https://api.semanticscholar.org/graph/v1/paper/batch",
                        params={"fields": "externalIds,openAccessPdf"},
                        json={"ids": ids},
                        timeout=20,
                    )
                    response.raise_for_status()
                    papers = response.json()
                    if not isinstance(papers, list):
                        continue
                    for paper in papers:
                        if not isinstance(paper, dict):
                            continue
                        paper_doi = self._extract_doi_from_s2(paper)
                        urls = self._extract_s2_pdf_urls(paper)
                        if paper_doi and urls:
                            result[paper_doi] = urls
                    batch_ok = True
                    break
                except Exception as exc:
                    if attempt == 0:
                        await asyncio.sleep(3)
                    else:
                        logger.debug("S2 batch failed (%s): %s", len(batch), exc)
            if not batch_ok:
                failed.extend(batch)

        for doi in failed:
            if doi in result:
                continue
            try:
                response = await self._client.get(
                    f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                    params={"fields": "externalIds,openAccessPdf"},
                    timeout=10,
                )
                response.raise_for_status()
                paper = response.json()
                urls = self._extract_s2_pdf_urls(paper)
                if urls:
                    result[doi.lower()] = urls
            except Exception as exc:
                logger.debug("S2 individual fallback failed for %s: %s", doi, exc)

        return result

    @staticmethod
    def _extract_doi_from_s2(paper: dict) -> str:
        raw = normalize_text(paper.get("externalIds", {}).get("DOI", "") or "")
        return raw.lower()

    @staticmethod
    def _extract_s2_pdf_urls(paper: dict) -> list[str]:
        urls: list[str] = []
        arxiv_id = normalize_text(paper.get("externalIds", {}).get("ArXiv", "") or "")
        if arxiv_id:
            urls.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
        oa = paper.get("openAccessPdf") or {}
        oa_url = normalize_text(oa.get("url", "") or "")
        if oa_url and oa_url.lower().endswith(".pdf") and oa_url not in urls:
            urls.append(oa_url)
        return urls

    async def _resolve_crossref_batch(self, dois: list[str]) -> dict[str, list[str]]:
        if PdfUrlResolver._crossref_semaphore is None:
            PdfUrlResolver._crossref_semaphore = asyncio.Semaphore(2)

        async def _lookup_one(doi: str) -> tuple[str, list[str]]:
            urls: list[str] = []
            async with PdfUrlResolver._crossref_semaphore:
                try:
                    response = await self._client.get(
                        f"https://api.crossref.org/works/{doi}",
                        timeout=10,
                    )
                    response.raise_for_status()
                except Exception as exc:
                    logger.debug("Crossref lookup failed for %s: %s", doi, exc)
                    return doi, []
                data = response.json()
                msg = data.get("message") or {}
                links = msg.get("link") or []
                if not isinstance(links, list):
                    return doi, []
                for link in links:
                    if not isinstance(link, dict):
                        continue
                    ct = normalize_text(link.get("content-type", ""), for_matching=True)
                    ia = normalize_text(link.get("intended-application", ""), for_matching=True)
                    candidate = normalize_text(str(link.get("URL") or link.get("url") or ""))
                    if not candidate:
                        continue
                    is_pdf = ct == "application/pdf" or candidate.lower().endswith(".pdf")
                    is_textmining = ia == "text-mining" or ct == "text/xml"
                    if is_pdf or is_textmining:
                        if candidate not in urls:
                            urls.append(candidate)
            return doi, urls

        tasks = [_lookup_one(d) for d in dois]
        gathered = await asyncio.gather(*tasks)
        result: dict[str, list[str]] = {}
        for doi, urls in gathered:
            if urls:
                result[doi.lower()] = urls
        return result

    async def _resolve_unpaywall_batch(self, dois: list[str]) -> dict[str, list[str]]:
        if PdfUrlResolver._unpaywall_semaphore is None:
            PdfUrlResolver._unpaywall_semaphore = asyncio.Semaphore(5)

        async def _lookup_one(doi: str) -> tuple[str, list[str]]:
            urls: list[str] = []
            async with PdfUrlResolver._unpaywall_semaphore:
                try:
                    response = await self._client.get(
                        f"https://api.unpaywall.org/v2/{doi}",
                        params={"email": self._settings.unpaywall_email},
                        timeout=10,
                    )
                    response.raise_for_status()
                    data = response.json()
                    if not data.get("is_oa"):
                        return doi, []
                    best = data.get("best_oa_location") or {}
                    pdf_url = normalize_text((best.get("url_for_pdf") or best.get("url") or ""))
                    if pdf_url and pdf_url.lower().endswith(".pdf"):
                        urls.append(pdf_url)
                except Exception as exc:
                    logger.debug("Unpaywall lookup failed for %s: %s", doi, exc)
            return doi, urls

        tasks = [_lookup_one(d) for d in dois]
        gathered = await asyncio.gather(*tasks)
        result: dict[str, list[str]] = {}
        for doi, urls in gathered:
            if urls:
                result[doi.lower()] = urls
        return result


_ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", re.IGNORECASE)
_SLUG_RE = re.compile(r"[^\w.+-]+")


def _paper_slug(paper: PaperDict) -> str:
    doi = normalize_text(paper.doi, for_matching=True)
    if doi:
        slug = _SLUG_RE.sub("_", doi)[:90].strip("_")
        return f"doi_{slug}" if slug else "paper"

    for candidate in (normalize_text(paper.url), normalize_text(paper.pdf_url)):
        match = _ARXIV_ID_RE.search(candidate)
        if match:
            arxiv_id = match.group(1).removesuffix(".pdf")
            slug = _SLUG_RE.sub("_", arxiv_id)[:90].strip("_")
            return f"arxiv_{slug}" if slug else "paper"

    title = normalize_text(paper.title)
    slug = _SLUG_RE.sub("_", title)[:90].strip("_")
    return slug or "paper"


class PdfDownloader:
    def __init__(self, settings: Settings, client: httpx.AsyncClient | None) -> None:
        self._settings = settings
        self._client = client

    async def download(self, papers: list[PaperDict], papers_pdf_dir: Path) -> None:
        """Download PDFs for papers with resolved URLs. Tries multiple URLs per paper with one retry on failure."""
        if self._client is None:
            return

        downloaded_count = 0
        failed_count = 0
        skipped_403 = 0
        for paper in papers:
            if paper.pdf_status != "available":
                continue
            slug = _paper_slug(paper)
            pdf_path = papers_pdf_dir / f"{slug}.pdf"
            urls = paper.pdf_urls or [paper.pdf_url]
            downloaded = False
            last_error = ""
            for pdf_url in urls:
                if not pdf_url:
                    continue
                for attempt in range(2):
                    try:
                        pdf_bytes = await self._fetch(pdf_url)
                        pdf_path.parent.mkdir(parents=True, exist_ok=True)
                        pdf_path.write_bytes(pdf_bytes)
                        paper.pdf_status = "downloaded"
                        paper.local_path = str(pdf_path)
                        paper.pdf_url = pdf_url
                        downloaded = True
                        logger.info(
                            "pdf ok: %s -> %s (%s)",
                            normalize_text(normalize_text(paper.title[:60])[:60]), slug,
                            url_source_label(pdf_url),
                        )
                        downloaded_count += 1
                        break
                    except Exception as exc:
                        status = extract_http_status(exc)
                        if status == 403:
                            last_error = f"403 Forbidden ({url_source_label(pdf_url)})"
                            skipped_403 += 1
                            break
                        if attempt == 0:
                            last_error = str(exc)[:120]
                            logger.debug(
                                "pdf retry: %s (%s) — %s",
                                normalize_text(normalize_text(paper.title[:60])[:60]),
                                url_source_label(pdf_url), last_error[:80],
                            )
                            await asyncio.sleep(3)
                        else:
                            last_error = str(exc)[:120]
                if downloaded:
                    break
            if not downloaded:
                paper.pdf_status = "failed"
                paper.local_path = ""
                logger.info("pdf fail: %s (%s)", normalize_text(normalize_text(paper.title[:60])[:60]), last_error[:80])
                failed_count += 1
        logger.info(
            "pdf download: %s ok, %s failed, %s skipped (403)",
            downloaded_count, failed_count, skipped_403,
        )

    async def _fetch(self, pdf_url: str) -> bytes:
        url = pdf_url
        if "content.openalex.org" in url and self._settings.openalex_api_key:
            sep = "&" if "?" in url else "?"
            url = f"{url}{sep}api_key={self._settings.openalex_api_key}"
        response = await self._client.get(url)
        response.raise_for_status()
        return response.content
