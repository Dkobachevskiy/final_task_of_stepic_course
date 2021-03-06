import pytest

from final_task_of_stepic_course.pages.basket_page import BasketPage
from final_task_of_stepic_course.pages.locators import MainPageLocators

from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(
            self,
            browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_be_empty_basket()
        page.should_be_basket_have_empty_message()

    def test_guest_should_be_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
