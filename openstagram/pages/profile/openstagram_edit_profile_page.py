from selenium.webdriver.common.by import By

from utils.openstagram_utils import OpenStagramUtils


class OpenStagramEditProfilePage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Edit Profile page
    '''

    EDIT_PROFILE_URL = '/edit-profile'
    # Username field
    USERNAME_LABEL = (By.XPATH, '//label[contains(text(),"Username")]')
    USERNAME_INPUT = (By.XPATH, '//input[@placeholder="Your username"]')
    # Profile Image field
    PROFILE_IMAGE_LABEL = (By.XPATH, '//label[contains(text(),"Profile Image")]')
    PROFILE_IMAGE_INPUT = (By.XPATH, '//input[@type="file"]')
    # Submit button
    EDIT_PROFILE_BUTTON = (By.XPATH, '//input[@value="Edit Profile"]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = f'{base_url}{self.EDIT_PROFILE_URL}'

    def load(self):
        '''Redirects to the /edit-profile page'''
        self.utils.load_page(self.page_url, 3)

    def find_edit_profile_header(self, username):
        '''Finds the Edit Profile header'''
        return self.utils.find_element((By.XPATH, f'//h2[contains(text(),"Edit Profile: {username}")]'))

    def find_username_label(self):
        '''Finds the Username label in the Edit Profile form'''
        return self.utils.find_element(self.USERNAME_LABEL)

    def find_username_input(self):
        '''Finds the Username input in the Edit Profile form'''
        return self.utils.find_element(self.USERNAME_INPUT)

    def fill_username_input(self, value, timeout=0):
        '''Fills the Username input in the Edit Profile form'''
        self.utils.clear_element(self.USERNAME_INPUT, 1)
        self.utils.fill_element(self.USERNAME_INPUT, value, timeout)

    def find_profile_image_label(self):
        '''Finds the Profile Image label in the Edit Profile form'''
        return self.utils.find_element(self.PROFILE_IMAGE_LABEL)

    def find_profile_image_input(self):
        '''Finds the Profile Image input in the Edit Profile form'''
        return self.utils.find_element(self.PROFILE_IMAGE_INPUT)

    def fill_profile_image_input(self, value, timeout=0):
        '''Fills the Profile Image input in the Edit Profile form'''
        self.utils.fill_element(self.PROFILE_IMAGE_INPUT, f'utils/img/{value}.jpg', timeout)

    def find_edit_profile_button(self):
        '''Finds the Edit Profile button in the Edit Profile form'''
        return self.utils.find_element(self.EDIT_PROFILE_BUTTON)

    def click_edit_profile_button(self, timeout=0):
        '''Clicks the Edit Profile button in the Edit Profile form'''
        self.utils.click_element(self.EDIT_PROFILE_BUTTON, timeout)

    def find_field_error_message(self, field_name, error_message):
        '''Finds a specific error message in the Registration form'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"The {field_name} {error_message}.")]'))

    def do_edit_profile(self, username, file):
        '''Do the Edit Profile process successfully'''
        self.fill_username_input(username, 1)
        self.fill_profile_image_input(file, 2)
        self.click_edit_profile_button(3)
