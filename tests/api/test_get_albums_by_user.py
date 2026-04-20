import pytest

from clients.http_client import HttpClient

TIMEOUT = 15


@pytest.mark.api
@pytest.mark.regression
def test_get_albums_by_user(api_headers):
    client = HttpClient()
    response = client.get("albums?userId=1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    albums = response.json()
    assert albums, "Expected albums for userId=1"
    assert all(a["userId"] == 1 for a in albums), "All albums should belong to userId=1"
    for field in ("id", "userId", "title"):
        assert field in albums[0], f"Missing field: {field}"
