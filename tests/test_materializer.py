from __future__ import annotations

import unittest

from paper_research_agent.materializer import build_raw_paper_slug, render_raw_paper_markdown


class MaterializerTests(unittest.TestCase):
    def test_slug_prefers_doi_then_arxiv_then_title(self) -> None:
        doi_slug = build_raw_paper_slug({"title": "Paper", "doi": "10.1145/example.123"})
        self.assertTrue(doi_slug.startswith("doi-10-1145-example-123"))

        arxiv_slug = build_raw_paper_slug({"title": "Paper", "url": "https://arxiv.org/abs/2501.12345"})
        self.assertEqual(arxiv_slug, "arxiv-2501-12345")

        title_slug = build_raw_paper_slug({"title": "Direct B-Rep Generation with Diffusion"})
        self.assertEqual(title_slug, "direct-brep-generation-with-diffusion")

    def test_render_marks_file_as_raw_source_material(self) -> None:
        content = render_raw_paper_markdown(
            {
                "title": "BrepGPT",
                "source": "arXiv",
                "authors": ["A. Author"],
                "year": 2025,
                "date": "2025-01-01",
                "url": "https://arxiv.org/abs/2501.12345",
                "doi": "",
                "_pdf_url": "https://arxiv.org/pdf/2501.12345.pdf",
                "evidence_snippets": [],
                "_matched_queries": ["brep generation"],
                "evidence_level": "title_only",
                "eligibility_score": 7,
            },
            project_slug="demo",
            user_query="papers on brep generation",
            generated_at="2026-04-15T10:00:00",
            local_pdf_path="projects/demo/raw/papers_pdf/arxiv-2501-12345.pdf",
            local_fulltext_path="projects/demo/raw/papers/fulltext/arxiv-2501-12345.md",
            local_page_image_dir="projects/demo/raw/papers/page_images/arxiv-2501-12345",
            pdf_download_status="downloaded",
        )

        self.assertIn("type: raw_source", content)
        self.assertIn("This file is raw source material prepared for downstream wiki ingestion.", content)
        self.assertIn("_No abstract or summary was available from the discovery sources._", content)
        self.assertIn("fetched_by: `raw-feeder-v1`", content)
        self.assertIn("Local converted markdown", content)
        self.assertIn("Local page images", content)
        self.assertIn("projects/demo/raw/papers/fulltext/arxiv-2501-12345.md", content)


if __name__ == "__main__":
    unittest.main()
