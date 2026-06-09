from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    # связь с ответами
    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan"
    )