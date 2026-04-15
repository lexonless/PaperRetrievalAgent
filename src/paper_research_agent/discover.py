from __future__ import annotations

import asyncio
from collections import OrderedDict
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Awaitable, Callable
from uuid import uuid4

import httpx

from .core.config import Settings
from .core.llm import build_chat_model, build_rerank_chat_model, invoke_structured_output
from .core.models import DiscoverBatch, DiscoverIntent, DiscoverReview, QueryExecution, RawPaperArtifact
from .core.normalization import normalize_string_list, normalize_text
from .feeder_store import append_log, ensure_project_paths, persist_batch
from .materializer import (
    build_raw_paper_slug,
    render_raw_paper_markdown,
    write_raw_paper,
)
from .retrieval.query_planning import build_query_plan
from .retrieval.ranking import PaperRankingEngine
from .retrieval.sources import PaperSourceCollector


DISCOVER_INTENT_SYSTEM_PROMPT = """You are the discover-intent parser for a raw feeder system.

Your job is to convert a user's natural-language paper discovery request into a lightweight discover intent.

Rules:
1. This system prepares raw source material for a downstream wiki agent.
2. Do not answer the user's question.
3. Do not produce synthesis, comparisons, or conclusions.
4. Focus only on paper discovery intent.
5. Return only these fields:
   - topic
   - must_include
   - must_exclude
   - domain_terms
   - negative_domains
   - source_hints
   - primary_queries
   - start_year
   - end_year
6. source_hints may only contain arXiv, Crossref, or OpenAlex.
7. topic must be a short domain phrase, not a restatement of the whole user sentence.
8. domain_terms must contain domain anchors that help avoid drift into the wrong field.
9. negative_domains should capture obvious false-positive domains to suppress.
10. primary_queries should be concise retrieval-friendly queries, not long prose.
11. Keep source_hints broad unless the user explicitly narrows them.
12. If the user asks for recent papers, infer a reasonable start_year.
"""

DISCOVER_REVIEW_SYSTEM_PROMPT = """You are reviewing a paper discovery attempt for a raw feeder system.

Your job is to decide whether the current retrieval results are good enough to materialize as raw source files.

Rules:
1. Return only these fields:
   - decision
   - review_summary
   - failure_reasons
   - query_adjustments
   - domain_drift_detected
2. decision must be PASS or RETRY.
3. Use RETRY when the top results drift into the wrong domain, are too generic, or miss obvious query anchors.
4. Prefer concrete retrieval corrections in query_adjustments, such as stronger domain anchors, missing exclusions, or time-range fixes.
5. Do not write synthesis about the papers themselves.
"""

MAX_DISCOVER_ATTEMPTS = 2


