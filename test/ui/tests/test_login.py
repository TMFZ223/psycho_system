import allure
import pytest
from playwright.sync_api import Page

from factories.user_factory import UserFactory
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.epic("Тесты авторизации")
class TestLogin:
    @allure.title("Позитивный тест авторизации пользователя с ролью преподаватель")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_positive_login(self, page: Page, login_page: LoginPage, main_page: MainPage):
        (login_page
         .open_login_page()
         .login(UserFactory().login_with_admin())
         .click_profile()
         .check_role("Преподаватель"))

    @allure.title("Негативный тест авторизации")
    def test_negative_login(self, page: Page, login_page: LoginPage):
        (login_page
         .open_login_page()
         .negative_login(UserFactory.login_with_empty_password())
         .check_auth_password_text("Обязательно для заполнения"))