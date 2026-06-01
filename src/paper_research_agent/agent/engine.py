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

from ..core.config import Settings
from ..core.llm import build_chat_model, invoke_structured_output
from ..core.models import PaperDict, QueryDecomposition, ReviewResult, paper_key
from ..core.normalization import normalize_string_list, normalize_text
from ..feeder_store import ensure_project_paths
from ..materializer import build_raw_paper_slug, render_raw_paper_markdown, write_raw_paper
from ..retrieval import PaperSourceCollector, PaperRankingEngine, build_query_entries, build_reranker
from .pdf import PdfDownloader, PdfUrlResolver
from .params import HARD_CAP, LLM_RERANK_TOP_N, QUERY_DECOMPOSITION_SYSTEM_PROMPT, REVIEW_SYSTEM_PROMPT, SEED_COUNT


logger = logging.getLogger(__name__)

_YEAR_RANGE_RE = re.compile(r"\b\d{4}\s*[-–—]\s*\d{4}\b", re.IGNORECASE)


def _strip_year_text(text: str) -> str:
    cleaned = re.sub(_YEAR_RANGE_RE, "", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or text


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
        self._ce_reranker, self._llm_reranker = build_reranker(settings)

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()

    @property
    def _pdf_url_resolver(self) -> PdfUrlResolver:
        return PdfUrlResolver(self._settings, self._client)

    @property
    def _pdf_downloader(self) -> PdfDownloader:
        return PdfDownloader(self._settings, self._client)

    # ── public entry point ────────────────────────────────────────────────

    async def discover(
        self,
        *,
        project_slug: str,
        query: str,
        year_from: int | None = None,
        year_to: int | None = None,
    ) -> tuple[dict[str, Any], Path]:
        state: dict[str, Any] = {
            "query": query,
            "all_papers": {},
            "all_records": [],
            "all_errors": [],
            "executed_queries": [],
            "search_iteration": 0,
            "is_converged": False,
            "rerank_log": [],
            "review_log": [],
            "current_search_query": _strip_year_text(query),
        }

        decomposition = await self._decompose_query(query)

        resolved_year_from = year_from
        resolved_year_to = year_to

        paths = ensure_project_paths(self._output_root, project_slug)

        while True:
            state["search_iteration"] += 1
            logger.info("=== iteration %s (hard cap %s) ===", state["search_iteration"], HARD_CAP)
            logger.info("search query: %s", state["current_search_query"])

            new_papers = await self._search_node(state, decomposition, year_from=resolved_year_from, year_to=resolved_year_to)
            await self._pdf_url_resolver.resolve_pdf_urls(new_papers)
            if new_papers:
                await self._rerank_node(state, new_papers, query)

            graph_papers = await self._expand_node(state, n=SEED_COUNT, year_from=resolved_year_from, year_to=resolved_year_to)
            await self._pdf_url_resolver.resolve_pdf_urls(graph_papers)
            if graph_papers:
                await self._rerank_node(state, graph_papers, query)

            review = await self._review_node(state, query, decomposition.desired_paper_count)
            state["is_converged"] = review["converged"]
            logger.info(
                "review: converged=%s, reason=%s, total_papers=%s",
                review["converged"], review.get("reason", ""), len(state["all_papers"]),
            )

            if review["converged"]:
                logger.info("LLM signals convergence → stopping")
                break

            if state["search_iteration"] >= HARD_CAP:
                logger.info("reached hard cap %s → stopping", HARD_CAP)
                break

            refined = review.get("refined_query", "")
            if not refined or refined.strip() == state["current_search_query"].strip():
                logger.info("LLM has no meaningful refined query → stopping")
                break

            state["current_search_query"] = _strip_year_text(refined)
            logger.info("LLM suggests refined query: %s", refined)

        sorted_papers: list[PaperDict] = sorted(
            state["all_papers"].values(),
            key=lambda p: (-p.relevance_score, -p.year if p.year else 0),
        )
        desired = decomposition.desired_paper_count
        selected_papers = sorted_papers[:desired]
        generated_at = datetime.now().isoformat(timespec="seconds")

        logger.info(
            "pipeline done: %s candidates, %s selected, converged=%s after %s iterations",
            len(state["all_papers"]), len(selected_papers),
            state["is_converged"], state["search_iteration"],
        )

        await self._pdf_downloader.download(selected_papers, paths.papers_pdf_dir)

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
                "available": sum(1 for p in selected_papers if p.pdf_status == "available"),
                "downloaded": sum(1 for p in selected_papers if p.pdf_status == "downloaded"),
                "failed": sum(1 for p in selected_papers if p.pdf_status == "failed"),
                "pending": sum(1 for p in selected_papers if p.pdf_status == "pending"),
            },
            "written_files": [p.model_dump() for p in selected_papers],
            "source_errors": state["all_errors"],
            "all_papers": {k: v.model_dump() for k, v in state["all_papers"].items()},
        }

        batch_path = paths.batches_dir / f"{batch_data['batch_id']}.json"
        batch_path.parent.mkdir(parents=True, exist_ok=True)
        batch_path.write_text(json.dumps(batch_data, ensure_ascii=False, indent=2), encoding="utf-8")

        self._write_feed_log(paths, batch_data, selected_papers, generated_at)
        return batch_data, batch_path

    # ═══════════════════════════════════════════════════════════════════════
    # Node 1: search_papers
    # ═══════════════════════════════════════════════════════════════════════

    async def _search_node(self, state: dict, decomposition: QueryDecomposition, year_from: int | None = None, year_to: int | None = None) -> list[PaperDict]:
        search_query = state["current_search_query"]
        stage = f"iter_{state['search_iteration']}"

        entries = build_query_entries(
            topic_phrases=[search_query] + decomposition.core_techs[:2],
            expanded_terms=decomposition.expanded_terms,
            domain_terms=decomposition.application_domains + decomposition.key_metrics,
        )

        all_records: list[PaperDict] = []
        all_spec_errors: list[dict[str, str]] = []

        for entry in entries:
            records, errors = await self._source_collector.collect_all_source_records(
                query=entry["query"],
                stage_name=stage,
                max_results_per_source=self._settings.max_results_per_source,
                target_source=entry["source"],
                year_from=year_from,
                year_to=year_to,
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

        new_papers: list[PaperDict] = []
        for paper in candidates:
            paper.relevance_score = 0
            key = paper_key(paper)
            if key not in state["all_papers"]:
                state["all_papers"][key] = paper
                new_papers.append(paper)

        logger.info("search: %s new papers (total: %s)", len(new_papers), len(state["all_papers"]))
        return new_papers

    # ═══════════════════════════════════════════════════════════════════════
    # Node 2: rerank_papers (CE coarse filter → LLM multi-dim scoring)
    # ═══════════════════════════════════════════════════════════════════════

    async def _rerank_node(self, state: dict, papers: list[PaperDict], query: str) -> None:
        if not papers:
            return
        new_papers = [p for p in papers if p.ce_score == 0.0]
        if not new_papers:
            return
        await self._rerank_ce(new_papers, query, state)
        await self._rerank_llm(new_papers, query, state)

    async def _rerank_ce(self, papers: list[PaperDict], query: str, state: dict) -> None:
        judgments = await self._ce_reranker.rerank(query, papers)
        batch_log: list[dict[str, Any]] = []
        scores: list[int] = []
        for j in judgments:
            key = j.get("paper_key", "")
            raw = float(j.get("raw_score", 0))
            mapped = int(j.get("relevance", 0))
            scores.append(mapped)
            batch_log.append({"paper_key": key, "ce_score": raw, "ce_mapped": mapped})
            if key in state["all_papers"]:
                paper = state["all_papers"][key]
                paper.ce_score = raw
                paper.ce_mapped_score = mapped
                if paper.relevance_score == 0:
                    paper.relevance_score = mapped
        if scores:
            logger.info(
                "CE rerank: %s papers, dist: 1=%s 2=%s 3=%s 4=%s 5=%s",
                len(scores),
                scores.count(1), scores.count(2), scores.count(3),
                scores.count(4), scores.count(5),
            )

    async def _rerank_llm(self, papers: list[PaperDict], query: str, state: dict) -> None:
        candidates = [p for p in papers if p.ce_score > 0.5]
        if not candidates:
            return
        candidates.sort(key=lambda p: -p.ce_score)
        top_n = candidates[:LLM_RERANK_TOP_N]

        judgments = await self._llm_reranker.rerank(query, top_n)
        batch_log: list[dict[str, Any]] = []
        scores: list[int] = []
        for j in judgments:
            key = j.get("paper_key", "")
            overall = int(j.get("overall", 0))
            reason = normalize_text(j.get("reason", ""))
            scores.append(overall)
            batch_log.append({
                "paper_key": key, "llm_overall": overall, "reason": reason,
            })
            if key in state["all_papers"]:
                paper = state["all_papers"][key]
                paper.llm_overall = overall
                paper.llm_reason = reason
                paper.relevance_score = overall
        state["rerank_log"].append({
            "iteration": state["search_iteration"],
            "ce_scored": len(papers),
            "llm_scored": len(top_n),
            "judgments": batch_log,
        })
        if scores:
            logger.info(
                "LLM rerank: %s papers, dist: 1=%s 2=%s 3=%s 4=%s 5=%s",
                len(scores),
                scores.count(1), scores.count(2), scores.count(3),
                scores.count(4), scores.count(5),
            )

    # ═══════════════════════════════════════════════════════════════════════
    # Node 3: expand_citations
    # ═══════════════════════════════════════════════════════════════════════

    async def _expand_node(self, state: dict, *, n: int = 3, year_from: int | None = None, year_to: int | None = None) -> list[PaperDict]:
        expanded_ids = state.setdefault("_expanded_oa_ids", set())
        seeds = [
            p for p in state["all_papers"].values()
            if (p.ce_score > 0.5 or p.relevance_score >= 3)
            and p.openalex_id
            and p.openalex_id not in expanded_ids
        ]
        seeds.sort(key=lambda p: -p.relevance_score)
        seeds = seeds[:n]

        if not seeds:
            logger.info("expand: no new seeds with score >= 3 (already expanded: %s)", len(expanded_ids))
            return []

        logger.info("expand: using %s seeds: %s", len(seeds), [normalize_text(s.title[:60]) for s in seeds])
        graph_papers: list[PaperDict] = []
        for seed in seeds:
            oa_id = seed.openalex_id
            expanded_ids.add(oa_id)
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
                if year_from is not None or year_to is not None:
                    yr = raw.year if raw.year else 0
                    if yr > 0:
                        if year_from is not None and yr < year_from:
                            continue
                        if year_to is not None and yr > year_to:
                            continue
                candidates = self._ranking_engine.prepare_agent_candidates(
                    records=[raw], matched_query=f"graph of: {normalize_text(seed.title)}",
                )
                for paper in candidates:
                    key = paper_key(paper)
                    if key not in state["all_papers"]:
                        paper.graph_seed = normalize_text(seed.title)
                        state["all_papers"][key] = paper
                        graph_papers.append(paper)

        logger.info("expand: %s new graph papers", len(graph_papers))
        return graph_papers

    # ═══════════════════════════════════════════════════════════════════════
    # Node 4: meta_review (global statistics → convergence judgment)
    # ═══════════════════════════════════════════════════════════════════════

    async def _review_node(self, state: dict, query: str, desired_count: int) -> dict[str, Any]:
        papers = list(state["all_papers"].values())
        total = len(papers)
        if total < 3:
            return {"converged": False, "refined_query": state["current_search_query"]}

        llm_dist = self._score_dist(papers, "llm_overall")
        years: list[int] = []
        for p in papers:
            if p.year > 1900:
                years.append(p.year)

        year_span = f"{min(years)}-{max(years)}" if years else "unknown"

        def _paper_score(p: PaperDict) -> int:
            return p.llm_overall or p.ce_mapped_score

        top10 = sorted(papers, key=lambda p: -_paper_score(p))[:10]
        paper_titles = [p.title for p in top10]
        high_quality_count = sum(1 for p in papers if _paper_score(p) >= 4)

        stats = {
            "query": query,
            "iteration": state["search_iteration"],
            "total_papers": total,
            "desired_count": desired_count,
            "high_quality_count": high_quality_count,
            "llm_score_distribution": llm_dist,
            "year_span": year_span,
            "paper_titles": paper_titles,
        }

        past_refined = [
            rl.get("refined_query", "") for rl in state["review_log"]
            if rl.get("refined_query") and rl.get("refined_query") != state["current_search_query"]
        ]
        user_prompt_data = dict(stats)
        if past_refined:
            user_prompt_data["previously_tried_queries"] = past_refined
            user_prompt_data["_note"] = (
                "Your refined_query MUST differ from all of the previously_tried_queries above. "
                "If you cannot think of a genuinely new search direction, set converged=true with "
                "a reason explaining why coverage is sufficient."
            )

        result = await invoke_structured_output(
            model=self._llm,
            schema=ReviewResult,
            system_prompt=REVIEW_SYSTEM_PROMPT,
            user_prompt=json.dumps(user_prompt_data, ensure_ascii=False, indent=2),
        )

        state["review_log"].append({
            "iteration": state["search_iteration"],
            "total_papers": total,
            "converged": result.converged,
            "convergence_reason": normalize_text(result.convergence_reason),
            "refined_query": normalize_text(result.refined_query),
        })

        logger.info(
            "review: converged=%s, total=%s, high_quality=%s, llm_dist=%s",
            result.converged, total, high_quality_count, llm_dist,
        )

        return {
            "converged": result.converged,
            "refined_query": normalize_text(result.refined_query) or state["current_search_query"],
        }

    @staticmethod
    def _score_dist(papers: list[PaperDict], field: str) -> dict[str, int]:
        dist: dict[str, int] = {}
        for p in papers:
            score = getattr(p, field, 0)
            if isinstance(score, (int, float)) and score > 0:
                bucket = str(int(score))
                dist[bucket] = dist.get(bucket, 0) + 1
        return dist

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
        return result

    # ── materialization ───────────────────────────────────────────────────

    async def _materialize_papers(
        self, *, selected_papers: list[PaperDict], paths: Any,
        project_slug: str, user_query: str, generated_at: str,
    ) -> list[PaperDict]:
        for paper in selected_papers:
            paper.slug = build_raw_paper_slug(paper)
            paper.pdf_downloaded = paper.pdf_status == "downloaded"
            target_path = paths.paper_metadata_dir / f"{paper.slug}.md"
            content = render_raw_paper_markdown(
                paper, project_slug=project_slug, user_query=user_query,
                generated_at=generated_at,
                local_pdf_path=paper.local_path,
                pdf_download_status=paper.pdf_status,
                pdf_error="",
            )
            write_raw_paper(target_path, content)
            paper.path = str(target_path)
            paper.source_family = normalize_text(paper.source)
            paper.canonical_url = paper.url
        return selected_papers

    def _write_feed_log(self, paths: Any, batch_data: dict, written_files: list[PaperDict], generated_at: str) -> None:
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
