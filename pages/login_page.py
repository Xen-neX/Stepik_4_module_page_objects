import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Url not contained 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REG_FORM), "Reg form is not presented"

    def register_new_user(self, email, password):
        field_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        field_email.send_keys(email)
        field_pass = self.browser.find_element(*LoginPageLocators.PASS_INPUT)
        field_pass.send_keys(password)
        field_pass_2 = self.browser.find_element(*LoginPageLocators.PASS_2_INPUT)
        field_pass_2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.SUBMIT)
        submit.click()
