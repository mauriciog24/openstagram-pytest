from selenium.webdriver.common.by import By

from utils.openstagram_utils import OpenStagramUtils


class OpenStagramHomePage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Home page
    '''

    HOME_URL = '/'
    # Page title
    HOME_HEADER = (By.XPATH, '//h2[contains(text(),"Home")]')
    # Posts section
    NO_POSTS_LABEL = (By.XPATH, '//p[contains(text(),"No posts available")]')
     # Pagination
    PREVIOUS_PAGE_BUTTON = (By.XPATH, '//a[@rel="prev"]')
    NEXT_PAGE_BUTTON = (By.XPATH, '//a[@rel="next"]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = f'{base_url}{self.HOME_URL}'

    def load(self):
        '''Redirects to the / page'''
        self.utils.load_page(self.page_url, 3)

    def find_home_header(self):
        '''Finds the Home header in the Home page'''
        return self.utils.find_element(self.HOME_HEADER)

    def find_post_by_title(self, title):
        '''Finds a Post by its title in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//img[@alt="{title} - post image"]//parent::a'))

    def click_post_by_title(self, title, timeout=0):
        '''Clicks a Post by its title in the Dashboard page'''
        self.utils.click_element((By.XPATH, f'//img[@alt="{title} - post image"]//parent::a'), timeout)

    def find_showing_results_label(self, initial, last, total):
        '''Finds the Showing "initial" to "last" of "total" results'''
        return self.utils.find_element((
            By.XPATH,
            f'//span[text()="{initial}"]//following::span[text()="{last}"]//following::span[text()="{total}"]//parent::p'
        ))

    def find_pagination_button(self, position):
        '''Finds a specific pagination button'''
        return self.utils.find_element((By.XPATH, f'//a[contains(text(),"{position}")]'))

    def click_pagination_button(self, position, timeout=0):
        '''Clicks a specific pagination button'''
        self.utils.click_element((By.XPATH, f'//a[contains(text(),"{position}")]'), timeout)

    def find_previous_pagination_button(self):
        '''Finds the Previous button in the pagination section'''
        return self.utils.find_element(self.PREVIOUS_PAGE_BUTTON)

    def click_previous_pagination_button(self, timeout=0):
        '''Clicks the Previous button in the pagination section'''
        self.utils.click_element(self.PREVIOUS_PAGE_BUTTON, timeout)

    def find_next_pagination_button(self):
        '''Finds the Next button in the pagination section'''
        return self.utils.find_element(self.NEXT_PAGE_BUTTON)

    def click_next_pagination_button(self, timeout=0):
        '''Clicks the Next button in the pagination section'''
        self.utils.click_element(self.NEXT_PAGE_BUTTON, timeout)

    def find_no_posts_label(self):
        '''Finds the No posts available label in the Home page'''
        return self.utils.find_element(self.NO_POSTS_LABEL)
