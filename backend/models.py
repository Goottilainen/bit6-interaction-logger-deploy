from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from database import Base

class InteractionLog(Base):
    __tablename__ = "interaction_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(Text, nullable=False)
    system_output = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
