import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"

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

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(hours=2)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)