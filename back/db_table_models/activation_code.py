from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime

from database import Base

class ActivationCode(Base):
    __tablename__ = "activation_codes"
    id = Column(Integer, primary_key=True)
    user_email = Column(String, nullable=False, index=True)
    code = Column(String, nullable=False, unique=True)
    is_used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)