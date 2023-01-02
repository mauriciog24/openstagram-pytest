from pytest import mark, param

from pages.posts.openstagram_create_post_page import OpenStagramCreatePostPage
from pages.openstagram_base_page import OpenStagramBasePage


@mark.parametrize(
    'title,expected_result',
    [
        param('Title greater than 255 characters' * 8, 'must not be greater than 255 characters')
    ]
)
def opst_verify_post_valid_title(browser, login, title, expected_result):
    '''Verify the "field is required" and "must not be greater than 255 characters" messages when title is invalid'''
    login
    base_page = OpenStagramBasePage(browser[0])
    base_page.click_create_button(1)
    create_post_page = OpenStagramCreatePostPage(*browser)
    # Title is required
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('title', 'field is required') is not None
    # Title greater than 255 characters
    create_post_page.load()
    create_post_page.fill_title_input(title)
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('title', expected_result) is not None


def opst_verify_post_valid_description(browser):
    '''Verify the "field is required" message when description is empty'''
    create_post_page = OpenStagramCreatePostPage(*browser)
    create_post_page.load()
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('description', 'field is required') is not None


def opst_verify_post_valid_image(browser):
    '''Verify the "field is required" message when image is empty'''
    create_post_page = OpenStagramCreatePostPage(*browser)
    create_post_page.load()
    create_post_page.click_create_post_button()
    assert create_post_page.find_field_error_message('image', 'field is required') is not None
