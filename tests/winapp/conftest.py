"""
Fixtures for Windows desktop app tests.

Prerequisites (Windows only):
  1. Download and run WinAppDriver:
     https://github.com/microsoft/WinAppDriver/releases
  2. Install Appium-Python-Client:
     pip install Appium-Python-Client

Tests in this folder are skipped automatically on non-Windows platforms.
Set the WINAPPDRIVER_URL env var if WinAppDriver runs on a different host/port
(default: http://127.0.0.1:4723).
"""
import sys
import pytest

NOTEPAD_APP = r"C:\Windows\System32\notepad.exe"

windows_only = pytest.mark.skipif(
    sys.platform != "win32",
    reason="Windows desktop tests require WinAppDriver on Windows",
)


@pytest.fixture(scope="function")
def notepad(request):
    """Launch Notepad and yield a NotepadPage; quit the app after the test."""
    pytest.importorskip("appium", reason="Install optional dependency: pip install -e .[windows]")
    from clients.winapp_client import WinAppClient
    from pages.notepad_page import NotepadPage

    client = WinAppClient(app=NOTEPAD_APP)
    page = NotepadPage(client.driver)
    yield page
    client.quit()
