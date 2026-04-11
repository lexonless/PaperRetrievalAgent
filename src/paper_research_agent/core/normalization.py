from __future__ import annotations

import re


MATCHING_REPLACEMENTS = (
    ("b-rep", "brep"),
    ("b rep", "brep"),
    ("boundary representation", "brep"),
    ("point cloud", "pointcloud"),
    ("point clouds", "pointclouds"),
)


def normalize_text(value: object, *, for_matching: bool = False) -> str:
    normalized = re.sub(r"\s+", " ", str(value or "")).strip()
    if not for_matching:
        return normalized

    normalized = normalized.lower()
    for source, target in MATCHING_REPLACEMENTS:
        normalized = normalized.replace(source, target)
    normalized = re.sub(r"[^a-z0-9\s]+", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def normalize_string_list(values: object, *, for_matching: bool = False) -> list[str]:
    if not isinstance(values, (list, tuple)):
        return []

    normalized: list[str] = []
    for value in values:
        cleaned = normalize_text(value, for_matching=for_matching)
        if cleaned:
            normalized.append(cleaned)
    return list(dict.fromkeys(normalized))
