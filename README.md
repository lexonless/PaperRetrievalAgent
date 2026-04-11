# Research Assistant

This repository now uses a **LangGraph-based research assistant** architecture instead of the old AutoGen team.

The assistant is organized around a **project library**:

- one top-level graph
- one retrieval subgraph with a `plan -> retrieve -> review -> revise` loop
- project-scoped research note drafts
- structured retrieval and trace artifacts

## Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Configure

Copy `.env.example` to `.env` and choose a model provider.

Supported providers:

- `glm`
- `deepseek`
- `qwen`
- `groq`
- `openrouter`

The existing environment variables remain valid:

```bash
MODEL_PROVIDER=glm
GLM_API_KEY=your_key
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
GLM_MODEL=glm-4.5-air
```

Optional rerank configuration:

```bash
RERANK_MODEL=
RERANK_BASE_URL=
RERANK_API_KEY=
```

## Run

Run a query for a project:

```bash
python -m paper_research_agent.main --project multimodal-imaging --query "recent papers on multimodal models for medical image segmentation"
```

Run from a query file:

```bash
python -m paper_research_agent.main --project brep-reconstruct --query-file query.txt
```

Attach a local PDF directory:

```bash
python -m paper_research_agent.main --project multimodal-imaging --query "foundation models for medical segmentation" --pdf-dir D:\papers
```

Change the project library root:

```bash
python -m paper_research_agent.main --project multimodal-imaging --query "..." --output-dir projects
```

## Project Layout

Each project is stored under:

```text
projects/<project_slug>/
  project.md
  notes/
  retrieval/
  traces/
  sources/
    manifest.json
```

Artifacts produced by each run:

- `notes/*.md`: research note drafts
- `retrieval/*.json`: planner / retrieval / review outputs
- `traces/*.json`: structured execution traces

## Graph Structure

Top-level graph:

1. `prepare_run_context`
2. `paper_retrieval_subgraph`
3. `generate_research_note`
4. `persist_project_artifacts`

Only the retrieval workflow is a subgraph. It contains:

1. `planner_node`
2. `build_retrieval_request_node`
3. `retrieval_node`
4. `reviewer_node`
5. `validate_review_gate_node`

The review gate keeps a strict revise loop with a fixed revision budget. If the budget is exhausted, the assistant still writes a note draft but must include limitations.

## Current Scope

The current assistant supports:

- online retrieval from `arXiv`, `Crossref`, and `OpenAlex`
- optional local PDF discovery from a project PDF directory
- retrieval reranking
- programmatic review validation
- project-scoped research note generation

The current version does **not** include:

- vector databases
- long-term conversational memory
- global supervisor routing
- citation manager integration
