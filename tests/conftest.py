import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()
