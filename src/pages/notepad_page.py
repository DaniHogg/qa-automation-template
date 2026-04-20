"""
Page object for Windows Notepad (classic win32 version).

App path used: 'C:\\Windows\\System32\\notepad.exe'
This is universally available on all modern Windows installations.
"""
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_winapp import BaseWinApp


class NotepadPage(BaseWinApp):
    # Locators
    TEXT_AREA = (AppiumBy.CLASS_NAME, "Edit")
    TITLE_BAR = (AppiumBy.NAME, "Notepad")
    FILE_MENU = (AppiumBy.NAME, "File")
    SAVE_AS_MENU_ITEM = (AppiumBy.NAME, "Save As...")
    FILENAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "1001")  # Save As dialog filename field
    CANCEL_BUTTON = (AppiumBy.NAME, "Cancel")

    def type_in_editor(self, text: str):
        self.type_text(self.TEXT_AREA, text)

    def editor_text(self) -> str:
        return self.text_of(self.TEXT_AREA)

    def window_title(self) -> str:
        return self.driver.title

    def open_save_as_dialog(self):
        self.click(self.FILE_MENU)
        self.click(self.SAVE_AS_MENU_ITEM)

    def cancel_dialog(self):
        self.click(self.CANCEL_BUTTON)
