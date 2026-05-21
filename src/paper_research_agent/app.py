from __future__ import annotations

from .agent import PaperDiscoveryAgent
from .core.config import Settings


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

    async def close(self) -> None:
        pass
