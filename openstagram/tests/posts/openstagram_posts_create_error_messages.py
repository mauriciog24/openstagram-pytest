from pages.posts.openstagram_create_post_page import OpenStagramCreatePostPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_post_valid_title(browser, base_url, user_login):
    '''Verify the "field is required" and "must not be greater than 255 characters" messages when title is invalid'''
    user_login
    base_page = OpenStagramBasePage(browser)
    base_page.click_create_button(1)
    create_post_page = OpenStagramCreatePostPage(browser, base_url)
    # Title is required
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('title', 'field is required') is not None
    # Title greater than 255 characters
    create_post_page.load()
    create_post_page.fill_title_input(
        'Title greater than 255 characters-\
         Title greater than 255 characters-\
         Title greater than 255 characters-\
         Title greater than 255 characters-\
         Title greater than 255 characters-\
         Title greater than 255 characters-\
         Title greater than 255 characters-\
         Title greater than 255 characters'
    )
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('title', 'must not be greater than 255 characters') is not None


def opst_verify_post_valid_description(browser, base_url):
    '''Verify the "field is required" message when description is empty'''
    create_post_page = OpenStagramCreatePostPage(browser, base_url)
    create_post_page.load()
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('description', 'field is required') is not None


def opst_verify_post_valid_image(browser, base_url):
    '''Verify the "field is required" message when image is empty'''
    create_post_page = OpenStagramCreatePostPage(browser, base_url)
    create_post_page.load()
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('image', 'field is required') is not None
