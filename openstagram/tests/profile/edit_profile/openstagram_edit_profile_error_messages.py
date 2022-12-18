from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage


def opst_verify_edit_profile_valid_username(browser, base_url, user_login):
    '''
    Verify the "must be at least 3 characters", "must not be greater than 20 characters"
    and "is invalid" messages when username is invalid"
    '''
    user_login
    edit_profile_page = OpenStagramEditProfilePage(browser, base_url)
    edit_profile_page.load()
    # Username less than 3 characters
    edit_profile_page.fill_username_input('SU')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('username', 'must be at least 3 characters') is not None
    # Username greater than 20 characters
    edit_profile_page.fill_username_input('UsernameGreaterThanTwentyCharacters')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('username', 'must not be greater than 20 characters') is not None
    # Username is invalid
    edit_profile_page.fill_username_input('register')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
    edit_profile_page.fill_username_input('login')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
    edit_profile_page.fill_username_input('logout')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
    edit_profile_page.fill_username_input('edit-profile')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
    edit_profile_page.fill_username_input('images')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
    edit_profile_page.fill_username_input('posts')
    edit_profile_page.click_edit_profile_button()
    assert edit_profile_page.find_field_error_message('selected username', 'is invalid') is not None
