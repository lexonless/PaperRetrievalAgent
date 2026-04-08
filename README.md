# Paper Retrieval Agent

This repository contains a starter paper-retrieval agent built with `AutoGen AgentChat 0.4+` and the `GLM API`.

The current version is intentionally lightweight, but it already uses a multi-agent workflow that you can evolve further:

- a richer multi-agent retrieval / screening / summarization system
- a retrieval pipeline with reranking
- a system connected to a vector store, database, or local paper archive
- a domain-specific prompt and tool stack

## 1. Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## 2. Configure

Copy `.env.example` to `.env` and choose a model provider.

GLM example:

```bash
MODEL_PROVIDER=glm
GLM_API_KEY=your_zhipu_api_key
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
GLM_MODEL=glm-4.5-air
```

DeepSeek example using DeepSeek's OpenAI-compatible endpoint:

```bash
MODEL_PROVIDER=deepseek
DEEPSEEK_API_KEY=your_deepseek_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

Qwen example using DashScope's OpenAI-compatible endpoint:

```bash
MODEL_PROVIDER=qwen
QWEN_API_KEY=your_qwen_api_key
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
QWEN_MODEL=qwen-max-latest
```

Groq example using Groq's OpenAI-compatible endpoint:

```bash
MODEL_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=llama-3.3-70b-versatile
```

OpenRouter example using the free Llama 3.3 70B route:

```bash
MODEL_PROVIDER=openrouter
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=meta-llama/llama-3.3-70b-instruct:free
OPENROUTER_HTTP_REFERER=
OPENROUTER_APP_TITLE=paper-retrieval-agent
```

Notes:

- The general GLM API endpoint is usually `https://open.bigmodel.cn/api/paas/v4`
- If you later switch to Coding Plan, use `https://open.bigmodel.cn/api/coding/paas/v4`
- `MODEL_PROVIDER` currently supports `glm`, `deepseek`, `qwen`, `groq`, and `openrouter`
- DeepSeek uses the OpenAI-compatible base URL `https://api.deepseek.com`
- For this project, prefer `deepseek-chat`; the official docs note that `deepseek-reasoner` does not support function calling
- Qwen uses DashScope's OpenAI-compatible base URL `https://dashscope.aliyuncs.com/compatible-mode/v1`
- Groq uses the OpenAI-compatible base URL `https://api.groq.com/openai/v1`
- OpenRouter uses a normal OpenRouter API key; the `:free` suffix is part of the model route, not a different key type
- You can optionally configure a dedicated rerank model with `RERANK_MODEL`, `RERANK_BASE_URL`, and `RERANK_API_KEY`. If these are omitted, retrieval reranking falls back to the main model settings.

## 3. Run

Run once:

```bash
python -m paper_research_agent.main --query "recent papers on multimodal models for medical image segmentation"
```

Run from a query file:

```bash
python -m paper_research_agent.main --query-file query.txt
```

Interactive mode:

```bash
python -m paper_research_agent.main
```

Reports are automatically saved as Markdown files under `reports/` by default.
They are split into:

- `reports/user_reports/`: final user-facing markdown
- `reports/debug_traces/`: full message trace for debugging

You can change the output directory with:

```bash
python -m paper_research_agent.main --query "your topic" --output-dir outputs
```

## 4. Built-in tools

Tools exposed to `RetrievalAgent`:

- `retrieve_candidates_from_plan`: the default retrieval tool; inherits the latest planner JSON and returns ranked candidates. It accepts `top_k`, `max_results_per_source`, and optional `query` for a narrower retrieval wording.

Internal retrieval helpers kept in the toolkit implementation:

- source-specific record fetchers for arXiv, Crossref, and OpenAlex
- retrieval-plan execution and staged fallback expansion
- PDF-based supplemental verification for a small number of high-potential candidates

The internal helpers are not exposed directly to the retrieval model, which reduces confusion between overlapping search tools.
The current built-in source mix is:

