import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_post_schema(api_headers):
    """Each post must have id, userId, title, and body fields."""
    client = HttpClient()
    response = client.get("posts/1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    post = response.json()
    for field in ("id", "userId", "title", "body"):
        assert field in post, f"Missing field: {field}"
    assert post["id"] == 1
