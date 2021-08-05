from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.BASKET_ITEM), \
            'There are items in basket'

    def should_be_empty_basket_messages(self):
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET_INFO), \
            'Empty basket message is presented'