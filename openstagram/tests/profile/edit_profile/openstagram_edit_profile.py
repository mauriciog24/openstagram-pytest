from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage
from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_successful_edit_profile(browser, base_url, user_login):
    ''''''
    user_login
    dashboard_page = OpenStagramDashboardPage(browser, base_url)
    dashboard_page.click_edit_profile_button('test')
    # Changes the username
    edit_profile_page = OpenStagramEditProfilePage(browser, base_url)
    edit_profile_page.fill_username_input('modified-username')
    edit_profile_page.click_edit_profile_button(1)
    # Checks URL changed
    assert browser.current_url != f'{base_url}/test'
    assert browser.current_url == f'{base_url}/modified-username'
    # Checks Username header changed
    assert dashboard_page.find_profile_header('test') is None
    assert dashboard_page.find_profile_header('modified-username') is not None
    # Checks Username label changed
    assert dashboard_page.find_username_label('test') is None
    assert dashboard_page.find_username_label('modified-username') is not None
    # Checks User Profile button changed
    base_page = OpenStagramBasePage(browser)
    assert base_page.find_user_profile_button('test') is None
    assert base_page.find_user_profile_button('modified-username') is not None


def opst_teardown(browser, base_url):
    '''Teardown the edit profile username change'''
    edit_profile_page = OpenStagramEditProfilePage(browser, base_url)
    edit_profile_page.load()
    edit_profile_page.fill_username_input('Test')
    edit_profile_page.click_edit_profile_button(1)