- `arXiv`: preprints and abstracts
- `Crossref`: broad metadata and DOI coverage
- `OpenAlex`: broader scholarly graph metadata with abstracts when available

The retrieval layer now includes a programmatic filtering/rerank step:

- deduplicate by DOI, URL, or normalized title
- apply light lexical filtering and ranking
- optionally call a dedicated rerank model on the top retrieval candidates for paper-level `relevance`, `task_fit`, and `verification` judgments
- verify a small number of high-potential candidates with extracted PDF text when a PDF link is available

The planner schema is also richer now. In addition to search queries, it is expected to produce:

- `fallback_queries`: broader backup queries used only when the primary queries remain sparse

Planner query-writing guidance:

- keep queries as short natural-language phrases
- avoid boolean/search-engine syntax such as `AND`, `OR`, parentheses, field tags, or bundled quoted tokens
- avoid embedding year literals into queries when the time window is already captured structurally

## 5. Output format

Each run produces two markdown files:

- the original query
- a user-facing final report
- a separate debug trace with tool-call outputs and intermediate messages

This keeps the user report clean while preserving the full trace for debugging.

## 6. Team orchestration

The current AutoGen team uses this flow:

- `PlannerAgent`: turns the user query into a concrete retrieval plan
- `RetrievalAgent`: runs tool-based searches and returns evidence-backed candidates
- `ReviewerAgent`: applies a strict `PASS / REVISE` gate
- `WriterAgent`: writes the final markdown report and terminates the run

Intermediate-state protocol:

- `PlannerAgent` returns structured JSON
- `RetrievalAgent` returns structured JSON
- `ReviewerAgent` returns structured JSON
- `WriterAgent` is the only agent that returns final user-facing markdown

Additional guardrails:

- relative time phrases such as `last 5 years` are anchored to the current run date and injected into the team task as runtime context
- retrieval results must label `verification_status`, `evidence_level`, and `time_range_status`
- title-only evidence must remain weak and cannot carry fabricated evidence snippets
- the final review gate is programmatically checked against both reviewer JSON and retrieval JSON

The reviewer now uses a stricter rubric before allowing the writer stage:

- at least 2 distinct sources searched unless the user explicitly narrowed the scope
- at least 5 non-duplicate candidates after obvious title / DOI / URL merging
- at least 3 strongly relevant papers among the top 5
- each retained candidate should have title, source, year/date, and URL when available
- query-specific constraints such as recency, domain, and task intent must be reflected in the set
- at least 3 in-range papers must be explicit core candidates for the user's topic with non-weak evidence
- the reviewer also scores coverage, relevance, metadata quality, diversity, and evidence quality on a 0-2 scale
- PASS requires all hard requirements to pass, total rubric score at least 8/10, and no category scored 0
- the reviewer now returns structured JSON, and the team programmatically validates the decision before moving to the writer, including evidence-level and time-range checks from retrieval output

If review still fails after 2 revise cycles, the team proceeds to the writer anyway, but the report must include clear limitations.

## 7. Suggested next steps

- Add `Semantic Scholar / OpenAlex / PubMed` retrieval tools
- Add DOI-based deduplication and result fusion
- Expand the team with dedicated `Normalizer` or `Domain Specialist` agents
- Add structured outputs and markdown report generation
- Add local PDF parsing and citation extraction

## 8. Prompt template

Use a query like this when you want stronger retrieval quality:

```text
Search research from [time range] on [topic].
Focus on: [subtopic 1], [subtopic 2], [subtopic 3].
Exclude: [irrelevant directions].
Output: [what each paper should include] and [what final summary should include].
```

Example:

```text
Search research from the last 5 years on multimodal models for medical image segmentation.
Focus on foundation models, multimodal fusion, and clinically relevant evaluation settings.
Exclude purely unimodal image segmentation papers and benchmark-only papers without methodological novelty.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
```
