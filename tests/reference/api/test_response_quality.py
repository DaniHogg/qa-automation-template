import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_response_content_type_is_json(api_headers):
    client = HttpClient()
    response = client.get("posts/1", headers=api_headers, timeout=TIMEOUT)
    content_type = response.headers.get("Content-Type", "")
    assert "application/json" in content_type, f"Unexpected Content-Type: {content_type}"


@pytest.mark.api
@pytest.mark.regression
def test_response_time_under_threshold(api_headers):
    client = HttpClient()
    response = client.get("posts", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200
    elapsed = response.elapsed.total_seconds()
    assert elapsed < 3.0, f"Response took {elapsed:.2f}s — exceeded 3s threshold"
