from pages.sbis_home import SbisHomePage
import time
import os
import logging

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
        file_size = os.path.getsize(file_path)
        assert file_size == 7570584, f"Ожидаемый размер файла 7570584 байт, фактический размер {file_size} байт"

        # Удаление файла после проверки
        os.remove(file_path)

        LOGGER.critical('test pass all fine')
