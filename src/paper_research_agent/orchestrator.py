from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool

from .core.config import Settings
from .core.llm import build_chat_model
from .feeder_store import (
    get_project_decomposition,
    get_project_query,
    get_project_review_stats,
    list_batches,
    load_batch_json,
    parse_metadata_papers,
)
from .materializer import write_text_artifact
from .synthesis.engine import SynthesisEngine

logger = logging.getLogger(__name__)

ORCHESTRATOR_SYSTEM_PROMPT = """你是一个学术调研助手。根据用户的需求，自主决定调用哪些工具来完成任务。

## 可用工具

1. **discover_papers**：搜索学术论文。输入研究主题，返回搜索结果摘要。
2. **synthesize_report**：根据已有的论文数据生成中文调研报告。需要项目目录中已有论文数据。
3. **get_project_status**：查看项目当前状态（论文数量、批次信息、是否已有报告等）。

## 决策规则

- 用户需要**调研某个新课题** → 先 get_project_status 查看状态，如果无数据则先 discover_papers，再 synthesize_report
- 用户**只需要找论文** → 只调用 discover_papers
- 用户**已有论文数据，需要写报告** → 先 get_project_status 确认有数据，再 synthesize_report
- 用户**询问项目进度** → 只调用 get_project_status

## 注意事项

- 有依赖关系的工具必须按顺序调用（如先 discover 再 synthesize）
- 调用工具后分析结果，如果成功则继续下一步
- 不需要过度解释，简洁高效地完成任务
- 最终需要给用户一个简洁的总结
"""


def _build_discover_papers_tool(settings: Settings, output_root: str) -> Any:
    @tool
    def discover_papers(query: str, project: str, top_k: int = 5) -> str:
        """搜索学术论文并下载PDF。输入研究query和项目名称，在arXiv/Crossref/OpenAlex中搜索论文。

        Args:
            query: 研究问题或搜索关键词（必填）
            project: 项目名称/slug（必填）
            top_k: 最终输出的论文数量上限，默认5
        """
        import asyncio
        from .agent import PaperDiscoveryAgent

        async def _run():
            agent = PaperDiscoveryAgent(settings, output_root=output_root)
            try:
                batch, batch_path = await agent.discover(
                    project_slug=project, query=query, top_k=max(1, min(top_k, 20)),
                )
                selected = batch.get("selected_count", 0) if isinstance(batch, dict) else 0
                candidates = batch.get("candidate_count", 0) if isinstance(batch, dict) else 0
                return (
                    f"论文搜索完成。\n"
                    f"- 搜索到 {candidates} 篇候选论文\n"
                    f"- 筛选后保留 {selected} 篇\n"
                    f"- 批次文件：{batch_path}\n"
                    f"- 论文元数据文件已写入 raw/papers/metadata/ 目录"
                )
            finally:
                await agent.close()

        return asyncio.run(_run())

    return discover_papers


def _build_synthesize_report_tool(settings: Settings, output_root: str) -> Any:
    @tool
    def synthesize_report(project: str) -> str:
        """根据已有论文数据生成中文调研报告。要求项目目录中已有论文元数据文件。报告保存为 project/report.md。

        Args:
            project: 项目名称/slug（必填）
        """
        root = Path(output_root).resolve()
        papers = parse_metadata_papers(root, project)
        if not papers:
            return f"项目 {project} 中没有找到论文数据。请先使用 discover_papers 工具搜索论文。"

        query = get_project_query(root, project)
        decomposition = get_project_decomposition(root, project)
        review_stats = get_project_review_stats(root, project)

        engine = SynthesisEngine(settings)
        import asyncio

        async def _run():
            return await engine.synthesize(
                papers=papers,
                query=query or "未指定查询",
                project_slug=project,
                decomposition=decomposition,
                review_stats=review_stats,
            )

        report = asyncio.run(_run())

        report_dir = root / project
        report_dir.mkdir(parents=True, exist_ok=True)
        report_path = report_dir / "report.md"
        write_text_artifact(report_path, report)

        return (
            f"调研报告已生成。\n"
            f"- 报告路径：{report_path}\n"
            f"- 引用论文：{len(papers)} 篇\n"
            f"- 报告长度：{len(report)} 字符"
        )

    return synthesize_report


