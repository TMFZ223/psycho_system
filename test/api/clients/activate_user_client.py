import allure

from clients.base_client import BaseClient
from schemas.activate_schema import ActivateSchema

class ActivateUserClient(BaseClient):

    @allure.step("Отправить запрос на активацию аккаунта")
    async def activate_user(self, activation_data: ActivateSchema):
        response = await self.client.post(
            "/user/activate",
            json =activation_data.model_dump()
        )

        return response

    @allure.step("Отправить запрос на активацию аккаунта (тестовый вариант)")
    async def activate_user_test_request(self, email: ActivateSchema):
        response = await self.client.get(
            f"/test/activation-code/{email}",
        )

        return response