import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_get_posts_by_user_filter(api_headers):
    client = HttpClient()
    response = client.get("posts?userId=1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    posts = response.json()
    assert posts, "Expected posts for userId=1"
    assert all(p["userId"] == 1 for p in posts), "All returned posts should belong to userId=1"
