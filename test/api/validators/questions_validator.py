from validators.base_validator import BaseValidator
import allure
from jsonschema import validate


class QuestionsValidator(BaseValidator):

    @allure.step("Проверить соответствие тела ответа после отправки позитивного запроса на добавление вопроса JSON схеме")
    def validate_questions_schema(self, response_json):
        schema = self.load_schema("questions_json_schema.json")
        validate(
            instance=response_json,
            schema=schema
        )

    @allure.step("Убедиться, что в списке вопросов содержится ранее добавленный вопрос {expected_len}")
    def check_questions_len(self, response_json, expected_len = 1):
        assert len(response_json["data"]) == expected_len
