import pytest

from core.config import _as_bool


@pytest.mark.unit
def test_as_bool_returns_default_when_value_is_none():
    assert _as_bool(None, default=False) is False


@pytest.mark.unit
def test_as_bool_recognises_truthy_values():
    for value in ("1", "true", "TRUE", "yes", "on"):
        assert _as_bool(value) is True


@pytest.mark.unit
def test_as_bool_rejects_non_truthy_values():
    for value in ("0", "false", "no", "off", "anything-else"):
        assert _as_bool(value) is False
