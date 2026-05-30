from __future__ import annotations

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from pathlib import Path

from ..core.config import Settings
from ..core.llm import build_chat_model
from ..core.models import PaperDict
from ..core.normalization import normalize_text

logger = logging.getLogger(__name__)


def build_synthesis_context(
    project_root: Path,
    slug: str,
) -> dict[str, Any]:
    from ..feeder_store import (
        get_project_decomposition,
        get_project_query,
        get_project_review_stats,
        parse_metadata_papers,
    )

    papers = parse_metadata_papers(project_root, slug)
    query = get_project_query(project_root, slug)
    decomposition = get_project_decomposition(project_root, slug)
    review_stats = get_project_review_stats(project_root, slug)

    return {
        "papers": papers,
        "query": query,
        "decomposition": decomposition,
        "review_stats": review_stats,
    }

SYNTHESIS_SYSTEM_PROMPT = """You are a senior academic research survey expert, skilled at writing comprehensive literature review reports.

## Core Responsibility

Generate a high-quality literature survey report based on the provided paper data.

## Report Format Requirements

**Important:** Carefully read the user's "Research Instructions". If the instructions specify a particular output format (e.g., taxonomy tree, sub-domain breakdown, per-paper detailed analysis, specific category buckets, summary tables, etc.), follow that format precisely. If no special format is specified, use the following default structure:

Default structure:
- **Executive Summary**: 2-3 sentence core conclusion
- **Research Background & Overview**: domain background, mainstream directions, and trends
- **Method Comparison**: cross-method comparison of different approaches (may be omitted if fewer than 3 papers)
- **Key Findings & Metrics**: key experimental results and performance metrics
- **Research Gaps & Future Directions**: uncovered gaps and feasible future directions
- **References**: `[N] Title —— Authors (Year), Source`

## Language Requirements

Write the main body in Chinese. For technical terms, model names, and algorithm names, annotate with the English original on first occurrence, e.g., "阻抗控制（impedance control）".

## Content Requirements

- Base analysis on specific information from paper abstracts; avoid vague generalizations
- Cite specific contributions of specific papers; use reference numbers when cross-referencing
- Distinguish the innovation level of different papers
- If the provided paper information is insufficient to support a given requirement, state this honestly and make the best inference based on available data
- Use Markdown tables, lists, and other syntax to enhance readability

## Output

Output a complete Markdown survey report directly. Do not wrap in JSON or code fences. Start from the title.
"""

SYNTHESIS_USER_PROMPT_TEMPLATE = """## Research Instructions

{user_instruction}

## Query Decomposition Dimensions
{decomposition}

## Paper Data Statistics
- Total candidate papers: {candidate_count}
- Selected papers: {selected_count}
- Average relevance score: {avg_relevance}
- Average novelty score: {avg_novelty}
- Average rigor score: {avg_rigor}
- Paper time span: {year_range}

## Paper List

{papers_detail}

Please generate the survey report strictly following the "Research Instructions" above. Prioritize the format and categorization specified in the instructions. If the paper data is insufficient to fully meet the instruction requirements, make your best effort based on available data and honestly note the data limitations.
"""


class SynthesisEngine:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._llm = build_chat_model(settings, temperature=0.3)
        self._llm.max_tokens = max(settings.max_output_tokens, 16384)

    async def synthesize(
        self,
        *,
        papers: list[PaperDict],
        query: str,
        project_slug: str,
        decomposition: dict | None = None,
        review_stats: dict | None = None,
    ) -> str:
        papers_detail = self._build_papers_detail(papers)
        stats = self._compute_stats(papers, review_stats or {})

        if decomposition:
            decomp_lines = []
            if decomposition.get("core_techs"):
                decomp_lines.append(f"- Core techs: {', '.join(decomposition['core_techs'])}")
            if decomposition.get("application_domains"):
                decomp_lines.append(f"- Application domains: {', '.join(decomposition['application_domains'])}")
            if decomposition.get("key_metrics"):
                decomp_lines.append(f"- Key metrics: {', '.join(decomposition['key_metrics'])}")
            decomp_text = "\n".join(decomp_lines) if decomp_lines else "N/A"
        else:
            decomp_text = "N/A"

        user_prompt = SYNTHESIS_USER_PROMPT_TEMPLATE.format(
            user_instruction=query if query else "Please write a comprehensive survey report based on the following paper data.",
            decomposition=decomp_text,
            candidate_count=stats["candidate_count"],
            selected_count=len(papers),
            avg_relevance=f"{stats['avg_relevance']:.1f}",
            avg_novelty=f"{stats['avg_novelty']:.1f}",
            avg_rigor=f"{stats['avg_rigor']:.1f}",
            year_range=stats["year_range"],
            papers_detail=papers_detail,
        )

        messages = [
            SystemMessage(content=SYNTHESIS_SYSTEM_PROMPT),
            HumanMessage(content=user_prompt),
        ]

        logger.info("synthesis: generating report for %s papers", len(papers))
        response = await self._llm.ainvoke(messages)
        content = response.content if hasattr(response, "content") else str(response)
        logger.info("synthesis: report generated (%s chars)", len(content))
        return content.strip()

    def _build_papers_detail(self, papers: list[PaperDict]) -> str:
        lines: list[str] = []
        for i, paper in enumerate(papers, 1):
            title = normalize_text(paper.title) or "Untitled"
            authors = paper.authors
            if isinstance(authors, list):
                authors_str = ", ".join(normalize_text(a) for a in authors[:5] if normalize_text(a))
                if len(authors) > 5:
                    authors_str += " et al."
            else:
                authors_str = str(authors) if authors else "Unknown"
            year = paper.year or "Unknown"
            source = normalize_text(paper.source) or "Unknown"
            doi = normalize_text(paper.doi)
            url = normalize_text(paper.url)

            evidence = paper.evidence_snippets
            if isinstance(evidence, list) and evidence:
                abstract = normalize_text(evidence[0])[:800]
            else:
                abstract = ""

            overall = paper.llm_overall or paper.ce_mapped_score
            reason = normalize_text(paper.llm_reason)

            lines.append(f"### [{i}] {title}")
            lines.append(f"- **Authors**: {authors_str}")
            lines.append(f"- **Year**: {year}")
            lines.append(f"- **Source**: {source}")
            if doi:
                lines.append(f"- **DOI**: {doi}")
            if url:
                lines.append(f"- **URL**: {url}")
            if overall:
                lines.append(f"- **Score**: overall={overall}")
            if reason:
                lines.append(f"- **Assessment**: {reason}")
            if abstract:
                lines.append(f"- **Abstract**: {abstract}")
            lines.append("")

        return "\n".join(lines)

    def _compute_stats(
        self, papers: list[PaperDict], review_stats: dict[str, Any],
    ) -> dict[str, Any]:
        overall_scores: list[float] = []
        years: list[int] = []

        for paper in papers:
            r = paper.llm_overall or paper.ce_mapped_score
            y = paper.year
            if isinstance(r, (int, float)) and r > 0:
                overall_scores.append(float(r))
            if isinstance(y, int) and y > 1900:
                years.append(y)

        avg_overall = sum(overall_scores) / len(overall_scores) if overall_scores else 0.0

        if years:
            year_range = f"{min(years)}-{max(years)}"
        else:
            year_range = "Unknown"

        return {
            "candidate_count": review_stats.get("candidate_count", len(papers)),
            "avg_relevance": avg_overall,
            "avg_novelty": 0.0,
            "avg_rigor": 0.0,
            "year_range": year_range,
        }
