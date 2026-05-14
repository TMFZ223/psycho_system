import allure
from jsonschema import validate

from validators.base_validator import BaseValidator

class NegativeRequestValidator(BaseValidator):

    @allure.step("Проверить соответствие тела ответа после отправки негативного запроса JSON схеме")
    def validate_negative_request_schema(self, response_json):
        schema = self.load_schema("negative_json_schema.json")
        validate(
            instance=response_json,
            schema=schema
        )

    @allure.step("Убедиться, что в ключе error_message отображается значение {expected_error_message}")
    def chek_error_message_key(self, response_json, expected_error_message):
        assert response_json["data"]["error_message"] == expected_error_message, f"actual error message: {response_json["data"]["error_message"]}"