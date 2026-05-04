import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.smoke
def test_get_posts_returns_200(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= contract.min_list_items, f"Expected at least {contract.min_list_items} post item(s)"
