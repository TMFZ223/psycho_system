import allure
from pages.base_page import BasePage
from playwright.sync_api import Locator, expect
from back.schemas.auth_schema import AuthSchema
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class LoginPage(BasePage):

    @property
    def email_input(self)-> Locator:
        return self.page.locator("#email")

    @property
    def password_input(self)-> Locator:
        return self.page.locator("#pass")

    @property
    def password_error_element(self)-> Locator:
        return self.page.locator("#auth-pass-error")

    @property
    def login_button(self)-> Locator:
        return self.page.locator("#login-button")

    @property
    def register_button(self)-> Locator:
        return self.page.locator("#register")

    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.page.goto(self.BASE_URL)
        return self

    def login(self, user: AuthSchema):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_login_button()
        return MainPage(self.page)

    def negative_login(self, user: AuthSchema):
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.click_login_button()
        return self

    @allure.step("Ввести в поле email значение {email_value}")
    def enter_email(self, email_value):
        self.highlight_and_attach(self.email_input, "Поле email")
        self.email_input.fill(email_value)

    @allure.step("Ввести в поле пароля значение {password_value}")
    def enter_password(self, password_value):
        self.highlight_and_attach(self.password_input, "Поле пароля")
        self.password_input.fill(password_value)

    @allure.step("Нажать на кнопку входа")
    def click_login_button(self):
        self.highlight_and_attach(self.login_button, "Кнопка входа")
        self.login_button.click()

    @allure.step("Нажать на кнопку регистрация для перехода на страницу регистрации")
    def go_to_register_page(self):
        self.register_button.click()
        return RegisterPage(self.page)

    @allure.step("Убедиться, что под полем пароля отображается текст {expected_error_auth_password_text}")
    def check_auth_password_text(self, expected_error_auth_password_text):
        self.highlight_and_attach(self.password_error_element, "Элемент предупреждения о необходимости заполнения пароля")
        expect(self.password_error_element).to_have_text(expected_error_auth_password_text)