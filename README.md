# Paper Research Agent

An LLM-powered academic paper discovery, reading, and synthesis tool. It uses LangChain + ChatOpenAI to search arXiv, Crossref, and OpenAlex for papers, rank them with a cross-encoder + LLM reranker, download and read full-text PDFs, and generate structured Chinese research reports.

## System Boundary

This system **does**:

- interpret natural-language research queries via LLM decomposition
- search arXiv, Crossref, and OpenAlex with source-aware boolean queries
- deduplicate and rank paper candidates (cross-encoder + LLM reranker)
- expand paper graphs via references and citations (OpenAlex)
- iterate with LLM meta-review until convergence (up to 6 rounds)
- download PDFs and cache resolved URLs
- extract full-text content from PDFs via docling
- read and analyze papers with LLM (structured understanding: problem, method, contributions, results, limitations)
- generate Chinese literature survey reports from paper data

This system **does not**:

- perform web searches or RAG over arbitrary documents
- edit or maintain wiki pages
- run as a persistent daemon or incremental sync

## Quick Start

### 1. Install

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -e .
```

### 2. Configure

Copy `.env.example` to `.env` and set `MODEL_PROVIDER` to one of: `glm`, `deepseek`, `qwen`, `groq`, `openrouter`. Provide the matching `*_API_KEY`.

```bash
MODEL_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-...
```

Optionally set a separate rerank model via `RERANK_API_KEY`, `RERANK_BASE_URL`, `RERANK_MODEL`.

### 3. Run

```bash
# Autonomous agent: discover papers + generate report
paper-agent plan --project my-topic --query "recent advances in humanoid robot whole-body control"

# Discovery only: search papers and materialize them
paper-agent discover --project my-topic --query "..." --year-from 2024

# Synthesis only: generate a report from existing paper data
paper-agent synthesize --project my-topic
```

Queries can also come from a file via `--query-txt <path>` (tries `utf-8`, `utf-16`, `gbk` in order).

## Entry Points

| Command | Purpose |
|---|---|
| `paper-agent plan` | Autonomous: LLM decides to discover papers, synthesize a report, or both. |
| `paper-agent discover` | Paper discovery + PDF download + materialization. |
| `paper-agent synthesize` | Generate a Chinese research report from existing paper data. |

### Options

| Flag | Commands | Default | Description |
|---|---|---|---|
| `--project` | all | (required) | Project slug for the work directory |
| `--query` | discover, plan | (required) | Natural-language research query |
| `--query-txt` | discover, plan | — | Path to a `.txt` file containing the query |
| `--output-dir` | all | `projects` | Root directory for project outputs |
| `--year-from` | discover, plan | — | Lower bound of publication year (inclusive) |
| `--year-to` | discover, plan | — | Upper bound of publication year (inclusive) |

The number of output papers is **not** a CLI flag — it is inferred by the LLM via `QueryDecomposition.desired_paper_count`.

## Architecture

### Discovery Agent (`agent/engine.py`)

The `PaperDiscoveryAgent` runs up to 6 iterations of a four-node loop:

1. **Search** — query decomposition via LLM → source-aware boolean queries → arXiv / Crossref / OpenAlex
2. **Rerank** — cross-encoder scores ALL candidates (filter: `ce_score > 0.5`), then LLM scores top-N on holistic recommendation (1–5)
3. **Expand** — top seeds (score ≥ 3 or ce_score > 0.5) have references + citations fetched from OpenAlex
4. **Review** — LLM meta-reviewer checks global stats → converged / not-converged → refined query or stop

### Orchestrator Agent (`orchestrator.py`)

A LangChain tool-calling agent that autonomously decides which tools to invoke:

| Tool | Purpose |
|---|---|
| `discover_papers` | Search for academic papers (may be called once) |
| `synthesize_report` | Generate a Chinese research report |
| `read_papers` | Read downloaded PDFs and return structured understanding |
| `get_project_status` | Check paper count, batch history, report status |

### PDF Reader (`agent/reader.py`)

Two-layer caching:

- `projects/<slug>/raw/papers/fulltext/<slug>_raw.md` — docling extracted raw markdown
- `projects/<slug>/raw/papers/fulltext/<slug>.json` — LLM structured reading (PaperReading JSON)

The synthesis engine auto-populates these caches before generating reports. Subsequent reads skip extraction entirely.

### Reranking

Two-stage reranking — both always built (no config switch):

1. **Cross-encoder** (`BAAI/bge-reranker-base`, ~1.1GB download on first use): scores all candidates, filters out those with `ce_score ≤ 0.5`
2. **LLM reranker**: scores top-15 survivors on holistic 1–5 scale (relevance + clarity + significance + methodology)

### Package Layout

```
src/paper_research_agent/
  agent/         Discovery engine, PDF resolution/reading, prompts/params
  core/          Config, LLM builder, Pydantic models, normalization
  retrieval/     Source collectors, cross-encoder/LLM reranker, query planning
  synthesis/     Chinese report generation engine
