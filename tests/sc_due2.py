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

class Sc2SbisContactsPage:
    def region_navigation(self):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        page = SbisContactsPage(browser)

        page.open()
        current_url1 = page.get_current_url()
        assert current_url1 == 'https://sbis.ru/contacts/69-tverskaya-oblast?tab=clients'

        page.click_anchor()
        page.select_region(41)
        current_url2 = page.get_current_url()
        assert current_url2 == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'

        browser.quit()

Sc2SbisContactsPage().region_navigation()
