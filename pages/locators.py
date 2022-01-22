from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    MESSAGE_WITH_BASKET_COST = (By.CSS_SELECTOR, "div.alertinner>p>strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p>a")
