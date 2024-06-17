from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.sbis_home import SbisHomePage
import time
import os


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
