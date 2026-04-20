"""
WinApp client using WinAppDriver (Appium protocol).

WinAppDriver acts as an Appium server for Windows desktop applications.
It must be running on Windows before tests execute:
  - Download from: https://github.com/microsoft/WinAppDriver/releases
  - Run: WinAppDriver.exe (defaults to http://127.0.0.1:4723)

Requires:
  pip install Appium-Python-Client
"""
import os

from appium import webdriver
from appium.options import AppiumOptions


WINAPPDRIVER_URL = os.getenv("WINAPPDRIVER_URL", "http://127.0.0.1:4723")


class WinAppClient:
    """Thin wrapper around a WinAppDriver session."""

    def __init__(self, app: str, app_working_dir: str | None = None):
        options = AppiumOptions()
        options.platform_name = "Windows"
        options.set_capability("app", app)
        if app_working_dir:
            options.set_capability("appWorkingDir", app_working_dir)

        self.driver = webdriver.Remote(
            command_executor=WINAPPDRIVER_URL,
            options=options,
        )

    def quit(self):
        if self.driver:
            self.driver.quit()
