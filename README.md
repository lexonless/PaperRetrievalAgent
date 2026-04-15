# Raw Feeder v1

A paper discovery feeder for an LLM Wiki workflow. This project takes a natural-language research query, searches academic sources, deduplicates and filters paper candidates, and materializes the top results as `raw/papers/*.md` files that a downstream wiki agent can ingest.

## System Boundary

This system **does**:

- interpret a fuzzy natural-language paper discovery request
- generate source-aware queries for `arXiv`, `Crossref`, and `OpenAlex`
- retrieve and deduplicate paper candidates
- materialize selected papers into stable raw markdown files
- write batch metadata and an append-only feeder log

This system **does not**:

- edit `wiki/index.md`, `wiki/overview.md`, or any wiki pages
- build concept/entity pages
- answer knowledge questions or write syntheses
- perform refresh, incremental sync, or repo discovery

The output of this repo is `raw/` input for a downstream wiki agent. It does not maintain the wiki itself.

## Quick Start

### 1. Install

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

### 2. Configure

Copy `.env.example` to `.env` and set a supported OpenAI-compatible model provider.

### 3. Run discovery

```bash
raw-feeder discover --project brep-discovery --query "recent papers on direct B-Rep generation from natural language descriptions" --top-k 15
```

## Output Layout

Each project is organized around raw feeder outputs:

```text
projects/<project_slug>/
  project.md
  raw/
    papers/
      *.md
  .feeder/
    log.md
    batches/
      *.json
```

- `project.md`: optional project context that shapes discovery intent
- `raw/papers/*.md`: source materials for downstream wiki ingest
- `.feeder/batches/*.json`: machine-readable records of each discovery run
- `.feeder/log.md`: append-only operation log

## Raw Paper Format

Every raw paper file is a single-source document. It includes:

- bibliographic metadata
- canonical URL / DOI / PDF URL when available
- abstract or best available summary
- matched discovery queries
- provenance fields (`fetched_at`, `fetched_by`, source family)

The file is explicitly marked as raw source material and not as a wiki page or synthesis.

## Example Flow

1. Create or edit `projects/<slug>/project.md` with domain context.
2. Run `raw-feeder discover ...`.
3. Inspect the generated files in `projects/<slug>/raw/papers/`.
4. Point your wiki agent at those raw markdown files and ingest them into the wiki layer.

A static demo is included under `projects/demo-paper-discovery/` so the final raw and batch shapes are visible without running a live networked discovery.

## Development Notes

- The codebase intentionally reuses the existing source collectors and ranking utilities from the previous retrieval prototype.
- The LLM is only used for lightweight discover-intent parsing. It does not perform review loops or note generation.
- v1 supports only paper discovery from zero. No refresh/update pipeline is implemented yet.
