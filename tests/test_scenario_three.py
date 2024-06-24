from pages.sbis_home import SbisHomePage
import time
import os
import logging
import filecmp

LOGGER = logging.getLogger(__name__)

class TestSbisHomePage:
    def test_download_file(self, browser):
        page = SbisHomePage(browser)

        page.open()
        page.navigate_to_download()
        page.download_file()
        time.sleep(10)

        # Проверка размера файла
        file_path = "/home/dbalynin/Downloads/sbisplugin-setup-web.exe"
        file_path_reference = "/home/dbalynin/Downloads/reference-sbisplugin-setup-web.exe"
        assert filecmp.cmp(file_path, file_path_reference)

        # Удаление файла после проверки
        os.remove(file_path)

        LOGGER.critical('test pass all fine')
