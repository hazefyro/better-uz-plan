import httpx
from fastapi import Request
from fastapi.testclient import TestClient

from app.api.deps import get_http_client
from app.main import app


def test_get_http_client():
    with TestClient(app):
        scope = {
            "type": "http",
            "app": app,
        }
        request = Request(scope)

        client = get_http_client(request)

        assert isinstance(client, httpx.AsyncClient)
        assert client is app.state.http
