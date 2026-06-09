import allure

from clients.base_client import BaseClient
from back.schemas.auth_schema import AuthSchema


class LoginClient(BaseClient):

    @allure.step("Отправить запрос на логин")
    async def login(self, user: AuthSchema):
        response = await self.client.post(
            "/user/auth",
            json  =user.model_dump()
        )

        return response