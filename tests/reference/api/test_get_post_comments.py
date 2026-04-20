import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_get_comments_for_post(api_headers):
    client = HttpClient()
    response = client.get("posts/1/comments", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    comments = response.json()
    assert isinstance(comments, list)
    assert comments, "Expected at least one comment"
    for comment in comments:
        assert "email" in comment
        assert "body" in comment
