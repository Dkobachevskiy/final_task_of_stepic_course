from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "Basket is not empty, but it should be"

    def basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "Basket is empty, but it should not"

    def basket_have_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), "text empty basket is missing, but it should be"

    def basket_dont_have_empty_message(self):
        assert self.is_not_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), "text empty basket is present, but it should not"
