from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_product_page()


