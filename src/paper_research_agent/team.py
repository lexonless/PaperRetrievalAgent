from __future__ import annotations

import json
import re
from typing import Sequence

from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.messages import BaseAgentEvent, BaseChatMessage
from autogen_agentchat.teams import SelectorGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

from .agent import (
    MAX_REVIEW_REVISIONS,
    PLANNER_NAME,
    RETRIEVAL_NAME,
    REVIEWER_NAME,
    WRITER_NAME,
    build_planner_agent,
    build_retrieval_agent,
    build_reviewer_agent,
    build_writer_agent,
)
from .normalization import normalize_string_list, normalize_text
from .toolkit import PaperSearchToolkit


SELECTOR_FALLBACK_PROMPT = "Select exactly one next agent from {participants}."
FALLBACK_STOPWORDS = {"a", "an", "and", "are", "for", "from", "into", "of", "on", "or", "the", "to", "using", "via", "with"}


def build_paper_search_team(
    model_client: OpenAIChatCompletionClient,
    toolkit: PaperSearchToolkit,
) -> SelectorGroupChat:
    planner_agent = build_planner_agent(model_client)
    retrieval_agent = build_retrieval_agent(model_client, toolkit)
    reviewer_agent = build_reviewer_agent(model_client)
    writer_agent = build_writer_agent(model_client)

    termination = TextMentionTermination("TERMINATE") | MaxMessageTermination(max_messages=20)

    return SelectorGroupChat(
        [planner_agent, retrieval_agent, reviewer_agent, writer_agent],
        model_client=model_client,
        termination_condition=termination,
        selector_prompt=SELECTOR_FALLBACK_PROMPT,
        allow_repeated_speaker=True,
        selector_func=lambda messages: _selector_func(messages, toolkit),
    )


def _selector_func(
    messages: Sequence[BaseAgentEvent | BaseChatMessage],
    toolkit: PaperSearchToolkit,
) -> str | None:
    if not messages:
        return PLANNER_NAME

    last_source = getattr(messages[-1], "source", "")
    if last_source == "user":
        return PLANNER_NAME
    if last_source == PLANNER_NAME:
        planner_payload = _latest_payload(messages, PLANNER_NAME)
        if planner_payload is not None:
            toolkit.set_latest_retrieval_request(_build_retrieval_request(planner_payload))
        return RETRIEVAL_NAME
    if last_source == RETRIEVAL_NAME:
        return REVIEWER_NAME
    if last_source == REVIEWER_NAME:
        if _has_pass_decision(messages):
            return WRITER_NAME
        if _count_revise_decisions(messages) >= MAX_REVIEW_REVISIONS:
            return WRITER_NAME
        return PLANNER_NAME
    return None


def _has_pass_decision(messages: Sequence[BaseAgentEvent | BaseChatMessage]) -> bool:
    review = _parse_review_payload(messages[-1])
    if review is None:
        return False
    retrieval = _latest_payload(messages, RETRIEVAL_NAME)
    return _review_passes_programmatic_validation(review, retrieval)


def _count_revise_decisions(messages: Sequence[BaseAgentEvent | BaseChatMessage]) -> int:
    count = 0
    for message in messages:
        if getattr(message, "source", "") != REVIEWER_NAME:
            continue
        review = _parse_review_payload(message)
        if review is not None and str(review.get("decision", "")).upper() == "REVISE":
            count += 1
    return count


def _parse_review_payload(message: BaseAgentEvent | BaseChatMessage) -> dict | None:
    return _parse_json_content(getattr(message, "content", ""))


def _review_passes_programmatic_validation(review: dict, retrieval: dict | None) -> bool:
    if str(review.get("decision", "")).upper() != "PASS":
        return False

    scores = review.get("scores")
    if not isinstance(scores, dict):
        return False

    score_keys = [
        "coverage_score",
        "relevance_score",
        "metadata_score",
        "diversity_score",
        "evidence_score",
    ]
    score_values: list[int] = []
    for key in score_keys:
        value = scores.get(key)
        if not isinstance(value, int):
            return False
        if value < 0 or value > 2:
            return False
        score_values.append(value)

    if any(value == 0 for value in score_values):
        return False
    if sum(score_values) < 8:
        return False

    hard_requirements = review.get("hard_requirements")
    if not isinstance(hard_requirements, dict):
        return False

    requirement_keys = [
        "source_coverage",
        "candidate_depth",
        "relevance",
        "query_fit",
        "core_method_fit",
        "time_consistency",
    ]
    for key in requirement_keys:
        item = hard_requirements.get(key)
        if not isinstance(item, dict):
            return False
        if item.get("passed") is not True:
            return False

    if retrieval is None:
        return False
    if not _retrieval_supports_pass(retrieval):
        return False

    return True


