from fastapi import APIRouter

from app.api.deps import Groups

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("/")
def get_groups(groups_data: Groups):
    return list(groups_data.values())
