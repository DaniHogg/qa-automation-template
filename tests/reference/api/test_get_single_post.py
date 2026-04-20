import pytest

from clients.http_client import HttpClient
from core.schema import Field, validate_schema

TIMEOUT = 15

POST_SCHEMA = [
    Field("id", int),
    Field("userId", int),
    Field("title", str),
    Field("body", str),
]


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_post_schema(api_headers):
    client = HttpClient()
    response = client.get("posts/1", headers=api_headers, timeout=TIMEOUT)
    assert response.status_code == 200

    post = response.json()
    validate_schema(post, POST_SCHEMA)
    assert post["id"] == 1
