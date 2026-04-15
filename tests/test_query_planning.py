from __future__ import annotations

import unittest

from paper_research_agent.retrieval.query_planning import apply_query_ir_update
from paper_research_agent.retrieval.query_planning import build_query_plan


class QueryPlanningTests(unittest.TestCase):
    def test_build_query_plan_normalizes_and_renders_source_queries(self) -> None:
        query_plan = build_query_plan(
            {
                "query_ir": {
                    "topic_phrases": ["direct B-Rep generation"],
                    "method_terms": ["neural network", "transformer"],
                    "optional_terms": ["boundary representation", "point cloud", "topology geometry joint learning"],
                    "excluded_terms": ["operation sequence", "CSG"],
                    "alias_groups": [],
                }
            }
        )

        self.assertIn("boundary representation", query_plan.semantic_core_terms)
        self.assertTrue(any(spec.source == "arXiv" for spec in query_plan.rendered_queries))
        self.assertTrue(any(spec.source == "OpenAlex" for spec in query_plan.rendered_queries))
        self.assertTrue(any(spec.source == "Crossref" for spec in query_plan.rendered_queries))
        arxiv_query = next(spec.query for spec in query_plan.rendered_queries if spec.source == "arXiv" and spec.purpose == "precision")
        self.assertIn("ANDNOT", arxiv_query)
        openalex_query = next(spec.query for spec in query_plan.rendered_queries if spec.source == "OpenAlex" and spec.purpose == "precision")
        self.assertIn("NOT", openalex_query)

    def test_apply_query_ir_update_only_changes_supplied_fields(self) -> None:
        updated_ir = apply_query_ir_update(
            {
                "topic_phrases": ["direct b-rep generation"],
                "method_terms": ["neural network"],
                "optional_terms": ["boundary representation", "point cloud"],
                "excluded_terms": ["program synthesis"],
                "alias_groups": [],
            },
            {
                "method_terms": ["diffusion"],
                "excluded_terms": ["construction tree"],
            },
        )

        self.assertEqual(updated_ir.topic_phrases, ["direct b-rep generation"])
        self.assertEqual(updated_ir.method_terms[0], "diffusion")
        self.assertIn("point cloud", updated_ir.optional_terms)
        self.assertIn("point clouds", updated_ir.optional_terms)
        self.assertIn("construction tree", updated_ir.excluded_terms)


if __name__ == "__main__":
    unittest.main()
