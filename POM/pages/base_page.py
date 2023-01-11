from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def move_element(self, locator):
        ActionChains(self.driver).move_to_element(locator).perform()

    def allure_attach_screen(self):
        return allure.attach(
            self.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=AttachmentType.PNG
        )
