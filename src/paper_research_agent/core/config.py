from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


def _build_openrouter_headers(env_prefix: str = "") -> dict[str, str] | None:
    headers: dict[str, str] = {}
    referer = os.getenv(f"{env_prefix}HTTP_REFERER", "").strip()
    app_title = os.getenv(f"{env_prefix}APP_TITLE", "").strip()
    if referer:
        headers["HTTP-Referer"] = referer
    if app_title:
        headers["X-Title"] = app_title
    return headers or None


_PROVIDER_CONFIGS = {
    "glm": {
        "api_key_env": "GLM_API_KEY",
        "env_prefix": "GLM_",
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4.5-air",
    },
    "deepseek": {
        "api_key_env": "DEEPSEEK_API_KEY",
        "env_prefix": "DEEPSEEK_",
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-chat",
    },
    "qwen": {
        "api_key_env": "QWEN_API_KEY",
        "env_prefix": "QWEN_",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-max-latest",
    },
    "groq": {
        "api_key_env": "GROQ_API_KEY",
        "env_prefix": "GROQ_",
        "base_url": "https://api.groq.com/openai/v1",
        "model": "llama-3.3-70b-versatile",
    },
    "openrouter": {
        "api_key_env": "OPENROUTER_API_KEY",
        "env_prefix": "OPENROUTER_",
        "base_url": "https://openrouter.ai/api/v1",
        "model": "meta-llama/llama-3.3-70b-instruct:free",
    },
}


@dataclass(slots=True)
class Settings:
    model_api_key: str
    model_base_url: str
    model_name: str
    default_headers: dict[str, str] | None
    rerank_model_api_key: str
    rerank_model_base_url: str
    rerank_model_name: str
    rerank_default_headers: dict[str, str] | None
    cross_encoder_model: str
    cross_encoder_device: str
    cross_encoder_batch_size: int
    cross_encoder_max_length: int
    request_timeout: float
    max_output_tokens: int
    max_results_per_source: int
    http_proxy: str
    openalex_api_key: str
    unpaywall_email: str

    @classmethod
    def from_env(cls) -> Settings:
        load_dotenv()

        provider = os.getenv("MODEL_PROVIDER", "glm").strip().lower()
        if provider not in _PROVIDER_CONFIGS:
            raise ValueError(
                f"Unsupported MODEL_PROVIDER '{provider}'. "
                f"Expected one of: {', '.join(_PROVIDER_CONFIGS)}."
            )
        cfg = _PROVIDER_CONFIGS[provider]

        api_key = os.getenv(cfg["api_key_env"], "").strip()
        if not api_key:
            raise ValueError(
                f"Missing {cfg['api_key_env']}. Please set it in your environment or .env file."
            )
        prefix = cfg["env_prefix"]
        base_url = os.getenv(f"{prefix}BASE_URL", cfg["base_url"]).rstrip("/")
        model_name = os.getenv(f"{prefix}MODEL", cfg["model"]).strip()

        default_headers = _build_openrouter_headers("OPENROUTER_") if provider == "openrouter" else None

        rerank_api_key = os.getenv("RERANK_API_KEY", api_key).strip() or api_key
        rerank_base_url = os.getenv("RERANK_BASE_URL", base_url).rstrip("/") or base_url
        rerank_model_name = os.getenv("RERANK_MODEL", model_name).strip() or model_name
        rerank_default_headers = default_headers
        if provider == "openrouter":
            rerank_oh = _build_openrouter_headers("RERANK_")
            if rerank_oh:
                rerank_default_headers = rerank_oh

        cross_encoder_model = os.getenv("CROSS_ENCODER_MODEL", "BAAI/bge-reranker-base").strip()
        cross_encoder_device = os.getenv("CROSS_ENCODER_DEVICE", "cpu").strip().lower()
        cross_encoder_batch_size = int(os.getenv("CROSS_ENCODER_BATCH_SIZE", "32"))
        cross_encoder_max_length = int(os.getenv("CROSS_ENCODER_MAX_LENGTH", "512"))

        return cls(
            model_api_key=api_key,
            model_base_url=base_url,
            model_name=model_name,
            default_headers=default_headers,
            rerank_model_api_key=rerank_api_key,
            rerank_model_base_url=rerank_base_url,
            rerank_model_name=rerank_model_name,
            rerank_default_headers=rerank_default_headers,
            cross_encoder_model=cross_encoder_model,
            cross_encoder_device=cross_encoder_device,
            cross_encoder_batch_size=cross_encoder_batch_size,
            cross_encoder_max_length=cross_encoder_max_length,
            request_timeout=float(os.getenv("REQUEST_TIMEOUT", "30")),
            max_results_per_source=int(os.getenv("MAX_RESULTS_PER_SOURCE", "10")),
            max_output_tokens=int(os.getenv("MAX_OUTPUT_TOKENS", "4096")),
            http_proxy=os.getenv("HTTP_PROXY", "").strip(),
            openalex_api_key=os.getenv("OPENALEX_API_KEY", "").strip(),
            unpaywall_email=os.getenv("UNPAYWALL_EMAIL", "").strip(),
        )
