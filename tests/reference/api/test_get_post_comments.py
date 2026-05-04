import pytest

from clients.http_client import HttpClient
from core.config import settings


@pytest.mark.api
@pytest.mark.regression
def test_get_comments_for_post(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts/1/comments", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) >= contract.min_list_items, f"Expected at least {contract.min_list_items} comment(s)"
    for comment in comments:
        assert "email" in comment
        assert "body" in comment
