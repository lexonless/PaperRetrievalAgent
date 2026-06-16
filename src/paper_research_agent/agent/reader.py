from __future__ import annotations

import json
import logging
from pathlib import Path

from ..core.config import Settings
from ..core.llm import build_chat_model, invoke_structured_output
from ..core.models import PaperReading

logger = logging.getLogger(__name__)

READ_PAPER_SYSTEM_PROMPT = """You are an expert academic paper reader. Your task is to thoroughly understand a research paper and extract structured insights from it.

## Section Guidance

Where to find each field in the paper:

1. **problem_statement** → Read the Introduction and Abstract. Identify the gap in prior work and the specific research question this paper addresses.

2. **proposed_method** → Read the Methods / Approach section. Describe the technical architecture, key algorithms, and backbone networks. Be specific: name models, formulations, data flows. Avoid vague descriptions like "a novel approach" — instead name the actual technique.

3. **key_contributions** → Look at Introduction (final paragraphs) and Conclusion. List what the paper CLAIMS as its own contributions. Each item must be a specific contribution, not a summary of background work.

4. **key_results** → Read the Experiments / Results section. For each result, include: what was measured, against which baselines, by what margin. Use concrete numbers wherever available.

5. **limitations** → Read Discussion, Limitations, and Future Work sections. If the paper does not discuss limitations anywhere, state this explicitly rather than guessing or fabricating.

6. **relevance_assessment** → If a research query context is provided, assess how directly this paper answers that query. If no context, leave empty.

## Quality Requirements

- Every field must be grounded in the actual paper text. Do NOT fabricate, guess, or generalize.
- Distinguish the paper's OWN work from cited prior work, background, and related work.
- If a field cannot be determined from the text, use empty string or empty list — never invent content.
- When describing results, include specific metrics, datasets, baselines, and performance margins.
- Avoid empty phrases like "the paper introduces a novel method". Instead explain WHAT the method is.

## Output

Return exactly one valid JSON object matching the schema. Do not use markdown code fences.
"""

def _slug_from_filename(pdf_path: Path) -> str:
    return pdf_path.stem


async def _extract_markdown(pdf_path: Path, slug: str, raw_path: Path) -> str:
    if raw_path.is_file():
        logger.info("reader: raw markdown cache hit for %s", slug)
        return raw_path.read_text(encoding="utf-8")

    from docling.document_converter import DocumentConverter

    logger.info("reader: docling convert start: %s (%s bytes)", slug, pdf_path.stat().st_size)
    converter = DocumentConverter()
    doc_result = converter.convert(str(pdf_path))
    logger.info("reader: docling convert done: %s", slug)
    markdown = doc_result.document.export_to_markdown()
    logger.info("reader: docling export: %s chars for %s", len(markdown), slug)

    if markdown and markdown.strip():
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_text(markdown, encoding="utf-8")
        logger.info("reader: cached raw markdown for %s (%s chars)", slug, len(markdown))

    return markdown


async def _generate_reading(markdown: str, slug: str, cache_path: Path, llm) -> PaperReading:
    logger.info("reader: generating JSON reading for %s", slug)

    reading = await invoke_structured_output(
        model=llm,
        schema=PaperReading,
        system_prompt=READ_PAPER_SYSTEM_PROMPT,
        user_prompt=json.dumps({"paper_content": markdown}, ensure_ascii=False),
    )
    reading.title = reading.title or slug

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(reading.model_dump_json(indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("reader: cached JSON reading for %s", slug)

    return reading


async def read_papers(project: str, paper_slug: str = "", raw: bool = False, *, output_dir: str) -> str:
    """Read academic paper PDFs and return structured understanding or raw content.

    Extracts paper content using document parsing. When `raw=False` (default),
    returns structured JSON with problem statement, method, contributions,
    results, limitations, and relevance assessment. When `raw=True`, returns
    the raw full-text markdown extracted from the PDF.

    Args:
        project: Project name/slug (required).
        paper_slug: Specific paper slug to read. If empty, reads ALL papers
                     that have downloaded PDFs in the project.
        raw: If True, return raw markdown instead of structured JSON.
        output_dir: Root directory for project outputs (required keyword).
    """
    resolved = Path(output_dir).resolve()
    pdf_dir = resolved / project / "raw" / "papers_pdf"
    fulltext_dir = resolved / project / "raw" / "papers" / "fulltext"

    if paper_slug:
        pdf_path = pdf_dir / f"{paper_slug}.pdf"
        if not pdf_path.is_file():
            return f"PDF not found: {pdf_path}"
        pdf_paths = [pdf_path]
    else:
        pdf_paths = sorted(pdf_dir.glob("*.pdf"))
        if not pdf_paths:
            return f"No PDFs found in {pdf_dir}"

    settings = Settings.from_env()
    llm = build_chat_model(settings, temperature=0.1)
    results: list[str] = []

    for pdf_path in pdf_paths:
        slug = _slug_from_filename(pdf_path)
        raw_path = fulltext_dir / f"{slug}_raw.md"
        cache_path = fulltext_dir / f"{slug}.json"

        if raw:
            try:
                markdown = await _extract_markdown(pdf_path, slug, raw_path)
            except Exception as exc:
                logger.exception("reader: extraction failed for %s", slug)
                results.append(f"Extraction failed: {exc}")
                continue
            results.append(markdown)
            continue

        if cache_path.is_file():
            logger.info("reader: JSON cache hit for %s", slug)
            reading = PaperReading.model_validate_json(cache_path.read_text(encoding="utf-8"))
            results.append(reading.model_dump_json(indent=2, ensure_ascii=False))
            continue

        logger.info("reader: extracting %s", slug)
        try:
            markdown = await _extract_markdown(pdf_path, slug, raw_path)
        except Exception as exc:
            logger.exception("reader: extraction failed for %s", slug)
            results.append(json.dumps({"error": str(exc), "slug": slug}, ensure_ascii=False))
            continue

        if not markdown or not markdown.strip():
            results.append(json.dumps({"error": "empty content", "slug": slug}, ensure_ascii=False))
            continue

        logger.info("reader: extracted %s chars for %s", len(markdown), slug)

        try:
            reading = await _generate_reading(markdown, slug, cache_path, llm)
            results.append(reading.model_dump_json(indent=2, ensure_ascii=False))
        except Exception as exc:
            logger.exception("reader: LLM reading failed for %s", slug)
            raw_content = markdown[:2000]
            results.append(json.dumps({
                "error": f"LLM reading failed: {exc}",
                "slug": slug,
                "raw_preview": raw_content,
            }, ensure_ascii=False))

    if len(pdf_paths) == 1:
        return results[0]
    if not raw:
        return "[" + ",".join(results) + "]"
    return "\n\n---\n\n".join(results)
