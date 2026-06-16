from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from paper_research_agent.core.config import Settings


class ConfigTests(unittest.TestCase):
    def test_from_env_reads_model_settings(self) -> None:
        env = {
            "MODEL_PROVIDER": "glm",
            "GLM_API_KEY": "test-key",
        }
        with patch.dict(os.environ, env, clear=False):
            settings = Settings.from_env()

        self.assertEqual(settings.model_name, "glm-4.5-air")
        self.assertEqual(settings.model_api_key, "test-key")


if __name__ == "__main__":
    unittest.main()
