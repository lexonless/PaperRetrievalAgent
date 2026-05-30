from __future__ import annotations

import unittest

from paper_research_agent.retrieval.query_planning import build_query_entries


class QueryPlanningTests(unittest.TestCase):
    def test_build_query_entries_renders_arxiv_crossref_openalex_queries(self) -> None:
        entries = build_query_entries(
            topic_phrases=["direct B-Rep generation", "diffusion model"],
            expanded_terms=["boundary representation", "DDPM", "denoising diffusion"],
            domain_terms=["CAD", "geometric modeling"],
        )

        sources = {e["source"] for e in entries}
        self.assertTrue(sources.issuperset({"arXiv", "Crossref", "OpenAlex"}))

        arxiv_entries = [e for e in entries if e["source"] == "arXiv"]
        self.assertTrue(len(arxiv_entries) >= 1)
        self.assertTrue(all("all:" in e["query"] for e in arxiv_entries))


if __name__ == "__main__":
    unittest.main()
