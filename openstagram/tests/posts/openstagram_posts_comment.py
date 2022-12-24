from pages.posts.openstagram_create_post_page import OpenStagramCreatePostPage
from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.posts.openstagram_post_page import OpenStagramPostPage


def opst_setup_new_post(browser, base_url, user_login):
    '''Sets up a new post to verify comments section'''
    user_login
    create_post_page = OpenStagramCreatePostPage(browser, base_url)
    create_post_page.load()
    create_post_page.do_create_post('Test Post Title', 'This is the description of the Test Post')
    dashboard_page = OpenStagramDashboardPage(browser, base_url)
    dashboard_page.click_post_by_title('Test Post Title', 1)


def opst_verify_comment_form_elements(browser, base_url):
    '''Verify comment section elements are displayed'''
    post_page = OpenStagramPostPage(browser, base_url)
    assert post_page.find_add_comment_label() is not None
    assert post_page.find_comment_label() is not None
    assert post_page.find_comment_input() is not None
    assert post_page.find_comment_button() is not None
    assert post_page.find_no_comments_label() is not None


def opst_verify_successful_comment(browser, base_url):
    '''Verify the successful submit of a Comment in a Post'''
    post_page = OpenStagramPostPage(browser, base_url)
    post_page.fill_comment_input('Test comment')
    post_page.click_comment_button(1)
    assert post_page.find_successful_comment_label() is not None
    assert post_page.find_no_comments_label() is None


def opst_teardown_new_post(browser, base_url):
    '''Teardown the created post'''
    post_page = OpenStagramPostPage(browser, base_url)
    post_page.click_delete_post_button(1)
