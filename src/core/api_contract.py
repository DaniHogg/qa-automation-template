import os
from dataclasses import dataclass

from core.schema import Field


@dataclass(frozen=True)
class ApiTargetContract:
    request_timeout_seconds: float
    expected_content_type: str
    expected_success_status: int
    expected_created_status: int
    expected_accepted_status: int
    expected_not_found_status: int
    response_time_threshold_seconds: float
    min_list_items: int


def _profile_jsonplaceholder() -> ApiTargetContract:
    return ApiTargetContract(
        request_timeout_seconds=float(os.getenv("API_REQUEST_TIMEOUT", "15")),
        expected_content_type=os.getenv("API_CONTENT_TYPE", "application/json"),
        expected_success_status=int(os.getenv("API_SUCCESS_STATUS", "200")),
        expected_created_status=int(os.getenv("API_CREATED_STATUS", "201")),
        expected_accepted_status=int(os.getenv("API_ACCEPTED_STATUS", "200")),
        expected_not_found_status=int(os.getenv("API_NOT_FOUND_STATUS", "404")),
        response_time_threshold_seconds=float(os.getenv("API_RESPONSE_TIME_THRESHOLD", "3.0")),
        min_list_items=int(os.getenv("API_MIN_LIST_ITEMS", "1")),
    )


_API_TARGET_PROFILES = {
    "jsonplaceholder": _profile_jsonplaceholder,
}


def load_api_contract(profile_name: str) -> ApiTargetContract:
    builder = _API_TARGET_PROFILES.get(profile_name)
    if builder is None:
        supported = ", ".join(sorted(_API_TARGET_PROFILES.keys()))
        raise ValueError(f"Unsupported API_TARGET_PROFILE '{profile_name}'. Supported profiles: {supported}")
    return builder()


# Shared API response schemas used across test suites.
# These define the expected structure of common resources.
# Tests import these directly to avoid duplication.

POST_SCHEMA = [
    Field("id", int),
    Field("userId", int),
    Field("title", str),
    Field("body", str),
]

USER_SCHEMA = [
    Field("id", int),
    Field("name", str),
    Field("email", str),
    Field("phone", str),
    Field("address", dict),
    Field("company", dict),
]

TODO_SCHEMA = [
    Field("id", int),
    Field("userId", int),
    Field("title", str),
    Field("completed", bool),
]

COMMENT_SCHEMA = [
    Field("id", int),
    Field("postId", int),
    Field("name", str),
    Field("email", str),
    Field("body", str),
]

ALBUM_SCHEMA = [
    Field("id", int),
    Field("userId", int),
    Field("title", str),
]
