from __future__ import annotations

import unittest

from paper_research_agent.graph.builder import _collect_failed_queries
from paper_research_agent.graph.builder import _should_target_query_rewrite


class QueryRewriteLogicTests(unittest.TestCase):
    def test_should_target_query_rewrite_requires_revision_and_prior_queries(self) -> None:
        self.assertFalse(_should_target_query_rewrite(0, {}))
        self.assertFalse(_should_target_query_rewrite(1, {}))
        self.assertFalse(_should_target_query_rewrite(1, {"query_plan": {}}))
        self.assertTrue(
            _should_target_query_rewrite(
                1,
                {"query_plan": {"primary_queries": ["direct b-rep reconstruction"], "semantic_core_terms": []}},
            )
        )

    def test_collect_failed_queries_combines_planned_and_executed_queries(self) -> None:
        payload = _collect_failed_queries(
            previous_task_interpretation_payload={
                "intent": {},
                "hard_requirements": {},
                "query_plan": {
                    "primary_queries": ["direct b-rep reconstruction", "neural brep generation"],
                    "semantic_core_terms": ["boundary representation", "topology geometry"],
                },
            },
            retrieval_output_payload={
                "queries_executed": [
                    {
                        "query": "direct b-rep reconstruction",
                        "sources": ["arXiv", "OpenAlex"],
                        "notes": "Primary query executed from the latest task interpretation.",
                    },
                    {
                        "query": "point cloud to boundary representation",
                        "sources": ["Semantic Scholar"],
                        "notes": "Rewritten expansion query.",
                    },
                ]
            },
        )

        self.assertEqual(
            payload["planned_primary_queries"],
            ["direct b-rep reconstruction", "neural brep generation"],
        )
        self.assertEqual(
            payload["planned_semantic_core_terms"],
            ["boundary representation", "topology geometry"],
        )
        self.assertEqual(
            payload["all_failed_queries"],
            [
                "direct b-rep reconstruction",
                "neural brep generation",
                "boundary representation",
                "topology geometry",
                "point cloud to boundary representation",
            ],
        )
        self.assertEqual(len(payload["executed_queries"]), 2)


if __name__ == "__main__":
    unittest.main()
