import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.smoke
def test_get_users_returns_200(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("users", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    users = response.json()
    assert isinstance(users, list)
    assert len(users) >= contract.min_list_items, f"Expected at least {contract.min_list_items} user(s)"
