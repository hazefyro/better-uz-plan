import datetime

import pytest
from bs4 import BeautifulSoup

from app.core.handlers.exceptions import ParsingException
from app.core.parser import parse_groups, parse_schedule
from app.models import Group, ScheduleEntry
from tests.mocks.mock_html import (
    INVALID_MOCK_GROUP_HTML,
    INVALID_MOCK_SCHEDULE,
    MOCK_GROUP_HTML,
    MOCK_SCHEDULE_HTML,
)


def test_schedule_parser():
    soup = BeautifulSoup(MOCK_SCHEDULE_HTML, "html.parser")

    expected = [
        ScheduleEntry(
            date=datetime.date(2026, 3, 4),
            subGroup=None,
            start=datetime.time(9, 15),
            end=datetime.time(10, 45),
            subject="Podstawy informatyki II",
            type="Ć",
            teacher=["dr hab. inż. Piotr Borowiecki, prof. UZ"],
            room="110/111 A-2",
        ),
        ScheduleEntry(
            date=datetime.date(2026, 3, 4),
            subGroup=None,
            start=datetime.time(12, 45),
            end=datetime.time(14, 15),
            subject="Podstawy analizy danych",
            type="W",
            teacher=["prof. dr hab. inż. Dariusz Uciński"],
            room="H044 A-10",
        ),
        ScheduleEntry(
            date=datetime.date(2026, 3, 4),
            subGroup=None,
            start=datetime.time(14, 30),
            end=datetime.time(15, 55),
            subject="Fizyka",
            type="W",
            teacher=["dr Stefan Jerzyniak"],
            room="106 A-29",
        ),
    ]

    assert parse_schedule(soup) == expected


def test_schedule_parser_none_table():
    soup = BeautifulSoup(
        """
    <html></html>
    """,
        features="html.parser",
    )

    with pytest.raises(ParsingException):
        parse_schedule(soup)


def test_schedule_parser_invalid_table():
    soup = BeautifulSoup(
        INVALID_MOCK_SCHEDULE,
        features="html.parser",
    )

    with pytest.raises(ParsingException):
        parse_schedule(soup)


def test_groups_parser():
    soup = BeautifulSoup(MOCK_GROUP_HTML, "html.parser")

    expected = [
        Group(name="11INF-SD(L)", group_id="30551"),
        Group(name="11INF-SP", group_id="30552"),
        Group(name="12INF-SD(L)", group_id="30553"),
        Group(name="12INF-SP", group_id="30554"),
        Group(name="13INF-SP", group_id="30555"),
    ]

    assert parse_groups(soup) == expected


def test_groups_parser_none_table():
    soup = BeautifulSoup("<html></html>", "html.parser")

    with pytest.raises(ParsingException):
        parse_groups(soup)


def test_groups_parser_none_id():
    soup = BeautifulSoup(INVALID_MOCK_GROUP_HTML, "html.parser")

    with pytest.raises(ParsingException):
        parse_groups(soup)
