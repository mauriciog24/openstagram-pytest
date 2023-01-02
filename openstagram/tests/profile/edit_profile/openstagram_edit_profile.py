from pytest import fixture, mark, param

from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage
from pages.profile.openstagram_dashboard_page import OpenStagramDashboardPage
from pages.openstagram_base_page import OpenStagramBasePage


@mark.parametrize(
    'username,modified_username',
    [
        param('test', 'modified-username')
    ]
)
def opst_verify_successful_edit_profile(browser, login, username, modified_username):
    '''Verify Profile is successfully edited'''
    login
    dashboard_page = OpenStagramDashboardPage(*browser)
    dashboard_page.click_edit_profile_button(username)
    # Changes the username
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.do_edit_profile(modified_username)
    # Checks URL changed
    assert browser[0].current_url != f'{browser[1]}/{username}'
    assert browser[0].current_url == f'{browser[1]}/{modified_username}'
    # Checks Username header changed
    assert dashboard_page.find_profile_header(username) is None
    assert dashboard_page.find_profile_header(modified_username) is not None
    # Checks Username label changed
    assert dashboard_page.find_username_label(username) is None
    assert dashboard_page.find_username_label(modified_username) is not None
    # Checks User Profile button changed
    base_page = OpenStagramBasePage(browser[0])
    assert base_page.find_user_profile_button(username) is None
    assert base_page.find_user_profile_button(modified_username) is not None


@fixture(scope='module', autouse=True)
def teardown_edit_profile(browser):
    '''Teardown the edit profile username change'''
    yield
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    edit_profile_page.fill_username_input('Test')
    edit_profile_page.click_edit_profile_button(1)
