import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_get_posts_by_user_filter(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts?userId=1", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    posts = response.json()
    assert len(posts) >= contract.min_list_items, f"Expected at least {contract.min_list_items} post(s) for userId=1"
    assert all(p["userId"] == 1 for p in posts), "All returned posts should belong to userId=1"