class RawFeederService:
    def __init__(
        self,
        settings: Settings,
        *,
        output_root: str = "projects",
        source_collector: PaperSourceCollector | None = None,
        ranking_engine: PaperRankingEngine | None = None,
        intent_resolver: Callable[[str, str], Awaitable[DiscoverIntent]] | None = None,
    ) -> None:
        self._settings = settings
        self._output_root = Path(output_root)
        self._intent_resolver = intent_resolver
        self._client: httpx.AsyncClient | None = None
        if source_collector is None:
            self._client = httpx.AsyncClient(
                timeout=settings.request_timeout,
                headers={
                    "User-Agent": "raw-feeder/0.1 (+paper discovery for llm-wiki)",
                    "Accept": "*/*",
                },
                follow_redirects=True,
            )
            self._source_collector = PaperSourceCollector(settings, self._client)
        else:
            self._source_collector = source_collector
        self._ranking_engine = ranking_engine or PaperRankingEngine(
            rerank_model_client=build_rerank_chat_model(settings) if intent_resolver is None else None
        )
        self._chat_model = build_chat_model(settings, temperature=0.1) if intent_resolver is None else None

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()

    async def discover(
        self,
        *,
        project_slug: str,
        query: str,
        top_k: int = 5,
    ) -> tuple[DiscoverBatch, Path]:
        paths = ensure_project_paths(self._output_root, project_slug, reset_existing=True)
        project_context = paths.project_file.read_text(encoding="utf-8") if paths.project_file.exists() else ""
        discover_intent = await self._resolve_discover_intent(query, project_context)
        review = DiscoverReview(decision="PASS", review_summary="Review was skipped.")
        records: list[Any] = []
        papers: list[dict[str, Any]] = []
        executed_specs: list[dict[str, Any]] = []
        source_errors: list[dict[str, str]] = []

        attempt_count = 0
        for attempt in range(1, MAX_DISCOVER_ATTEMPTS + 1):
            attempt_count = attempt
            records, papers, executed_specs, source_errors = await self._retrieve_rank_and_rerank(discover_intent)
            review = await self._review_discovery_attempt(
                query=query,
                project_context=project_context,
                discover_intent=discover_intent,
                executed_specs=executed_specs,
                papers=papers,
                source_errors=source_errors,
                attempt=attempt,
            )
            if review.decision == "PASS" or attempt >= MAX_DISCOVER_ATTEMPTS:
                break
            discover_intent = await self._resolve_discover_intent(
                query,
                project_context,
                previous_intent=discover_intent,
                review=review,
            )

        selected_papers = papers[: max(1, min(top_k, 20))]

        generated_at = datetime.now().isoformat(timespec="seconds")
        written_files: list[RawPaperArtifact] = []
        for paper in selected_papers:
            slug = build_raw_paper_slug(paper)
            pdf_assets = await self._prepare_pdf_assets(
                papers_pdf_dir=paths.papers_pdf_dir,
                paper_fulltext_dir=paths.paper_fulltext_dir,
                paper_page_images_dir=paths.paper_page_images_dir,
                slug=slug,
                paper=paper,
            )
            target_path = paths.paper_metadata_dir / f"{slug}.md"
            content = render_raw_paper_markdown(
                paper,
                project_slug=project_slug,
                user_query=query,
                generated_at=generated_at,
                local_pdf_path=pdf_assets["local_pdf_path"],
                local_fulltext_path=pdf_assets["local_fulltext_path"],
                local_page_image_dir=pdf_assets["local_page_image_dir"],
                pdf_download_status=pdf_assets["pdf_download_status"],
                pdf_error=pdf_assets["pdf_error"],
            )
            write_raw_paper(target_path, content)
            written_files.append(
                RawPaperArtifact(
                    slug=slug,
                    title=normalize_text(paper.get("title", "")),
                    path=str(target_path),
                    source_family=normalize_text(paper.get("source", "")),
                    canonical_url=normalize_text(paper.get("url", "")),
                    doi=normalize_text(paper.get("doi", "")),
                    pdf_url=normalize_text(paper.get("_pdf_url", "")),
                    pdf_downloaded=pdf_assets["pdf_downloaded"],
                    local_pdf_path=pdf_assets["local_pdf_path"],
                    fulltext_extracted=pdf_assets["fulltext_extracted"],
                    local_fulltext_path=pdf_assets["local_fulltext_path"],
                    page_images_exported=pdf_assets["page_images_exported"],
                    local_page_image_dir=pdf_assets["local_page_image_dir"],
                    pdf_error=pdf_assets["pdf_error"],
                )
            )

        batch = DiscoverBatch(
            batch_id=f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid4().hex[:8]}",
            project_slug=project_slug,
            query=query,
            generated_at=generated_at,
            project_context_used=bool(normalize_text(project_context)),
            discover_intent=discover_intent,
            attempt_count=attempt_count,
            review_decision=review.decision,
            review_summary=review.review_summary,
            executed_queries=[
                QueryExecution(
                    query=item["query"],
                    sources=item["sources"],
                    notes=normalize_text(item.get("notes", "")) or "Executed during raw paper discovery.",
                )
                for item in executed_specs
            ],
            retrieved_record_count=len(records),
            candidate_count=len(papers),
            selected_count=len(selected_papers),
            written_files=written_files,
            source_errors=source_errors,
        )
        batch_path = persist_batch(paths, batch)
        append_log(paths, batch=batch, batch_path=batch_path)
        return batch, batch_path

    async def _resolve_discover_intent(
        self,
        query: str,
        project_context: str,
        *,
        previous_intent: DiscoverIntent | None = None,
        review: DiscoverReview | None = None,
    ) -> DiscoverIntent:
        if self._intent_resolver is not None:
            return _normalize_discover_intent(await self._intent_resolver(query, project_context))
        if self._chat_model is None:
            raise RuntimeError("No discover intent resolver is configured.")
        payload = {
            "query": query,
            "project_context": project_context,
            "allowed_sources": ["arXiv", "Crossref", "OpenAlex"],
            "today": datetime.now().date().isoformat(),
            "previous_intent": previous_intent.model_dump() if previous_intent is not None else None,
            "review_feedback": review.model_dump() if review is not None else None,
        }
        result = await invoke_structured_output(
            model=self._chat_model,
            schema=DiscoverIntent,
            system_prompt=DISCOVER_INTENT_SYSTEM_PROMPT,
            user_prompt=json.dumps(payload, ensure_ascii=False, indent=2),
        )
        return _normalize_discover_intent(result)

    async def _retrieve_rank_and_rerank(
        self,
        discover_intent: DiscoverIntent,
    ) -> tuple[list[Any], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, str]]]:
        query_plan = build_discover_query_plan(discover_intent)
        source_hints = _normalize_source_hints(discover_intent.source_hints)
        if source_hints:
            filtered_queries = [spec for spec in query_plan.rendered_queries if spec.source in source_hints]
            if filtered_queries:
                query_plan = query_plan.model_copy(update={"rendered_queries": filtered_queries})

        stage_groups = _group_query_specs(query_plan.rendered_queries)
        executed_specs: list[dict[str, Any]] = []
        records = []
        source_errors: list[dict[str, str]] = []
        for stage_name, specs in stage_groups:
            stage_records, stage_errors, stage_executed = await self._source_collector.collect_records_for_query_specs(
                query_specs=[spec.model_dump() for spec in specs],
                stage_name=stage_name,
                max_results_per_source=self._settings.max_results_per_source,
                from_year=discover_intent.start_year,
            )
            records.extend(stage_records)
            source_errors.extend(stage_errors)
            executed_specs.extend(stage_executed)

        ranking_input = {
            "intent": {
                "topic": discover_intent.topic,
                "goal": "discover raw paper source materials",
                "must_include": [*discover_intent.domain_terms, *discover_intent.must_include],
                "must_exclude": [*discover_intent.must_exclude, *discover_intent.negative_domains],
                "time_range": {
                    "start_year": discover_intent.start_year,
                    "end_year": discover_intent.end_year,
                },
            },
            "query_plan": query_plan.model_dump(),
        }
        context = self._ranking_engine.build_retrieval_context(ranking_input, executed_specs)
        papers, _, _ = self._ranking_engine.prepare_ranked_papers(
            records=records,
            from_year=discover_intent.start_year,
            end_year=discover_intent.end_year,
            context=context,
        )
        papers = await self._ranking_engine.rerank_with_model(papers, ranking_input)
        papers = self._ranking_engine.finalize_ranked_papers(papers)
        return records, papers, executed_specs, source_errors

    async def _review_discovery_attempt(
        self,
        *,
        query: str,
        project_context: str,
        discover_intent: DiscoverIntent,
        executed_specs: list[dict[str, Any]],
        papers: list[dict[str, Any]],
        source_errors: list[dict[str, str]],
        attempt: int,
    ) -> DiscoverReview:
        if self._chat_model is None:
            return DiscoverReview(
                decision="PASS",
                review_summary="Review skipped because no review model is configured.",
            )

        payload = {
            "query": query,
            "project_context": project_context,
            "attempt": attempt,
            "discover_intent": discover_intent.model_dump(),
            "executed_queries": executed_specs,
            "source_errors": source_errors,
            "candidate_papers": [
                {
                    "title": normalize_text(paper.get("title", "")),
                    "source": normalize_text(paper.get("source", "")),
                    "year": paper.get("year", ""),
                    "topical_relevance": normalize_text(paper.get("topical_relevance", "")),
                    "task_fit": normalize_text(paper.get("task_fit", "")),
                    "evidence_sufficiency": normalize_text(paper.get("evidence_sufficiency", "")),
                    "matched_queries": paper.get("_matched_queries", [])[:4],
                    "rank_reason": normalize_text(paper.get("rank_reason", "")),
                }
                for paper in papers[:12]
            ],
        }
        result = await invoke_structured_output(
            model=self._chat_model,
            schema=DiscoverReview,
            system_prompt=DISCOVER_REVIEW_SYSTEM_PROMPT,
            user_prompt=json.dumps(payload, ensure_ascii=False, indent=2),
        )
        return result

    async def _prepare_pdf_assets(
        self,
        *,
        papers_pdf_dir: Path,
        paper_fulltext_dir: Path,
        paper_page_images_dir: Path,
        slug: str,
        paper: dict[str, Any],
    ) -> dict[str, Any]:
        pdf_url = normalize_text(paper.get("_pdf_url", ""))
        if not pdf_url:
            return {
                "pdf_download_status": "unavailable",
                "pdf_downloaded": False,
                "local_pdf_path": "",
                "fulltext_extracted": False,
                "local_fulltext_path": "",
                "page_images_exported": False,
                "local_page_image_dir": "",
                "pdf_error": "",
            }

        pdf_path = papers_pdf_dir / f"{slug}.pdf"
        fulltext_path = paper_fulltext_dir / f"{slug}.md"
        try:
            pdf_bytes = await self._download_pdf(pdf_url)
        except Exception as exc:
            return {
                "pdf_download_status": "failed",
                "pdf_downloaded": False,
                "local_pdf_path": "",
                "fulltext_extracted": False,
                "local_fulltext_path": "",
                "page_images_exported": False,
                "local_page_image_dir": "",
                "pdf_error": f"PDF download failed: {exc}",
            }

        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        pdf_path.write_bytes(pdf_bytes)
        docling_result = await asyncio.to_thread(
            self._process_pdf_with_docling,
            pdf_path,
            fulltext_path,
            paper_page_images_dir / slug,
        )
        return {
            "pdf_download_status": "downloaded",
            "pdf_downloaded": True,
            "local_pdf_path": str(pdf_path),
            **docling_result,
        }

    async def _download_pdf(self, pdf_url: str) -> bytes:
        if self._client is None:
            raise RuntimeError("PDF download is unavailable because no HTTP client was initialized.")
        response = await self._client.get(pdf_url)
        response.raise_for_status()
        return response.content

    def _process_pdf_with_docling(
        self,
        pdf_path: Path,
        fulltext_path: Path,
        page_image_dir: Path,
    ) -> dict[str, Any]:
        try:
            from docling.datamodel.base_models import InputFormat
            from docling.datamodel.pipeline_options import PdfPipelineOptions
            from docling.document_converter import DocumentConverter, PdfFormatOption
        except ImportError:
            return {
                "fulltext_extracted": False,
                "local_fulltext_path": "",
                "page_images_exported": False,
                "local_page_image_dir": "",
                "pdf_error": "Docling processing skipped because docling is not installed.",
            }

        try:
            pipeline_options = PdfPipelineOptions()
            pipeline_options.generate_page_images = True
            converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(
                        pipeline_options=pipeline_options,
                    )
                }
            )
            conversion_result = converter.convert(str(pdf_path))
        except Exception as exc:
            return {
                "fulltext_extracted": False,
                "local_fulltext_path": "",
                "page_images_exported": False,
                "local_page_image_dir": "",
                "pdf_error": f"Docling failed while processing the PDF: {exc}",
            }

        try:
            markdown = conversion_result.document.export_to_markdown()
        except Exception as exc:
            markdown = ""
            markdown_error = f" Docling markdown export failed: {exc}"
        else:
            markdown_error = ""

        fulltext_extracted = False
        fulltext_path_value = ""
        if normalize_text(markdown):
            fulltext_path.parent.mkdir(parents=True, exist_ok=True)
            fulltext_path.write_text(markdown, encoding="utf-8")
            fulltext_extracted = True
            fulltext_path_value = str(fulltext_path)

        page_image_paths: list[str] = []
        page_image_error = ""
        try:
            pages = getattr(conversion_result.document, "pages", {}) or {}
            if pages:
                page_image_dir.mkdir(parents=True, exist_ok=True)
            for page_no, page in pages.items():
                image = getattr(page, "image", None)
                pil_image = getattr(image, "pil_image", None) if image is not None else None
                if pil_image is None:
                    continue
                image_path = page_image_dir / f"page-{int(page_no):03d}.png"
                pil_image.save(image_path)
                page_image_paths.append(str(image_path))
        except Exception as exc:
            page_image_error = f" Docling page image export failed: {exc}"

        error_message = ""
        if not fulltext_extracted:
            error_message = "Docling did not produce non-empty markdown."
        error_message = f"{error_message}{markdown_error}{page_image_error}".strip()

        return {
            "fulltext_extracted": fulltext_extracted,
            "local_fulltext_path": fulltext_path_value,
            "page_images_exported": bool(page_image_paths),
            "local_page_image_dir": str(page_image_dir) if page_image_paths else "",
            "pdf_error": error_message,
        }


