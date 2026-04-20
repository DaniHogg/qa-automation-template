import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_update_post_returns_200(api_headers):
    client = HttpClient()
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    response = client.put("posts/1", json=payload, headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    updated = response.json()
    assert updated["title"] == "Updated Title"
