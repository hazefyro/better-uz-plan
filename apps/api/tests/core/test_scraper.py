import httpx
import pytest
import respx

from app.core.handlers.exceptions import FetchScheduleException
from app.core.scraper import async_fetch


@pytest.mark.asyncio
@respx.mock
async def test_async_fetch(client):
    url = httpx.URL("https://example.com/")
    respx.get("https://example.com/").mock(return_value=httpx.Response(200))

    assert await async_fetch(httpx.URL(url), client) is not None


@pytest.mark.asyncio
@respx.mock
async def test_async_fetch_request_error(client):
    url = httpx.URL("https://example.com/")

    respx.get("https://example.com/").mock(
        side_effect=httpx.ConnectError(
            "Connection failed",
            request=httpx.Request("GET", url),
        )
    )

    with pytest.raises(FetchScheduleException):
        await async_fetch(url, client)


@pytest.mark.asyncio
@respx.mock
async def test_async_fetch_http_error(client):
    url = httpx.URL("https://example.com/404")
    respx.get("https://example.com/404").mock(
        return_value=httpx.Response(404, request=httpx.Request("GET", url))
    )

    with pytest.raises(FetchScheduleException, match="HTTP error"):
        await async_fetch(url, client)
