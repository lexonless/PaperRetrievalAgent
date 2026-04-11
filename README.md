# Paper Retrieval Agent

A LangGraph-based research assistant for project-centered literature analysis.

It turns natural-language research tasks into structured retrieval workflows, searches across multiple academic sources, reviews and revises candidate sets, and produces project-scoped research notes with traceable artifacts.

## Highlights

- project-centered literature retrieval instead of one-off search results
- task interpretation from natural-language research prompts
- multi-source retrieval from `arXiv`, `Crossref`, and `OpenAlex`
- optional local PDF discovery and integration
- ranking, deduplication, and eligibility filtering for candidates
- reviewer-guided revision loop for low-quality retrieval results
- PDF-based evidence verification for promising papers
- structured research note generation
- persistent project artifacts: notes, retrieval JSON, traces, and manifests

## Quick Start

### 1. Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

### 2. Configure

Copy `.env.example` to `.env` and select a model provider.

Example:

```bash
MODEL_PROVIDER=glm
GLM_API_KEY=your_key
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
GLM_MODEL=glm-4.5-air
```

Optional rerank settings:

```bash
RERANK_MODEL=
RERANK_BASE_URL=
RERANK_API_KEY=
```

Supported providers currently include:

- `glm`
- `deepseek`
- `qwen`
- `groq`
- `openrouter`

### 3. Run

Run a direct query:

```bash
python -m paper_research_agent.main --project multimodal-imaging --query "recent papers on multimodal models for medical image segmentation"
```

Run from a query file:

```bash
python -m paper_research_agent.main --project brep-reconstruct --query-file query.txt
```

Use a local PDF directory:

```bash
python -m paper_research_agent.main --project multimodal-imaging --query "foundation models for medical segmentation" --pdf-dir D:\papers
```

You can also use the installed script entrypoint:

```bash
paper-agent --help
```

## How It Works

The workflow is organized as a top-level LangGraph graph plus a retrieval subgraph.

Top-level graph:

1. `prepare_run_context`
2. `paper_retrieval_subgraph`
3. `generate_research_note`
4. `persist_project_artifacts`

Retrieval subgraph:

1. `task_interpretation_node`
2. `retrieval_node`
3. `reviewer_node`
4. `validate_review_gate_node`

High-level execution flow:

1. interpret the task into a structured intent and query plan
2. retrieve candidates from academic sources
3. rank, filter, and deduplicate results
4. review retrieval quality against task constraints
5. revise and retry if needed
6. verify promising papers with PDF evidence when possible
7. generate a research note
8. persist all project artifacts

## Project Layout

```text
src/paper_research_agent/
  app.py
  config.py
  graph.py
  llm.py
  main.py
  models.py
  normalization.py
  project_store.py
  reporting.py
  retrieval_ranking.py
  retrieval_sources.py
  retrieval_utils.py
  retrieval_verification.py
  state.py
  toolkit.py

projects/
  <project_slug>/
    project.md
    notes/
    retrieval/
    traces/
    sources/
      manifest.json
```

## Output Artifacts

Each run writes reusable project materials:

- `notes/*.md`: project-scoped research notes
- `retrieval/*.json`: structured retrieval and review outputs
- `traces/*.json`: execution traces
- `sources/manifest.json`: accumulated project source and run metadata

## CLI Options

- `--project`: project slug used for the project library
- `--query`: direct natural-language research task
- `--query-file`: read the task from a text file
- `--pdf-dir`: optional local PDF directory
- `--output-dir`: custom root for project artifacts
- `--no-stream`: disable streaming progress output

## Current Scope

This repository currently focuses on:

- project-scoped retrieval workflows
- traceable intermediate artifacts
- reviewer-driven quality control
- research note generation from retrieved and verified candidates

It does **not** currently focus on:

- vector database indexing
- long-term conversational memory
- citation manager integration
- advanced downstream workflows such as paper comparison tables or experiment extraction

## Development Notes

- package metadata is defined in `pyproject.toml`
- the main CLI entrypoint is `paper_research_agent.main`
- the application wrapper lives in `paper_research_agent.app`
- artifact persistence is handled in `paper_research_agent.project_store`
- note and trace rendering lives in `paper_research_agent.reporting`

## Repository Description

> A LangGraph-based research assistant that transforms natural-language research tasks into structured paper retrieval workflows, searches across multiple academic sources, reviews and refines results through an iterative quality loop, and produces project-scoped research notes with traceable artifacts for continuous literature analysis.
