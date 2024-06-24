from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time


options = Options()
options.add_argument("--headless=new")
link = "https://sbis.ru/contacts/"
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get(link)
current_url1 = browser.current_url

def current_url69():
    assert current_url1 == 'https://sbis.ru/contacts/69-tverskaya-oblast?tab=clients'

# def get_page_source():
#     current_html_source = browser.page_source
#     with open('69.pkl', 'wb') as file:
#         pickle.dump(current_html_source, file)
#
#     with open('reference.pkl', 'rb') as file:
#         reference_current_html_source = pickle.load(file)
#
#         assert


current_url69()
#get_page_source()

anchor = browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[5]/div[1]/span/span')
browser.execute_script("arguments[0].scrollIntoView(true);", anchor)
anchor.click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span').click()
time.sleep(5)
current_url2 = browser.current_url


def current_url41():
    assert current_url2 == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'


current_url41()

browser.quit()
