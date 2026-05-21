import allure

from clients.base_client import BaseClient
from schemas.question_create_schema import QuestionCreateSchema


class QuestionClient(BaseClient):

    @allure.step("Отправить запрос на добавление запроса")
    async def add_question(self, question: QuestionCreateSchema, token):
        response = await self.client.post(
            "/questions",
            headers = {"Authorization": f"Bearer {token}"},
            json =question.model_dump()
        )

        return response

    @allure.step("Отправить запрос на получение списка вопросов")
    async def пet_question_list(self, token):
        response = await self.client.get(
            "/questions",
            headers = {"Authorization": f"Bearer {token}"}
        )

        return response

    @allure.step("Отправить запрос на удаление вопроса")
    async def delete_question_by_id(self, question_id, token):
        response = await self.client.delete(
            f"/questions{question_id}",
            headers = {"Authorization": f"Bearer {token}"}
        )

        return response
