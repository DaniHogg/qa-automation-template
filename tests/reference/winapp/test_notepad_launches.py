import pytest

from tests.reference.winapp.conftest import windows_only


@pytest.mark.winapp
@pytest.mark.smoke
@windows_only
def test_notepad_launches(notepad):
    title = notepad.window_title()
    assert "Notepad" in title, f"Unexpected window title: {title}"
