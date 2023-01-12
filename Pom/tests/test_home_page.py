import pytest
from ..pages.main_page import HomePage
from ..pages.elements_page import ElementsPage
import allure
from ..tests.utils import *
from time import sleep


@allure.feature('Home page')
def test_open_site(driver):
    with allure.step('Open home page'):
        home = HomePage(driver)
        home.open_main_page()
        home.allure_attach_screen()
    title = home.find_title_of_page()
    assert title.is_displayed()


@allure.feature('Elements')
def test_press_elements_button(driver):
    with allure.step('Open home page'):
        home = HomePage(driver)
        home.open_main_page()
    with allure.step('Click button elements'):
        home.click_button_elements()
        element = ElementsPage(driver)
        name = element.return_name_of_pege()
        element.allure_attach_screen()
    assert 'Elements' in name.text and name.is_displayed()


@allure.feature('Elements')
def test_check_text_box(driver):
    with allure.step('Open home page'):
        home = HomePage(driver)
        home.open_main_page()
    with allure.step('Click button elements'):
        home.click_button_elements()
    elements_page = ElementsPage(driver)
    with allure.step('Click open text box'):
        elements_page.open_text_box()
        name = elements_page.find_name_text_box()
        elements_page.allure_attach_screen()
    assert 'Text Box' in name.text and name.is_displayed()


@allure.feature('Elements')
def test_submit_form_positive(driver):
    with allure.step('Open elements page'):
        elements = ElementsPage(driver)
        elements.open_elements_page()
    with allure.step('Click open text box'):
        elements.open_text_box()
    with allure.step('Fill fields'):
        elements.fill_name('Joric')
        elements.fill_email('meme228@aa.com')
        elements.fill_current_address('New York')
    with allure.step('Submit form'):
        driver.execute_script("window.scrollTo(500, 600)")
        elements.press_submit_button()
        elements.allure_attach_screen()
    sub_name = elements.find_filled_name()
    sub_email = elements.find_filled_email()
    sub_addr = elements.find_filled_address()
    assert 'Joric' in sub_name.text and 'meme228@aa.com' in sub_email.text and \
           sub_name.is_displayed() and sub_email.is_displayed() and sub_addr.is_displayed()
