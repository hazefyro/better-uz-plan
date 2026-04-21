from typing import Annotated

import httpx
import redis.asyncio as redis
from fastapi import Depends, Path, Request

from app.config.settings import settings
from app.core.handlers.exceptions import GroupsDataException
from app.models import Group


def get_http_client(request: Request) -> httpx.AsyncClient:
    client: httpx.AsyncClient = request.app.state.http
    return client


def get_groups_data(request: Request) -> dict[str, Group]:
    try:
        groups_data: dict[str, Group] = request.app.state.groups_by_id
    except AttributeError as exc:
        raise GroupsDataException(f"Groups data not loaded properly: {exc}")
    if groups_data is None:
        raise GroupsDataException("Groups data not found")
    return groups_data


def get_redis(request: Request) -> redis.Redis:
    client: redis.Redis = request.app.state.redis
    return client


HttpClient = Annotated[httpx.AsyncClient, Depends(get_http_client)]
Groups = Annotated[dict[str, Group], Depends(get_groups_data)]
GroupId = Annotated[
    str,
    Path(
        min_length=1,
        max_length=settings.LONGEST_ID,
        pattern=r"^\d+$",
        description=f"Numeric group ID, max {settings.LONGEST_ID} digits",
    ),
]
Database = Annotated[redis.Redis, Depends(get_redis)]
