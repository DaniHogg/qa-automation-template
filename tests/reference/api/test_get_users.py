import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.smoke
def test_get_users_returns_200(api_headers):
    client = HttpClient()
    response = client.get("users", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert users, "Expected at least one user"
