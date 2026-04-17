from google import genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL
from llm.base import BaseLLM

class GeminiClient(BaseLLM):
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text.strip()