from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import filecmp

link = "https://sbis.ru"
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get(link)
anchor = browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')
browser.execute_script("arguments[0].scrollIntoView(true);", anchor)
anchor.click()
btn = browser.find_element(By.PARTIAL_LINK_TEXT, 'Скачать (Exe 7.22 МБ)')
action = ActionChains(browser)
action.move_to_element(btn).click().perform()
time.sleep(15)
browser.quit()


def download_file_size():
    assert filecmp.cmp("/home/dbalynin/Downloads/sbisplugin-setup-web.exe", "/home/dbalynin/Downloads/sbisplugin-setup-web.exe")

download_file_size()

os.remove("/home/dbalynin/Downloads/sbisplugin-setup-web.exe")