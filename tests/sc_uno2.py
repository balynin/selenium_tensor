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

class Sc1SbisContactsPage:
    def pic_sizes(self):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        page = SbisContactsPage(browser)

        page.open()
        page.click_clients_button()
        page.click_anchor()

        pic1_height, pic1_width = page.get_pic_size(1)
        pic2_height, pic2_width = page.get_pic_size(2)
        pic3_height, pic3_width = page.get_pic_size(3)
        pic4_height, pic4_width = page.get_pic_size(4)

        assert pic1_width == pic2_width == pic3_width == pic4_width, 'pic width wrong'
        assert pic1_height == pic2_height == pic3_height == pic4_height, 'pic height wrong'

        browser.quit()


inst_sc1 = Sc1SbisContactsPage()
inst_sc1.pic_sizes()
