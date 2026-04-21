import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.main import api_router
from app.api.routes import health
from app.clients.http_client import create_httpx_client
from app.clients.redis_client import create_redis_client
from app.config.settings import settings
from app.core.handlers.exceptions import ParsingException
from app.core.handlers.handlers import register_exception_handlers
from app.core.parser import parse_groups
from app.core.scraper import fetch_groups

logger = logging.getLogger("uvicorn.error")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Connecting to redis")
    redis_client = create_redis_client()
    await redis_client.execute_command("PING")
    app.state.redis = redis_client
    logger.info("Redis connected")

    logger.info("Creating httpx client")
    httpx_client = create_httpx_client()
    app.state.http = httpx_client
    logger.info("Httpx client created")

    logger.info("Loading groups")
    raw_groups = await fetch_groups(httpx_client)
    try:
        groups_data = parse_groups(raw_groups)
        app.state.groups_by_id = {g.group_id: g for g in groups_data}
        logger.info("Groups loaded")

    except ParsingException as exc:
        raise RuntimeError("Failed to load groups at startup") from exc

    yield

    logger.info("Shutting down application")
    await httpx_client.aclose()
    await redis_client.aclose()
    logger.info("Application closed")


app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(health.router)


register_exception_handlers(app)
