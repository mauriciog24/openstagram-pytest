from pytest import mark, param

from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage


@mark.parametrize(
    'username,expected_result',
    [
        param('SU', 'must be at least 3 characters'),
        param('UsernameGreaterThanTwentyCharacters', 'must not be greater than 20 characters')
    ]
)
def opst_verify_edit_profile_valid_username(browser, login, username, expected_result):
    '''
    Verify the "must be at least 3 characters", "must not be greater than 20 characters"
    and "is invalid" messages when username is invalid"
    '''
    login
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    edit_profile_page.fill_username_input(username)
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('username', expected_result) is not None


@mark.parametrize(
    'username',
    [
        param('register'),
        param('login'),
        param('logout'),
        param('edit-profile'),
        param('images'),
        param('posts')
    ]
)
def opst_verify_username_is_not_an_existing_url(browser, username):
    '''Verify the "is invalid" message when username is an existing url'''
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    edit_profile_page.fill_username_input(username)
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
