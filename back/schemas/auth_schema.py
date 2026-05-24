from pydantic import BaseModel

class AuthSchema(BaseModel):
    email: str | None = None
    password: str | None = None