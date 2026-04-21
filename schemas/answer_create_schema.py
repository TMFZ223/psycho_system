from pydantic import BaseModel
from typing import Optional
class AnswerCreateSchema(BaseModel):
    variant: str
    is_correct: int
    position: Optional[int]