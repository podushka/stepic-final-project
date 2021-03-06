from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span.btn-group > a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class BasketPageLocators():
    EMPTY_BASKET_INFO = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEM = (By.CSS_SELECTOR, '#basket_formset > div.basket-items')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCES_MESSAGES = (By.CSS_SELECTOR, '#messages')
    SUCCES_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert')
    