from pages.posts.openstagram_post_page import OpenStagramPostPage


def opst_verify_comment_form_elements(browser, login, new_post):
    '''Verify comment section elements are displayed'''
    login
    new_post
    post_page = OpenStagramPostPage(*browser)
    assert post_page.find_add_comment_label() is not None
    assert post_page.find_comment_label() is not None
    assert post_page.find_comment_input() is not None
    assert post_page.find_comment_button() is not None
    assert post_page.find_no_comments_label() is not None


def opst_verify_successful_comment(browser):
    '''Verify the successful submit of a Comment in a Post'''
    post_page = OpenStagramPostPage(*browser)
    post_page.fill_comment_input('Test comment')
    post_page.click_comment_button(1)
    assert post_page.find_successful_comment_label() is not None
    assert post_page.find_no_comments_label() is None
