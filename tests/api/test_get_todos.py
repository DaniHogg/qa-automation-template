import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.smoke
def test_get_todos_returns_200(api_headers):
    client = HttpClient()
    response = client.get("todos", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    todos = response.json()
    assert isinstance(todos, list)
    assert todos, "Expected at least one todo item"
    for field in ("id", "userId", "title", "completed"):
        assert field in todos[0], f"Missing field: {field}"
