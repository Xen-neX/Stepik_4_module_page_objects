from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_item(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM), \
            "Item is presented, but should not be"

    def should_be_empty(self):
        # проверка названия продукта
        assert self.browser.find_element(*BasketPageLocators.EMPTY), "Basket is empty"
