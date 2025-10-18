from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import recommend

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Recommendation API")

# Allow frontend origin
origins = [
    "http://localhost:5173",   # React dev server
    "http://127.0.0.1:5173",
    "https://movie-recommendation-frontend-one.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] for all (dev only)
    allow_credentials=True,
    allow_methods=["*"],            # <-- must include OPTIONS!
    allow_headers=["*"],
)

app.include_router(recommend.router)

@app.get("/")
def root():
    return {"message": "Movie Recommendation API is running!"}
