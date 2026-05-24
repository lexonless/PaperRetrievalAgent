from __future__ import annotations

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from ..core.config import Settings
from ..core.llm import build_chat_model
from ..core.normalization import normalize_text

logger = logging.getLogger(__name__)

SYNTHESIS_SYSTEM_PROMPT = """你是一位资深的学术调研专家，擅长撰写综合性的学术文献调研报告。

## 核心职责

根据提供的论文数据，生成一份高质量的文献调研报告。

## 报告格式要求

**重要：** 请仔细阅读用户给出的「调研指令」。如果指令中包含了特定的输出格式要求（例如：分类体系树、子领域拆解、逐篇详细分析、特定分类桶、总结表等），请严格按照指令中的格式组织报告。如果指令没有指定特殊格式，则使用以下默认结构：

默认结构：
- **执行摘要**：2-3 句核心结论
- **研究背景与概览**：领域背景、主流方向和趋势
- **方法对比**：横向对比不同方法/技术路线的优劣（不足3篇论文时可省略）
- **关键发现与指标**：关键实验结果和性能指标
- **研究空白与未来方向**：未覆盖的研究空白和可行方向
- **参考文献**：`[序号] 标题 —— 作者 (年份), 来源`

## 语言要求

主体使用中文撰写。专业术语、模型名称、算法名称在首次出现时标注英文原文，例如"阻抗控制（impedance control）"。

## 内容要求

- 基于论文摘要中提供的具体信息进行分析，避免泛泛而谈
- 引用具体论文的具体贡献，交叉引用时标注参考文献编号
- 区分不同论文的创新程度
- 如果提供的论文信息不足以支撑某个要求，请如实说明并根据现有信息做最佳推断
- 使用 Markdown 表格、列表等语法增强可读性

## 输出

直接输出完整的 Markdown 格式调研报告。不要用 JSON 包裹或代码块包装。从标题开始。
"""

SYNTHESIS_USER_PROMPT_TEMPLATE = """## 调研指令

{user_instruction}

## 查询分解维度
{decomposition}

## 论文数据统计
- 候选论文总数：{candidate_count}
- 入选论文数：{selected_count}
- 平均相关性评分：{avg_relevance}
- 平均新颖性评分：{avg_novelty}
- 平均严谨性评分：{avg_rigor}
- 论文时间跨度：{year_range}

## 论文清单

{papers_detail}

请严格按照"调研指令"中的要求生成调研报告。优先使用指令中指定的格式和分类方式。如果论文数据不足以完全满足指令要求，请根据现有数据做最佳努力，并如实说明数据局限性。"""


class SynthesisEngine:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._llm = build_chat_model(settings, temperature=0.3)
        self._llm.max_tokens = max(settings.max_output_tokens, 16384)

    async def synthesize(
        self,
        *,
        papers: list[dict[str, Any]],
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
                decomp_lines.append(f"- 核心技术：{', '.join(decomposition['core_techs'])}")
            if decomposition.get("application_domains"):
                decomp_lines.append(f"- 应用领域：{', '.join(decomposition['application_domains'])}")
            if decomposition.get("key_metrics"):
                decomp_lines.append(f"- 关键指标：{', '.join(decomposition['key_metrics'])}")
            decomp_text = "\n".join(decomp_lines) if decomp_lines else "无"
        else:
            decomp_text = "无"

        user_prompt = SYNTHESIS_USER_PROMPT_TEMPLATE.format(
            user_instruction=query if query else "请根据以下论文数据撰写综合调研报告。",
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

    def _build_papers_detail(self, papers: list[dict[str, Any]]) -> str:
        lines: list[str] = []
        for i, paper in enumerate(papers, 1):
            title = normalize_text(paper.get("title", "")) or "无标题"
            authors = paper.get("authors", [])
            if isinstance(authors, list):
                authors_str = ", ".join(normalize_text(a) for a in authors[:5] if normalize_text(a))
                if len(authors) > 5:
                    authors_str += " 等"
            else:
                authors_str = str(authors) if authors else "未知"
            year = paper.get("year", "未知")
            source = normalize_text(paper.get("source", "")) or "未知"
            doi = normalize_text(paper.get("doi", ""))
            url = normalize_text(paper.get("url", ""))

            evidence = paper.get("evidence_snippets") or []
            if isinstance(evidence, list) and evidence:
                abstract = normalize_text(evidence[0])[:800]
            else:
                abstract = ""

            review_relevance = paper.get("review_relevance", paper.get("relevance_score", 0))
            review_novelty = paper.get("review_novelty", 0)
            review_rigor = paper.get("review_rigor", 0)
            review_reason = normalize_text(paper.get("review_reason", ""))

            lines.append(f"### [{i}] {title}")
            lines.append(f"- **作者**：{authors_str}")
            lines.append(f"- **年份**：{year}")
            lines.append(f"- **来源**：{source}")
            if doi:
                lines.append(f"- **DOI**：{doi}")
            if url:
                lines.append(f"- **URL**：{url}")
            if review_relevance:
                lines.append(f"- **评分**：相关性={review_relevance} 新颖性={review_novelty} 严谨性={review_rigor}")
            if review_reason:
                lines.append(f"- **评价**：{review_reason}")
            if abstract:
                lines.append(f"- **摘要**：{abstract}")
            lines.append("")

        return "\n".join(lines)

    def _compute_stats(
        self, papers: list[dict[str, Any]], review_stats: dict[str, Any],
    ) -> dict[str, Any]:
        rel_scores: list[float] = []
        nov_scores: list[float] = []
        rig_scores: list[float] = []
        years: list[int] = []

        for paper in papers:
            r = paper.get("review_relevance", paper.get("relevance_score", 0))
            n = paper.get("review_novelty", 0)
            g = paper.get("review_rigor", 0)
            y = paper.get("year")
            if isinstance(r, (int, float)) and r > 0:
                rel_scores.append(float(r))
            if isinstance(n, (int, float)) and n > 0:
                nov_scores.append(float(n))
            if isinstance(g, (int, float)) and g > 0:
                rig_scores.append(float(g))
            if isinstance(y, int) and y > 1900:
                years.append(y)

        avg_rel = sum(rel_scores) / len(rel_scores) if rel_scores else 0.0
        avg_nov = sum(nov_scores) / len(nov_scores) if nov_scores else 0.0
        avg_rig = sum(rig_scores) / len(rig_scores) if rig_scores else 0.0

        if years:
            year_range = f"{min(years)}-{max(years)}"
        else:
            year_range = "未知"

        return {
            "candidate_count": review_stats.get("candidate_count", len(papers)),
            "avg_relevance": avg_rel,
            "avg_novelty": avg_nov,
            "avg_rigor": avg_rig,
            "year_range": year_range,
        }
