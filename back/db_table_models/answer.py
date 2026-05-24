from sqlalchemy import Column, Integer, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(
        Integer,
        ForeignKey("questions.id", ondelete="CASCADE"),
        nullable=False
    )
    variant = Column(Text, nullable=False)
    score = Column(Integer, default=0)
    position = Column(Integer)

    question = relationship("Question", back_populates="answers")

    # важно для составного внешнего ключа
    __table_args__ = (
        UniqueConstraint("id", "question_id", name="uix_answer_id_question_id"),
    )