import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_filter_todos_by_completed(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("todos?completed=true", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    todos = response.json()
    assert len(todos) >= contract.min_list_items, f"Expected at least {contract.min_list_items} completed todo(s)"
    assert all(t["completed"] is True for t in todos), "All returned todos should be completed"
