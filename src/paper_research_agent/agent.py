from __future__ import annotations

import asyncio
import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

import httpx

from .core.config import Settings
from .core.llm import build_chat_model, invoke_structured_output
from .core.models import PaperRecord, QueryDecomposition, RawPaperArtifact
from .core.normalization import normalize_string_list, normalize_text
from .feeder_store import ensure_project_paths
from .materializer import build_raw_paper_slug, render_raw_paper_markdown, write_raw_paper
from .retrieval.query_planning import build_query_entries
from .retrieval.ranking import PaperRankingEngine
from .retrieval.reranker import build_reranker
from .retrieval.sources import PaperSourceCollector

logger = logging.getLogger(__name__)

QUERY_DECOMPOSITION_SYSTEM_PROMPT = """You are a scholarly query decomposer. Your job is to convert a user's natural-language research question into structured search dimensions.

RULES:
1. core_techs: the core technologies, algorithms, or models mentioned (e.g. "diffusion model", "transformer", "CNN"). Limit to 5 entries.
2. application_domains: the application fields or domains (e.g. "medical imaging", "CAD", "NLP"). Limit to 5 entries.
3. key_metrics: evaluation metrics, tasks, or desired outcomes (e.g. "segmentation accuracy", "Dice score", "reconstruction quality"). Limit to 5 entries.
4. expanded_terms: academic synonyms, abbreviations, full names, and related concepts for each core_tech and domain. Include both formal names and common abbreviations. (e.g. for "diffusion model": "DDPM", "score-based model", "denoising diffusion", "latent diffusion"; for "boundary representation": "B-Rep", "BRep", "BREP"). Limit to 10 entries.
5. excluded_terms: ONLY include terms from truly irrelevant application domains or fields. Do NOT exclude technical methods (e.g. "mesh", "voxel", "point cloud") that papers might mention as comparison baselines. Limit to 3 entries.

Return ONLY the structured JSON and nothing else.
"""

REVIEW_SYSTEM_PROMPT = """You are a research supervisor conducting a second-stage review of papers that have already passed a coarse relevance filter.

For each paper, assign multi-dimensional scores:
- relevance (1-5): how directly the paper addresses the user's research query
- novelty (1-5): how novel or innovative the approach is compared to established methods
- rigor (1-5): experimental and data support completeness inferred from the abstract. Look for signals such as:
  * benchmark evaluation on recognized datasets (e.g. ImageNet, COCO, SQuAD, GLUE, etc.)
  * comparison against established baselines or SOTA methods
  * ablation study mentioned
  * reported quantitative metrics with clear improvement margins
  * statistical significance or error bars mentioned
  Score 5 = multiple strong signals present; 3 = some evidence but incomplete; 1 = no empirical support hinted in abstract
- overall (1-5): your holistic recommendation score
- reason: one sentence summarizing your assessment

Also assess whether the current search has converged:
- converged = true: multiple papers score 4+ across dimensions, diverse sources/years covered, further searching unlikely to yield substantially better results
- converged = false: key aspects uncovered, too few high-quality papers (< 5), or top papers are marginal (overall < 3)

If not converged, provide a refined search query (3-8 words) targeting uncovered areas.

Return exactly one JSON object with keys "papers" (array of judgments), "converged" (bool), "convergence_reason" (string), "refined_query" (string).
Do not use markdown code fences.
"""

MAX_ITERATIONS = 3
SEED_COUNT = 3
REVIEW_TOP_K = 15


