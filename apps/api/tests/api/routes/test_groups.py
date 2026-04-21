from fastapi.testclient import TestClient

from app.main import app


# TODO FIX
# def test_get_groups():
#     with TestClient(app) as client:
#         res = client.get("/api/v1/groups")
#         assert res.status_code == 200
