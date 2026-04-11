from __future__ import annotations

import asyncio
from io import BytesIO
from pathlib import Path
from typing import Any, Callable

from ..core.normalization import normalize_text
from .utils import normalize_pdf_url


class PaperVerificationEngine:
    def __init__(
        self,
        client: Any,
        *,
        score_eligibility: Callable[[dict[str, Any], dict[str, Any]], dict[str, Any] | None],
        finalize_ranked_papers: Callable[[list[dict[str, Any]]], list[dict[str, Any]]],
    ) -> None:
        self._client = client
        self._score_eligibility = score_eligibility
        self._finalize_ranked_papers = finalize_ranked_papers

    async def verify_promising_candidates(self, papers: list[dict[str, Any]], context: dict[str, Any]) -> list[dict[str, Any]]:
        updated_papers = [dict(paper) for paper in papers]
        verification_targets: list[int] = []
        for index, paper in enumerate(updated_papers[:15]):
            if len(verification_targets) >= 8:
                break
            if not paper.get("eligible"):
                continue
            if not self._resolve_pdf_url(paper):
                continue
            evidence_level = str(paper.get("evidence_level", "")).strip().lower()
            task_fit = str(paper.get("task_fit", "")).strip().lower()
            topical_relevance = str(paper.get("topical_relevance", "")).strip().lower()
            evidence_sufficiency = str(paper.get("evidence_sufficiency", "")).strip().lower()
            eligibility_score = int(paper.get("eligibility_score", 0))

            should_verify = False
            if evidence_level == "title_only":
                should_verify = eligibility_score >= 6 or (task_fit in {"direct", "related"} and topical_relevance in {"high", "medium"})
            elif evidence_level == "abstract":
                should_verify = task_fit in {"direct", "related"} and topical_relevance in {"high", "medium"} and evidence_sufficiency in {"weak", "partial"}
            if should_verify:
                verification_targets.append(index)

        for index in verification_targets:
            paper = updated_papers[index]
            pdf_url = self._resolve_pdf_url(paper)
            if not pdf_url:
                continue
            try:
                pdf_text = await self._fetch_pdf_text(url=pdf_url, max_chars=2500)
            except Exception:
                continue
            if not pdf_text:
                continue

            evidence_snippets: list[str] = []
            for item in paper.get("evidence_snippets", []) or []:
                normalized = normalize_text(item)
                if normalized and normalized not in evidence_snippets:
                    evidence_snippets.append(normalized[:800])
                if len(evidence_snippets) >= 1:
                    break
            normalized_pdf_text = normalize_text(pdf_text)
            evidence_snippets.append((normalized_pdf_text or pdf_text)[:800])
            paper["evidence_snippets"] = list(dict.fromkeys(evidence_snippets))[:2]
            paper["evidence_level"] = "excerpt"
            rescored = self._score_eligibility(paper, context)
            if rescored is None:
                paper["verification_status"] = "weak"
                paper["eligible"] = False
                paper["eligibility_score"] = 0
                continue

            task_fit = str(rescored.get("task_fit", "")).strip().lower()
            topical_relevance = str(rescored.get("topical_relevance", "")).strip().lower()
            evidence_sufficiency = str(rescored.get("evidence_sufficiency", "")).strip().lower()
            rescored["verification_status"] = "verified" if task_fit == "direct" and topical_relevance == "high" and evidence_sufficiency in {"strong", "partial"} else "partial"
            updated_papers[index] = rescored

        return self._finalize_ranked_papers(updated_papers)

    async def _fetch_pdf_text(self, url: str, max_chars: int = 1800) -> str:
        path = Path(url)
        if path.exists():
            return await asyncio.to_thread(self._read_local_pdf_text, path, max_chars)
        try:
            from pypdf import PdfReader
        except ImportError:
            return ""
        response = await self._client.get(url)
        response.raise_for_status()
        content = response.content
        content_type = str(response.headers.get("content-type", "")).lower()
        if b"%PDF" not in content[:8] and "application/pdf" not in content_type:
            return ""
        try:
            reader = PdfReader(BytesIO(content))
        except Exception:
            return ""

        chunks: list[str] = []
        remaining = max_chars
        for page in reader.pages[:3]:
            if remaining <= 0:
                break
            try:
                page_text = page.extract_text() or ""
            except Exception:
                continue
            normalized = normalize_text(page_text)
            if not normalized:
                continue
            snippet = normalized[:remaining]
            if snippet:
                chunks.append(snippet)
                remaining -= len(snippet)
        return normalize_text(" ".join(chunks))[:max_chars]

    def _read_local_pdf_text(self, path: Path, max_chars: int = 1800) -> str:
        try:
            from pypdf import PdfReader
        except ImportError:
            return ""
        if not path.exists():
            return ""
        try:
            reader = PdfReader(str(path))
        except Exception:
            return ""
        chunks: list[str] = []
        remaining = max_chars
        for page in reader.pages[:3]:
            if remaining <= 0:
                break
            try:
                page_text = page.extract_text() or ""
            except Exception:
                continue
            normalized = normalize_text(page_text)
            if not normalized:
                continue
            snippet = normalized[:remaining]
            if snippet:
                chunks.append(snippet)
                remaining -= len(snippet)
        return normalize_text(" ".join(chunks))[:max_chars]

    def _resolve_pdf_url(self, paper: dict[str, Any]) -> str:
        preferred = normalize_pdf_url(str(paper.get("_pdf_url", "") or ""))
        if preferred:
            return preferred
        return normalize_pdf_url(normalize_text(paper.get("url", "")))
