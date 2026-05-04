import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_response_content_type_is_json(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts/1", headers=api_headers, timeout=contract.request_timeout_seconds)
    content_type = response.headers.get("Content-Type", "")
    assert contract.expected_content_type in content_type, f"Unexpected Content-Type: {content_type}"


@pytest.mark.api
@pytest.mark.regression
def test_response_time_under_threshold(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status
    elapsed = response.elapsed.total_seconds()
    assert elapsed < contract.response_time_threshold_seconds, f"Response took {elapsed:.2f}s — exceeded {contract.response_time_threshold_seconds}s threshold"
