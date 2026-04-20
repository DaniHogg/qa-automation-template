import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_get_nonexistent_post_returns_404(api_headers):
    client = HttpClient()
    response = client.get("posts/99999", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 404
