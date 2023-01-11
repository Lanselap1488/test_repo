from ..pages.base_page import BasePage
from ..locators.locators_elements import *
from selenium.webdriver.common.keys import Keys


class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_elements_page(self):
        self.driver.get('https://demoqa.com/elements')

    def return_name_of_pege(self):
        return self.find_element(NAME)

    def open_text_box(self):
        self.find_element(TEXT_BOX).click()

    def find_name_text_box(self):
        return self.find_element(NAME_TEXT_BOX)

    def fill_name(self, name):
        self.find_element(FULL_NAME).send_keys(name)

    def fill_email(self, email):
        self.find_element(EMAIL).send_keys(email)

    def fill_current_address(self, cur_address):
        self.find_element(CURRENT_ADDRESS).send_keys(cur_address)

    def fill_permanent_address(self, per_address):
        self.find_element(PERMANENT_ADDRESS).send_keys(per_address)

    def press_submit_button(self):
        self.find_element(SUBMIT_BUTTON).click()

    def find_filled_name(self):
        return self.find_element(SUBMITED_NAME)

    def find_filled_email(self):
        return self.find_element(SUBMITED_EMAIL)

    def find_filled_address(self):
        return self.find_element(SUBMITED_ADDRESS)



