from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert button, "Add to card button isn't found"