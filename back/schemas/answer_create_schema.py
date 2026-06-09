from pydantic import BaseModel
from typing import Optional
class AnswerCreateSchema(BaseModel):
    variant: str
    score: int
    position: Optional[int]