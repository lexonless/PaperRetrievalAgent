from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(slots=True)
class Settings:
    model_provider: str
    model_api_key: str
    model_base_url: str
    model_name: str
    default_headers: dict[str, str] | None
    rerank_model_api_key: str
    rerank_model_base_url: str
    rerank_model_name: str
    rerank_default_headers: dict[str, str] | None
    request_timeout: float
    max_results_per_source: int
    docling_accelerator: str
    docling_ocr_backend: str

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()

        provider = os.getenv("MODEL_PROVIDER", "glm").strip().lower()
        default_headers: dict[str, str] | None = None

        if provider == "glm":
            api_key = os.getenv("GLM_API_KEY", "").strip()
            if not api_key:
                raise ValueError("Missing GLM_API_KEY. Please set it in your environment or .env file.")
            base_url = os.getenv("GLM_BASE_URL", "https://open.bigmodel.cn/api/paas/v4").rstrip("/")
            model_name = os.getenv("GLM_MODEL", "glm-4.5-air").strip()
        elif provider == "deepseek":
            api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
            if not api_key:
                raise ValueError("Missing DEEPSEEK_API_KEY. Please set it in your environment or .env file.")
            base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
            model_name = os.getenv("DEEPSEEK_MODEL", "deepseek-chat").strip()
        elif provider == "qwen":
            api_key = os.getenv("QWEN_API_KEY", "").strip()
            if not api_key:
                raise ValueError("Missing QWEN_API_KEY. Please set it in your environment or .env file.")
            base_url = os.getenv("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1").rstrip("/")
            model_name = os.getenv("QWEN_MODEL", "qwen-max-latest").strip()
        elif provider == "groq":
            api_key = os.getenv("GROQ_API_KEY", "").strip()
            if not api_key:
                raise ValueError("Missing GROQ_API_KEY. Please set it in your environment or .env file.")
            base_url = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1").rstrip("/")
            model_name = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()
        elif provider == "openrouter":
            api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
            if not api_key:
                raise ValueError("Missing OPENROUTER_API_KEY. Please set it in your environment or .env file.")
            base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
            model_name = os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.3-70b-instruct:free").strip()
            headers: dict[str, str] = {}
            referer = os.getenv("OPENROUTER_HTTP_REFERER", "").strip()
            app_title = os.getenv("OPENROUTER_APP_TITLE", "").strip()
            if referer:
                headers["HTTP-Referer"] = referer
            if app_title:
                headers["X-Title"] = app_title
            default_headers = headers or None
        else:
            raise ValueError(
                "Unsupported MODEL_PROVIDER. Expected 'glm', 'deepseek', 'qwen', 'groq', or 'openrouter'."
            )

        rerank_api_key = os.getenv("RERANK_API_KEY", api_key).strip() or api_key
        rerank_base_url = os.getenv("RERANK_BASE_URL", base_url).rstrip("/") or base_url
        rerank_model_name = os.getenv("RERANK_MODEL", model_name).strip() or model_name
        rerank_default_headers = default_headers

        rerank_headers: dict[str, str] = {}
        rerank_referer = os.getenv("RERANK_HTTP_REFERER", "").strip()
        rerank_app_title = os.getenv("RERANK_APP_TITLE", "").strip()
        if rerank_referer:
            rerank_headers["HTTP-Referer"] = rerank_referer
        if rerank_app_title:
            rerank_headers["X-Title"] = rerank_app_title
        if rerank_headers:
            rerank_default_headers = rerank_headers

        return cls(
            model_provider=provider,
            model_api_key=api_key,
            model_base_url=base_url,
            model_name=model_name,
            default_headers=default_headers,
            rerank_model_api_key=rerank_api_key,
            rerank_model_base_url=rerank_base_url,
            rerank_model_name=rerank_model_name,
            rerank_default_headers=rerank_default_headers,
            request_timeout=float(os.getenv("REQUEST_TIMEOUT", "30")),
            max_results_per_source=int(os.getenv("MAX_RESULTS_PER_SOURCE", "10")),
            docling_accelerator=os.getenv("DOCLING_ACCELERATOR", "AUTO").strip().upper() or "AUTO",
            docling_ocr_backend=os.getenv("DOCLING_OCR_BACKEND", "torch").strip().lower() or "torch",
        )
