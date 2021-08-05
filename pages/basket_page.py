from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            'There are items in basket'

    def should_be_empty_basket_messages(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_INFO), \
            'Empty basket message is presented'