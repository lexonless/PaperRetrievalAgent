from __future__ import annotations

import json
from typing import TypeVar

from pydantic import BaseModel

from .config import Settings


StructuredModelT = TypeVar("StructuredModelT", bound=BaseModel)


def build_chat_model(settings: Settings, *, temperature: float = 0.1, rerank: bool = False):
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=settings.rerank_model_name if rerank else settings.model_name,
        api_key=settings.rerank_model_api_key if rerank else settings.model_api_key,
        base_url=settings.rerank_model_base_url if rerank else settings.model_base_url,
        default_headers=settings.rerank_default_headers if rerank else settings.default_headers,
        timeout=settings.request_timeout,
        temperature=0.0 if rerank else temperature,
        max_tokens=settings.max_output_tokens,
    )


async def invoke_structured_output(
    *,
    model,
    schema: type[StructuredModelT],
    system_prompt: str,
    user_prompt: str,
) -> StructuredModelT:
    from langchain_core.messages import HumanMessage, SystemMessage

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ]

    try:
        structured_model = model.with_structured_output(schema)
        result = await structured_model.ainvoke(messages)
        return coerce_model(schema, result)
    except Exception as exc:
        if not _should_fallback_to_prompt_json(exc):
            raise

    fallback_messages = [
        SystemMessage(content=_build_json_fallback_system_prompt(system_prompt, schema)),
        HumanMessage(content=user_prompt),
    ]
    fallback_result = await model.ainvoke(fallback_messages)
    return coerce_model(schema, _extract_text_content(fallback_result))


def coerce_model(schema: type[StructuredModelT], value: StructuredModelT | BaseModel | dict | str) -> StructuredModelT:
    if isinstance(value, schema):
        return value
    if isinstance(value, BaseModel):
        return schema.model_validate(value.model_dump())
    if isinstance(value, dict):
        return schema.model_validate(value)
    if isinstance(value, str):
        cleaned = _clean_json_text(value)
        try:
            return schema.model_validate_json(cleaned)
        except Exception:
            repaired = _repair_truncated_json(cleaned)
            return schema.model_validate_json(repaired)
    raise TypeError(f"Cannot coerce {type(value)!r} into {schema.__name__}")


def _repair_truncated_json(text: str) -> str:
    text = text.rstrip(",\n\r ")
    open_braces = text.count("{") - text.count("}")
    open_brackets = text.count("[") - text.count("]")
    return text + "]" * open_brackets + "}" * open_braces


def _clean_json_text(value: str) -> str:
    cleaned = value.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.lstrip("`")
        if "\n" in cleaned:
            cleaned = cleaned.split("\n", 1)[1]
        cleaned = cleaned.rsplit("```", 1)[0]
    return cleaned.strip()


def _build_json_fallback_system_prompt(system_prompt: str, schema: type[StructuredModelT]) -> str:
    schema_json = json.dumps(schema.model_json_schema(), ensure_ascii=False, indent=2)
    return (
        f"{system_prompt}\n\n"
        "Return exactly one valid JSON object and nothing else.\n"
        "Do not use markdown code fences.\n"
        "The JSON must satisfy this schema:\n"
        f"{schema_json}"
    )


def _should_fallback_to_prompt_json(exc: Exception) -> bool:
    message = str(exc).lower()
    return "response_format" in message or "structured output" in message or "json_schema" in message


def _extract_text_content(value) -> str:
    content = getattr(value, "content", value)
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        text_parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                text_parts.append(item)
                continue
            if isinstance(item, dict):
                text = item.get("text")
                if isinstance(text, str):
                    text_parts.append(text)
        return "\n".join(part for part in text_parts if part).strip()
    return str(content)
