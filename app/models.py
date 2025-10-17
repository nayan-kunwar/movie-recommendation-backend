from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String(255), nullable=False)
    recommended_movies = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