class PaperDiscoveryAgent:
    def __init__(
        self,
        settings: Settings,
        *,
        output_root: str = "projects",
        source_collector: PaperSourceCollector | None = None,
        ranking_engine: PaperRankingEngine | None = None,
    ) -> None:
        self._settings = settings
        self._output_root = Path(output_root)
        self._client: httpx.AsyncClient | None = None

        if source_collector is None:
            self._client = httpx.AsyncClient(
                timeout=settings.request_timeout,
                proxy=settings.http_proxy or None,
                headers={
                    "User-Agent": "paper-discovery-agent/0.1 (academic paper discovery)",
                    "Accept": "*/*",
                },
                follow_redirects=True,
            )
            self._source_collector = PaperSourceCollector(settings, self._client)
        else:
            self._source_collector = source_collector

        self._ranking_engine = ranking_engine or PaperRankingEngine()
        self._llm = build_chat_model(settings, temperature=0.1)
        self._reranker = build_reranker(settings)

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()

    # ── public entry point ────────────────────────────────────────────────

    async def discover(
        self,
        *,
        project_slug: str,
        query: str,
        top_k: int = 5,
    ) -> tuple[dict[str, Any], Path]:
        state: dict[str, Any] = {
            "query": query,
            "all_papers": {},          # key → paper dict
            "all_records": [],
            "all_errors": [],
            "executed_queries": [],
            "search_iteration": 0,
            "is_converged": False,
            "rerank_log": [],
            "review_log": [],
            "current_search_query": query,
        }

        decomposition = await self._decompose_query(query)
        paths = ensure_project_paths(self._output_root, project_slug, reset_existing=True)

        while not self._should_stop(state):
            state["search_iteration"] += 1
            logger.info("=== iteration %s/%s ===", state["search_iteration"], MAX_ITERATIONS)
            logger.info("search query: %s", state["current_search_query"])

            new_papers = await self._search_node(state, decomposition)
            await self._resolve_pdf_urls(new_papers)
            if new_papers:
                await self._rerank_node(state, new_papers, query)

            graph_papers = await self._expand_node(state, n=SEED_COUNT)
            await self._resolve_pdf_urls(graph_papers)
            if graph_papers:
                await self._rerank_node(state, graph_papers, query)

            review = await self._review_node(state, query, decomposition)
            state["is_converged"] = review["converged"]
            logger.info(
                "review: converged=%s, reason=%s, total_papers=%s",
                review["converged"], review.get("reason", ""), len(state["all_papers"]),
            )
            if not state["is_converged"] and state["search_iteration"] < MAX_ITERATIONS:
                state["current_search_query"] = review["refined_query"]
                logger.info("rewritten query: %s", state["current_search_query"])

        sorted_papers = sorted(
            state["all_papers"].values(),
            key=lambda p: (-p.get("relevance_score", 0), -(p.get("year") if isinstance(p.get("year"), int) else 0)),
        )
        selected_papers = sorted_papers[: max(1, min(top_k, 20))]
        generated_at = datetime.now().isoformat(timespec="seconds")

        logger.info(
            "pipeline done: %s candidates, %s selected, converged=%s after %s iterations",
            len(state["all_papers"]), len(selected_papers),
            state["is_converged"], state["search_iteration"],
        )

        await self._download_selected_pdfs(selected_papers, paths, top_k)

        written_files = await self._materialize_papers(
            selected_papers=selected_papers, paths=paths,
            project_slug=project_slug, user_query=query, generated_at=generated_at,
        )

        batch_data = {
            "batch_id": f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid4().hex[:8]}",
            "project_slug": project_slug,
            "query": query,
            "generated_at": generated_at,
            "query_decomposition": decomposition.model_dump(),
            "iterations": state["search_iteration"],
            "converged": state["is_converged"],
            "rerank_log": state["rerank_log"],
            "review_log": state["review_log"],
            "executed_queries": state["executed_queries"],
            "candidate_count": len(state["all_papers"]),
            "selected_count": len(selected_papers),
            "pdf_stats": {
                "available": sum(1 for p in selected_papers if p.get("pdf_status") == "available"),
                "downloaded": sum(1 for p in selected_papers if p.get("pdf_status") == "downloaded"),
                "failed": sum(1 for p in selected_papers if p.get("pdf_status") == "failed"),
                "pending": sum(1 for p in selected_papers if p.get("pdf_status") == "pending"),
            },
            "written_files": [item.model_dump() for item in written_files],
            "source_errors": state["all_errors"],
        }

        batch_path = paths.batches_dir / f"{batch_data['batch_id']}.json"
        batch_path.parent.mkdir(parents=True, exist_ok=True)
        batch_path.write_text(json.dumps(batch_data, ensure_ascii=False, indent=2), encoding="utf-8")

        self._write_feed_log(paths, batch_data, written_files, generated_at)
        return batch_data, batch_path

    # ── pipeline control ──────────────────────────────────────────────────

    def _should_stop(self, state: dict) -> bool:
        return state["is_converged"] or state["search_iteration"] >= MAX_ITERATIONS

    # ── PDF resolution and download ────────────────────────────────────────

    async def _resolve_pdf_urls(self, papers: list[dict[str, Any]]) -> None:
        resolved = 0
        for paper in papers:
            if paper.get("pdf_status") == "available":
                continue
            urls = _extract_direct_pdf_urls(paper)
            doi = normalize_text(paper.get("doi", ""))
            if doi and doi.startswith("10.") and self._settings.unpaywall_email:
                upw_url = await self._resolve_unpaywall(doi)
                if upw_url:
                    urls.append(upw_url)
            if urls:
                paper["pdf_urls"] = urls
                paper["pdf_url"] = urls[0]
                paper["pdf_status"] = "available"
                resolved += 1
        if resolved:
            logger.info("pdf resolve: %s/%s papers got PDF URLs", resolved, len(papers))

    async def _resolve_unpaywall(self, doi: str) -> str:
        email = self._settings.unpaywall_email
        if not email:
            return ""
        try:
            response = await self._client.get(
                f"https://api.unpaywall.org/v2/{doi}",
                params={"email": email},
            )
            response.raise_for_status()
            data = response.json()
            if not data.get("is_oa"):
                return ""
            best = data.get("best_oa_location") or {}
            pdf_url = (best.get("url_for_pdf") or best.get("url") or "").strip()
            if not pdf_url:
                return ""

            from urllib.parse import urlparse

            path = urlparse(pdf_url).path.lower()
            return pdf_url if path.endswith(".pdf") else ""
        except Exception:
            return ""

    async def _download_selected_pdfs(
        self, papers: list[dict[str, Any]], paths: Any, limit: int,
    ) -> None:
        downloaded_count = 0
        failed_count = 0
        for paper in papers[:limit]:
            if paper.get("pdf_status") != "available":
                continue
            slug = build_raw_paper_slug(paper)
            pdf_path = paths.papers_pdf_dir / f"{slug}.pdf"
            urls = paper.get("pdf_urls", [paper.get("pdf_url", "")])
            downloaded = False
            last_error = ""
            for pdf_url in urls:
                if not pdf_url:
                    continue
                try:
                    pdf_bytes = await self._download_pdf(pdf_url)
                    pdf_path.parent.mkdir(parents=True, exist_ok=True)
                    pdf_path.write_bytes(pdf_bytes)
                    paper["pdf_status"] = "downloaded"
                    paper["local_path"] = str(pdf_path)
                    paper["pdf_url"] = pdf_url
                    downloaded = True
                    logger.info("pdf ok: %s -> %s", normalize_text(paper.get("title", "")[:60]), slug)
                    downloaded_count += 1
                    break
                except Exception as exc:
                    last_error = str(exc)
            if not downloaded:
                paper["pdf_status"] = "failed"
                paper["local_path"] = ""
                logger.info("pdf fail: %s (%s)", normalize_text(paper.get("title", "")[:60]), last_error[:80])
                failed_count += 1
        logger.info("pdf download: %s ok, %s failed", downloaded_count, failed_count)

    # ═══════════════════════════════════════════════════════════════════════
    # Node 1: search_papers
    # ═══════════════════════════════════════════════════════════════════════

    async def _search_node(self, state: dict, decomposition: QueryDecomposition) -> list[dict[str, Any]]:
        search_query = state["current_search_query"]
        stage = f"iter_{state['search_iteration']}"

        entries = build_query_entries(
            topic_phrases=[search_query] + decomposition.core_techs[:2],
            expanded_terms=decomposition.expanded_terms,
            domain_terms=decomposition.application_domains + decomposition.key_metrics,
            excluded_terms=decomposition.excluded_terms,
        )

        all_records: list[PaperRecord] = []
        all_spec_errors: list[dict[str, str]] = []

        for entry in entries:
            records, errors = await self._source_collector.collect_all_source_records(
                query=entry["query"],
                stage_name=stage,
                max_results_per_source=self._settings.max_results_per_source,
                target_source=entry["source"],
            )
            all_records.extend(records)
            all_spec_errors.extend(errors)
            state["executed_queries"].append({
                "query": entry["query"], "sources": [entry["source"]],
                "stage": stage, "purpose": entry["purpose"], "notes": entry["notes"],
            })

        state["all_records"].extend(all_records)
        state["all_errors"].extend(all_spec_errors)

        logger.info("search: %s records from %s entries, %s errors", len(all_records), len(entries), len(all_spec_errors))
        for err in all_spec_errors:
            logger.warning("source error [%s]: %s", err.get("source", "?"), err.get("error", "")[:100])

        candidates = self._ranking_engine.prepare_agent_candidates(
            records=all_records, matched_query=search_query,
        )

        new_papers: list[dict[str, Any]] = []
        for paper in candidates:
            paper["relevance_score"] = 0
            key = _paper_key(paper)
            if key not in state["all_papers"]:
                state["all_papers"][key] = paper
                new_papers.append(paper)

        logger.info("search: %s new papers (total: %s)", len(new_papers), len(state["all_papers"]))
        return new_papers

    # ═══════════════════════════════════════════════════════════════════════
    # Node 2: rerank_papers
    # ═══════════════════════════════════════════════════════════════════════

    async def _rerank_node(self, state: dict, papers: list[dict[str, Any]], query: str) -> None:
        if not papers:
            return
        to_score = [p for p in papers if p.get("relevance_score", 0) == 0]
        if not to_score:
            return
        judgments = await self._reranker.rerank(query, to_score)
        batch_log: list[dict[str, Any]] = []
        scores = []
        for j in judgments:
            key = j.get("paper_key", "")
            score = int(j.get("relevance", 0))
            reason = normalize_text(j.get("reason", ""))
            scores.append(score)
            batch_log.append({"paper_key": key, "relevance": score, "reason": reason})
            if key in state["all_papers"]:
                state["all_papers"][key]["relevance_score"] = score
                state["all_papers"][key]["rank_reason"] = reason
        state["rerank_log"].append({
            "iteration": state["search_iteration"],
            "scored_count": len(to_score),
            "judgments": batch_log,
        })
        if scores:
            logger.info(
                "rerank: scored %s papers, distribution: 1=%s 2=%s 3=%s 4=%s 5=%s",
                len(scores),
                scores.count(1), scores.count(2), scores.count(3),
                scores.count(4), scores.count(5),
            )

    # ═══════════════════════════════════════════════════════════════════════
    # Node 3: expand_citations
    # ═══════════════════════════════════════════════════════════════════════

    async def _expand_node(self, state: dict, *, n: int = 3) -> list[dict[str, Any]]:
        seeds = [
            p for p in state["all_papers"].values()
            if p.get("relevance_score", 0) >= 3 and p.get("_openalex_id")
        ]
        seeds.sort(key=lambda p: -p.get("relevance_score", 0))
        seeds = seeds[:n]

        if not seeds:
            logger.info("expand: no seeds with score >= 3")
            return []

        logger.info("expand: using %s seeds: %s", len(seeds), [normalize_text(s.get("title", "")[:60]) for s in seeds])
        graph_papers: list[dict[str, Any]] = []
        for seed in seeds:
            oa_id = seed.get("_openalex_id", "")
            try:
                refs = await self._source_collector.fetch_references(oa_id, top_k=20)
                cites = await self._source_collector.fetch_citations(oa_id, top_k=20)
            except Exception as exc:
                logger.warning("expand: graph fetch failed for %s: %s", oa_id, exc)
                state["all_errors"].append({
                    "source": "openalex_graph",
                    "openalex_id": oa_id,
                    "error": str(exc),
                })
                continue

            for raw in [*refs, *cites]:
                candidates = self._ranking_engine.prepare_agent_candidates(
                    records=[raw], matched_query=f"graph of: {normalize_text(seed.get('title', ''))}",
                )
                for paper in candidates:
                    key = _paper_key(paper)
                    if key not in state["all_papers"]:
                        paper["relevance_score"] = 0
                        paper["_graph_seed"] = normalize_text(seed.get("title", ""))
                        state["all_papers"][key] = paper
                        graph_papers.append(paper)

        logger.info("expand: %s new graph papers", len(graph_papers))
        return graph_papers

    # ═══════════════════════════════════════════════════════════════════════
    # Node 4: llm_review (multi-dim second-stage review + convergence + rewrite)
    # ═══════════════════════════════════════════════════════════════════════

    async def _review_node(self, state: dict, query: str, decomposition: QueryDecomposition) -> dict[str, Any]:
        top = sorted(
            state["all_papers"].values(),
            key=lambda p: -p.get("relevance_score", 0),
        )[:REVIEW_TOP_K]

        if len(top) < 3:
            return {"converged": False, "refined_query": state["current_search_query"]}

        top_data = []
        for p in top:
            key = _paper_key(p)
            title = normalize_text(p.get("title", ""))
            score = p.get("relevance_score", 0)
            year = p.get("year", "")
            source = normalize_text(p.get("source", ""))
            snippets = p.get("evidence_snippets", [])
            abstract = normalize_text(snippets[0])[:400] if snippets else ""
            top_data.append({
                "paper_key": key, "title": title, "cross_encoder_score": score,
                "year": year, "source": source, "abstract": abstract,
            })

        result = await invoke_structured_output(
            model=self._llm,
            schema=_ReviewResult,
            system_prompt=REVIEW_SYSTEM_PROMPT,
            user_prompt=json.dumps({
                "query": query, "iteration": state["search_iteration"],
                "total_papers": len(state["all_papers"]),
                "domains_covered": decomposition.application_domains[:5],
                "papers": top_data,
            }, ensure_ascii=False, indent=2),
        )

        review_entries: list[dict[str, Any]] = []
        for j in result.papers:
            key = j.paper_key
            review_entries.append({
                "paper_key": key, "relevance": j.relevance,
                "novelty": j.novelty, "rigor": j.rigor, "overall": j.overall,
                "reason": normalize_text(j.reason),
            })
            if key in state["all_papers"]:
                state["all_papers"][key]["review_relevance"] = j.relevance
                state["all_papers"][key]["review_novelty"] = j.novelty
                state["all_papers"][key]["review_rigor"] = j.rigor
                state["all_papers"][key]["review_overall"] = j.overall
                state["all_papers"][key]["review_reason"] = normalize_text(j.reason)
                state["all_papers"][key]["relevance_score"] = j.overall

        state["review_log"].append({
            "iteration": state["search_iteration"],
            "reviewed_count": len(top),
            "converged": result.converged,
            "convergence_reason": normalize_text(result.convergence_reason),
            "papers": review_entries,
        })

        avg_scores = ""
        if review_entries:
            avg_rel = sum(e["relevance"] for e in review_entries) / len(review_entries)
            avg_nov = sum(e["novelty"] for e in review_entries) / len(review_entries)
            avg_rig = sum(e["rigor"] for e in review_entries) / len(review_entries)
            avg_ovr = sum(e["overall"] for e in review_entries) / len(review_entries)
            avg_scores = f", avg: rel={avg_rel:.1f} nov={avg_nov:.1f} rig={avg_rig:.1f} ovr={avg_ovr:.1f}"
        logger.info("review: %s papers reviewed%s", len(review_entries), avg_scores)

        return {
            "converged": result.converged,
            "refined_query": normalize_text(result.refined_query) or state["current_search_query"],
        }

    # ── query decomposition ───────────────────────────────────────────────

    async def _decompose_query(self, query: str) -> QueryDecomposition:
        result = await invoke_structured_output(
            model=self._llm,
            schema=QueryDecomposition,
            system_prompt=QUERY_DECOMPOSITION_SYSTEM_PROMPT,
            user_prompt=json.dumps({"query": query}, ensure_ascii=False, indent=2),
        )
        result.core_techs = normalize_string_list(result.core_techs)
        result.application_domains = normalize_string_list(result.application_domains)
        result.key_metrics = normalize_string_list(result.key_metrics)
        result.expanded_terms = normalize_string_list(result.expanded_terms)
        result.excluded_terms = normalize_string_list(result.excluded_terms)
        return result

    # ── materialization ───────────────────────────────────────────────────

    async def _materialize_papers(
        self, *, selected_papers: list[dict[str, Any]], paths: Any,
        project_slug: str, user_query: str, generated_at: str,
    ) -> list[RawPaperArtifact]:
        written_files: list[RawPaperArtifact] = []
        for paper in selected_papers:
            slug = build_raw_paper_slug(paper)
            pdf_assets = {
                "pdf_download_status": paper.get("pdf_status", "pending"),
                "pdf_downloaded": paper.get("pdf_status") == "downloaded",
                "local_pdf_path": paper.get("local_path", ""),
                "fulltext_extracted": False,
                "local_fulltext_path": "",
                "page_images_exported": False,
                "local_page_image_dir": "",
                "pdf_error": "",
            }
            target_path = paths.paper_metadata_dir / f"{slug}.md"
            content = render_raw_paper_markdown(
                paper, project_slug=project_slug, user_query=user_query,
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
                    slug=slug, title=normalize_text(paper.get("title", "")),
                    path=str(target_path),
                    source_family=normalize_text(paper.get("source", "")),
                    canonical_url=normalize_text(paper.get("url", "")),
                    doi=normalize_text(paper.get("doi", "")),
                    pdf_url=normalize_text(paper.get("pdf_url", "")),
                    pdf_downloaded=pdf_assets["pdf_downloaded"],
                    local_pdf_path=pdf_assets["local_pdf_path"],
                    fulltext_extracted=pdf_assets["fulltext_extracted"],
                    local_fulltext_path=pdf_assets["local_fulltext_path"],
                    page_images_exported=pdf_assets["page_images_exported"],
                    local_page_image_dir=pdf_assets["local_page_image_dir"],
                    pdf_error=pdf_assets["pdf_error"],
                )
            )
        return written_files

    # ── PDF helpers ───────────────────────────────────────────────────────

    async def _download_pdf(self, pdf_url: str) -> bytes:
        if self._client is None:
            raise RuntimeError("HTTP client not initialized.")
        if "content.openalex.org" in pdf_url and self._settings.openalex_api_key:
            sep = "&" if "?" in pdf_url else "?"
            pdf_url = f"{pdf_url}{sep}api_key={self._settings.openalex_api_key}"
        response = await self._client.get(pdf_url)
        response.raise_for_status()
        return response.content

    async def _process_with_docling(self, pdf_path: Path, fulltext_path: Path, page_image_dir: Path) -> dict[str, Any]:
        try:
            from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
            from docling.datamodel.base_models import InputFormat
            from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions
            from docling.document_converter import DocumentConverter, PdfFormatOption
        except ImportError:
            return {"fulltext_extracted": False, "local_fulltext_path": "", "page_images_exported": False,
                    "local_page_image_dir": "", "pdf_error": "Docling is not installed."}
        def _convert():
            device = self._resolve_docling_accelerator()
            opts = PdfPipelineOptions()
            opts.accelerator_options = AcceleratorOptions(device=device)
            opts.generate_page_images = True
            opts.ocr_options = RapidOcrOptions(backend=self._settings.docling_ocr_backend)
            converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})
            return converter.convert(str(pdf_path))
        try:
            cr = await asyncio.to_thread(_convert)
        except Exception as exc:
            return {"fulltext_extracted": False, "local_fulltext_path": "", "page_images_exported": False,
                    "local_page_image_dir": "", "pdf_error": f"Docling failed: {exc}"}
        try:
            markdown = cr.document.export_to_markdown()
        except Exception as exc:
            markdown = ""
            md_error = f" markdown export failed: {exc}"
        else:
            md_error = ""
        fe = False; fpv = ""
        if normalize_text(markdown):
            fulltext_path.parent.mkdir(parents=True, exist_ok=True)
            fulltext_path.write_text(markdown, encoding="utf-8")
            fe = True; fpv = str(fulltext_path)
        page_image_paths: list[str] = []; pi_error = ""
        try:
            pages = getattr(cr.document, "pages", {}) or {}
            if pages: page_image_dir.mkdir(parents=True, exist_ok=True)
            for pn, page in pages.items():
                img = getattr(page, "image", None)
                pil = getattr(img, "pil_image", None) if img is not None else None
                if pil is None: continue
                ipath = page_image_dir / f"page-{int(pn):03d}.png"
                pil.save(ipath); page_image_paths.append(str(ipath))
        except Exception as exc:
            pi_error = f" page image export failed: {exc}"
        err = ""
        if not fe: err = "Docling did not produce non-empty markdown."
        err = f"{err}{md_error}{pi_error}".strip()
        return {"fulltext_extracted": fe, "local_fulltext_path": fpv,
                "page_images_exported": bool(page_image_paths), "local_page_image_dir": str(page_image_dir) if page_image_paths else "",
                "pdf_error": err}

    def _resolve_docling_accelerator(self):
        from docling.datamodel.accelerator_options import AcceleratorDevice
        c = normalize_text(self._settings.docling_accelerator, for_matching=True)
        m = {"auto": AcceleratorDevice.AUTO, "cpu": AcceleratorDevice.CPU,
             "cuda": AcceleratorDevice.CUDA, "mps": AcceleratorDevice.MPS}
        return m.get(c, AcceleratorDevice.AUTO)

    def _write_feed_log(self, paths: Any, batch_data: dict, written_files: list[RawPaperArtifact], generated_at: str) -> None:
        lines = [
            f"## [{generated_at[:10]}] discover | {batch_data['query']}", "",
            f"- Batch: `{batch_data['batch_id']}`",
            f"- Project: `{batch_data['project_slug']}`",
            f"- Iterations: {batch_data.get('iterations', 1)}",
            f"- Converged: {batch_data.get('converged', False)}",
            f"- Candidates: {batch_data.get('candidate_count', 0)}",
            f"- Selected: {len(written_files)}",
            f"- Batch file: `{batch_data['batch_id']}.json`",
        ]
        if written_files:
            lines.append("- Raw files:")
            for item in written_files:
                lines.append(f"  - `{item.path}`")
        errors = batch_data.get("source_errors", [])
        if errors:
            lines.append("- Source errors:")
            for item in errors[:5]:
                lines.append(f"  - `{item.get('source', 'unknown')}`: {item.get('error', '')}")
        lines.extend(["", ""])
        existing = paths.log_path.read_text(encoding="utf-8") if paths.log_path.exists() else ""
        paths.log_path.write_text("\n".join(lines) + existing, encoding="utf-8")


