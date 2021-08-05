from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_succes_messages()
        self.compare_names()
        self.compare_prices()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add button is not presented'

    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        #self.solve_quiz_and_get_code()

    def add_to_cart_with_code(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_succes_messages(self):
        assert self.is_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
            'Succes messages is not presented'

    def should_not_be_succes_messages(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
            'Succes messages is presented'

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), \
            'Succes messages is not disappeared'

    def compare_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert product_price.text == product_price_in_message.text, 'Prices are not equal'

    def compare_names(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name.text == product_name_in_message.text, 'Names are different'

    

