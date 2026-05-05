import pytest

from clients.http_client import HttpClient
from core.api_contract import POST_SCHEMA
from core.config import settings
from core.schema import validate_schema


@pytest.mark.api
@pytest.mark.regression
def test_create_post_returns_201(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    payload = {"title": "new post", "body": "test body", "userId": 1}
    response = client.post("posts", json=payload, headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_created_status
    created = response.json()
    validate_schema(created, POST_SCHEMA)
    assert created["title"] == payload["title"]
    assert created["userId"] == payload["userId"]


@pytest.mark.api
@pytest.mark.regression
def test_get_nonexistent_post_returns_404(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts/99999", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_not_found_status