def _build_get_project_status_tool(output_root: str) -> Any:
    @tool
    def get_project_status(project: str) -> str:
        """查看项目当前状态。返回已有论文数量、批次列表、是否已有报告等信息。

        Args:
            project: 项目名称/slug（必填）
        """
        root = Path(output_root).resolve()
        project_dir = root / project
        if not project_dir.is_dir():
            return f"项目 {project} 不存在。需要先创建项目。"

        papers = parse_metadata_papers(root, project)
        batches = list_batches(root, project)
        report_exists = (project_dir / "report.md").is_file()

        lines = [
            f"项目 {project} 状态：",
            f"- 论文元数据文件：{len(papers)} 个",
            f"- 批次记录：{len(batches)} 个",
            f"- 调研报告：{'已存在' if report_exists else '未生成'}",
        ]

        if batches:
            latest = batches[0]
            lines.append(f"- 最新批次：{latest.name}")
            try:
                data = load_batch_json(latest)
                lines.append(f"- 最新批次查询：{data.get('query', '未知')}")
            except Exception:
                pass

        return "\n".join(lines)

    return get_project_status


class ResearchOrchestrator:
    def __init__(self, settings: Settings, *, output_root: str = "projects") -> None:
        self._settings = settings
        self._output_root = output_root
        self._llm = build_chat_model(settings, temperature=0.1)
        self._tools = [
            _build_discover_papers_tool(settings, output_root),
            _build_synthesize_report_tool(settings, output_root),
            _build_get_project_status_tool(output_root),
        ]
        self._tool_map = {t.name: t for t in self._tools}

    async def plan(self, user_query: str, project_slug: str, top_k: int = 5) -> str:
        llm_with_tools = self._llm.bind_tools(self._tools)

        messages = [
            SystemMessage(content=ORCHESTRATOR_SYSTEM_PROMPT),
            HumanMessage(content=f"项目名称：{project_slug}\n默认论文数：{top_k}\n\n用户需求：{user_query}"),
        ]

        final_answer = ""
        max_steps = 6
        for _step in range(max_steps):
            response = await llm_with_tools.ainvoke(messages)
            messages.append(response)

            tool_calls: list[dict] = getattr(response, "tool_calls", None) or []

            text_content = response.content if hasattr(response, "content") and isinstance(response.content, str) else ""
            if tool_calls:
                pass
            elif text_content.strip():
                final_answer = text_content.strip()
                break
            else:
                break

            for tc in tool_calls:
                name = tc.get("name", "")
                args = tc.get("args", {})
                tool_id = tc.get("id", "")

                project_value = args.get("project") or args.get("project_slug") or project_slug
                if name == "discover_papers":
                    args = {
                        "query": args.get("query", ""),
                        "project": project_value,
                        "top_k": args.get("top_k", top_k),
                    }
                elif name == "synthesize_report":
                    args = {"project": project_value}
                elif name == "get_project_status":
                    args = {"project": project_value}

                logger.info("agent: calling tool %s for project=%s", name, project_value)
                print(f"  [Agent] 调用工具: {name}")

                if name not in self._tool_map:
                    result_text = f"未知工具: {name}"
                else:
                    try:
                        result_text = self._tool_map[name].invoke(args)
                        if isinstance(result_text, list):
                            result_text = json.dumps(result_text, ensure_ascii=False)
                    except Exception as exc:
                        result_text = f"工具执行失败: {exc}"
                        logger.warning("tool %s failed: %s", name, exc)

                print(f"  [Agent] 结果: {result_text}")
                messages.append(ToolMessage(content=str(result_text)[:6000], tool_call_id=tool_id))
        else:
            if not final_answer:
                final_answer = "任务已完成。"

        return final_answer
