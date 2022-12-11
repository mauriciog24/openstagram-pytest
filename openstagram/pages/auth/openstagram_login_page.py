from selenium.webdriver.common.by import By

from pages.tools.openstagram_utils import OpenStagramUtils


class OpenStagramLoginPage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Login page
    '''

    LOGIN_PAGE_URL = '/login'
    # Page title
    LOGIN_ON_OPENSTAGRAM_HEADER = (By.XPATH, '//h2[contains(text(),"Login on OpenStagram")]')
    # Email field
    EMAIL_LABEL = (By.XPATH, '//label[contains(text(),"Email")]')
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Your email"]')
    # Password field
    PASSWORD_LABEL = (By.XPATH, '//label[contains(text(),"Password")]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Your password"]')
    # Remember Me checkbox
    REMEMBER_ME_LABEL = (By.XPATH, '//label[contains(text(),"Remember Me")]')
    REMEMBER_ME_CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    # Submit button
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Login"]')
    # Error message
    BAD_CREDENTIALS_LABEL = (By.XPATH, '//p[contains(text(),"Bad credentials")]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = f'{base_url}{self.LOGIN_PAGE_URL}'

    def load(self):
        '''Redirects to the /login page'''
        self.utils.load_page(self.page_url, 3)

    def find_login_on_openstagram_header(self):
        '''Finds the Login on OpenStagram header'''
        return self.utils.find_element(self.LOGIN_ON_OPENSTAGRAM_HEADER)

    def find_email_label(self):
        '''Finds the Email label in the Login form'''
        return self.utils.find_element(self.EMAIL_LABEL)

    def find_email_input(self):
        '''Finds the Email input in the Login form'''
        return self.utils.find_element(self.EMAIL_INPUT)

    def fill_email_input(self, value, timeout=0):
        '''Fills the Email input in the Login form'''
        self.utils.fill_element(self.EMAIL_INPUT, value, timeout)

    def find_password_label(self):
        '''Finds the Password label in the Login form'''
        return self.utils.find_element(self.PASSWORD_LABEL)

    def find_password_input(self):
        '''Finds the Password input in the Login form'''
        return self.utils.find_element(self.PASSWORD_INPUT)

    def fill_password_input(self, value, timeout=0):
        '''Fills the Password input in the Login form'''
        self.utils.fill_element(self.PASSWORD_INPUT, value, timeout)

    def find_login_button(self):
        '''Finds the Login button in the Login form'''
        return self.utils.find_element(self.LOGIN_BUTTON)

    def click_login_button(self, timeout=0):
        '''Finds the Login button in the Login form'''
        self.utils.click_element(self.LOGIN_BUTTON, timeout)

    def find_bad_credentials_label(self):
        '''Finds the Bad credentials label in the Login form'''
        return self.utils.find_element(self.BAD_CREDENTIALS_LABEL)

    def find_field_error_message(self, field_name, error_message):
        '''Finds a specific error message in the Login form'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"The {field_name} {error_message}.")]'))

    def do_login(self, email, password):
        '''Do the Login process successfully'''
        self.fill_email_input(email, 1)
        self.fill_password_input(password, 1)
        self.click_login_button(3)
