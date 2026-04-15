from __future__ import annotations

from .core.config import Settings
from .discover import RawFeederService


class RawFeederApplication:
    def __init__(self, settings: Settings, *, output_root: str = "projects") -> None:
        self._service = RawFeederService(settings, output_root=output_root)

    async def discover(
        self,
        *,
        project_slug: str,
        query: str,
        top_k: int = 5,
    ):
        return await self._service.discover(project_slug=project_slug, query=query, top_k=top_k)

    async def close(self) -> None:
        await self._service.close()
