# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class RecommendationCreate(BaseModel):
    user_input: str

class RecommendationResponse(BaseModel):
    id: int
    user_input: str
    recommended_movies: list[str]
    timestamp: datetime

    class Config:
        orm_mode = True
