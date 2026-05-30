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
from ..core.llm import build_chat_model, invoke_structured_output
from ..core.models import PaperDict, paper_key
from ..core.normalization import normalize_text

logger = logging.getLogger(__name__)

LLM_RERANK_PROMPT = """You are an expert scholarly paper evaluator performing a professional re-ranking task. Your goal is to score the given papers with a holistic recommendation based ON THEIR ABSTRACTS.

### INPUT FORMAT EXPECTATION
You will be provided with a "Query" and a list of papers, each containing a "paper_id" and an "abstract".

### SCORING CRITERIA (1-5)
Evaluate and assign an 'overall' score based on these precise anchor definitions:
- 5 (Exceptional): Highly relevant to the query AND demonstrates a major breakthrough, state-of-the-art (SOTA) results, or exemplary methodology (benchmarks, ablations).
- 4 (Strong): Highly relevant with a clear, solid contribution and good clarity, though perhaps incremental rather than revolutionary.
- 3 (Borderline/Neutral): Relevant but ordinary/trivial contribution, OR slightly tangential but possesses exceptional methodological quality. 
- 2 (Weak): Marginally relevant to the query, or relevant but poorly written with vague contributions.
- 1 (Irrelevant): Completely off-topic or provides zero scientific value to the query.

*Note: Do not penalize if quality signals (like ablation studies) cannot be assessed from the abstract; score neutrally on what is visible.*

### OUTPUT FORMAT
Return EXACTLY ONE valid JSON object. Do NOT wrap the response in markdown code fences (e.g., do NOT use ```json ... 
```). Start the response directly with the opening curly brace { and end with }.

The JSON must follow this exact structure:
{
  "papers": [
    {
      "paper_id": "string/int",
      "overall": int,
      "reason": "Exactly one sentence summarizing your assessment."
    }
  ]
}
"""

LLM_BATCH_SIZE = 8


class RerankJudgment(BaseModel):
    paper_key: str
    overall: int = 0
    reason: str = ""


class RerankResult(BaseModel):
    papers: list[RerankJudgment] = Field(default_factory=list)


def _build_paper_text(paper: PaperDict, max_length: int = 512) -> str:
    title = normalize_text(paper.title)
    abstract = normalize_text(paper.evidence_snippets[0])[:max_length] if paper.evidence_snippets else ""
    if abstract:
        return f"{title}. {abstract}"
    return title


class BaseReranker(ABC):

    @abstractmethod
    async def rerank(self, query: str, papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """返回 [{paper_key, relevance, ...}, ...]"""
        ...


class CrossEncoderReranker(BaseReranker):

    _shared_model: Any = None
    _shared_model_name: str = ""

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

    @property
    def _model(self) -> Any:
        return CrossEncoderReranker._shared_model

    @_model.setter
    def _model(self, value: Any) -> None:
        CrossEncoderReranker._shared_model = value

    def _ensure_model(self) -> None:
        if self._model is not None and self._shared_model_name == self._model_name:
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
        CrossEncoderReranker._shared_model_name = self._model_name
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

        return [
            {
                "paper_key": paper_key(p),
                "relevance": 1 + round(score * 4),
                "raw_score": float(score),
            }
            for p, score in zip(papers, scores)
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
            judgments = await self._judge_batch(batch, query)
            all_judgments.extend(judgments)
        return all_judgments

    async def _judge_batch(
        self, batch: list[PaperDict], query: str
    ) -> list[dict[str, Any]]:
        papers_data = []
        for p in batch:
            key = paper_key(p)
            abstract = normalize_text(p.evidence_snippets[0])[:500] if p.evidence_snippets else ""
            papers_data.append({
                "paper_key": key,
                "title": normalize_text(p.title),
                "year": p.year,
                "abstract": abstract,
            })

        result = await invoke_structured_output(
            model=self._model,
            schema=RerankResult,
            system_prompt=LLM_RERANK_PROMPT,
            user_prompt=json.dumps({"query": query, "papers": papers_data}, ensure_ascii=False, indent=2),
        )
        return [
            {
                "paper_key": j.paper_key,
                "overall": j.overall,
                "reason": j.reason,
            }
            for j in result.papers
        ]


def build_reranker(settings: Settings) -> tuple[CrossEncoderReranker, LLMReranker]:
    ce_reranker = CrossEncoderReranker(
        model_name=settings.cross_encoder_model,
        device=settings.cross_encoder_device,
        batch_size=settings.cross_encoder_batch_size,
        max_length=settings.cross_encoder_max_length,
    )

    llm = build_chat_model(settings, rerank=True)
    llm_reranker = LLMReranker(llm)

    return ce_reranker, llm_reranker
