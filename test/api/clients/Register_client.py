import allure

from clients.base_client import BaseClient
from back.schemas.register_schema import RegisterSchema


class RegisterClient(BaseClient):

    @allure.step("Отправить запрос на регистрацию")
    async def register(self, register_data: RegisterSchema):
        response = await self.client.post(
            "/user/register",
            json =register_data.model_dump()
        )
        return response