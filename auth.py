import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"

access_token_expire_minutes = 30
refresh_token_expire_days = 7

def hash_password(password):
    """Хеширует пароль с использованием bcrypt"""
    if len(password.encode('utf-8')) > 72:
        raise ValueError("Пароль не может быть длиннее 72 байт")
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def verify_password(plain, hashed):
    """Проверяет пароль против хеша"""
    plain_bytes = plain.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes)

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=access_token_expire_minutes
    )

    to_encode.update({
        "exp": expire,
        "type": "access"
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        days = refresh_token_expire_days
    )

    to_encode.update({
        "exp": expire,
        "type": "refresh"
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )