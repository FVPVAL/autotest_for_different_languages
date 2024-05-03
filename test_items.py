from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_contains_an_add_button(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed, "there is no add to cart button"
