from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT = (By.XPATH, "//button[@value = 'Register']")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_ALERT_ADDED = (
        By.XPATH,
        "//div[@class='alert alert-safe alert-noicon alert-success  fade in']/div[@class='alertinner ']/strong")
    BASKET_ALERT_ADDED_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_ALERT_PRICE = (
        By.XPATH,
        "//div[@class='alert alert-safe alert-noicon alert-info  fade in']/div[@class='alertinner ']/p/strong")
    BASKET_ALERT_PRICE_NAME = (By.CSS_SELECTOR, "p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_TOP = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEM = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY = (By.CSS_SELECTOR, "#content_inner")
