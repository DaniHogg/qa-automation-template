import pytest

from core.schema import Field, validate_list_schema


ITEM_SCHEMA = [Field("id", int), Field("title", str)]


@pytest.mark.unit
def test_validate_list_schema_passes_for_valid_list():
    data = [{"id": 1, "title": "A"}, {"id": 2, "title": "B"}]
    validate_list_schema(data, ITEM_SCHEMA)


@pytest.mark.unit
def test_validate_list_schema_fails_when_not_a_list():
    with pytest.raises(AssertionError, match="Expected a JSON array"):
        validate_list_schema({"id": 1, "title": "A"}, ITEM_SCHEMA)


@pytest.mark.unit
def test_validate_list_schema_fails_when_below_min_items():
    with pytest.raises(AssertionError, match="Expected at least 2 item"):
        validate_list_schema([{"id": 1, "title": "A"}], ITEM_SCHEMA, min_items=2)


@pytest.mark.unit
def test_validate_list_schema_reports_item_index_on_failure():
    data = [{"id": 1, "title": "A"}, {"id": "bad", "title": "B"}]
    with pytest.raises(AssertionError, match=r"Item\[1\]"):
        validate_list_schema(data, ITEM_SCHEMA)
