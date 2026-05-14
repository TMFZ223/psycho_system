from fastapi import FastAPI

import asyncio
from database import engine
from db_table_models.user import Base 
from db_table_models.question import Base 
from db_table_models.answer  import Base 
from db_table_models.user_answer import Base
from db_table_models.attempt import Base
from routers import user, questions

app = FastAPI()

# Создаём таблицы асинхронно при запуске
@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Подключаем роутеры
app.include_router(user.router)
app.include_router(questions.router)