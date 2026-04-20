import pytest

from core.schema import Field, validate_schema


SIMPLE_SCHEMA = [
    Field("id", int),
    Field("name", str),
]


@pytest.mark.unit
def test_validate_schema_passes_for_valid_data():
    validate_schema({"id": 1, "name": "Alice"}, SIMPLE_SCHEMA)


@pytest.mark.unit
def test_validate_schema_fails_on_missing_required_field():
    with pytest.raises(AssertionError, match="Missing required field: 'name'"):
        validate_schema({"id": 1}, SIMPLE_SCHEMA)


@pytest.mark.unit
def test_validate_schema_fails_on_wrong_type():
    with pytest.raises(AssertionError, match="expected int, got str"):
        validate_schema({"id": "not-an-int", "name": "Alice"}, SIMPLE_SCHEMA)


@pytest.mark.unit
def test_validate_schema_rejects_none_by_default():
    with pytest.raises(AssertionError, match="null is not allowed"):
        validate_schema({"id": None, "name": "Alice"}, SIMPLE_SCHEMA)


@pytest.mark.unit
def test_validate_schema_allows_none_when_declared():
    nullable_schema = [Field("id", int, allow_none=True), Field("name", str)]
    validate_schema({"id": None, "name": "Alice"}, nullable_schema)


@pytest.mark.unit
def test_validate_schema_skips_optional_absent_field():
    optional_schema = [Field("id", int), Field("email", str, required=False)]
    validate_schema({"id": 1}, optional_schema)


@pytest.mark.unit
def test_validate_schema_fails_when_data_is_not_a_dict():
    with pytest.raises(AssertionError, match="Expected a JSON object"):
        validate_schema([{"id": 1}], SIMPLE_SCHEMA)
