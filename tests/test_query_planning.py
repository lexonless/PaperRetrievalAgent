from __future__ import annotations

import unittest

from paper_research_agent.retrieval.query_planning import build_query_entries


class QueryPlanningTests(unittest.TestCase):
    def test_build_query_entries_renders_arxiv_crossref_openalex_queries(self) -> None:
        entries = build_query_entries(
            topic_phrases=["direct B-Rep generation", "diffusion model"],
            expanded_terms=["boundary representation", "DDPM", "denoising diffusion"],
            domain_terms=["CAD", "geometric modeling"],
            excluded_terms=["CSG", "mesh reconstruction"],
        )

        sources = {e["source"] for e in entries}
        self.assertTrue(sources.issuperset({"arXiv", "Crossref", "OpenAlex"}))

        arxiv_entries = [e for e in entries if e["source"] == "arXiv"]
        self.assertTrue(any("ANDNOT" in e["query"] for e in arxiv_entries))

    def test_excluded_terms_appear_in_andnot_clauses(self) -> None:
        entries = build_query_entries(
            topic_phrases=["image segmentation"],
            expanded_terms=["U-Net", "CNN"],
            domain_terms=["medical", "MRI"],
            excluded_terms=["text-to-image", "generation", "style transfer"],
        )

        arxiv_precision = next(
            e["query"] for e in entries if e["source"] == "arXiv" and e["purpose"] == "precision"
        )
        self.assertIn("ANDNOT", arxiv_precision)
        self.assertIn("text-to-image", arxiv_precision)


if __name__ == "__main__":
    unittest.main()
