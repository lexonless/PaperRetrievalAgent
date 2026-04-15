from __future__ import annotations

from typing import Iterable

from ..core.models import QueryAliasGroup
from ..core.models import SourceQuerySpec
from ..core.models import TaskQueryIR
from ..core.models import TaskQueryIRUpdate
from ..core.models import TaskQueryPlan
from ..core.normalization import normalize_string_list, normalize_text


KNOWN_ALIAS_MAP = {
    normalize_text("b-rep", for_matching=True): ["brep", "boundary representation"],
    normalize_text("brep", for_matching=True): ["b-rep", "boundary representation"],
    normalize_text("boundary representation", for_matching=True): ["b-rep", "brep"],
    normalize_text("graph neural network", for_matching=True): ["gnn"],
    normalize_text("variational autoencoder", for_matching=True): ["vae"],
    normalize_text("point cloud", for_matching=True): ["point clouds", "3d scan", "3d scans"],
    normalize_text("program synthesis", for_matching=True): ["cad program"],
}

MAX_TERMS_PER_BUCKET = 8
MAX_ALIASES_PER_GROUP = 6


def build_query_plan(query_plan_payload: TaskQueryPlan | dict) -> TaskQueryPlan:
    query_plan = query_plan_payload if isinstance(query_plan_payload, TaskQueryPlan) else TaskQueryPlan.model_validate(query_plan_payload or {})
    normalized_ir = normalize_query_ir(_coerce_query_ir(query_plan))
    rendered_queries = render_source_query_specs(normalized_ir)
    primary_queries = derive_primary_queries(normalized_ir)
    semantic_core_terms = derive_semantic_core_terms(normalized_ir)
    return query_plan.model_copy(
        update={
            "query_ir": normalized_ir,
            "rendered_queries": rendered_queries,
            "primary_queries": primary_queries,
            "semantic_core_terms": semantic_core_terms,
        }
    )


def apply_query_ir_update(base_ir_payload: TaskQueryIR | dict, update_payload: TaskQueryIRUpdate | dict) -> TaskQueryIR:
    base_ir = base_ir_payload if isinstance(base_ir_payload, TaskQueryIR) else TaskQueryIR.model_validate(base_ir_payload or {})
    update = update_payload if isinstance(update_payload, TaskQueryIRUpdate) else TaskQueryIRUpdate.model_validate(update_payload or {})
    merged = base_ir.model_dump()
    for key, value in update.model_dump(exclude_none=True).items():
        merged[key] = value
    return normalize_query_ir(TaskQueryIR.model_validate(merged))


def normalize_query_ir(query_ir_payload: TaskQueryIR | dict) -> TaskQueryIR:
    query_ir = query_ir_payload if isinstance(query_ir_payload, TaskQueryIR) else TaskQueryIR.model_validate(query_ir_payload or {})
    normalized_groups = _normalize_alias_groups(query_ir.alias_groups)
    bucket_values = {
        "topic_phrases": _normalize_bucket(query_ir.topic_phrases),
        "method_terms": _normalize_bucket(query_ir.method_terms),
        "optional_terms": _normalize_bucket(query_ir.optional_terms),
        "excluded_terms": _normalize_bucket(query_ir.excluded_terms),
    }
    alias_groups_by_canonical = {normalize_text(group.canonical, for_matching=True): group for group in normalized_groups if normalize_text(group.canonical, for_matching=True)}
    for bucket_name in ("topic_phrases", "method_terms", "optional_terms", "excluded_terms"):
        expanded_values = list(bucket_values[bucket_name])
        for term in bucket_values[bucket_name]:
            key = normalize_text(term, for_matching=True)
            known_aliases = KNOWN_ALIAS_MAP.get(key, [])
            if known_aliases:
                expanded_values.extend(known_aliases)
            existing_group = alias_groups_by_canonical.get(key)
            if existing_group is not None:
                expanded_values.extend(existing_group.aliases)
            elif known_aliases:
                alias_groups_by_canonical[key] = QueryAliasGroup(canonical=term, aliases=_normalize_bucket(known_aliases, limit=MAX_ALIASES_PER_GROUP))
        bucket_values[bucket_name] = _normalize_bucket(expanded_values)
    normalized_groups = [
        QueryAliasGroup(canonical=group.canonical, aliases=_normalize_bucket(group.aliases, limit=MAX_ALIASES_PER_GROUP))
        for group in alias_groups_by_canonical.values()
        if normalize_text(group.canonical)
    ]
    return TaskQueryIR(
        topic_phrases=bucket_values["topic_phrases"],
        method_terms=bucket_values["method_terms"],
        optional_terms=bucket_values["optional_terms"],
        excluded_terms=bucket_values["excluded_terms"],
        alias_groups=normalized_groups[:MAX_TERMS_PER_BUCKET],
    )


