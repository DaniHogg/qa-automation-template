import pytest

from clients.http_client import HttpClient


@pytest.mark.unit
def test_http_client_normalises_base_url_and_path():
    client = HttpClient(base_url="https://api.example.com/")
    assert client._url("posts/1") == "https://api.example.com/posts/1"


@pytest.mark.unit
def test_http_client_strips_leading_slash_from_path():
    client = HttpClient(base_url="https://api.example.com")
    assert client._url("/users") == "https://api.example.com/users"
