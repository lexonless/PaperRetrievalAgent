from __future__ import annotations

from .config import Settings
from .graph import build_research_assistant_graph, create_resources
from .state import create_initial_state


class ResearchAssistantApplication:
    def __init__(self, settings: Settings, *, output_root: str = "projects") -> None:
        self.settings = settings
        self.resources = create_resources(settings, output_root=output_root)
        self.graph = build_research_assistant_graph(self.resources)

    async def run(
        self,
        *,
        project_slug: str,
        task: str,
        pdf_dir: str = "",
    ) -> dict:
        initial_state = create_initial_state(project_slug=project_slug, query=task)
        initial_state["project"]["pdf_dir"] = pdf_dir
        return await self.graph.ainvoke(initial_state)

    async def run_stream(
        self,
        *,
        project_slug: str,
        task: str,
        pdf_dir: str = "",
    ):
        initial_state = create_initial_state(project_slug=project_slug, query=task)
        initial_state["project"]["pdf_dir"] = pdf_dir
        return self.graph.astream(initial_state, stream_mode="values")

    async def close(self) -> None:
        await self.resources.toolkit.close()
