from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timedelta
from database import SessionLocal
from db_table_models.user import User
from db_table_models.refresh_token import RefreshToken
from db_table_models.activation_code import ActivationCode
from schemas.register_schema import RegisterSchema
from schemas.activate_schema import ActivateSchema
from schemas.auth_schema import AuthSchema
from utils import validate_email, validate_password, generate_code
from auth import hash_password, verify_password, create_access_token, create_refresh_token

router = APIRouter(prefix="/user", tags=["User"])


async def get_db():
    async with SessionLocal() as db:
        yield db


@router.post("/register")
async def register(
    data: RegisterSchema,
    db: AsyncSession = Depends(get_db)
):

    if not data.email:
        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": "email should not be empty"
            }
        }

    err = validate_email(data.email)
    if err:
        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": err
            }
        }

    err = validate_password(data.password)
    if err:
        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": err
            }
        }

    if data.password != data.verify_password:
        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": "input passwords don't match"
            }
        }

    result = await db.execute(
        select(User)
        .where(User.email == data.email)
    )

    existing = result.scalar_one_or_none()

    if existing:
        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": "email already in use"
            }
        }

    user = User(
        email=data.email,
        password=hash_password(data.password),
        role="user",
        is_active=False
    )

    db.add(user)

    code = generate_code()

    activation = ActivationCode(
        user_email=data.email,
        code=code,
        expires_at=datetime.utcnow() + timedelta(minutes=15)
    )

    db.add(activation)

    await db.commit()

    print(f"Activation code: {code}")

    return {
        "success": True,
        "status": 200,
        "data": {
            "message": "check your email and send the code to activate account"
        }
    }

@router.post("/activate")
async def activate(
    data: ActivateSchema,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(ActivationCode)
        .where(
            ActivationCode.code == data.activation_code,
            ActivationCode.is_used == False
        )
    )

    activation = result.scalar_one_or_none()

    if activation is None:
        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": "invalid activation code"
            }
        }

    if activation.expires_at < datetime.utcnow():

        return {
            "success": False,
            "status": 400,
            "data": {
                "error_message": "activation code expired"
            }
        }

    result = await db.execute(
        select(User)
        .where(
            User.email == activation.user_email
        )
    )

    user = result.scalar_one_or_none()

    if user is None:

        return {
            "success": False,
            "status": 404,
            "data": {
                "error_message": "user not found"
            }
        }

    user.is_active = True

    activation.is_used = True

    await db.commit()

    return {
        "success": True,
        "status": 200,
        "data": {
            "message": "user activated"
        }
    }

@router.post("/auth")
async def auth(data: AuthSchema, db: AsyncSession = Depends(get_db)):
    if not data.email:
        return {"success": False, "status": 400, "data": {"error_message": "email should not be empty"}}

    err = validate_email(data.email)
    if err:
        return {"success": False, "status": 400, "data": {"error_message": err}}
    if not data.password:
        return {"success": False, "status": 400, "data": {"error_message": "password should not be empty"}}
    try:
        result = await db.execute(
            select(User).where(User.email == data.email)
        )
        user = result.scalar_one_or_none()

        if not user or not user.password:
            return {"success": False, "status": 400, "data": {"error_message": "invalid credentials"}}

        if not verify_password(data.password, user.password):
            return {"success": False, "status": 400, "data": {"error_message": "invalid credentials"}}

        access_token = create_access_token({
            "sub": user.email
        })

        refresh_token = create_refresh_token({
            "sub": user.email
        })

        db_refresh = RefreshToken(
            user_id=user.id,
            token=refresh_token
        )

        db.add(db_refresh)

        await db.commit()
        return {
            "success": True, "status": 200,
            "data": {
                "role": user.role,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        }

    except Exception as e:
        print("AUTH ERROR:", str(e))
        return {
            "success": False, "status": 500,
            "data": {"error_message": "internal server error"}
        }

@router.post("/locked_out")
async def locked_out(
    refresh_token: str = Header(...),
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(RefreshToken).where(
                RefreshToken.token == refresh_token
            )
        )

        token = result.scalar_one_or_none()

        if not token:
            return {
                "success": False,
                "status": 400,
                "data": {
                    "error_message": "invalid refresh token"
                }
            }

        await db.delete(token)
        await db.commit()

        return {
            "success": True,
            "status": 200,
            "data": {
                "message": "logged out"
            }
        }

    except Exception as e:
        print("LOGOUT ERROR:", str(e))

        return {
            "success": False,
            "status": 500
        }