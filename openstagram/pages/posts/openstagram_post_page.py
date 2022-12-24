from selenium.webdriver.common.by import By

from utils.openstagram_utils import OpenStagramUtils


class OpenStagramPostPage:
    '''
    This Page contains the locators and methods to interact with the OpenStagram Post page
    '''

    # Post section
    LIKE_BUTTON = (By.XPATH, '//*[local-name()="svg"]//parent::button')
    DELETE_POST_BUTTON = (By.XPATH, '//input[@value="Delete Post"]')
    # Comments section
    ADD_COMMENT_LABEL = (By.XPATH, '//p[contains(text(),"Add a Comment")]')
    SUCCESSFUL_COMMENT_LABEL = (By.XPATH, '//div[contains(text(),"Successful comment")]')
    NO_COMMENTS_LABEL = (By.XPATH, '//p[contains(text(),"This post doesn\'t have comments yet")]')
    # Comment field
    COMMENT_LABEL = (By.XPATH, '//label[contains(text(),"Comment")]')
    COMMENT_INPUT = (By.XPATH, '//textarea[@placeholder="Add a comment"]')
    # Submit button
    COMMENT_BUTTON = (By.XPATH, '//input[@value="Comment"]')

    def __init__(self, browser, base_url):
        '''Initialize the Utils class and URL'''
        self.utils = OpenStagramUtils(browser)
        self.page_url = base_url

    def load(self, username, post):
        '''Redirects to the /username/posts/post page'''
        self.utils.load_page(f'{self.page_url}/{username}/posts/{post}', 3)

    def find_post_title(self, title):
        '''Finds the Post title in the Post page'''
        return self.utils.find_element((By.XPATH, f'//h2[contains(text(),"{title}")]'))

    def find_post_image(self, title):
        '''Finds the Post image in the Post page'''
        return self.utils.find_element((By.XPATH, f'//img[@alt="{title} - post image"]'))

    def find_like_button(self):
        '''Finds the Like button in the Post page'''
        return self.utils.find_element(self.LIKE_BUTTON)

    def click_like_button(self, timeout=0):
        '''Clicks the Like button in the Post page'''
        self.utils.click_element(self.LIKE_BUTTON, timeout)

    def find_like_button_by_status(self, status):
        '''Finds the Like button by its status in the Post page'''
        return self.utils.find_element((By.XPATH, f'//*[local-name()="svg" and contains(@fill,"{status}")]'))

    def find_likes_label(self, likes_count):
        '''Finds the Likes label in the Post page'''
        return self.utils.find_element((
            By.XPATH,
            f'//span[contains(text(),"Likes")]//parent::p[contains(text(),"{likes_count}")]'
        ))

    def find_post_username(self, username):
        '''Finds the Post username in the Post page'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"{username}")]'))

    def find_post_description(self, username, description):
        '''Finds the Post description in the Post page'''
        return self.utils.find_element((
            By.XPATH,
            f'//p[contains(text(),"{username}")]//following::p[contains(text(),"{description}")]'
        ))

    def find_delete_post_button(self):
        '''Finds the Delete Post button in the Post page'''
        return self.utils.find_element(self.DELETE_POST_BUTTON)

    def click_delete_post_button(self, timeout=0):
        '''Clicks the Delete Post button in the Post page'''
        self.utils.click_element(self.DELETE_POST_BUTTON, timeout)

    def find_add_comment_label(self):
        '''Finds the Add a Comment label in the Comment form'''
        return self.utils.find_element(self.ADD_COMMENT_LABEL)

    def find_successful_comment_label(self):
        '''Finds the Successful comment label in the Comment form'''
        return self.utils.find_element(self.SUCCESSFUL_COMMENT_LABEL)

    def find_no_comments_label(self):
        '''Finds the This post doesn't have comments yet label in the Comment form'''
        return self.utils.find_element(self.NO_COMMENTS_LABEL)

    def find_comment_label(self):
        '''Finds the Comment label in the Comment form'''
        return self.utils.find_element(self.COMMENT_LABEL)

    def find_comment_input(self):
        '''Finds the Comment input in the Comment form'''
        return self.utils.find_element(self.COMMENT_INPUT)

    def fill_comment_input(self, value, timeout=0):
        '''Fills the Comment input in the Comment form'''
        self.utils.fill_element(self.COMMENT_INPUT, value, timeout)

    def find_comment_button(self):
        '''Finds the Comment button in the Comment form'''
        return self.utils.find_element(self.COMMENT_BUTTON)

    def click_comment_button(self, timeout=0):
        '''Clicks the Comment button in the Comment form'''
        return self.utils.click_element(self.COMMENT_BUTTON, timeout)

    def find_specific_comment(self, username, comment):
        '''Finds a specific Comment by its username and comment in the Comment form'''
        return self.utils.find_element((
            By.XPATH,
            f'//a[contains(text(),"{username}")]//following::p[contains(text(),"{comment}")]'
        ))

    def find_field_error_message(self, field_name, error_message):
        '''Finds a specific error message in the Comment form'''
        return self.utils.find_element((By.XPATH, f'//p[contains(text(),"The {field_name} {error_message}.")]'))
