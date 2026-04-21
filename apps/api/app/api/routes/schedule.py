import json
import logging
from datetime import date
from typing import List

from fastapi import APIRouter

from app.api.deps import Database, GroupId, Groups, HttpClient
from app.core.parser import parse_schedule
from app.core.scraper import fetch_schedule
from app.models import ScheduleEntry
from app.utils.date import get_week_end

router = APIRouter(prefix="/schedule", tags=["schedule"])
logger = logging.getLogger("uvicorn.error")


async def get_schedule(
    id: GroupId, groups_data: Groups, client: HttpClient, redis: Database
) -> List[ScheduleEntry]:
    cache_key = f"schedule:{id}"
    cached = await redis.get(cache_key)
    if cached:
        data = json.loads(cached)
        return [ScheduleEntry(**entry) for entry in data]

    soup = await fetch_schedule(id, groups_data, client)
    schedules_entries = parse_schedule(soup)
    # Push date=null to the bottom of the list
    schedules_entries.sort(key=lambda entry: (entry.date is None, entry.date))

    await redis.set(
        cache_key,
        json.dumps(
            [entry.model_dump(mode="json") for entry in schedules_entries]
        ),
        ex=60 * 60 * 12,
    )

    return schedules_entries


@router.get("/{id}")
async def get_entries(
    id: GroupId, groups_data: Groups, client: HttpClient, redis: Database
) -> List[ScheduleEntry]:
    return await get_schedule(id, groups_data, client, redis)


@router.get("/{id}/by-day")
async def get_entry_by_day(
    id: GroupId,
    groups_data: Groups,
    date: date,
    client: HttpClient,
    redis: Database,
) -> List[ScheduleEntry]:
    schedule_entries = await get_schedule(id, groups_data, client, redis)
    day_entries: List[ScheduleEntry] = [
        entry for entry in schedule_entries if date == entry.date
    ]

    return day_entries


@router.get("/{id}/by-week")
async def get_entries_by_week(
    id: GroupId,
    date: date,
    groups_data: Groups,
    client: HttpClient,
    redis: Database,
) -> List[ScheduleEntry]:
    schedule_entries = await get_schedule(id, groups_data, client, redis)
    week_end = get_week_end(date)
    week_entries: List[ScheduleEntry] = [
        entry
        for entry in schedule_entries
        if entry.date is not None and date <= entry.date <= week_end
    ]

    return week_entries
