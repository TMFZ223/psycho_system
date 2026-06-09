import pytest_asyncio
import httpx
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from back.main import app
from back.routers.user import get_db
from test_utils.env_reader import EnvReader

TEST_DATABASE_URL = (
    "postgresql+asyncpg://test_admin:test_password_1234@localhost:5432/work_polygon_base"
)

engine = create_async_engine(
    TEST_DATABASE_URL,
    pool_pre_ping=True
)

TestingSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


@pytest_asyncio.fixture(scope="function", autouse=True)
async def prepare_database():
    yield
    async with engine.begin() as conn:
        await conn.execute(
            text("""
                TRUNCATE TABLE
                    refresh_tokens,
                    activation_codes
                RESTART IDENTITY CASCADE
            """)
        )
    await engine.dispose()

@pytest_asyncio.fixture(scope="function")
async def db_session():

    async with TestingSessionLocal() as session:
        yield session

        await session.rollback()

async def override_get_db():

    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest_asyncio.fixture(scope="function")
async def api_client():
    async with httpx.AsyncClient(
        base_url=EnvReader.get_env_variable_value("base_url_test_stage"),
        headers={
            "Content-Type": "application/json"
        },
        timeout=10.0
    ) as client:

        yield client