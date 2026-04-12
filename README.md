# Paper Retrieval Agent

A lightweight multi-agent paper search assistant built with AutoGen AgentChat.

It turns a research query into a retrieval plan, searches multiple academic sources, filters candidates, and writes a Markdown report.

## Features

- Multi-agent workflow: Planner, Retrieval, Reviewer, Writer
- Multi-source search with `arXiv`, `Crossref`, and `OpenAlex`
- Optional reranking and PDF-based verification
- Markdown output for both final report and debug trace
- Supports `glm`, `deepseek`, `qwen`, `groq`, and `openrouter`

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

Create `.env` from `.env.example`, then choose one provider:

```bash
MODEL_PROVIDER=glm
GLM_API_KEY=your_api_key
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
GLM_MODEL=glm-4.5-air
```

## Usage

Run a single query:

```bash
python -m paper_research_agent.main --query "recent papers on multimodal medical image segmentation"
```

Run from a file:

```bash
python -m paper_research_agent.main --query-file query.txt
```

Interactive mode:

```bash
python -m paper_research_agent.main
```

Custom output directory:

```bash
python -m paper_research_agent.main --query "your topic" --output-dir outputs
```

You can also use the installed CLI entry:

```bash
paper-agent --query "your topic"
```

## Output

Reports are saved under `reports/` by default:

- `reports/user_reports/`: final user-facing report
- `reports/debug_traces/`: full agent trace

## Workflow

1. `PlannerAgent` builds a search plan
2. `RetrievalAgent` searches and ranks papers
3. `ReviewerAgent` checks relevance and coverage
4. `WriterAgent` generates the final Markdown report

## Notes

- Relative time constraints are anchored to the runtime date
- Reranking can use a separate model via `RERANK_MODEL`, `RERANK_BASE_URL`, and `RERANK_API_KEY`
- Query quality matters: short, specific, natural-language prompts work best
