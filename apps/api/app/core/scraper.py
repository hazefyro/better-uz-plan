import httpx
from bs4 import BeautifulSoup

from app.config.settings import settings
from app.core.handlers.exceptions import (
    FetchScheduleException,
)
from app.models import Group
from app.utils.id import get_url_by_id


async def async_fetch(
    url: httpx.URL, client: httpx.AsyncClient
) -> BeautifulSoup:
    try:
        response = await client.get(url)
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise FetchScheduleException(f"HTTP error: {exc}")
    except httpx.RequestError as exc:
        raise FetchScheduleException(f"Request error: {exc}")

    return BeautifulSoup(response.text, "html.parser")


async def fetch_schedule(
    id: str, groups_data: dict[str, Group], client: httpx.AsyncClient
) -> BeautifulSoup:
    url = get_url_by_id(id, groups_data)

    soup = await async_fetch(url, client)

    return soup


async def fetch_groups(client: httpx.AsyncClient) -> BeautifulSoup:
    url = settings.SUPPORTED_MAJOR

    soup = await async_fetch(url, client)

    return soup
