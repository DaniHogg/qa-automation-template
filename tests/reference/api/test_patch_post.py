import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_patch_post_title(api_headers):
    client = HttpClient()
    response = client.patch("posts/1", json={"title": "Patched Title"}, headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200
    assert response.json()["title"] == "Patched Title"
