from pydantic import BaseModel

class ActivateSchema(BaseModel):
    activation_code: str
