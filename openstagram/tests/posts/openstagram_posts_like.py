from pages.posts.openstagram_post_page import OpenStagramPostPage


def opst_verify_like_post(browser, login, new_post):
    '''Verify the Like functionality in a specific Post'''
    login
    new_post
    post_page = OpenStagramPostPage(*browser)
    post_page.click_like_button(1)
    assert post_page.find_like_button_by_status('red') is not None
    assert post_page.find_like_button_by_status('white') is None
    assert post_page.find_likes_label(1) is not None


def opst_verify_dislike_post(browser):
    '''Verify the Dislike functionality in a specific Post'''
    post_page = OpenStagramPostPage(*browser)
    post_page.click_like_button(1)
    assert post_page.find_like_button_by_status('white') is not None
    assert post_page.find_like_button_by_status('red') is None
    assert post_page.find_likes_label(0) is not None
