import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.smoke
def test_get_posts_returns_200(api_headers):
    client = HttpClient()
    response = client.get("posts", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, list)
    assert payload, "Expected at least one post item"
