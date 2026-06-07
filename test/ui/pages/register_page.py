import allure
from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

from back.schemas.register_schema import RegisterSchema


class RegisterPage(BasePage):
    @property
    def email_input(self)-> Locator:
        return self.page.locator("#reg-email")

    @property
    def email_error_element(self)-> Locator:
        return self.page.locator("#email_error")

    @property
    def password_input(self)-> Locator:
        return self.page.locator("#user-pass")

    @property
    def password_error_element(self)-> Locator:
        return self.page.locator("#password_error")

    @property
    def verify_password_input(self)-> Locator:
        return self.page.locator("#verify_pass")

    @property
    def verify_password_error_element(self)-> Locator:
        return self.page.locator("#verify_password_error")

    @property
    def register_button(self)-> Locator:
        return self.page.locator("#register-BTN")

    def incorrect_register(self, user: RegisterSchema):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.enter_verify_password(user.verify_password)
        self.click_register_button()
        return self

    @allure.step("Ввести в поле email значение {email_value}")
    def enter_email(self, email_value):
        self.email_input.fill(email_value)

    @allure.step("Ввести в поле пароля значение {password_value}")
    def enter_password(self, password_value):
        self.password_input.fill(password_value)

    @allure.step("Ввести в поле подтверждения пароля значение {verify_password_value}")
    def enter_verify_password(self, verify_password_value):
        self.verify_password_input.fill(verify_password_value)

    @allure.step("Нажать на кнопку регистрация")
    def click_register_button(self):
        self.register_button.click()

    @allure.step("Убедиться, что под полем email отображается текст {expected_email_error_text}")
    def check_email_error(self, expected_email_error_text):
        expect(self.email_error_element).to_have_text(expected_email_error_text)

    @allure.step("Убедиться, что под полем пароля отображается текст {expected_password_error_text}")
    def check_password_error(self, expected_password_error_text):
        expect(self.password_error_element).to_have_text(expected_password_error_text)

    @allure.step("Убедиться, что под полем подтверждения пароля отображается текст {expected_verify_password_error_text}")
    def check_verify_password_error(self, expected_verify_password_error_text):
        expect(self.verify_password_error_element).to_have_text(expected_verify_password_error_text)