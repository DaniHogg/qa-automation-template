import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_get_single_user_schema(api_headers):
    client = HttpClient()
    response = client.get("users/1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    user = response.json()
    for field in ("id", "name", "email", "phone", "address", "company"):
        assert field in user, f"Missing field: {field}"
    assert user["id"] == 1
    assert "@" in user["email"], "Email should contain @"
