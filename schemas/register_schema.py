from pydantic import BaseModel

class RegisterSchema(BaseModel):
    email: str
    password: str
    verify_password: str
