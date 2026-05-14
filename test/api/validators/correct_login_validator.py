import allure
from jsonschema import validate

from validators.base_validator import BaseValidator

class CorrectLoginValidator(BaseValidator):

    @allure.step("Проверить соответствие тела ответа после успешного логина JSON схеме")
    def validate_correct_login_schema(self, response_json):
        schema = self.load_schema("correct_login_schema.json")
        validate(
            instance=response_json,
            schema=schema
        )
    @allure.step("Убедиться, что пользователь залогинен под ролью {expected_role}")
    def check_role(self, response_json, expected_role):
        assert response_json["data"]["role"] == expected_role, f"actual role: {response_json["data"]["role"]}"

    @allure.step("Проверить целостность значений токенов пользователя")
    def check_tokens(self, response_json):
        assert response_json["data"]["access_token"] != None
        assert response_json["data"]["refresh_token"] != None