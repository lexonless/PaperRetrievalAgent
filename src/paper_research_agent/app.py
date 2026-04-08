from __future__ import annotations

import re
from datetime import date

from autogen_agentchat.base import TaskResult

from .agent import build_model_client, build_rerank_model_client
from .config import Settings
from .team import build_paper_search_team
from .toolkit import PaperSearchToolkit

RELATIVE_YEAR_PATTERN = re.compile(r"\b(?:last|past)\s+(?P<count>\d{1,2})\s+years?\b", re.IGNORECASE)
RECENCY_HINT_PATTERN = re.compile(r"\b(recent|latest|newest|current)\b", re.IGNORECASE)


class PaperSearchApplication:
    """Owns the model client, toolkit, and top-level team."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.model_client = build_model_client(settings)
        self.rerank_model_client = build_rerank_model_client(settings)
        self.toolkit = PaperSearchToolkit(settings, rerank_model_client=self.rerank_model_client)
        self.team = build_paper_search_team(self.model_client, self.toolkit)

    async def run_stream(self, task: str):
        self.toolkit.clear_latest_retrieval_request()
        await self.team.reset()
        return self.team.run_stream(task=_prepare_task(task))

    async def run(self, task: str) -> TaskResult:
        self.toolkit.clear_latest_retrieval_request()
        await self.team.reset()
        return await self.team.run(task=_prepare_task(task))

    async def close(self) -> None:
        await self.toolkit.close()
        await self.rerank_model_client.close()
        await self.model_client.close()


def _prepare_task(task: str) -> str:
    today = date.today()
    notes = [
        f"Today's date for this run is {today.isoformat()}.",
    ]

    relative_notes: list[str] = []
    seen_phrases: set[str] = set()
    for match in RELATIVE_YEAR_PATTERN.finditer(task):
        phrase = match.group(0)
        if phrase.lower() in seen_phrases:
            continue
        seen_phrases.add(phrase.lower())
        count = int(match.group("count"))
        start_year = today.year - count + 1
        end_year = today.year
        relative_notes.append(
            f'- Resolve "{phrase}" as the inclusive year window {start_year}-{end_year}.'
        )

    if relative_notes:
        notes.extend(relative_notes)
        notes.append("- Treat that resolved year window as authoritative unless a later agent explicitly labels a broader range as an extra.")
    elif RECENCY_HINT_PATTERN.search(task):
        notes.append(
            "- The query contains a vague recency hint. PlannerAgent must resolve it into an explicit year range against today's date and all later agents must preserve that range."
        )

    runtime_context = "\n".join(notes)
    return f"{task}\n\n[Runtime Search Context]\n{runtime_context}"
