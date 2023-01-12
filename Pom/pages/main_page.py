from ..pages.base_page import BasePage
from selenium.webdriver.common.by import By

ELEMENTS = (By.XPATH, '//h5[contains(text(),"Elements")]/../..')
TITLE = (By.XPATH, '//img[@src="/images/Toolsqa.jpg"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        self.driver.get('https://demoqa.com/')

    def find_title_of_page(self):
        return self.find_element(TITLE)

    def click_button_elements(self):
        return self.find_element(ELEMENTS).click()
