import pytest

from tests.winapp.conftest import windows_only


@pytest.mark.winapp
@pytest.mark.regression
@windows_only
def test_notepad_save_as_dialog_opens_and_cancels(notepad):
    notepad.type_in_editor("temp content")
    notepad.open_save_as_dialog()
    notepad.cancel_dialog()
    # After cancelling, the main editor should still be accessible
    assert notepad.editor_text() == "temp content"
