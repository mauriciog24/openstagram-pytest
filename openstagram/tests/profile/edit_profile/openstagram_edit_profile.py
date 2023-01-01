from pytest import fixture

from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage
from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_successful_edit_profile(browser, login):
    '''Verify Profile is successfully edited'''
    login
    dashboard_page = OpenStagramDashboardPage(*browser)
    dashboard_page.click_edit_profile_button('test')
    # Changes the username
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.do_edit_profile('modified-username')
    # Checks URL changed
    assert browser[0].current_url != f'{browser[1]}/test'
    assert browser[0].current_url == f'{browser[1]}/modified-username'
    # Checks Username header changed
    assert dashboard_page.find_profile_header('test') is None
    assert dashboard_page.find_profile_header('modified-username') is not None
    # Checks Username label changed
    assert dashboard_page.find_username_label('test') is None
    assert dashboard_page.find_username_label('modified-username') is not None
    # Checks User Profile button changed
    base_page = OpenStagramBasePage(browser[0])
    assert base_page.find_user_profile_button('test') is None
    assert base_page.find_user_profile_button('modified-username') is not None


@fixture(scope='module', autouse=True)
def teardown_edit_profile(browser):
    '''Teardown the edit profile username change'''
    yield
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    edit_profile_page.fill_username_input('Test')
    edit_profile_page.click_edit_profile_button(1)
