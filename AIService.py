from google import genai
from dotenv import load_dotenv
import os
import json 

class AIService:
    client = None

    def __init__(self):
        load_dotenv()

        self.client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))


    def ask_gemini(self, prompt):
        """
        Ask the Gemini AI model a question and return the response.
        """
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            return response.text

        except Exception as e:
            print(f"Error: {e}")
            return None

    def ask_gemini_json(self, prompt):
        """
        Ask the Gemini AI model a question and return the response.
        """
        try:
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents = prompt,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': list[str],
                },
            )
            return response.text

        except Exception as e:
            print(f"Error: {e}")
            return None

    def ask_gemini_list(self, prompt):
        """
        Ask the Gemini AI model a question and return the response.
        """
        try:
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents = prompt,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': list[str],
                },
            )
            list_response = json.loads(response.text )

            return list_response

        except Exception as e:
            print(f"Error: {e}")
            return None