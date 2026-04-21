import httpx

from app.config.settings import settings
from app.core.handlers.exceptions import UrlException
from app.models import Group


def get_url_by_id(id: str, groups_data: dict[str, Group]) -> httpx.URL:
    if not id.isdigit() or len(id) > settings.LONGEST_ID:
        raise UrlException("Invalid ID.")

    group = groups_data.get(id)

    if group is None:
        raise UrlException(
            "The provided ID does not map to a valid URL."
        )

    return httpx.URL(f"{settings.SCHEDULE_LINK}{group.group_id}")
