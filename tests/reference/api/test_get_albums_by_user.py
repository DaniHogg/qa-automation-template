import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_get_albums_by_user(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("albums?userId=1", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    albums = response.json()
    assert len(albums) >= contract.min_list_items, f"Expected at least {contract.min_list_items} album(s) for userId=1"
    assert all(a["userId"] == 1 for a in albums), "All albums should belong to userId=1"
    for field in ("id", "userId", "title"):
        assert field in albums[0], f"Missing field: {field}"
