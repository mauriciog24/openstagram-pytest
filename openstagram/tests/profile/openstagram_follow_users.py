from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.auth.openstagram_register_page import OpenStagramRegisterPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_setup_new_user(browser, base_url):
    '''Sets up a new user to verify follow and unfollow buttons'''
    user = {
        'name': 'User Test2',
        'username': 'Test2',
        'email': 'test2@email.com',
        'password': 'pass123'
    }
    # Do register
    register_page = OpenStagramRegisterPage(browser, base_url)
    register_page.load()
    register_page.do_register(user['name'], user['username'], user['email'], user['password'])
    # Check if User is registered
    if register_page.find_field_error_message('username', 'has already been taken') is None:
        # Logs out the created user
        base_page = OpenStagramBasePage(browser)
        base_page.click_logout_button(3)


def opst_verify_follow_users(browser, base_url, user_login):
    '''Verify the properly Follow functionality'''
    user_login
    dashboard_page = OpenStagramDashboardPage(browser, base_url)
    dashboard_page.load('test2')
    # Check buttons visibility
    assert dashboard_page.find_follow_button() is not None
    assert dashboard_page.find_unfollow_button() is None
    dashboard_page.click_follow_button(1)
    # Checks follow count label
    assert dashboard_page.find_followers_label(1) is not None
    base_page = OpenStagramBasePage(browser)
    base_page.click_user_profile_button()
    assert dashboard_page.find_following_label(1) is not None


def opst_verify_unfollow_users(browser, base_url):
    '''Verify the properly Unfollow functionality'''
    dashboard_page = OpenStagramDashboardPage(browser, base_url)
    dashboard_page.load('test2')
    # Check buttons visibility
    assert dashboard_page.find_unfollow_button() is not None
    assert dashboard_page.find_follow_button() is None
    dashboard_page.click_unfollow_button(1)
    # Checks follow count label
    assert dashboard_page.find_followers_label(0) is not None
    base_page = OpenStagramBasePage(browser)
    base_page.click_user_profile_button()
    assert dashboard_page.find_following_label(0) is not None
