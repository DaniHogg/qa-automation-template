import pytest

from clients.http_client import HttpClient
from core.schema import Field, validate_schema

TIMEOUT = 15

USER_SCHEMA = [
    Field("id", int),
    Field("name", str),
    Field("email", str),
    Field("phone", str),
    Field("address", dict),
    Field("company", dict),
]


@pytest.mark.api
@pytest.mark.regression
def test_get_single_user_schema(api_headers):
    client = HttpClient()
    response = client.get("users/1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    user = response.json()
    validate_schema(user, USER_SCHEMA)
    assert user["id"] == 1
    assert "@" in user["email"], "Email should contain @"
