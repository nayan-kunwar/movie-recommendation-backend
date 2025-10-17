from google import genai
import os
import re

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

async def get_movie_recommendations(user_input: str):
    prompt = f"Suggest 5 movies based on this description: '{user_input}'. Return only movie titles, one per line."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        # Extract raw text
        raw_text = response.text.strip()
        print(f"Gemini raw response:\n{raw_text}\n")

        # Clean and split text into movie titles
        # Remove numbering like "1. Movie", "-", "*", etc.
        movies = re.sub(r"^\d+[\).\s-]*", "", raw_text, flags=re.MULTILINE)
        movies = [m.strip() for m in movies.split("\n") if m.strip()]
        
        # Limit to 5 results
        return movies[:5]

    except Exception as e:
        print(f"Error fetching recommendations: {e}")
        return ["Something went wrong while fetching movie recommendations."]
