from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


link = "https://sbis.ru/contacts/"
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get(link)
browser.find_element(By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a').click()
browser.switch_to.window(browser.window_handles[1])
anchor = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
browser.execute_script("arguments[0].scrollIntoView(true);", anchor)
anchor.click()

pic1_size = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img').size
pic1_height = pic1_size['height']
pic1_width = pic1_size['width']

pic2_size = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img').size
pic2_height = pic2_size['height']
pic2_width = pic2_size['width']

pic3_size = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img').size
pic3_height = pic3_size['height']
pic3_width = pic3_size['width']

pic4_size = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img').size
pic4_height = pic4_size['height']
pic4_width = pic4_size['width']

def pic_width():
    assert pic1_width == pic2_width, 'pic width wrong'
    assert pic2_width == pic3_width, 'pic width wrong'
    assert pic3_width == pic4_width, 'pic width wrong'

def pic_height():
    assert pic1_height == pic2_height, 'pic height wrong'
    assert pic2_height == pic3_height, 'pic height wrong'
    assert pic3_height == pic4_height, 'pic height wrong'

pic_width()
pic_height()

browser.quit()
