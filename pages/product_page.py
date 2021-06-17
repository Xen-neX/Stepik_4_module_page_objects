from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):


    def click_basket_button(self):
        # реализуйте проверку, что есть кнопка
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "Button is not presented"
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def should_be_added(self):
        # проверка названия продукта
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERT_ADDED), "Alert about adding not presented"
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERT_ADDED_NAME), "Product name not presented"
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERT_ADDED).text == self.browser.find_element(*ProductPageLocators.BASKET_ALERT_ADDED_NAME).text, "Product names not matched"

    def should_be_price(self):
        # проверка названия продукта
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE), "Alert about price not presented"
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE_NAME), "Product price not presented"
        assert self.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BASKET_ALERT_PRICE_NAME).text, "Product prices not matched"
