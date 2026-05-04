import pytest

from clients.http_client import HttpClient
from core.api_contract import TODO_SCHEMA
from core.config import settings
from core.schema import validate_list_schema


@pytest.mark.api
@pytest.mark.smoke
def test_get_todos_returns_200(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("todos", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    validate_list_schema(response.json(), TODO_SCHEMA, min_items=contract.min_list_items)
