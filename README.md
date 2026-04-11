# Paper Retrieval Agent

A LangGraph-based research agent prototype for project-centered literature retrieval.

This repository contains the current mid-stage implementation of a research workflow that can interpret a literature task, retrieve papers from multiple sources, run a review-and-revise loop, and write project-scoped research notes with structured artifacts.

## Current Progress

At the current stage, the repository already includes:

- a LangGraph workflow for task interpretation, retrieval, review, note generation, and artifact persistence
- multi-source retrieval from `arXiv`, `Crossref`, and `OpenAlex`
- optional local PDF integration
- reviewer-guided revision when retrieval quality is insufficient
- project-scoped outputs including notes, retrieval JSON, traces, and manifests

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
python -m paper_research_agent.main --project multimodal-imaging --query "foundation models for medical segmentation" --pdf-dir E:\Search\参考\B-Rep
```

You can also use the installed script entrypoint:

```bash
paper-agent --help
```

## Workflow

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

Current high-level execution flow:

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

This repository should currently be viewed as the groundwork for a larger research agent, not as a full end-to-end research platform.

The current implementation focuses on:

- building the retrieval workflow itself
- making intermediate outputs traceable
- producing reusable project-scoped artifacts

It does **not** yet focus on:

- long-term memory
- vector database indexing