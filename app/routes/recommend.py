from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.services.openai_service import get_movie_recommendations
import json

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@router.post("/", response_model=schemas.RecommendationResponse)
async def recommend_movies(request: schemas.RecommendationCreate, db: Session = Depends(get_db)):
    movies = await get_movie_recommendations(request.user_input)

    print(request.user_input)
    new_entry = models.Recommendation(
        user_input=request.user_input,
        recommended_movies=json.dumps(movies)
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return {
        "id": new_entry.id,
        "user_input": new_entry.user_input,
        "recommended_movies": movies,
        "timestamp": new_entry.timestamp
    }
