from selenium.webdriver.common.by import By
from random import randrange
from os import getcwd

from utils.openstagram_utils import OpenStagramUtils


class OpenStagramCreatePostPage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Create Post page
    '''

    CREATE_POST_URL = '/posts/create'
    # Page title
    CREATE_NEW_POST_HEADER = (By.XPATH, '//h2[contains(text(),"Create a new Post")]')
    # Title field
    TITLE_LABEL = (By.XPATH, '//label[contains(text(),"Title")]')
    TITLE_INPUT = (By.XPATH, '//input[@placeholder="Post title"]')
    # Description field
    DESCRIPTION_LABEL = (By.XPATH, '//label[contains(text(),"Description")]')
    DESCRIPTION_INPUT = (By.XPATH, '//textarea[@placeholder="Post description"]')
    # Image field
    IMAGE_INPUT = (By.CSS_SELECTOR, '.dz-hidden-input')
    # Submit button
    CREATE_POST_BUTTON = (By.XPATH, '//input[@value="Create Post"]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = f'{base_url}{self.CREATE_POST_URL}'

    def load(self):
        '''Redirects to the /posts/create page'''
        self.utils.load_page(self.page_url, 3)

    def find_create_new_post_header(self):
        '''Finds the Create a new Post header'''
        return self.utils.find_element(self.CREATE_NEW_POST_HEADER)

    def find_title_label(self):
        '''Finds the Title label in the Create Post form'''
        return self.utils.find_element(self.TITLE_LABEL)

    def find_title_input(self):
        '''Finds the Title input in the Create Post form'''
        return self.utils.find_element(self.TITLE_INPUT)

    def fill_title_input(self, value, timeout=0):
        '''Fills the Title input in the Create Post form'''
        self.utils.fill_element(self.TITLE_INPUT, value, timeout)

    def find_description_label(self):
        '''Finds the Description label in the Create Post form'''
        return self.utils.find_element(self.DESCRIPTION_LABEL)

    def find_description_input(self):
        '''Finds the Description input in the Create Post form'''
        return self.utils.find_element(self.DESCRIPTION_INPUT)

    def fill_description_input(self, value, timeout=0):
        '''Fills the Description input in the Create Post form'''
        self.utils.fill_element(self.DESCRIPTION_INPUT, value, timeout)

    def fill_image_input(self, timeout=0):
        '''Fills the Image input in the Create Post form'''
        self.utils.fill_element(
            self.IMAGE_INPUT,
            f'{getcwd()}//utils/img/{randrange(1, 20)}.jpg',
            timeout
        )

    def find_create_post_button(self):
        '''Finds the Create Post button in the Create Post form'''
        return self.utils.find_element(self.CREATE_POST_BUTTON)

    def click_create_post_button(self, timeout=0):
        '''Clicks the Create Post button in the Create Post form'''
        self.utils.click_element(self.CREATE_POST_BUTTON, timeout)

    def find_field_error_message(self, field_name, error_message):
        '''Finds a specific error message in the Create Post form'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"The {field_name} {error_message}.")]'))

    def do_create_post(self, title, description):
        '''Do the Create Post process successfully'''
        self.fill_title_input(title, 1)
        self.fill_description_input(description, 1)
        self.fill_image_input(1)
        self.click_create_post_button(3)
