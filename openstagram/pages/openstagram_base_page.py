from selenium.webdriver.common.by import By

from utils.openstagram_utils import OpenStagramUtils


class OpenStagramBasePage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Base page
    '''

    # Navbar section
    HOME_BUTTON = (By.XPATH, '//a[contains(text(),"OpenStagram")]')
    # Guest
    LOGIN_BUTTON = (By.XPATH, '//a[contains(text(),"Login")]')
    REGISTER_BUTTON = (By.XPATH, '//a[contains(text(),"Register")]')
    # Auth
    CREATE_BUTTON = (By.XPATH, '( //*[local-name()="svg"]//parent::a)[1]')
    USER_PROFILE_BUTTON = (By.XPATH, '//a[contains(text(),"Hi,")]')
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(),"Logout")]')
    # Footer section
    FOOTER_LABEL = (By.XPATH, '//footer[contains(text(),"OpenStagram - All rights reserved")]')

    def __init__(self, browser):
        '''Initialize the Utils class'''
        self.utils = OpenStagramUtils(browser)

    def find_home_button(self):
        '''Finds the Home button in the navbar'''
        return self.utils.find_element(self.HOME_BUTTON)

    def click_home_button(self, timeout=0):
        '''Clicks the Home button in the navbar'''
        self.utils.click_element(self.HOME_BUTTON, timeout)

    def find_login_button(self):
        '''Finds the Login button in the navbar'''
        return self.utils.find_element(self.LOGIN_BUTTON)

    def click_login_button(self, timeout=0):
        '''Clicks the Login button in the navbar'''
        self.utils.click_element(self.LOGIN_BUTTON, timeout)

    def find_register_button(self):
        '''Finds the Register button in the navbar'''
        return self.utils.find_element(self.REGISTER_BUTTON)

    def click_register_button(self, timeout=0):
        '''Clicks the Register button in the navbar'''
        self.utils.click_element(self.REGISTER_BUTTON, timeout)

    def find_create_button(self):
        '''Finds the Create button in the navbar'''
        return self.utils.find_element(self.CREATE_BUTTON)

    def click_create_button(self, timeout=0):
        '''Clicks the Create button in the navbar'''
        self.utils.click_element(self.CREATE_BUTTON, timeout)

    def find_user_profile_button(self):
        '''Finds the User Profile button in the navbar'''
        return self.utils.find_element(self.USER_PROFILE_BUTTON)

    def click_user_profile_button(self, timeout=0):
        '''Clicks the User Profile button in the navbar'''
        self.utils.click_element(self.USER_PROFILE_BUTTON, timeout)

    def find_logout_button(self):
        '''Finds the Logout button in the navbar'''
        return self.utils.find_element(self.LOGOUT_BUTTON)

    def click_home_button(self, timeout=0):
        '''Clicks the Logout button in the navbar'''
        self.utils.click_element(self.LOGOUT_BUTTON, timeout)

    def find_footer_label(self):
        '''Finds the Footer label'''
        return self.utils.find_element(self.FOOTER_LABEL)
