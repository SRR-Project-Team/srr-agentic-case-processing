from __future__ import annotations


ROUTING_RULES = (
    ("hazardous tree", "Tree Management Team", 0.93),
    ("fallen tree", "Tree Management Team", 0.91),
    ("tree trimming", "Tree Management Team", 0.88),
    ("pruning", "Tree Management Team", 0.88),
    ("slope", "Slope Safety Team", 0.86),
    ("erosion", "Slope Safety Team", 0.84),
    ("blocked drain", "Drainage Liaison Team", 0.82),
)


def route_department(fields: dict[str, str]) -> dict[str, object]:
    text = " ".join(
        str(fields.get(key, ""))
        for key in ("nature_of_request", "subject_matter", "location")
    ).lower()

    for keyword, department, confidence in ROUTING_RULES:
        if keyword in text:
            return {
                "department": department,
                "confidence": confidence,
                "matched_rule": keyword,
            }

    return {
        "department": "Manual Review Queue",
        "confidence": 0.35,
        "matched_rule": "fallback",
    }
