from google import genai

from app.config import google_api 

GOOGLE_API_KEY= google_api.GEMINI_API_KEY
GEMINI_MODEL = google_api.GEMINI_MODEL

class AIClient:
    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)

    def generate_strategy_advice(self, prompt: str) -> str | None:
        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            if response and response.text:
                return response.text.strip()

            return None

        except Exception as e:
            print(f"Error using Gemini API: {e}")
            return None