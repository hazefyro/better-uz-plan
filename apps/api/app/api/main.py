from fastapi import APIRouter

from app.api.routes import groups, schedule

api_router = APIRouter()

api_router.include_router(schedule.router)
api_router.include_router(groups.router)
