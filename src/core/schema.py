"""
Schema validation helpers for API response bodies.

Provides lightweight dictionary/list schema checking without an external
library dependency. Use these in tests to keep assertions readable and
produce descriptive failure messages.

Usage example:
    from core.schema import validate_schema, Field

    POST_SCHEMA = [
        Field("id", int),
        Field("userId", int),
        Field("title", str),
        Field("body", str),
    ]

    validate_schema(response.json(), POST_SCHEMA)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Type


@dataclass
class Field:
    """Declares one expected field in a JSON object.

    Args:
        name:       The key that must be present in the response.
        type:       The Python type the value must be an instance of.
        required:   Whether to fail if the key is absent (default True).
        allow_none: Whether ``None`` is an acceptable value (default False).
    """

    name: str
    type: Type
    required: bool = True
    allow_none: bool = False


def validate_schema(data: dict, schema: list[Field]) -> None:
    """Assert that *data* matches every Field in *schema*.

    Raises ``AssertionError`` with a descriptive message on the first violation.
    """
    assert isinstance(data, dict), f"Expected a JSON object (dict), got {type(data).__name__}"
    for f in schema:
        if f.required:
            assert f.name in data, f"Missing required field: '{f.name}'"
        if f.name not in data:
            continue
        value = data[f.name]
        if value is None:
            assert f.allow_none, (
                f"Field '{f.name}' is None but null is not allowed"
            )
        else:
            assert isinstance(value, f.type), (
                f"Field '{f.name}': expected {f.type.__name__}, got {type(value).__name__} ({value!r})"
            )


def validate_list_schema(data: list, schema: list[Field], *, min_items: int = 1) -> None:
    """Assert that *data* is a non-empty list and every item matches *schema*.

    Args:
        data:      The parsed JSON response body (must be a list).
        schema:    Field declarations to validate against each item.
        min_items: Minimum number of items the list must contain.
    """
    assert isinstance(data, list), f"Expected a JSON array (list), got {type(data).__name__}"
    assert len(data) >= min_items, (
        f"Expected at least {min_items} item(s), got {len(data)}"
    )
    for index, item in enumerate(data):
        try:
            validate_schema(item, schema)
        except AssertionError as exc:
            raise AssertionError(f"Item[{index}] failed schema check: {exc}") from exc
