import pytest

from clients.http_client import HttpClient
from core.api_contract import USER_SCHEMA
from core.config import settings
from core.schema import validate_schema


@pytest.mark.api
@pytest.mark.regression
def test_get_single_user_schema(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("users/1", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    user = response.json()
    validate_schema(user, USER_SCHEMA)
    assert user["id"] == 1
    assert "@" in user["email"], "Email should contain @"
