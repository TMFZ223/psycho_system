from pydantic import BaseModel

class RegisterSchema(BaseModel):
    email: str | None = None
    password: str | None = None
    verify_password: str | None = None
