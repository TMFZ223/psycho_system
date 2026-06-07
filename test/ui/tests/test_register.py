import allure
import re
import pytest
from playwright.sync_api import Page

from factories.user_factory import UserFactory
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

@allure.epic("Регистрация пользователя")
class TestRegister:

    @pytest.mark.parametrize("user", [(UserFactory.register_with_email_without_add_symbol()), (UserFactory.register_with_email_without_dod_symbol()), (UserFactory.register_with_email_without_required_symbols()), (UserFactory.register_with_empty_email())])
    @allure.title("Регистрация пользователя с некорректным значением в поле email")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_with_incorrect_email(self, user, page: Page, login_page: LoginPage, register_page: RegisterPage):
        if len(user.email) == 0:
            expected_text = "Обязательно для заполнения"
        else:
            expected_text = "Некорректный формат email"
        (login_page
         .open_login_page()
         .go_to_register_page()
         .incorrect_register(user)
         .check_email_error(expected_text))

    @pytest.mark.parametrize("user", [(UserFactory.register_with_6_character_password()), (UserFactory.register_with_31_character_password()), (UserFactory.register_with_empty_password()), (UserFactory.register_with_cyrilic_symbols_in_password()), (UserFactory.register_with_cyrilic_and_latinic_symbols_in_password()), (UserFactory.register_with_special_and_space_symbols_in_password()), (UserFactory.register_with_differents_password_verify_password())])
    @allure.title("Регистрация пользователя с некорректным значением в поле пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_with_incorrect_password(self, user, page: Page, login_page: LoginPage, register_page: RegisterPage):
        if len(user.password) == 0:
            expected_text = "Обязательно для заполнения"
        elif re.search(r"\s", user.password) or re.search(r"[а-яА-Я]", user.password):
            expected_text = "Некорректный формат пароля"
        else:
            expected_text = "Пароль должен быть не короче 7 и не длиннее 30 символов"
        (login_page
         .open_login_page()
         .go_to_register_page()
         .incorrect_register(user)
         .check_password_error(expected_text))

    @pytest.mark.parametrize("user, expected_text", [(UserFactory.register_with_differents_password_verify_password(), "Пароли не совпадают"), (UserFactory.register_with_empty_verify_password(), "Обязательно для заполнения")])
    @allure.title("Регистрация пользователя – разные значения в полях пароля и его подтверждения и пустое подтверждение пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register_different_passwords_and_empty_verify(self, user, expected_text, page: Page, login_page: LoginPage, register_page: RegisterPage):
        (login_page
         .open_login_page()
         .go_to_register_page()
         .incorrect_register(user)
         .check_verify_password_error(expected_text))