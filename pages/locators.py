from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_ALERT_ADDED = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']/div[@class='alertinner ']/strong")
    BASKET_ALERT_ADDED_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_ALERT_PRICE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/div[@class='alertinner ']/p/strong")
    BASKET_ALERT_PRICE_NAME = (By.CSS_SELECTOR, "p.price_color")