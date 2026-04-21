from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import SessionLocal
from db_table_models.user import User
from schemas.register_schema import RegisterSchema
from schemas.activate_schema import ActivateSchema
from schemas.auth_schema import AuthSchema
from utils import validate_email, validate_password, generate_code, activation_storage
from auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/user", tags=["User"])


async def get_db():
    async with SessionLocal() as db:
        yield db


@router.post("/register")
async def register(data: RegisterSchema, db: AsyncSession = Depends(get_db)):

    if not data.email:
        return {"success": False, "status": 400, "data": {"errorMessage": "email should not be empty"}}

    err = validate_email(data.email)
    if err:
        return {"success": False, "status": 400, "data": {"errorMessage": err}}

    err = validate_password(data.password)
    if err:
        return {"success": False, "status": 400, "data": {"errorMessage": err}}

    if data.password != data.verifyPassword:
        return {"success": False, "status": 400, "data": {"errorMessage": "input passwords don't match"}}

    result = await db.execute(
        select(User).where(User.email == data.email)
    )
    existing = result.scalar_one_or_none()

    if existing:
        return {"success": False, "status": 400, "data": {"errorMessage": "email already in use"}}

    code = generate_code()
    activation_storage[code] = data

    print(f"Activation code: {code}")

    return {
        "success": True, "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
    }


@router.post("/activate")
async def activate(data: ActivateSchema, db: AsyncSession = Depends(get_db)):
    stored = activation_storage.get(data.activationCode)

    if not stored:
        return {"success": False, "status": 400, "data": {"errorMessage": "invalid activation code"}}

    try:
        user = User(
            email=stored.email,
            password=hash_password(stored.password),
            role="user"
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        del activation_storage[data.activationCode]

        return {
            "success": True, "status": 200,
            "data": {"message": "user created"}
        }

    except Exception as e:
        await db.rollback()
        print("ACTIVATE ERROR:", str(e))
        return {
            "success": False, "status": 500,
            "data": {"errorMessage": "failed to create user"}
        }


@router.post("/auth")
async def auth(data: AuthSchema, db: AsyncSession = Depends(get_db)):
    if not data.email:
        return {"success": False, "status": 400, "data": {"errorMessage": "email should not be empty"}}

    err = validate_email(data.email)
    if err:
        return {"success": False, "status": 400, "data": {"errorMessage": err}}
    if not data.password:
        return {"success": False, "status": 400, "data": {"errorMessage": "password should not be empty"}}
    try:
        result = await db.execute(
            select(User).where(User.email == data.email)
        )
        user = result.scalar_one_or_none()

        if not user or not user.password:
            return {"success": False, "status": 400, "data": {"errorMessage": "invalid credentials"}}

        if not verify_password(data.password, user.password):
            return {"success": False, "status": 400, "data": {"errorMessage": "invalid credentials"}}

        token = create_token({"sub": user.email})

        return {
            "success": True, "status": 200,
            "data": {
                "role": user.role,
                "accessToken": token
            }
        }

    except Exception as e:
        print("AUTH ERROR:", str(e))
        return {
            "success": False, "status": 500,
            "data": {"errorMessage": "internal server error"}
        }