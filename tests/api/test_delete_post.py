import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_delete_post_returns_200(api_headers):
    client = HttpClient()
    response = client.delete("posts/1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200
