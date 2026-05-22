from __future__ import annotations

from .deadline_rules import calculate_deadlines
from .domain import CaseState
from .field_extractor import extract_fields
from .quality_gate import score_quality, validate_fields
from .router import route_department
from .self_repair import repair_fields


def run_pipeline(raw_text: str) -> dict[str, object]:
    """Run the SRR public reference workflow."""

    state = CaseState(raw_text=raw_text)
    state.fields = extract_fields(raw_text)
    state.missing_fields, state.validation_errors = validate_fields(state.fields)
    state.quality = score_quality(state.missing_fields, state.validation_errors)

    state.fields, state.repair_log = repair_fields(
        state.fields,
        state.missing_fields,
        state.validation_errors,
    )
    if state.repair_log:
        state.missing_fields, state.validation_errors = validate_fields(state.fields)
        state.quality = score_quality(state.missing_fields, state.validation_errors)

    state.fields.update(calculate_deadlines(state.fields))
    state.department_routing = route_department(state.fields)
    return state.public_dict()