```

## Output Layout

```text
projects/<project_slug>/
  project.md                          # Project context stub
  report.md                           # Generated synthesis report
  raw/
    papers/
      metadata/<slug>.md             # Paper frontmatter + abstract
      fulltext/<slug>.json           # PaperReading structured JSON
      fulltext/<slug>_raw.md         # docling raw markdown
    papers_pdf/<slug>.pdf            # Downloaded PDFs
  .feeder/
    log.md                           # Append-only operation log
    agent.log                        # DEBUG-level agent log
    batches/<batch_id>.json          # Full batch data (papers, reviews, errors)
```

## Configuration

### Model Providers

Set `MODEL_PROVIDER` to one of `glm`, `deepseek`, `qwen`, `groq`, `openrouter`. All five use OpenAI-compatible endpoints.

### Rerank Model

By default, the same model is used for reranking. To use a separate model:

```bash
RERANK_API_KEY=sk-...
RERANK_BASE_URL=https://api.example.com/v1
RERANK_MODEL=your-rerank-model
```

### Cross-Encoder

| Env Var | Default | Description |
|---|---|---|
| `CROSS_ENCODER_MODEL` | `BAAI/bge-reranker-base` | Model name or path |
| `CROSS_ENCODER_DEVICE` | `cpu` | `cpu` or `cuda` |
| `CROSS_ENCODER_BATCH_SIZE` | `32` | Batch size for scoring |
| `CROSS_ENCODER_MAX_LENGTH` | `512` | Max input length per text |

### Other

| Env Var | Default | Description |
|---|---|---|
| `REQUEST_TIMEOUT` | `30` | HTTP timeout in seconds |
| `MAX_RESULTS_PER_SOURCE` | `10` | Results per API call |
| `HTTP_PROXY` | — | HTTP proxy for API calls |
| `UNPAYWALL_EMAIL` | — | Email for Unpaywall DOI→PDF resolution |

## Standalone Tools

### DOI → PDF URL Resolver

```bash
python resolve_pdf.py 10.1109/icra55743.2025.11128271
python resolve_pdf.py [--email user@example.com] <doi> [doi...]
```

## Development

```bash
pip install -e .                             # Install for development
python -m pytest tests/                      # Run all tests
python -m tests.test_config                  # Run a single test file
```

Tests use `unittest` (standard library). No linter, typecheck, or CI/CD configuration.

## Dependencies

- `langchain-core` + `langchain-openai` — LLM agent framework
- `FlagEmbedding` — cross-encoder reranker (BAAI/bge-reranker-base)
- `docling` — PDF extraction and parsing
- `pyalex` — OpenAlex API client
- `pypdf` — PDF reading fallback
- `httpx` — HTTP client with proxy support
- `pydantic` — data models and structured output validation
