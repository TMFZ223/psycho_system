import allure
import pytest

from clients.Register_client import RegisterClient
from clients.activate_user_client import ActivateUserClient
from factories.user_factory import UserFactory
from clients.login_client import LoginClient
from schemas.activate_schema import ActivateSchema
from schemas.auth_schema import AuthSchema
from validators.correct_login_validator import CorrectLoginValidator
from validators.negative_request_validator import NegativeRequestValidator
from validators.positive_request_validator import PositiveRequestValidator
from test_helpers import check_response_status_code, get_activation_code, delete_users_by_role
from test_utils.env_reader import EnvReader

@pytest.mark.asyncio
@allure.title("Авторизация пользователя с ролью admin (тестовый аккаунт)")
@allure.severity(allure.severity_level.CRITICAL)
async def test_positive_login_admin(api_client):
    login_client = LoginClient(api_client)
    validator_of_login = CorrectLoginValidator()
    login_response = await login_client.login(UserFactory.login_with_admin())
    check_response_status_code(login_response, 200)
    login_response_body = login_response.json()
    validator_of_login.validate_correct_login_schema(login_response_body)
    validator_of_login.check_role(login_response_body, EnvReader.get_env_variable_value("admin_role"))
    validator_of_login.check_tokens(login_response_body)

@pytest.mark.parametrize("user", [(UserFactory.standard_register()), (UserFactory.register_with_7_character_password()), (UserFactory.register_with_8_character_password()), (UserFactory.register_with_29_character_password()), (UserFactory.register_with_30_character_password())])
@allure.title("Позитивный тест регистрации пользователя")
@allure.severity(allure.severity_level.CRITICAL)
async def test_positive_register(api_client, user, db_session):
    register_client = RegisterClient(api_client)
    login_client = LoginClient(api_client)
    activate_user_client = ActivateUserClient(api_client)
    validator_positive = PositiveRequestValidator()
    validator_of_login = CorrectLoginValidator()
    after_register_response = await register_client.register(user)
    check_response_status_code(after_register_response, 200)
    after_register_response_body = after_register_response.json()
    validator_positive.validate_positive_request_schema(after_register_response_body)
    validator_positive.chek_message_key(after_register_response_body, "check your email and send the code to activate account")
    actual_activation_code = await get_activation_code(db_session, user.email)
    activation_data = ActivateSchema(activation_code=actual_activation_code)
    after_activate_response = await activate_user_client.activate_user(activation_data)
    check_response_status_code(after_activate_response, 200)
    after_activate_response_body = after_activate_response.json()
    validator_positive.validate_positive_request_schema(after_activate_response_body)
    validator_positive.chek_message_key(after_activate_response_body, "user activated")
    auth_data = AuthSchema(email=user.email, password=user.password)
    after_login_response = await login_client.login(auth_data)
    check_response_status_code(after_login_response, 200)
    after_login_response_body = after_login_response.json()
    validator_of_login.validate_correct_login_schema(after_login_response_body)
    validator_of_login.check_role(after_login_response_body, EnvReader.get_env_variable_value("user_role"))
    await delete_users_by_role(db_session)

@pytest.mark.parametrize("user, expected_error_message", [(UserFactory.register_with_existing_email(), "email already in use"), (UserFactory.register_with_empty_email(), "email should not be empty"), (UserFactory.register_with_none_email(), "email should not be empty"), (UserFactory.register_with_email_without_add_symbol(), "email should be an email"), (UserFactory.register_with_email_without_dod_symbol(), "email should be an email"), (UserFactory.register_with_email_without_required_symbols(), "email should be an email"), (UserFactory.register_with_6_character_password(), "Password must be between 7 and 30 characters"), (UserFactory.register_with_31_character_password(), "Password must be between 7 and 30 characters"), (UserFactory.register_with_cyrilic_symbols_in_password(), "invalid format of password"), (UserFactory.register_with_cyrilic_and_latinic_symbols_in_password(), "invalid format of password"), (UserFactory.register_with_special_and_space_symbols_in_password(), "invalid format of password"), (UserFactory.register_with_empty_password(), "password should not be empty"), (UserFactory.register_with_none_password(), "password should not be empty"), (UserFactory.register_with_empty_verify_password(), "input passwords don't match"), (UserFactory.register_with_none_verify_password(), "input passwords don't match"), (UserFactory.register_with_differents_password_verify_password(), "input passwords don't match")])
@allure.title("Негативный тест регистрации пользователя")
@allure.severity(allure.severity_level.CRITICAL)
async def test_negative_register(api_client, user, expected_error_message):
    register_client = RegisterClient(api_client)
    validator_negative = NegativeRequestValidator()
    after_register_response = await register_client.register(user)
    check_response_status_code(after_register_response, 200)
    after_register_response_body = after_register_response.json()
    validator_negative.validate_negative_request_schema(after_register_response_body)
    validator_negative.chek_error_message_key(after_register_response_body, expected_error_message)