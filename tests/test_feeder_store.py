from __future__ import annotations

import shutil
import unittest
from pathlib import Path
from uuid import uuid4

from paper_research_agent.feeder_store import ensure_project_paths


class FeederStoreTests(unittest.TestCase):
    def test_ensure_project_paths_creates_full_directory_structure(self) -> None:
        project_root = Path.cwd() / f"tmp-feeder-store-{uuid4().hex[:8]}"
        project_root.mkdir(parents=True, exist_ok=True)
        try:
            paths = ensure_project_paths(project_root, "demo-project")

            self.assertTrue(paths.root_dir.exists())
            self.assertTrue(paths.paper_metadata_dir.exists())
            self.assertTrue(paths.paper_fulltext_dir.exists())
            self.assertTrue(paths.paper_page_images_dir.exists())
            self.assertTrue(paths.papers_pdf_dir.exists())
            self.assertTrue(paths.batches_dir.exists())
            self.assertTrue(paths.project_file.exists())
            self.assertIn("Project context for raw paper discovery", paths.project_file.read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(project_root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
