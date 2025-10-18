# Movie Recommender Backend

This is the **FastAPI backend** for the Movie Recommender project. It provides APIs for fetching movie recommendations and connects to a PostgreSQL database.

---

## Clone the Repository

```bash
git clone <your-backend-repo-url>
cd movie-recommender-backend
```

---

## Setup Environment Variables

Create a `.env` file in the root of the project:

```env
# PostgreSQL database connection
DATABASE_URL=postgresql+psycopg2://nayan:password123@localhost:5432/movie_recommender

# API key for movie recommendation service
GEMINI_API_KEY=AIzaSyBEaL-Ki5C8kcK8TwI2Xa5ekcD3EMiJj5c
```

---

## Start PostgreSQL with Docker Compose

Make sure you have Docker and Docker Compose installed. In the project root, create a `docker-compose.yml` file:

```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    container_name: movie_recommender_db
    restart: always
    environment:
      POSTGRES_USER: nayan
      POSTGRES_PASSWORD: password123
      POSTGRES_DB: movie_recommender
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Then start PostgreSQL:

```bash
docker-compose up -d
```

This will start PostgreSQL in the background on `localhost:5432`.

---

## Install Python Dependencies

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Run the Backend Server

```bash
uvicorn app.main:app --reload
```

The backend server will start at `http://127.0.0.1:8000` and automatically reload on code changes.

---

## Notes

- Make sure PostgreSQL is running (`docker-compose up -d`) before starting the backend.
- The backend reads the database URL and API key from `.env`. If you change `.env`, restart the backend.
- You can also use **Postman or frontend** to test the API endpoints.

