from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.BASKET_BUTTON
        )
        add_button.click()

    def should_be_add_basket_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "there is no message about adding to basket"

    def should_be_alerts_with_product_name(self):
        prod_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        all_with_prod_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text
        assert prod_name == all_with_prod_name, \
            "the message about adding to the basket does not "\
            "contain the product name"

    def should_be_correct_price(self):
        product_price_on_page = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        product_price_in_message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_BASKET_COST
        ).text
        assert product_price_on_page in product_price_in_message, \
            "the cost of the basket does not match the price of the product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message has not disappeared, but it should"

    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
