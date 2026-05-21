from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, ForeignKeyConstraint, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False)

    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # связь с ответами пользователя
    user_answers = relationship(
        "UserAnswer",
        back_populates="attempt",
        cascade="all, delete-orphan"
    )