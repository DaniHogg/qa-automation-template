import pytest

from clients.http_client import HttpClient
from core.api_contract import POST_SCHEMA
from core.config import settings
from core.schema import validate_schema


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_post_schema(api_headers):
    client = HttpClient()
    contract = settings.api_contract
    response = client.get("posts/1", headers=api_headers, timeout=contract.request_timeout_seconds)
    assert response.status_code == contract.expected_success_status

    post = response.json()
    validate_schema(post, POST_SCHEMA)
    assert post["id"] == 1
