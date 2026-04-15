from __future__ import annotations

import shutil
import unittest
from pathlib import Path
from uuid import uuid4

from paper_research_agent.feeder_store import ensure_project_paths


class FeederStoreTests(unittest.TestCase):
    def test_ensure_project_paths_resets_existing_project_directory(self) -> None:
        project_root = Path.cwd() / f"tmp-feeder-store-{uuid4().hex[:8]}"
        project_root.mkdir(parents=True, exist_ok=True)
        try:
            existing_root = project_root / "demo-project"
            (existing_root / "raw" / "papers" / "metadata").mkdir(parents=True)
            (existing_root / ".feeder" / "batches").mkdir(parents=True)
            (existing_root / "raw" / "papers" / "metadata" / "old.md").write_text("old", encoding="utf-8")
            (existing_root / "project.md").write_text("old project context", encoding="utf-8")

            paths = ensure_project_paths(project_root, "demo-project", reset_existing=True)

            self.assertEqual(paths.root_dir, existing_root.resolve())
            self.assertFalse((existing_root / "raw" / "papers" / "metadata" / "old.md").exists())
            self.assertTrue(paths.project_file.exists())
            self.assertTrue(paths.paper_metadata_dir.exists())
            self.assertTrue(paths.paper_fulltext_dir.exists())
            self.assertTrue(paths.paper_page_images_dir.exists())
            self.assertTrue(paths.papers_pdf_dir.exists())
            self.assertIn("Project context for raw paper discovery", paths.project_file.read_text(encoding="utf-8"))
        finally:
            shutil.rmtree(project_root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
