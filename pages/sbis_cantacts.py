from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class SbisContactsPage:
    def __init__(self, browser):
        self.browser = browser
        self.link = "https://sbis.ru/contacts/"
        self.clients_button_xpath = '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'
        self.anchor_xpath = '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
        self.pic_xpath_prefix = '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div'

    def open(self):
        self.browser.get(self.link)

    def click_clients_button(self):
        self.browser.find_element(By.XPATH, self.clients_button_xpath).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def click_anchor(self):
        anchor = self.browser.find_element(By.XPATH, self.anchor_xpath)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", anchor)
        anchor.click()

    def get_pic_size(self, index):
        pic_xpath = f'{self.pic_xpath_prefix}{index}/a/div[1]/img'
        pic_size = self.browser.find_element(By.XPATH, pic_xpath).size
        return pic_size['height'], pic_size['width']


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class SbisContactsPage:
    def init(self, browser):
        self.browser = browser
        self.link = "https://sbis.ru/contacts/"
        self.anchor_xpath = '//*[@id="container"]/div[2]/div[1]/div[5]/div[1]/span/span'
        self.region_button_xpath = '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[{region_id}]/span/span'

    def open(self):
        self.browser.get(self.link)

    def click_anchor(self):
        anchor = self.browser.find_element(By.XPATH, self.anchor_xpath)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", anchor)
        anchor.click()
        time.sleep(5)

    def select_region(self, region_id):
        region_button_xpath = self.region_button_xpath.format(region_id=region_id)
        self.browser.find_element(By.XPATH, region_button_xpath).click()
        time.sleep(5)

    def get_current_url(self):
        return self.browser.current_url