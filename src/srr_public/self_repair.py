from __future__ import annotations

from typing import Any


SUBJECT_NORMALIZATION = {
    "fallen branch": "Fallen Tree",
    "branch may fall": "Hazardous Tree",
    "tree trim": "Tree Trimming",
    "tree trimming": "Tree Trimming",
    "pruning": "Tree Trimming",
    "surface erosion": "Surface Erosion",
}


def repair_fields(fields: dict[str, Any], missing: list[str], errors: list[str]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Apply deterministic, explainable repairs for public demo cases."""

    repaired = dict(fields)
    log: list[dict[str, Any]] = []

    subject = str(repaired.get("subject_matter") or "").strip()
    subject_lower = subject.lower()
    for keyword, normalized in SUBJECT_NORMALIZATION.items():
        if keyword in subject_lower and subject != normalized:
            repaired["subject_matter"] = normalized
            log.append({
                "strategy": "normalize_subject_matter",
                "before": subject,
                "after": normalized,
            })
            break

    if "request_type" in missing:
        text = " ".join(str(value).lower() for value in repaired.values())
        inferred = "Urgent" if "urgent" in text or "hazard" in text else "General"
        repaired["request_type"] = inferred
        log.append({
            "strategy": "infer_request_type",
            "after": inferred,
        })

    if errors:
        log.append({
            "strategy": "flag_remaining_errors",
            "errors": errors,
            "next_step": "human_review",
        })

    return repaired, log

