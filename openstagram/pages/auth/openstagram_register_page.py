from selenium.webdriver.common.by import By

from openstagram.pages.tools.openstagram_utils import OpenStagramUtils


class OpenStagramRegisterPage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Register page
    '''

    REGISTER_PAGE_URL = '/register'
    # Page title
    REGISTER_ON_OPENSTAGRAM_HEADER = (By.XPATH, '//h2[contains(text(),"Register on OpenStagram")]')
    # Name field
    NAME_LABEL = (By.XPATH, '//label[contains(text(),"Name")]')
    NAME_INPUT = (By.XPATH, '//input[@placeholder="Your name"]')
    # Username field
    USERNAME_LABEL = (By.XPATH, '//label[contains(text(),"Username")]')
    USERNAME_INPUT = (By.XPATH, '//input[@placeholder="Your username"]')
    # Email field
    EMAIL_LABEL = (By.XPATH, '//label[contains(text(),"Email")]')
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Your email"]')
    # Password field
    PASSWORD_LABEL = (By.XPATH, '//label[contains(text(),"Password")]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Your password"]')
    # Password Confirmation field
    PASSWORD_CONFIRMATION_LABEL = (By.XPATH, '//label[contains(text(),"Password Confirmation")]')
    PASSWORD_CONFIRMATION_INPUT = (By.XPATH, '//input[@placeholder="Your password confirmation"]')
    # Submit button
    REGISTER_BUTTON = (By.XPATH, '//input[@value="Register"]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = f'{base_url}{self.REGISTER_PAGE_URL}'

    def load(self):
        '''Redirects to the /register page'''
        self.utils.load(self.page_url, 3)

    def find_register_on_openstagram_header(self):
        '''Finds the Register on OpenStagram header'''
        return self.utils.find_element(self.REGISTER_ON_OPENSTAGRAM_HEADER)

    def find_name_label(self):
        '''Finds the Name label in the Registration form'''
        return self.utils.find_element(self.NAME_LABEL)

    def find_name_input(self):
        '''Finds the Name input in the Registration form'''
        return self.utils.find_element(self.NAME_INPUT)

    def fill_name_input(self, value, timeout=0):
        '''Fills the Name input in the Registration form'''
        self.utils.fill_element(self.NAME_INPUT, value, timeout)

    def find_username_input(self):
        '''Finds the Username input in the Registration form'''
        return self.utils.find_element(self.USERNAME_INPUT)

    def fill_username_input(self, value, timeout=0):
        '''Fills the Username input in the Registration form'''
        self.utils.fill_element(self.USERNAME_INPUT, value, timeout)

    def find_email_input(self):
        '''Finds the Email input in the Registration form'''
        return self.utils.find_element(self.EMAIL_INPUT)

    def fill_email_input(self, value, timeout=0):
        '''Fills the Email input in the Registration form'''
        self.utils.fill_element(self.EMAIL_INPUT, value, timeout)

    def find_password_input(self):
        '''Finds the Password input in the Registration form'''
        return self.utils.find_element(self.PASSWORD_INPUT)

    def fill_password_input(self, value, timeout=0):
        '''Fills the Password input in the Registration form'''
        self.utils.fill_element(self.PASSWORD_INPUT, value, timeout)

    def find_password_confirmation_input(self):
        '''Finds the Password Confirmation input in the Registration form'''
        return self.utils.find_element(self.PASSWORD_CONFIRMATION_INPUT)

    def fill_password_confirmation_input(self, value, timeout=0):
        '''Fills the Password Confirmation input in the Registration form'''
        self.utils.fill_element(self.PASSWORD_CONFIRMATION_INPUT, value, timeout)

    def find_register_button(self):
        '''Finds the Register button in the Registration form'''
        return self.utils.find_element(self.REGISTER_BUTTON)

    def click_register_button(self, timeout=0):
        '''Finds the Register button in the Registration form'''
        self.utils.click_element(self.REGISTER_BUTTON, timeout)

    def find_field_error_message(self, field_name, error_message):
        '''Finds a specific error message'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"The {field_name} {error_message}.")]'))

    def do_register(self, name, username, email, password):
        '''Do the Register process successfully'''
        self.fill_name_input(name, 1)
        self.fill_username_input(username, 1)
        self.fill_email_input(email, 1)
        self.fill_password_input(password, 1)
        self.fill_password_confirmation_input(password, 1)
        self.click_register_button(3)
