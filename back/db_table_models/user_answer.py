from sqlalchemy import Column, Integer, ForeignKey, ForeignKeyConstraint, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id", ondelete="CASCADE"),
        nullable=False
    )

    answer_id = Column(Integer, nullable=False)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id", ondelete="CASCADE"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    question = relationship("Question")
    answer = relationship("Answer")

    attempt = relationship(
        "Attempt",
        back_populates="user_answers"
    )

    __table_args__ = (
        UniqueConstraint(
            "attempt_id",
            "question_id",
            name="uix_attempt_question"
        ),

        ForeignKeyConstraint(
            ["answer_id", "question_id"],
            ["answers.id", "answers.question_id"],
            name="fk_answer_question"
        ),
    )