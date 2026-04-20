import pytest

from tests.winapp.conftest import windows_only


@pytest.mark.winapp
@pytest.mark.regression
@windows_only
def test_notepad_type_text(notepad):
    sample = "Hello from automated QA test!"
    notepad.type_in_editor(sample)
    assert notepad.editor_text() == sample
