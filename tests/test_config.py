from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from paper_research_agent.core.config import Settings


class ConfigTests(unittest.TestCase):
    def test_from_env_reads_docling_runtime_settings(self) -> None:
        env = {
            "MODEL_PROVIDER": "glm",
            "GLM_API_KEY": "test-key",
            "DOCLING_ACCELERATOR": "cpu",
            "DOCLING_OCR_BACKEND": "torch",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings.from_env()

        self.assertEqual(settings.docling_accelerator, "CPU")
        self.assertEqual(settings.docling_ocr_backend, "torch")


if __name__ == "__main__":
    unittest.main()
