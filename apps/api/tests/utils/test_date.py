from datetime import date

import pytest

from app.core.handlers.exceptions import ParsingException
from app.utils.date import (
    get_week_end,
    parse_date,
    parse_time,
    to_monday,
)


def test_parse_date():
    assert parse_date("2023-10-10") is not None


def test_parse_date_invalid():
    with pytest.raises(ParsingException):
        parse_date("2043-30-40")


def test_parse_date_none():
    assert parse_date(None) is None


def test_parse_time():
    assert parse_time("10:35") is not None


def test_parse_time_invalid():
    with pytest.raises(ParsingException):
        parse_time("100:75")


def test_parse_time_none():
    assert parse_time(None) is None


def test_to_monday():
    assert to_monday(date(2026, 3, 4)) == date(2026, 3, 2)


def test_get_week_end():
    assert get_week_end(date(2026, 3, 2)) == date(2026, 3, 8)