# ── Pydantic schemas for structured LLM output ────────────────────────────

from pydantic import BaseModel, Field

class _ReviewJudgment(BaseModel):
    paper_key: str
    relevance: int = 0
    novelty: int = 0
    rigor: int = 0
    overall: int = 0
    reason: str = ""

class _ReviewResult(BaseModel):
    papers: list[_ReviewJudgment] = Field(default_factory=list)
    converged: bool = False
    convergence_reason: str = ""
    refined_query: str = ""


# ── helpers ────────────────────────────────────────────────────────────────

def _paper_key(paper: dict[str, Any]) -> str:
    oa_id = normalize_text(paper.get("_openalex_id", ""), for_matching=True)
    if oa_id:
        return f"oa:{oa_id}"
    doi = normalize_text(paper.get("doi", ""), for_matching=True)
    if doi:
        return f"doi:{doi}"
    title = normalize_text(paper.get("title", ""), for_matching=True)
    return f"title:{title}" if title else f"unknown_{id(paper)}"


def _extract_direct_pdf_urls(paper: dict[str, Any]) -> list[str]:
    source = normalize_text(paper.get("source", ""), for_matching=True)
    oa_id = paper.get("_openalex_id", "")
    url = normalize_text(paper.get("url", ""))
    urls: list[str] = []

    if "openalex" in source and oa_id:
        urls.append(f"https://content.openalex.org/works/{oa_id}.pdf")

    if "arxiv" in source or "arxiv.org" in url:
        match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url, re.IGNORECASE)
        if match:
            arxiv_id = match.group(1).removesuffix(".pdf")
            urls.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")

    doi = normalize_text(paper.get("doi", ""))
    if doi.startswith("10.1145/"):
        urls.append(f"https://dl.acm.org/doi/pdf/{doi}")

    return urls


def _format_search_results(search_query: str, papers: list[dict[str, Any]]) -> str:
    lines = [f"Search '{search_query}' returned {len(papers)} papers:"]
    for i, paper in enumerate(papers[:15], 1):
        title = normalize_text(paper.get("title", ""))
        source = normalize_text(paper.get("source", ""))
        year = paper.get("year", "")
        snippets = paper.get("evidence_snippets", [])
        abstract = normalize_text(snippets[0])[:300] if snippets else ""
        lines.append(f"{i}. \"{title}\" ({source}, {year})")
        if abstract:
            lines.append(f"   {abstract}")
    if len(papers) > 15:
        lines.append(f"   ... and {len(papers) - 15} more papers.")
    return "\n".join(lines)
