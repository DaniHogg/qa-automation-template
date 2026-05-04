import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_patch_post_title(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.patch("posts/1", json={"title": "Patched Title"}, headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status
    assert response.json()["title"] == "Patched Title"
