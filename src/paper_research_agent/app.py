from __future__ import annotations

from pathlib import Path

from .agent import PaperDiscoveryAgent
from .core.config import Settings
from .feeder_store import (
    get_project_decomposition,
    get_project_query,
    get_project_review_stats,
    parse_metadata_papers,
)
from .materializer import write_text_artifact
from .orchestrator import ResearchOrchestrator
from .synthesis.engine import SynthesisEngine


class RawFeederApplication:
    def __init__(self, settings: Settings, *, output_root: str = "projects") -> None:
        self._settings = settings
        self._output_root = output_root

    async def discover(
        self,
        *,
        project_slug: str,
        query: str,
        top_k: int = 5,
    ):
        agent = PaperDiscoveryAgent(self._settings, output_root=self._output_root)
        try:
            return await agent.discover(project_slug=project_slug, query=query, top_k=top_k)
        finally:
            await agent.close()

    async def plan(
        self,
        *,
        project_slug: str,
        query: str,
        top_k: int = 5,
    ) -> str:
        orchestrator = ResearchOrchestrator(self._settings, output_root=self._output_root)
        return await orchestrator.plan(user_query=query, project_slug=project_slug, top_k=top_k)

    async def synthesize(
        self,
        *,
        project_slug: str,
    ) -> None:
        root = Path(self._output_root).resolve()
        papers = parse_metadata_papers(root, project_slug)
        if not papers:
            print(f"项目 {project_slug} 中没有找到论文元数据文件。")
            return

        query = get_project_query(root, project_slug)
        decomposition = get_project_decomposition(root, project_slug)
        review_stats = get_project_review_stats(root, project_slug)

        print(f"共读取 {len(papers)} 篇论文元数据，开始生成报告...")

        engine = SynthesisEngine(self._settings)
        report = await engine.synthesize(
            papers=papers,
            query=query or project_slug,
            project_slug=project_slug,
            decomposition=decomposition,
            review_stats=review_stats,
        )

        report_path = root / project_slug / "report.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        write_text_artifact(report_path, report)

        print(f"调研报告已生成：{report_path}")

    async def close(self) -> None:
        pass
