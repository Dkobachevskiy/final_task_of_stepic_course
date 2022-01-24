from datetime import datetime

import pytest

from .pages.generator import generate_random_string
from .pages.locators import (BasketPageLocators, LoginPageLocators,
                             ProductPageLocators)
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                       marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_basket_message()
    page.should_be_alerts_with_product_name()
    page.should_be_correct_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)
        self.page.open()
        email = (
            generate_random_string(10) + str(datetime.now().microsecond)
            + '@email.com'
        )
        password = generate_random_string(9)
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_LINK_PROMO
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_add_basket_message()
        page.should_be_alerts_with_product_name()
        page.should_be_correct_price()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
