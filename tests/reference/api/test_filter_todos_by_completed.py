import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_filter_todos_by_completed(api_headers):
    client = HttpClient()
    response = client.get("todos?completed=true", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    todos = response.json()
    assert todos, "Expected completed todos"
    assert all(t["completed"] is True for t in todos), "All returned todos should be completed"
