import pytest

from tests.reference.winapp.conftest import windows_only


@pytest.mark.winapp
@pytest.mark.regression
@windows_only
def test_notepad_title_updates_with_unsaved_changes(notepad):
    notepad.type_in_editor("unsaved content")
    title = notepad.window_title()
    assert "*" in title, f"Expected unsaved marker (*) in title, got: {title}"