def _latest_payload(messages: Sequence[BaseAgentEvent | BaseChatMessage], source_name: str) -> dict | None:
    for message in reversed(messages):
        if getattr(message, "source", "") != source_name:
            continue
        payload = _parse_json_content(getattr(message, "content", ""))
        if payload is not None:
            return payload
    return None


def _parse_json_content(content: object) -> dict | None:
    if isinstance(content, dict):
        return content
    if not isinstance(content, str):
        return None
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def _retrieval_supports_pass(retrieval: dict) -> bool:
    sources = retrieval.get("sources_used")
    papers = retrieval.get("papers")
    if not isinstance(sources, list) or not isinstance(papers, list):
        return False

    distinct_sources = {str(source).strip() for source in sources if str(source).strip()}
    if len(distinct_sources) < 2:
        return False

    paper_dicts = [paper for paper in papers if isinstance(paper, dict)]
    if len(paper_dicts) < 5:
        return False

    allowed_verification = {"verified", "partial", "weak"}
    allowed_evidence = {"abstract", "excerpt", "title_only"}
    allowed_time = {"in_range", "out_of_range", "unknown"}

    in_range_count = 0
    supported_evidence_count = 0

    for paper in paper_dicts:
        verification_status = str(paper.get("verification_status", "")).strip().lower()
        evidence_level = str(paper.get("evidence_level", "")).strip().lower()
        time_range_status = str(paper.get("time_range_status", "")).strip().lower()
        evidence_snippets = paper.get("evidence_snippets")

        if verification_status not in allowed_verification:
            return False
        if evidence_level not in allowed_evidence:
            return False
        if time_range_status not in allowed_time:
            return False
        if not isinstance(evidence_snippets, list):
            return False
        if evidence_level == "title_only" and evidence_snippets:
            return False
        if evidence_level == "title_only" and verification_status != "weak":
            return False

        if time_range_status == "in_range":
            in_range_count += 1
        if (
            verification_status in {"partial", "verified"}
            and evidence_level in {"abstract", "excerpt"}
            and any(str(item).strip() for item in evidence_snippets)
        ):
            supported_evidence_count += 1

    if in_range_count < 5:
        return False
    if supported_evidence_count < 3:
        return False

    return True


def _build_retrieval_request(planner_payload: dict) -> dict:
    time_range = planner_payload.get("time_range")
    from_year = None
    end_year = None
    if isinstance(time_range, dict):
        start_year = time_range.get("start_year")
        end_year_value = time_range.get("end_year")
        if isinstance(start_year, int):
            from_year = start_year
        if isinstance(end_year_value, int):
            end_year = end_year_value

    planned_queries = _extract_queries(planner_payload.get("queries"))
    topic = normalize_text(planner_payload.get("topic", ""))
    user_intent = normalize_text(planner_payload.get("user_intent", ""))
    focus_areas = normalize_string_list(planner_payload.get("focus_areas"))
    exclude_areas = normalize_string_list(planner_payload.get("exclude_areas"))
    fallback_queries = normalize_string_list(planner_payload.get("fallback_queries"))[:3]
    if not fallback_queries:
        fallback_queries = _build_fallback_queries(topic, planned_queries)
    return {
        "from_year": from_year,
        "end_year": end_year,
        "topic": topic,
        "user_intent": user_intent,
        "focus_areas": focus_areas,
        "exclude_areas": exclude_areas,
        "planned_queries": planned_queries,
        "fallback_queries": fallback_queries,
        "planner_query_source": {
            "fallback_queries": fallback_queries,
        },
    }


def _extract_queries(raw_items: object) -> list[str]:
    if not isinstance(raw_items, list):
        return []

    normalized_items: list[str] = []
    seen_queries: set[str] = set()
    for item in raw_items:
        if not isinstance(item, dict):
            continue
        query = normalize_text(item.get("query", ""))
        if not query or query in seen_queries:
            continue
        seen_queries.add(query)
        normalized_items.append(query)
    return normalized_items


def _build_fallback_queries(topic: str, planned_queries: list[str]) -> list[str]:
    tokens: list[str] = []
    for text in [topic, *planned_queries]:
        for token in re.findall(r"[a-z0-9]+", text.lower()):
            if token in FALLBACK_STOPWORDS or len(token) < 3:
                continue
            if token not in tokens:
                tokens.append(token)

    fallback_queries: list[str] = []
    for width in (5, 4, 3):
        query = " ".join(tokens[:width]).strip()
        if query and query not in fallback_queries:
            fallback_queries.append(query)
        if len(fallback_queries) >= 3:
            break
    return fallback_queries
