import allure
from jsonschema import validate

from validators.base_validator import BaseValidator

class PositiveRequestValidator(BaseValidator):

    @allure.step("Проверить соответствие тела ответа после отправки позитивного запроса JSON схеме")
    def validate_positive_request_schema(self, response_json):
        schema = self.load_schema("positive_json_schema.json")
        validate(
            instance=response_json,
            schema=schema
        )

    @allure.step("Убедиться, что в ключе message отображается значение {expected_message}")
    def chek_message_key(self, response_json, expected_message):
        assert response_json["data"]["message"] == expected_message, f"actual message: {response_json["data"]["message"]}"