import pytest

from clients.http_client import HttpClient
from core.schema import Field, validate_list_schema

TIMEOUT = 15

TODO_SCHEMA = [
    Field("id", int),
    Field("userId", int),
    Field("title", str),
    Field("completed", bool),
]


@pytest.mark.api
@pytest.mark.smoke
def test_get_todos_returns_200(api_headers):
    client = HttpClient()
    response = client.get("todos", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    validate_list_schema(response.json(), TODO_SCHEMA)
