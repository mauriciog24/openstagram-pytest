from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_follow_users(browser, register, login):
    '''Verify the properly Follow functionality'''
    register
    login
    dashboard_page = OpenStagramDashboardPage(*browser)
    dashboard_page.load('test2')
    # Check buttons visibility
    assert dashboard_page.find_follow_button() is not None
    assert dashboard_page.find_unfollow_button() is None
    # Checks follow count label
    dashboard_page.click_follow_button(1)
    assert dashboard_page.find_followers_label(1) is not None
    base_page = OpenStagramBasePage(browser[0])
    base_page.click_user_profile_button()
    assert dashboard_page.find_following_label(1) is not None


def opst_verify_unfollow_users(browser):
    '''Verify the properly Unfollow functionality'''
    dashboard_page = OpenStagramDashboardPage(*browser)
    dashboard_page.load('test2')
    # Check buttons visibility
    assert dashboard_page.find_unfollow_button() is not None
    assert dashboard_page.find_follow_button() is None
    # Checks follow count label
    dashboard_page.click_unfollow_button(1)
    assert dashboard_page.find_followers_label(0) is not None
    base_page = OpenStagramBasePage(browser[0])
    base_page.click_user_profile_button()
    assert dashboard_page.find_following_label(0) is not None
