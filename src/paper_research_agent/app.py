from __future__ import annotations

from pathlib import Path

from .agent import PaperDiscoveryAgent
from .core.config import Settings
from .materializer import write_text_artifact
from .orchestrator import ResearchOrchestrator
from .synthesis.engine import SynthesisEngine, build_synthesis_context


def _init_pyalex(settings: Settings) -> None:
    try:
        import pyalex
    except ImportError:
        return
    if settings.openalex_api_key:
        pyalex.config.api_key = settings.openalex_api_key
    email = getattr(settings, "unpaywall_email", "") or ""
    if email:
        pyalex.config.email = email


class RawFeederApplication:
    def __init__(self, settings: Settings, *, output_root: str = "projects") -> None:
        self._settings = settings
        self._output_root = output_root
        _init_pyalex(settings)

    async def discover(
        self,
        *,
        project_slug: str,
        query: str,
    ):
        agent = PaperDiscoveryAgent(self._settings, output_root=self._output_root)
        try:
            return await agent.discover(project_slug=project_slug, query=query)
        finally:
            await agent.close()

    async def plan(
        self,
        *,
        project_slug: str,
        query: str,
    ) -> str:
        orchestrator = ResearchOrchestrator(self._settings, output_root=self._output_root)
        return await orchestrator.plan(user_query=query, project_slug=project_slug)

    async def synthesize(
        self,
        *,
        project_slug: str,
    ) -> None:
        root = Path(self._output_root).resolve()
        ctx = build_synthesis_context(root, project_slug)
        papers = ctx["papers"]

        if not papers:
            print(f"项目 {project_slug} 中没有找到论文元数据文件。")
            return

        print(f"共读取 {len(papers)} 篇论文元数据，开始生成报告...")

        engine = SynthesisEngine(self._settings)
        report = await engine.synthesize(
            papers=papers,
            query=ctx["query"] or project_slug,
            project_slug=project_slug,
            decomposition=ctx["decomposition"],
            review_stats=ctx["review_stats"],
        )

        report_path = root / project_slug / "report.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        write_text_artifact(report_path, report)

        print(f"调研报告已生成：{report_path}")

    async def close(self) -> None:
        pass
