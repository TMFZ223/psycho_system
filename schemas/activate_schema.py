from pydantic import BaseModel

class ActivateSchema(BaseModel):
    activationCode: str
