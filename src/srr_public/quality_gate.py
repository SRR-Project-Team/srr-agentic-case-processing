from __future__ import annotations

import re
from datetime import datetime
from typing import Any

from .domain import REQUIRED_FIELDS


DATE_FORMATS = ("%d-%b-%Y", "%Y-%m-%d", "%d/%m/%Y")
REQUEST_TYPES = {"Emergency", "Urgent", "General"}
SLOPE_PATTERN = re.compile(r"^\d{1,2}[A-Z]{2,3}[-/][A-Z0-9/()\-]+$")


def _parse_date(value: str) -> bool:
    for fmt in DATE_FORMATS:
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            continue
    return False


def validate_fields(fields: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Return missing fields and rule-level validation errors."""

    missing = [key for key in REQUIRED_FIELDS if not fields.get(key)]
    errors: list[str] = []

    date_received = str(fields.get("date_received") or "").strip()
    if date_received and not _parse_date(date_received):
        errors.append("format:date_received must be dd-MMM-yyyy, yyyy-mm-dd, or dd/mm/yyyy")

    request_type = str(fields.get("request_type") or "").strip().title()
    if request_type and request_type not in REQUEST_TYPES:
        errors.append(f"enum:request_type must be one of {sorted(REQUEST_TYPES)}")

    slope_number = str(fields.get("slope_number") or "").strip().upper()
    if slope_number and not SLOPE_PATTERN.match(slope_number):
        errors.append("format:slope_number does not match the public SRR demo pattern")

    return missing, errors


def score_quality(missing: list[str], errors: list[str]) -> dict[str, Any]:
    required_count = len(REQUIRED_FIELDS)
    coverage = (required_count - len(missing)) / required_count
    penalty = min(0.4, 0.1 * len(errors))
    score = max(0.0, round(coverage - penalty, 3))
    if score >= 0.85:
        level = "pass"
    elif score >= 0.55:
        level = "repair"
    else:
        level = "human_review"
    return {"score": score, "level": level, "coverage": round(coverage, 3)}

