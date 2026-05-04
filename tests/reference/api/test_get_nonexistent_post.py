import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_get_nonexistent_post_returns_404(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts/99999", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_not_found_status
    content_type = response.headers.get("Content-Type", "")
    assert contract.expected_content_type in content_type, f"Unexpected Content-Type: {content_type}"
