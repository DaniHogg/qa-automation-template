import pytest

from tests.reference.winapp.conftest import windows_only


@pytest.mark.winapp
@pytest.mark.regression
@windows_only
def test_notepad_save_as_dialog_opens_and_cancels(notepad):
    notepad.type_in_editor("temp content")
    notepad.open_save_as_dialog()
    notepad.cancel_dialog()
    assert notepad.editor_text() == "temp content"
