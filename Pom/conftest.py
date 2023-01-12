import allure
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.firefox.options import Options as firefox_Options
from .settings import BROWSER


@pytest.fixture(scope='function')
def driver():
    chrome_options = chrome_Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    if BROWSER == 'Firefox':
        with allure.step("Run Firefox"):
            firefox_options = firefox_Options()
            # firefox_options.add_argument("--headless")
            firefox_options.add_argument("--start-maximized")
            my_driver = webdriver.Firefox(options=firefox_options)
    else:
        with allure.step("Run Chrome"):
            my_driver = webdriver.Chrome(options=chrome_options)
    my_driver.implicitly_wait(10)
    yield my_driver
    my_driver.quit()
