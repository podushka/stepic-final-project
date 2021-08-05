import pytest, time, random
from conftest import browser
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


#@pytest.mark.parametrize('url', [*range(7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
#def test_guest_can_add_product_to_basket(browser, url):
    #url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    #url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(url)
    #product_page = ProductPage(browser, url)
    #product_page.open()
    #product_page.add_to_cart()
    #product_page.should_be_product_page()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_succes_messages()

def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_not_be_succes_messages()

def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_disappear_message()

def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_messages()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, url)
        #login_page.generate_register()
        login_page.open()
        login_page.register_new_user(*login_page.generate_register())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_not_be_succes_messages()

    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_be_product_page()