def _coerce_query_ir(query_plan: TaskQueryPlan) -> TaskQueryIR:
    if any(
        [
            query_plan.query_ir.topic_phrases,
            query_plan.query_ir.method_terms,
            query_plan.query_ir.optional_terms,
            query_plan.query_ir.excluded_terms,
            query_plan.query_ir.alias_groups,
        ]
    ):
        return query_plan.query_ir
    return TaskQueryIR(
        topic_phrases=list(query_plan.primary_queries[:3]),
        optional_terms=list(query_plan.semantic_core_terms[:4]),
    )


def render_source_query_specs(query_ir_payload: TaskQueryIR | dict) -> list[SourceQuerySpec]:
    query_ir = normalize_query_ir(query_ir_payload)
    positive_groups = _build_positive_groups(query_ir)
    excluded_terms = query_ir.excluded_terms[:6]
    specs: list[SourceQuerySpec] = []

    arxiv_precision = _render_arxiv_query(positive_groups[:4], excluded_terms)
    if arxiv_precision:
        specs.append(SourceQuerySpec(source="arXiv", query=arxiv_precision, purpose="precision", stage="primary", notes="Structured boolean query rendered for arXiv."))
    arxiv_recall = _render_arxiv_query(positive_groups[:2], [])
    if arxiv_recall and arxiv_recall != arxiv_precision:
        specs.append(SourceQuerySpec(source="arXiv", query=arxiv_recall, purpose="recall", stage="primary", notes="Broader arXiv recall query rendered from the query IR."))

    openalex_precision = _render_openalex_query(positive_groups[:4], excluded_terms)
    if openalex_precision:
        specs.append(SourceQuerySpec(source="OpenAlex", query=openalex_precision, purpose="precision", stage="primary", notes="Boolean query rendered for OpenAlex search syntax."))
    openalex_recall = _render_openalex_query(positive_groups[:3], [])
    if openalex_recall and openalex_recall != openalex_precision:
        specs.append(SourceQuerySpec(source="OpenAlex", query=openalex_recall, purpose="recall", stage="primary", notes="Broader OpenAlex recall query rendered from the query IR."))

    crossref_precision = _render_crossref_query(query_ir, include_optional=False)
    if crossref_precision:
        specs.append(SourceQuerySpec(source="Crossref", query=crossref_precision, purpose="precision", stage="primary", notes="Compact keyword query rendered for Crossref fuzzy search."))
    crossref_recall = _render_crossref_query(query_ir, include_optional=True)
    if crossref_recall and crossref_recall != crossref_precision:
        specs.append(SourceQuerySpec(source="Crossref", query=crossref_recall, purpose="recall", stage="primary", notes="Broader keyword query rendered for Crossref fuzzy search."))

    deduped: list[SourceQuerySpec] = []
    seen: set[str] = set()
    for spec in specs:
        key = spec.model_dump_json()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(spec)
    return deduped


def derive_primary_queries(query_ir_payload: TaskQueryIR | dict) -> list[str]:
    query_ir = normalize_query_ir(query_ir_payload)
    candidates = [
        " ".join(query_ir.topic_phrases[:2] + query_ir.method_terms[:2] + query_ir.optional_terms[:2]),
        " ".join(query_ir.topic_phrases[:1] + query_ir.method_terms[:2] + query_ir.optional_terms[:2]),
    ]
    return _normalize_bucket(candidates)


