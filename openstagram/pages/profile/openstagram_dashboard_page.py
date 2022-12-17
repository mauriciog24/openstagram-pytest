from selenium.webdriver.common.by import By

from utils.openstagram_utils import OpenStagramUtils


class OpenStagramDashboardPage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Dashboard page
    '''

    # Profile section
    FOLLOW_BUTTON = (By.XPATH, '//input[@value="Follow"]')
    UNFOLLOW_BUTTON = (By.XPATH, '//input[@value="Unfollow"]')
    # Posts section
    POSTS_HEADER = (By.XPATH, '//h2[contains(text(),"Posts")]')
    NO_POSTS_LABEL = (By.XPATH, '//p[contains(text(),"No posts available")]')
    # Pagination
    PREVIOUS_PAGE_BUTTON = (By.XPATH, '//a[@rel="prev"]')
    NEXT_PAGE_BUTTON = (By.XPATH, '//a[@rel="next"]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = base_url

    def load(self, username):
        '''Redirects to the /username page'''
        self.utils.load_page(f'{self.page_url}/{username}', 3)

    def find_profile_header(self, username):
        '''Finds the username's Profile header in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//h2[contains(text(),"{username}\'s Profile")]'))

    def find_username_label(self, username):
        '''Finds the username label in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"{username}")]'))

    def find_edit_profile_button(self, username):
        '''Finds the Edit Profile button in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"{username}")]//following::a'))

    def click_edit_profile_button(self, username, timeout=0):
        '''Clicks the Edit Profile button in the Dashboard page'''
        return self.utils.click_element((By.XPATH, f'//p[contains(text(),"{username}")]//following::a'), timeout)

    def find_followers_label(self, followers_count):
        '''Finds the Followers label in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//span[contains(text(),"Follower")]//parent::p[contains(text(),"{followers_count}")]'))

    def find_following_label(self, following_count):
        '''Finds the Following label in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//span[contains(text(),"Following")]//parent::p[contains(text(),"{following_count}")]'))

    def find_posts_label(self, posts_count):
        '''Finds the Posts label in the Dashboard page'''
        return self.utils.find_element((By.XPATH, f'//span[contains(text(),"Posts")]//parent::p[contains(text(),"{posts_count}")]'))

    def find_follow_button(self):
        '''Finds the Follow button in the Dashboard page'''
        return self.utils.find_element(self.FOLLOW_BUTTON)

    def click_follow_button(self, timeout=0):
        '''Clicks the Follow button in the Dashboard page'''
        return self.utils.click_element(self.FOLLOW_BUTTON, timeout)

    def find_unfollow_button(self):
        '''Finds the Unfollow button in the Dashboard page'''
        return self.utils.find_element(self.UNFOLLOW_BUTTON)

    def click_unfollow_button(self, timeout=0):
        '''Clicks the Unfollow button in the Dashboard page'''
        return self.utils.click_element(self.UNFOLLOW_BUTTON, timeout)

    def find_posts_header(self):
        '''Finds the Posts header in the Dashboard page'''
        return self.utils.find_element(self.POSTS_HEADER)

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
        '''Finds the No posts available label in the Dashboard page'''
        return self.utils.find_element(self.NO_POSTS_LABEL)
