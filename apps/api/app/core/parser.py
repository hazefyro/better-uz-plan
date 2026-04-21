from typing import List

from bs4 import BeautifulSoup
from pydantic import ValidationError

from app.config.settings import settings
from app.core.handlers.exceptions import ParsingException
from app.models import Group, ScheduleEntry
from app.utils.date import parse_date, parse_time


def parse_schedule(soup: BeautifulSoup) -> List[ScheduleEntry]:
    table = soup.find(id="table_details")
    if table is None:
        raise ParsingException("Schedule table not found")

    schedule_entries: List[ScheduleEntry] = []

    for row in table.find_all("tr"):
        cells = [cell.text.strip() for cell in row.find_all("td")]

        if len(cells) < 9:
            continue

        try:
            entry = ScheduleEntry(
                date=parse_date(cells[0]),
                # Skipping day
                subGroup=cells[2] or None,
                start=parse_time(cells[3]),
                end=parse_time(cells[4]),
                subject=cells[5] or None,
                type=cells[6] or None,
                teacher=[t.strip() for t in cells[7].split(";") if t.strip()],
                room=cells[8] or None,
            )
        except (ParsingException, IndexError, ValidationError) as exc:
            raise ParsingException(f"Invalid schedule row {cells}: {exc}")

        schedule_entries.append(entry)

    return schedule_entries


def parse_groups(soup: BeautifulSoup) -> List[Group]:
    table = soup.find("table", class_="table table-bordered table-condensed")
    if table is None:
        raise ParsingException("Groups table not found")

    group_entries: List[Group] = []

    for cell in table.find_all("tr"):
        name = cell.text.split(" ")[0].strip()

        if not name:
            raise ParsingException(f"Group row: {cell} does not have name")

        a = cell.find("a", href=True)

        if not a:
            raise ParsingException(f"Group {name} does not have id")

        group_id = str(a.get("href")).split("ID=")[-1]

        if not group_id.isdigit() or len(group_id) > settings.LONGEST_ID:
            raise ParsingException(f"Group: {name} does not have valid id")

        entry = Group(name=name, group_id=group_id)
        group_entries.append(entry)

    return group_entries
