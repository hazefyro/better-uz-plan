import httpx
import pytest

from app.config.settings import settings
from app.core.handlers.exceptions import UrlException
from app.models import Group
from app.utils.id import get_url_by_id

raw_mock = [
    {"group_id": "30560", "name": "INF1"},
    {"group_id": "30561", "name": "INF2"},
]
raw_data = [Group.model_validate(g) for g in raw_mock]
MOCK_DATA = {g.group_id: g for g in raw_data}


def test_get_url_by_id():
    assert get_url_by_id("30560", MOCK_DATA) == httpx.URL(
        f"{settings.SCHEDULE_LINK}30560"
    )


def test_get_url_by_id_none():
    with pytest.raises(UrlException):
        get_url_by_id("34328", MOCK_DATA)


def test_get_url_by_id_invalid():
    with pytest.raises(UrlException):
        get_url_by_id("invalid", MOCK_DATA)
