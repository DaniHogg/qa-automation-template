import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_delete_post_returns_200(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.delete("posts/1", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status
