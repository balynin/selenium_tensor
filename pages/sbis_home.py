from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os


class SbisHomePage:
    def init(self, browser):
        self.browser = browser
        self.link = "https://sbis.ru"
        self.anchor_xpath = '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a'
        self.download_button_partial_link_text = 'Скачать (Exe 7.22 МБ)'

    def open(self):
        self.browser.get(self.link)

    def navigate_to_download(self):
        anchor = self.browser.find_element(By.XPATH, self.anchor_xpath)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", anchor)
        anchor.click()

    def download_file(self):
        btn = self.browser.find_element(By.PARTIAL_LINK_TEXT, self.download_button_partial_link_text)
        action = ActionChains(self.browser)
        action.move_to_element(btn).click().perform()
        time.sleep(10)  # Ждем завершения загрузки файла