from selenium.webdriver.common.by import By


NAME = (By.XPATH, '//div[contains(text(),"Elements")]')
NAME_TEXT_BOX = (By.XPATH, '//div[contains(text(),"Text Box")]')
TEXT_BOX = (By.ID, 'item-0')
FULL_NAME = (By.ID, 'userName')
EMAIL = (By.ID, 'userEmail')
CURRENT_ADDRESS = (By.ID, 'currentAddress')
PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
SUBMIT_BUTTON = (By.ID, 'submit')
EMAIL_ERROR =(By.CSS_SELECTOR, 'input[class="mr-sm-2 field-error form-control"]')
SUBMITED_NAME = (By.ID, 'name')
SUBMITED_EMAIL = (By.ID, 'email')
SUBMITED_ADDRESS = (By.ID, 'currentAddress')