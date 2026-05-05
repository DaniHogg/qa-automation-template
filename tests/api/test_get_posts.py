import pytest

from clients.http_client import HttpClient
from core.api_contract import POST_SCHEMA
from core.config import settings
from core.schema import validate_list_schema


@pytest.mark.api
@pytest.mark.smoke
def test_get_posts_returns_list(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status
    validate_list_schema(response.json(), POST_SCHEMA, min_items=contract.min_list_items)


@pytest.mark.api
@pytest.mark.smoke
def test_get_posts_content_type(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert contract.expected_content_type in response.headers.get("content-type", "")


@pytest.mark.api
@pytest.mark.smoke
def test_get_posts_response_time(api_headers):
    import time
    client = HttpClient()
    contract = settings.api_contract
    start = time.monotonic()
    response = client.get("posts", headers=api_headers, timeout=contract.request_timeout_seconds)
    elapsed = time.monotonic() - start
    assert response.status_code == contract.expected_success_status
    assert elapsed < contract.response_time_threshold_seconds, (
        f"Response took {elapsed:.2f}s, threshold is {contract.response_time_threshold_seconds}s"
    )
