from pydantic import BaseModel
from typing import List
from .answer_create_schema import AnswerCreateSchema

class QuestionCreateSchema(BaseModel):
    question_text: str
    answers: List[AnswerCreateSchema]