def derive_semantic_core_terms(query_ir_payload: TaskQueryIR | dict) -> list[str]:
    query_ir = normalize_query_ir(query_ir_payload)
    values = [
        *query_ir.method_terms,
        *query_ir.topic_phrases,
        *query_ir.optional_terms,
    ]
    return _normalize_bucket(values)


def _normalize_alias_groups(groups: Iterable[QueryAliasGroup]) -> list[QueryAliasGroup]:
    normalized_groups: list[QueryAliasGroup] = []
    for group in groups:
        canonical = normalize_text(group.canonical)
        if not canonical:
            continue
        aliases = _normalize_bucket(group.aliases, limit=MAX_ALIASES_PER_GROUP)
        normalized_groups.append(QueryAliasGroup(canonical=canonical, aliases=[alias for alias in aliases if normalize_text(alias, for_matching=True) != normalize_text(canonical, for_matching=True)]))
    return normalized_groups


def _normalize_bucket(values: object, *, limit: int = MAX_TERMS_PER_BUCKET) -> list[str]:
    cleaned = []
    for value in normalize_string_list(values):
        normalized = normalize_text(value)
        if not normalized:
            continue
        if len(normalized.split()) > 8:
            continue
        cleaned.append(normalized)
    return list(dict.fromkeys(cleaned))[:limit]


def _build_positive_groups(query_ir: TaskQueryIR) -> list[list[str]]:
    positive_groups: list[list[str]] = []
    for term in [*query_ir.topic_phrases[:3], *query_ir.method_terms[:2], *query_ir.optional_terms[:3]]:
        aliases = _aliases_for_term(query_ir, term)
        positive_groups.append(_normalize_bucket([term, *aliases], limit=3))
    return [group for group in positive_groups if group]


def _aliases_for_term(query_ir: TaskQueryIR, term: str) -> list[str]:
    key = normalize_text(term, for_matching=True)
    aliases = list(KNOWN_ALIAS_MAP.get(key, []))
    for group in query_ir.alias_groups:
        if normalize_text(group.canonical, for_matching=True) == key:
            aliases.extend(group.aliases)
    return _normalize_bucket(aliases, limit=MAX_ALIASES_PER_GROUP)


def _format_phrase(term: str) -> str:
    cleaned = normalize_text(term)
    if not cleaned:
        return ""
    if " " in cleaned or "-" in cleaned:
        return f"\"{cleaned}\""
    return cleaned


def _render_arxiv_query(positive_groups: list[list[str]], excluded_terms: list[str]) -> str:
    clauses = []
    for group in positive_groups:
        members = [f"all:{_format_phrase(term)}" for term in group if _format_phrase(term)]
        if not members:
            continue
        clauses.append(f"({' OR '.join(members)})" if len(members) > 1 else members[0])
    if not clauses:
        return ""
    query = " AND ".join(clauses[:4])
    for term in excluded_terms:
        formatted = _format_phrase(term)
        if formatted:
            query = f"{query} ANDNOT all:{formatted}"
    return query


def _render_openalex_query(positive_groups: list[list[str]], excluded_terms: list[str]) -> str:
    clauses = []
    for group in positive_groups:
        members = [_format_phrase(term) for term in group if _format_phrase(term)]
        if not members:
            continue
        clauses.append(f"({' OR '.join(members)})" if len(members) > 1 else members[0])
    if not clauses:
        return ""
    query = " AND ".join(clauses[:4])
    negative_members = [_format_phrase(term) for term in excluded_terms if _format_phrase(term)]
    if negative_members:
        query = f"{query} NOT ({' OR '.join(negative_members)})"
    return query


def _render_crossref_query(query_ir: TaskQueryIR, *, include_optional: bool) -> str:
    tokens = [
        *query_ir.topic_phrases[:2],
        *query_ir.method_terms[:2],
    ]
    if include_optional:
        tokens.extend(query_ir.optional_terms[:2])
    return " ".join(_normalize_bucket(tokens, limit=6))
