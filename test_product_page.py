from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('url', [*range(7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, url):
    #url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}".format(url)
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_product_page()


