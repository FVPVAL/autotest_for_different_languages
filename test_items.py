from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."


def test_contains_an_add_button(browser):
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")) == 1, "there is no add to cart button"
