from __future__ import annotations

import asyncio
import json
import logging
import os
import sys
from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field

from ..core.config import Settings
from ..core.llm import build_rerank_chat_model, invoke_structured_output
from ..core.normalization import normalize_text

logger = logging.getLogger(__name__)

RERANK_SYSTEM_PROMPT = """You are a scholarly paper reranker. Score each paper independently on how well it addresses the user's research query.

For each paper return:
- paper_key: the provided paper_key unchanged
- relevance: integer 1-5 (1=off-topic, 2=vaguely related, 3=somewhat relevant, 4=relevant, 5=highly relevant)
- reason: one sentence explaining the score

Return exactly one JSON object with key "papers" containing an array of judgments.
Do not use markdown code fences.
"""

LLM_BATCH_SIZE = 8


class RerankJudgment(BaseModel):
    paper_key: str
    relevance: int
    reason: str = ""


class RerankResult(BaseModel):
    papers: list[RerankJudgment] = Field(default_factory=list)


def _paper_key(paper: dict[str, Any]) -> str:
    oa_id = normalize_text(paper.get("_openalex_id", ""), for_matching=True)
    if oa_id:
        return f"oa:{oa_id}"
    doi = normalize_text(paper.get("doi", ""), for_matching=True)
    if doi:
        return f"doi:{doi}"
    title = normalize_text(paper.get("title", ""), for_matching=True)
    return f"title:{title}" if title else f"unknown_{id(paper)}"


def _build_paper_text(paper: dict[str, Any], max_length: int = 512) -> str:
    title = normalize_text(paper.get("title", ""))
    snippets = paper.get("evidence_snippets", [])
    abstract = normalize_text(snippets[0])[:max_length] if snippets else ""
    if abstract:
        return f"{title}. {abstract}"
    return title


class BaseReranker(ABC):

    @abstractmethod
    async def rerank(self, query: str, papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """返回 [{paper_key, relevance, reason}, ...]"""
        ...


class CrossEncoderReranker(BaseReranker):

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-base",
        device: str = "cpu",
        batch_size: int = 32,
        max_length: int = 512,
    ) -> None:
        self._model_name = model_name
        self._device = device
        self._batch_size = batch_size
        self._max_length = max_length
        self._model: Any = None

    def _ensure_model(self) -> None:
        if self._model is not None:
            return
        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
        os.environ.setdefault("TOKENIZERS_USE_FAST", "True")
        if self._device == "cpu":
            os.environ["CUDA_VISIBLE_DEVICES"] = ""
        try:
            from FlagEmbedding import FlagReranker
        except ImportError:
            raise ImportError(
                "FlagEmbedding is required for cross-encoder reranking. "
                "Install it with: pip install FlagEmbedding"
            )
        logging.getLogger("transformers").setLevel(logging.WARNING)
        logger.info("Loading cross-encoder model %s on %s ...", self._model_name, self._device)
        sys.stdout.flush()
        self._model = FlagReranker(self._model_name, use_fp16=False)
        logger.info("Cross-encoder model loaded.")

    async def rerank(self, query: str, papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not papers:
            return []

        self._ensure_model()

        pairs = [[query, _build_paper_text(p, self._max_length)] for p in papers]

        scores = await asyncio.to_thread(
            self._model.compute_score,
            pairs,
            normalize=True,
        )

        if not isinstance(scores, list):
            scores = [scores]

        mapped = [1 + round(score * 4) for score in scores]

        return [
            {
                "paper_key": _paper_key(p),
                "relevance": int(m),
                "reason": f"cross-encoder score: {float(scores[i]):.3f}",
            }
            for i, (p, m) in enumerate(zip(papers, mapped))
        ]


class LLMReranker(BaseReranker):

    def __init__(self, model: Any) -> None:
        self._model = model

    async def rerank(self, query: str, papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not papers:
            return []

        all_judgments: list[dict[str, Any]] = []
        for start in range(0, len(papers), LLM_BATCH_SIZE):
            batch = papers[start : start + LLM_BATCH_SIZE]
            judgments = await self._judge_rerank_batch(batch, query)
            all_judgments.extend(judgments)
        return all_judgments

    async def _judge_rerank_batch(
        self, batch: list[dict[str, Any]], query: str
    ) -> list[dict[str, Any]]:
        papers_data = []
        for p in batch:
            key = _paper_key(p)
            title = normalize_text(p.get("title", ""))
            year = p.get("year", "")
            snippets = p.get("evidence_snippets", [])
            abstract = normalize_text(snippets[0])[:500] if snippets else ""
            papers_data.append({
                "paper_key": key,
                "title": title,
                "year": year,
                "abstract": abstract,
            })

        result = await invoke_structured_output(
            model=self._model,
            schema=RerankResult,
            system_prompt=RERANK_SYSTEM_PROMPT,
            user_prompt=json.dumps({"query": query, "papers": papers_data}, ensure_ascii=False, indent=2),
        )
        return [
            {"paper_key": j.paper_key, "relevance": j.relevance, "reason": j.reason}
            for j in result.papers
        ]


def build_reranker(settings: Settings) -> BaseReranker:
    strategy = settings.rerank_strategy
    if strategy == "llm":
        llm = build_rerank_chat_model(settings)
        return LLMReranker(llm)

    return CrossEncoderReranker(
        model_name=settings.cross_encoder_model,
        device=settings.cross_encoder_device,
        batch_size=settings.cross_encoder_batch_size,
        max_length=settings.cross_encoder_max_length,
    )