def build_discover_query_plan(intent: DiscoverIntent) -> Any:
    normalized_intent = _normalize_discover_intent(intent)
    primary_queries = [
        query
        for query in normalized_intent.primary_queries
        if len(normalize_text(query).split()) <= 8
    ]
    payload = {
        "query_ir": {
            "topic_phrases": [normalized_intent.topic] if normalized_intent.topic else primary_queries[:1],
            "method_terms": [*normalized_intent.domain_terms[:3], *normalized_intent.must_include[:3]],
            "optional_terms": primary_queries[1:3],
            "excluded_terms": [*normalized_intent.must_exclude[:3], *normalized_intent.negative_domains[:3]],
            "alias_groups": [],
        },
        "primary_queries": primary_queries[:4],
    }
    query_plan = build_query_plan(payload)
    if not query_plan.primary_queries and primary_queries:
        query_plan = query_plan.model_copy(update={"primary_queries": primary_queries[:4]})
    return query_plan


def _normalize_discover_intent(intent: DiscoverIntent) -> DiscoverIntent:
    topic = normalize_text(intent.topic)
    primary_queries = normalize_string_list(intent.primary_queries)
    if topic and topic not in primary_queries:
        primary_queries.insert(0, topic)
    source_hints = _normalize_source_hints(intent.source_hints) or ["arXiv", "Crossref", "OpenAlex"]
    return DiscoverIntent(
        topic=topic or (primary_queries[0] if primary_queries else ""),
        must_include=normalize_string_list(intent.must_include),
        must_exclude=normalize_string_list(intent.must_exclude),
        domain_terms=normalize_string_list(intent.domain_terms),
        negative_domains=normalize_string_list(intent.negative_domains),
        source_hints=source_hints,
        primary_queries=primary_queries[:6],
        start_year=int(intent.start_year) if isinstance(intent.start_year, int) else None,
        end_year=int(intent.end_year) if isinstance(intent.end_year, int) else None,
    )


def _normalize_source_hints(values: list[str]) -> list[str]:
    mapping = {
        "arxiv": "arXiv",
        "crossref": "Crossref",
        "openalex": "OpenAlex",
    }
    normalized: list[str] = []
    for value in values:
        key = normalize_text(value, for_matching=True)
        if key in mapping:
            normalized.append(mapping[key])
    return list(dict.fromkeys(normalized))


def _group_query_specs(rendered_queries: list[Any]) -> list[tuple[str, list[Any]]]:
    grouped: OrderedDict[str, list[Any]] = OrderedDict()
    for spec in rendered_queries:
        grouped.setdefault(spec.stage, []).append(spec)
    return list(grouped.items())
