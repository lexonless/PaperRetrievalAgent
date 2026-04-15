from __future__ import annotations

import unittest

from paper_research_agent.core.models import DiscoverIntent
from paper_research_agent.discover import build_discover_query_plan


class DiscoverQueryPlanningTests(unittest.TestCase):
    def test_build_discover_query_plan_renders_source_queries(self) -> None:
        query_plan = build_discover_query_plan(
            DiscoverIntent(
                topic="direct B-Rep generation",
                must_include=["diffusion model", "boundary representation"],
                must_exclude=["CSG"],
                domain_terms=["CAD", "geometric modeling"],
                negative_domains=["natural language generation"],
                source_hints=["arXiv", "OpenAlex", "Crossref"],
                primary_queries=["direct brep generation diffusion"],
                start_year=2021,
            )
        )

        self.assertTrue(any(spec.source == "arXiv" for spec in query_plan.rendered_queries))
        self.assertTrue(any(spec.source == "OpenAlex" for spec in query_plan.rendered_queries))
        self.assertTrue(any(spec.source == "Crossref" for spec in query_plan.rendered_queries))
        arxiv_query = next(
            spec.query for spec in query_plan.rendered_queries if spec.source == "arXiv" and spec.purpose == "precision"
        )
        self.assertIn("ANDNOT", arxiv_query)
        self.assertTrue(query_plan.primary_queries)


if __name__ == "__main__":
    unittest.main()
