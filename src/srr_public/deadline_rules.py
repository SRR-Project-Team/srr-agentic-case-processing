from __future__ import annotations

from datetime import datetime, timedelta


DATE_FORMATS = ("%d-%b-%Y", "%Y-%m-%d", "%d/%m/%Y")
WORKS_DAYS = {"Emergency": 1, "Urgent": 3, "General": 12}


def parse_date(raw: str) -> datetime | None:
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(raw.strip(), fmt)
        except ValueError:
            continue
    return None


def format_date(value: datetime | None) -> str:
    return value.strftime("%d-%b-%Y") if value else ""


def inclusive_offset(days: int) -> int:
    """Business rule used by the demo: day one is the received day."""

    return max(days - 1, 0)


def calculate_deadlines(fields: dict[str, str]) -> dict[str, str]:
    base = parse_date(str(fields.get("date_received") or ""))
    if not base:
        return {}

    request_type = str(fields.get("request_type") or "General").title()
    return {
        "ten_day_due": format_date(base + timedelta(days=inclusive_offset(10))),
        "interim_reply_due": format_date(base + timedelta(days=inclusive_offset(10))),
        "final_reply_due": format_date(base + timedelta(days=21)),
        "works_completion_due": format_date(base + timedelta(days=WORKS_DAYS.get(request_type, 12))),
    }

