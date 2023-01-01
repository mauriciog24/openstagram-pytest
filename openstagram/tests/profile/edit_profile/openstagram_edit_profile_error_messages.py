from pytest import mark, param

from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage


def opst_verify_edit_profile_valid_username(browser, login):
    '''
    Verify the "must be at least 3 characters", "must not be greater than 20 characters"
    and "is invalid" messages when username is invalid"
    '''
    login
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    # Username less than 3 characters
    edit_profile_page.fill_username_input('SU')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('username', 'must be at least 3 characters') is not None
    # Username greater than 20 characters
    edit_profile_page.fill_username_input('UsernameGreaterThanTwentyCharacters')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('username', 'must not be greater than 20 characters') is not None


@mark.parametrize(
    "username",
    [
        param("register"),
        param("login"),
        param("logout"),
        param("edit-profile"),
        param("images"),
        param("posts")
    ]
)
def opst_verify_username_is_not_an_existing_url(browser, username):
    # Username is invalid
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    edit_profile_page.fill_username_input(username)
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
