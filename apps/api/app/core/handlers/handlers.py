import logging

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.core.handlers.exceptions import (
    DatabaseException,
    FetchScheduleException,
    GroupsDataException,
    ParsingException,
    UrlException,
)

logger = logging.getLogger("uvicorn.error")


async def fetch_schedule_exception_handler(
    _request: Request, exc: Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_502_BAD_GATEWAY,
        content={"detail": str(exc)},
    )


async def parsing_exception_handler(
    _request: Request, exc: Exception
) -> JSONResponse:
    logger.exception("Parsing failure", exc_info=exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal parsing error"},
    )


async def url_exception_handler(
    _request: Request, exc: Exception
) -> JSONResponse:
    logger.exception("Invalid or unknown group ID", exc_info=exc)
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Invalid or unknown group ID"},
    )


async def groups_data_exception_handler(
    _request: Request, exc: Exception
) -> JSONResponse:
    logger.exception("Groups data unavailable", exc_info=exc)
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"detail": "Groups data unavailable"},
    )


async def database_exception_handler(
    _request: Request, exc: Exception
) -> JSONResponse:
    logger.exception("Database unavalible", exc_info=exc)
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"detail": "Database unavailable"},
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        FetchScheduleException, fetch_schedule_exception_handler
    )
    app.add_exception_handler(ParsingException, parsing_exception_handler)
    app.add_exception_handler(UrlException, url_exception_handler)
    app.add_exception_handler(
        GroupsDataException, groups_data_exception_handler
    )
    app.add_exception_handler(DatabaseException, database_exception_handler)
