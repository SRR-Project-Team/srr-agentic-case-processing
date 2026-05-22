from __future__ import annotations

import re


FIELD_PATTERNS: dict[str, re.Pattern[str]] = {
    "date_received": re.compile(r"Date Received:\s*(.+)", re.I),
    "source": re.compile(r"Source:\s*(.+)", re.I),
    "case_number": re.compile(r"Case Number:\s*(.+)", re.I),
    "request_type": re.compile(r"Type:\s*(Emergency|Urgent|General)", re.I),
    "caller": re.compile(r"Caller:\s*(.+)", re.I),
    "contact": re.compile(r"Contact:\s*(.+)", re.I),
    "slope_number": re.compile(r"Slope Number:\s*(.+)", re.I),
    "location": re.compile(r"Location:\s*(.+)", re.I),
    "nature_of_request": re.compile(r"Nature of Request:\s*(.+)", re.I),
    "subject_matter": re.compile(r"Subject Matter:\s*(.+)", re.I),
}


def extract_fields(raw_text: str) -> dict[str, str]:
    """Extract public demo fields from a synthetic text case.

    The production project supports PDFs, scans, email text, and structured
    records. This public version keeps the extraction deterministic so the
    repository is safe to run without external services.
    """

    fields: dict[str, str] = {}
    for key, pattern in FIELD_PATTERNS.items():
        match = pattern.search(raw_text)
        if match:
            fields[key] = match.group(1).strip()
    return fields

