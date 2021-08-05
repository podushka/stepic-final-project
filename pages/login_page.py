import pytest, time, random
from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def generate_register(self):
        email = str(time.time()) + "@fakemail.org"
        password = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, 10)])
        return (email, password)

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_repeat_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_repeat_field.send_keys(password)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert 'login' in url, 'No \"login\" in url.'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'