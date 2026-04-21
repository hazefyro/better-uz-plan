import pytest_asyncio
from httpx import AsyncClient


@pytest_asyncio.fixture
async def client():
    async with AsyncClient() as client:
        yield client
