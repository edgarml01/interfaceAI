from google import genai
from dotenv import load_dotenv
import os

class AIService:

    def __init__(self):
        load_dotenv()

        client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))


    def ask_gemini(self, prompt):
        """
        Ask the Gemini AI model a question and return the response.
        """
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            return response.text

        except Exception as e:
            print(f"Error: {e}")
            return None