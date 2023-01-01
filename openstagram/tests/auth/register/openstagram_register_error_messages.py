from pages.auth.openstagram_register_page import OpenStagramRegisterPage


def opst_verify_register_required_fields_message(browser):
    '''Verify the "field is required" message for the form fields'''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.click_register_button()
    assert register_page.find_field_error_message('name', 'field is required') is not None
    assert register_page.find_field_error_message('username', 'field is required') is not None
    assert register_page.find_field_error_message('email', 'field is required') is not None
    assert register_page.find_field_error_message('password', 'field is required') is not None


def opst_verify_register_valid_name(browser):
    '''Verify the "must not be greater than 30 characters" message when name is invalid'''
    register_page = OpenStagramRegisterPage(*browser)
    register_page.load()
    register_page.fill_name_input('NameGreaterThanThirtyCharacters')
    register_page.click_register_button()
    assert register_page.find_field_error_message('name', 'must not be greater than 30 characters') is not None


def opst_verify_register_valid_username(browser):
    '''
    Verify the "must be at least 3 characters" and "must not be greater than 20 characters"
    messages when username is invalid
    '''
    register_page = OpenStagramRegisterPage(*browser)
    # Username less than 3 characters
    register_page.load()
    register_page.fill_username_input('SU')
    register_page.click_register_button()
    assert register_page.find_field_error_message('username', 'must be at least 3 characters') is not None
    # Username greater than 20 characters
    register_page.load()
    register_page.fill_username_input('UsernameGreaterThanTwentyCharacters')
    register_page.click_register_button()
    assert register_page.find_field_error_message('username', 'must not be greater than 20 characters') is not None


def opst_verify_register_valid_email(browser):
    '''
    Verify the "must be a valid email address" and "must not be greater than 60 characters"
    messages when email is invalid
    '''
    register_page = OpenStagramRegisterPage(*browser)
    # Invalid email
    register_page.load()
    register_page.fill_email_input('invalidemail.com')
    register_page.click_register_button()
    assert register_page.find_field_error_message('email', 'must be a valid email address') is not None
    # Email grater than 60 characters
    register_page.load()
    register_page.fill_email_input('EmailFieldGreaterThanSixtyCharacters123456789012345@email.com')
    register_page.click_register_button()
    assert register_page.find_field_error_message('email', 'must not be greater than 60 characters') is not None


def opst_verify_register_valid_password(browser):
    '''
    Verify the "must be at least 6 characters" and "confirmation does not match"
    messages when password is invalid
    '''
    register_page = OpenStagramRegisterPage(*browser)
    # Password less than 6 characters
    register_page.load()
    register_page.fill_password_input('12345')
    register_page.fill_password_confirmation_input('12345')
    register_page.click_register_button()
    assert register_page.find_field_error_message('password', 'must be at least 6 characters') is not None
    # Password Confirmation not matching
    register_page.load()
    register_page.fill_password_input('123456')
    register_page.fill_password_confirmation_input('654321')
    register_page.click_register_button()
    assert register_page.find_field_error_message('password', 'confirmation does not match') is not None
