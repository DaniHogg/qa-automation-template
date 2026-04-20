import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_create_post_returns_201(api_headers):
    client = HttpClient()
    payload = {"title": "QA Test Post", "body": "Automated test body", "userId": 1}
    response = client.post("posts", json=payload, headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 201

    created = response.json()
    assert created["title"] == payload["title"]
    assert "id" in created
