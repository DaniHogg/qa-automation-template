import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_create_post_returns_201(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    payload = {"title": "QA Test Post", "body": "Automated test body", "userId": 1}
    response = client.post("posts", json=payload, headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_created_status

    created = response.json()
    assert created["title"] == payload["title"]
    assert "id" in created
