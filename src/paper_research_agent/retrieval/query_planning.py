from __future__ import annotations

from ..core.normalization import normalize_string_list, normalize_text

MAX_TERMS_PER_BUCKET = 8


def build_query_entries(
    *,
    topic_phrases: list[str],
    expanded_terms: list[str],
    domain_terms: list[str],
) -> list[dict[str, str]]:
    normalized_topic = _normalize_bucket(topic_phrases)
    normalized_expanded = _normalize_bucket(expanded_terms)
    normalized_domain = _normalize_bucket(domain_terms)

    combined = _normalize_bucket(normalized_topic[:3] + normalized_expanded[:4])
    positive_groups = _build_positive_groups(combined, normalized_domain)

    entries: list[dict[str, str]] = []

    arxiv_recall = _render_arxiv_query(positive_groups[:2])
    if arxiv_recall:
        entries.append({"source": "arXiv", "query": arxiv_recall, "purpose": "recall", "stage": "primary", "notes": "Boolean query for arXiv."})

    oa_precision = _render_openalex_query(positive_groups[:4])
    if oa_precision:
        entries.append({"source": "OpenAlex", "query": oa_precision, "purpose": "precision", "stage": "primary", "notes": "Boolean query for OpenAlex."})

    oa_recall = _render_openalex_query(positive_groups[:3])
    if oa_recall and oa_recall != oa_precision:
        entries.append({"source": "OpenAlex", "query": oa_recall, "purpose": "recall", "stage": "primary", "notes": "Broader OpenAlex recall query."})

    cr_precision = _render_crossref_query(combined, normalized_domain, include_optional=False)
    if cr_precision:
        entries.append({"source": "Crossref", "query": cr_precision, "purpose": "precision", "stage": "primary", "notes": "Keyword query for Crossref fuzzy search."})

    cr_recall = _render_crossref_query(combined, normalized_domain, include_optional=True)
    if cr_recall and cr_recall != cr_precision:
        entries.append({"source": "Crossref", "query": cr_recall, "purpose": "recall", "stage": "primary", "notes": "Broader keyword query for Crossref fuzzy search."})

    deduped: list[dict[str, str]] = []
    seen: set[str] = set()
    for entry in entries:
        key = f"{entry['source']}|{entry['query']}|{entry['purpose']}"
        if key not in seen:
            seen.add(key)
            deduped.append(entry)
    return deduped



def _build_positive_groups(expanded_terms: list[str], domain_terms: list[str]) -> list[list[str]]:
    groups: list[list[str]] = []
    for term in expanded_terms[:4] + domain_terms[:2]:
        groups.append([term])
    return [g for g in groups if g]


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


def _format_phrase(term: str) -> str:
    cleaned = normalize_text(term)
    if not cleaned:
        return ""
    if " " in cleaned or "-" in cleaned:
        return f"\"{cleaned}\""
    return cleaned


def _render_arxiv_query(positive_groups: list[list[str]]) -> str:
    clauses = []
    for group in positive_groups:
        members = [f"all:{_format_phrase(t)}" for t in group if _format_phrase(t)]
        if not members:
            continue
        clauses.append(f"({' OR '.join(members)})" if len(members) > 1 else members[0])
    if not clauses:
        return ""
    return " AND ".join(clauses[:4])


def _render_openalex_query(positive_groups: list[list[str]]) -> str:
    clauses = []
    for group in positive_groups:
        members = [_format_phrase(t) for t in group if _format_phrase(t)]
        if not members:
            continue
        clauses.append(f"({' OR '.join(members)})" if len(members) > 1 else members[0])
    if not clauses:
        return ""
    return " AND ".join(clauses[:4])


def _render_crossref_query(expanded_terms: list[str], domain_terms: list[str], *, include_optional: bool) -> str:
    tokens = list(expanded_terms[:2]) + list(domain_terms[:2])
    if include_optional:
        tokens.extend(domain_terms[2:4])
    return " ".join(_normalize_bucket(tokens, limit=6))
