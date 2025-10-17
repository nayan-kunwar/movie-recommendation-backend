from fastapi import FastAPI
from app.database import engine, Base
from app.routes import recommend

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Recommendation API")

app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "Movie Recommendation API is running!"}
