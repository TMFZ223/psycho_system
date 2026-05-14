import allure
from sqlalchemy import select, delete
from db_table_models.activation_code import ActivationCode
from db_table_models.user import User

@allure.step("Удалить пользователя с ролью {role}")
async def delete_users_by_role(db, role: str = "user"):

    await db.execute(
        delete(User).where(User.role == role)
    )

    await db.commit()

@allure.step("Получить код активации из таблицы базы данных для {email}")
async def get_activation_code(db, email: str):

    result = await db.execute(
        select(ActivationCode)
        .where(
            ActivationCode.user_email == email
        )
        .order_by(
            ActivationCode.id.desc()
        )
        .limit(1)
    )

    activation = result.scalars().first()

    return activation.code if activation else None
@allure.step("Убедиться, что ответ пришёл со статус кодом {expected_status_code}")
def check_response_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code