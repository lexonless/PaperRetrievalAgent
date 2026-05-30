from __future__ import annotations

import asyncio
import re
import time
import xml.etree.ElementTree as ET
from typing import Any

from ..core.config import Settings
from ..core.models import PaperDict
from ..core.normalization import normalize_string_list, normalize_text
from .utils import DEFAULT_SOURCE_ORDER, normalize_pdf_url


class PaperSourceCollector:
    _arxiv_lock = asyncio.Lock()
    _last_arxiv_call: float = 0
    _arxiv_min_interval: float = 5.0

    def __init__(self, settings: Settings, client: Any) -> None:
        self._settings = settings
        self._client = client

    async def collect_records_for_query_specs(
        self,
        query_specs: list[str] | list[dict[str, Any]],
        stage_name: str,
        max_results_per_source: int | None,
        from_year: int | None,
    ) -> tuple[list[PaperDict], list[dict[str, str]], list[dict[str, Any]]]:
        records: list[PaperDict] = []
        source_errors: list[dict[str, str]] = []
        executed_specs: list[dict[str, Any]] = []

        for query_spec in query_specs:
            if isinstance(query_spec, dict):
                query = normalize_text(query_spec.get("query", ""))
                target_source = normalize_text(query_spec.get("source", ""))
                purpose = normalize_text(query_spec.get("purpose", "")) or "precision"
                notes = normalize_text(query_spec.get("notes", ""))
            else:
                query = normalize_text(query_spec)
                target_source = ""
                purpose = "precision"
                notes = ""
            if not query:
                continue
            query_records, query_errors = await self.collect_all_source_records(
                query=query,
                stage_name=stage_name,
                max_results_per_source=max_results_per_source,
                from_year=from_year,
                target_source=target_source,
            )
            records.extend(query_records)
            source_errors.extend(query_errors)
            sources = [target_source] if target_source else list(DEFAULT_SOURCE_ORDER)
            executed_specs.append({"query": query, "sources": sources, "stage": stage_name, "purpose": purpose, "notes": notes})
        return records, source_errors, executed_specs

    async def collect_all_source_records(
        self,
        query: str,
        stage_name: str,
        max_results_per_source: int | None = None,
        from_year: int | None = None,
        target_source: str = "",
    ) -> tuple[list[PaperDict], list[dict[str, str]]]:
        tasks: list[tuple[str, Any]] = []
        for source_name in DEFAULT_SOURCE_ORDER:
            if target_source and source_name != target_source:
                continue
            if source_name == "arXiv":
                tasks.append(("arXiv", self.search_arxiv_records(query, max_results=max_results_per_source)))
            elif source_name == "Crossref":
                tasks.append(("Crossref", self.search_crossref_records(query, max_results=max_results_per_source, from_year=from_year)))
            elif source_name == "OpenAlex":
                tasks.append(("OpenAlex", self.search_openalex_records(query, max_results=max_results_per_source, from_year=from_year)))

        rendered_results = await asyncio.gather(*(task for _, task in tasks), return_exceptions=True)
        records: list[PaperDict] = []
        source_errors: list[dict[str, str]] = []
        for (source_name, _), rendered in zip(tasks, rendered_results, strict=False):
            if isinstance(rendered, Exception):
                source_errors.append({"source": source_name, "error": str(rendered), "query": query})
                continue
            for record in rendered:
                records.append(
                    PaperDict(
                        title=record.title,
                        source=record.source,
                        evidence_snippets=record.evidence_snippets,
                        authors=record.authors,
                        date=record.date,
                        url=record.url,
                        pdf_url=record.pdf_url,
                        doi=record.doi,
                        source_rank=record.source_rank,
                        matched_query=query,
                        query_stage=stage_name,
                        openalex_id=record.openalex_id,
                        cited_by_count=record.cited_by_count,
                    )
                )
        return records, source_errors

    async def search_arxiv_records(self, query: str, max_results: int | None = None) -> list[PaperDict]:
        async with PaperSourceCollector._arxiv_lock:
            elapsed = time.monotonic() - PaperSourceCollector._last_arxiv_call
            if elapsed < PaperSourceCollector._arxiv_min_interval:
                await asyncio.sleep(PaperSourceCollector._arxiv_min_interval - elapsed)
            limit = self._resolve_limit(max_results)
            search_query = self._format_arxiv_search_query(query)
            response = await self._client.get(
                "https://export.arxiv.org/api/query",
                params={"search_query": search_query, "start": 0, "max_results": limit, "sortBy": "relevance", "sortOrder": "descending"},
            )
            PaperSourceCollector._last_arxiv_call = time.monotonic()
        response.raise_for_status()
        root = ET.fromstring(response.text)
        namespace = {"atom": "http://www.w3.org/2005/Atom"}
        entries = root.findall("atom:entry", namespace)

        records: list[PaperDict] = []
        for rank, entry in enumerate(entries, start=1):
            authors = [author.findtext("atom:name", default="", namespaces=namespace).strip() for author in entry.findall("atom:author", namespace)]
            title = entry.findtext("atom:title", default="", namespaces=namespace).strip()
            summary = entry.findtext("atom:summary", default="", namespaces=namespace).strip()
            published = entry.findtext("atom:published", default="", namespaces=namespace).strip()
            url = entry.findtext("atom:id", default="", namespaces=namespace).strip()
            pdf_url = ""
            for link in entry.findall("atom:link", namespace):
                href = normalize_text(link.attrib.get("href", ""))
                title_attr = normalize_text(link.attrib.get("title", "")).lower()
                type_attr = normalize_text(link.attrib.get("type", "")).lower()
                if title_attr == "pdf" or type_attr == "application/pdf" or href.lower().endswith(".pdf"):
                    pdf_url = href
                    break
            records.append(PaperDict(title=normalize_text(title), source="arXiv", evidence_snippets=[normalize_text(summary)], authors=[a for a in authors if a], date=published, url=url, pdf_url=normalize_pdf_url(pdf_url) or normalize_pdf_url(url), source_rank=rank))
        return records

    async def search_crossref_records(self, query: str, max_results: int | None = None, from_year: int | None = None) -> list[PaperDict]:
        limit = self._resolve_limit(max_results)
        params: dict[str, Any] = {"query": query, "rows": limit, "select": "title,author,DOI,URL,published-print,published-online,issued,container-title,abstract,link"}
        if from_year is not None:
            params["filter"] = f"from-pub-date:{from_year}-01-01"
        response = await self._client.get("https://api.crossref.org/works", params=params)
        response.raise_for_status()
        items = response.json().get("message", {}).get("items", [])

        records: list[PaperDict] = []
        for rank, item in enumerate(items, start=1):
            title_list = item.get("title") or []
            title = title_list[0].strip() if title_list else "Untitled"
            authors: list[str] = []
            for author in item.get("author", []):
                given = (author.get("given") or "").strip()
                family = (author.get("family") or "").strip()
                full_name = " ".join(part for part in [given, family] if part)
                if full_name:
                    authors.append(full_name)
            venue_list = item.get("container-title") or []
            venue = venue_list[0].strip() if venue_list else "Crossref"
            records.append(
                PaperDict(
                    title=normalize_text(title),
                    source=f"Crossref / {venue}",
                    evidence_snippets=[normalize_text(item.get("abstract", ""))],
                    authors=authors,
                    date=self._extract_crossref_date(item),
                    url=(item.get("URL") or "").strip(),
                    pdf_url=self._extract_crossref_pdf_url(item),
                    doi=(item.get("DOI") or "").strip(),
                    source_rank=rank,
                )
            )
        return records

    async def search_openalex_records(self, query: str, max_results: int | None = None, from_year: int | None = None) -> list[PaperDict]:
        limit = self._resolve_limit(max_results)
        params: dict[str, Any] = {
            "search": query,
            "per-page": limit,
            "sort": "relevance_score:desc",
            "select": ",".join(["display_name", "authorships", "publication_year", "publication_date", "ids", "doi", "primary_location", "abstract_inverted_index", "abstract", "type", "cited_by_count"]),
        }
        if from_year is not None:
            params["filter"] = f"from_publication_date:{from_year}-01-01"
        response = await self._client.get("https://api.openalex.org/works", params=params)
        response.raise_for_status()
        items = response.json().get("results", [])

        records: list[PaperDict] = []
        for rank, item in enumerate(items, start=1):
            title = normalize_text(item.get("display_name", "") or "Untitled")
            authors: list[str] = []
            for authorship in item.get("authorships") or []:
                if not isinstance(authorship, dict):
                    continue
                author = authorship.get("author") or {}
                if not isinstance(author, dict):
                    continue
                name = normalize_text(author.get("display_name", ""))
                if name:
                    authors.append(name)
            published = normalize_text(item.get("publication_date") or str(item.get("publication_year") or ""))
            ids = item.get("ids") or {}
            primary_location = item.get("primary_location") or {}
            landing_page = ""
            pdf_url = ""
            openalex_id = ""
            if isinstance(primary_location, dict):
                landing_page = normalize_text(primary_location.get("landing_page_url", ""))
                pdf_url = normalize_pdf_url(primary_location.get("pdf_url", "") or "")
            if isinstance(ids, dict):
                openalex_url = normalize_text(ids.get("openalex", ""))
                landing_page = landing_page or openalex_url
                if "/W" in openalex_url:
                    openalex_id = openalex_url.rsplit("/", 1)[-1]
            cited_by = item.get("cited_by_count") or 0
            doi = normalize_text(item.get("doi", ""))
            if doi.startswith("https://doi.org/"):
                doi = doi.removeprefix("https://doi.org/")
            records.append(
                PaperDict(
                    title=title,
                    source="OpenAlex",
                    evidence_snippets=[self._extract_openalex_abstract(item)],
                    authors=authors,
                    date=published,
                    url=landing_page,
                    pdf_url=pdf_url,
                    doi=doi,
                    source_rank=rank,
                    openalex_id=openalex_id,
                    cited_by_count=cited_by,
                )
            )
        return records

    async def fetch_references(self, openalex_id: str, top_k: int = 5) -> list[PaperDict]:
        """Fetch papers that this paper references (前向溯源)."""
        response = await self._client.get(f"https://api.openalex.org/works/{openalex_id}")
        response.raise_for_status()
        work = response.json()
        ref_urls = work.get("referenced_works", []) or []
        ref_ids = [_extract_openalex_id_from_url(u) for u in ref_urls[:30]]
        ref_ids = [rid for rid in ref_ids if rid]
        if not ref_ids:
            return []
        filter_param = "|".join(ref_ids[:25])
        params: dict[str, Any] = {
            "filter": f"openalex_id:{filter_param}",
            "per-page": 25,
            "sort": "cited_by_count:desc",
            "select": "display_name,authorships,publication_year,publication_date,ids,doi,primary_location,abstract_inverted_index,cited_by_count",
        }
        resp = await self._client.get("https://api.openalex.org/works", params=params)
        resp.raise_for_status()
        return self._parse_openalex_batch(resp.json().get("results", []))[:top_k]

    async def fetch_citations(self, openalex_id: str, top_k: int = 5) -> list[PaperDict]:
        """Fetch papers that cite this paper (后向追踪), filtered for recency and impact."""
        import datetime as dt
        two_years_ago = (dt.date.today().replace(year=dt.date.today().year - 2)).isoformat()
        params: dict[str, Any] = {
            "filter": f"cites:{openalex_id},from_publication_date:{two_years_ago}",
            "per-page": 20,
            "sort": "cited_by_count:desc",
            "select": "display_name,authorships,publication_year,publication_date,ids,doi,primary_location,abstract_inverted_index,cited_by_count",
        }
        response = await self._client.get("https://api.openalex.org/works", params=params)
        response.raise_for_status()
        items = response.json().get("results", [])
        records = self._parse_openalex_batch(items)
        return [r for r in records if r.source_rank > 0][:top_k]

    def _parse_openalex_batch(self, items: list[dict[str, Any]]) -> list[PaperDict]:
        records: list[PaperDict] = []
        for rank, item in enumerate(items, start=1):
            title = normalize_text(item.get("display_name", "") or "Untitled")
            if not title or title == "Untitled":
                continue
            authors: list[str] = []
            for a in item.get("authorships") or []:
                if isinstance(a, dict) and isinstance(a.get("author"), dict):
                    name = normalize_text(a["author"].get("display_name", ""))
                    if name:
                        authors.append(name)
            published = normalize_text(item.get("publication_date") or str(item.get("publication_year") or ""))
            ids = item.get("ids") or {}
            loc = item.get("primary_location") or {}
            landing = normalize_text(loc.get("landing_page_url", "") or ids.get("openalex", ""))
            pdf = normalize_pdf_url(loc.get("pdf_url", "") or "")
            doi = normalize_text(item.get("doi", ""))
            if doi.startswith("https://doi.org/"):
                doi = doi.removeprefix("https://doi.org/")
            oa_id = ""
            oa_url = normalize_text(ids.get("openalex", ""))
            if "/W" in oa_url:
                oa_id = oa_url.rsplit("/", 1)[-1]
            cited_by = item.get("cited_by_count") or 0
            records.append(
                PaperDict(
                    title=title,
                    source="OpenAlex",
                    evidence_snippets=[self._extract_openalex_abstract(item)],
                    authors=authors,
                    date=published,
                    url=landing,
                    pdf_url=pdf,
                    doi=doi,
                    source_rank=rank,
                    openalex_id=oa_id,
                    cited_by_count=cited_by,
                )
            )
        return records

    def _format_arxiv_search_query(self, query: str) -> str:
        cleaned = normalize_text(query)
        if not cleaned:
            return ""
        if re.search(r"\b(?:all|ti|abs|au|cat|id|jr|co|rn):", cleaned, flags=re.IGNORECASE):
            return cleaned
        return f"all:{cleaned}"

    def _resolve_limit(self, max_results: int | None) -> int:
        if max_results is None:
            return self._settings.max_results_per_source
        return max(1, min(max_results, 20))

    def _extract_crossref_date(self, item: dict[str, Any]) -> str:
        for field_name in ("published-print", "published-online", "issued"):
            field = item.get(field_name)
            if not field:
                continue
            parts = field.get("date-parts", [])
            if not parts or not parts[0]:
                continue
            return "-".join(str(part) for part in parts[0])
        return ""

    def _extract_crossref_pdf_url(self, item: dict[str, Any]) -> str:
        links = item.get("link")
        if not isinstance(links, list):
            return ""
        for link in links:
            if not isinstance(link, dict):
                continue
            content_type = normalize_text(link.get("content-type", "")).lower()
            candidate = normalize_pdf_url(str(link.get("URL") or link.get("url") or ""))
            if candidate and (content_type == "application/pdf" or candidate.lower().endswith(".pdf")):
                return candidate
        return ""

    @staticmethod
    def _extract_openalex_abstract(item: dict[str, Any]) -> str:
        inv_index = item.get("abstract_inverted_index")
        if isinstance(inv_index, dict):
            from pyalex import invert_abstract

            text = invert_abstract(inv_index)
            if text:
                return normalize_text(text)
        plain = item.get("abstract")
        if isinstance(plain, str):
            plain = normalize_text(plain)
            if plain:
                return plain
        return ""


def _extract_openalex_id_from_url(url: str) -> str:
    if "/W" in url:
        return url.rsplit("/", 1)[-1].strip()
    return ""
