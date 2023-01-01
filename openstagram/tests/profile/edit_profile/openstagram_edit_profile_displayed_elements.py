from pages.profile.openstagram_edit_profile_page import OpenStagramEditProfilePage
from pages.openstagram_base_page import OpenStagramBasePage


def opst_verify_edit_profile_form_elements(browser, login):
    '''Verify edit profile elements are displayed'''
    login
    edit_profile_page = OpenStagramEditProfilePage(*browser)
    edit_profile_page.load()
    # Header displayed
    assert edit_profile_page.find_edit_profile_header('test') is not None
    # Username field
    assert edit_profile_page.find_username_label() is not None
    assert edit_profile_page.find_username_input() is not None
    # Profile Image field
    assert edit_profile_page.find_profile_image_label() is not None
    assert edit_profile_page.find_profile_image_input() is not None
    # Edit Profile button
    assert edit_profile_page.find_edit_profile_button() is not None


def opst_verify_edit_profile_navbar_buttons(browser):
    '''Verify the navbar buttons are the correct to be displayed'''
    base_page = OpenStagramBasePage(browser[0])
    # Buttons should be displayed
    assert base_page.find_home_button() is not None
    assert base_page.find_create_button() is not None
    assert base_page.find_user_profile_button() is not None
    assert base_page.find_logout_button() is not None
    # Buttons shouldn't be displayed
    assert base_page.find_login_button() is None
    assert base_page.find_register_button() is None
