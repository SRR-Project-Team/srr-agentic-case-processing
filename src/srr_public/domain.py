from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


REQUIRED_FIELDS = (
    "date_received",
    "source",
    "case_number",
    "request_type",
    "location",
    "nature_of_request",
    "subject_matter",
)


@dataclass
class CaseState:
    """Shared state passed between processing abilities."""

    raw_text: str
    fields: dict[str, Any] = field(default_factory=dict)
    validation_errors: list[str] = field(default_factory=list)
    missing_fields: list[str] = field(default_factory=list)
    department_routing: dict[str, Any] = field(default_factory=dict)
    quality: dict[str, Any] = field(default_factory=dict)
    repair_log: list[dict[str, Any]] = field(default_factory=list)

    def public_dict(self) -> dict[str, Any]:
        return {
            "fields": self.fields,
            "validation_errors": self.validation_errors,
            "missing_fields": self.missing_fields,
            "department_routing": self.department_routing,
            "quality": self.quality,
            "repair_log": self.repair_log,
        }
