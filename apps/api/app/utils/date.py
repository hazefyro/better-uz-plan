from datetime import date, datetime, time, timedelta

from app.core.handlers.exceptions import ParsingException


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    value = value.strip()
    try:
        return datetime.fromisoformat(value).date()
    except ValueError as exc:
        raise ParsingException(f"Date parsing error: {exc}")


def parse_time(value: str | None) -> time | None:
    if not value:
        return None
    value = value.strip()
    try:
        return time.fromisoformat(value)
    except ValueError as exc:
        raise ParsingException(f"Time parsing error: {exc}")


def to_monday(date: date) -> date:
    return date - timedelta(days=date.weekday())


def get_week_end(date: date) -> date:
    date = to_monday(date)
    return date + timedelta(days=6)
