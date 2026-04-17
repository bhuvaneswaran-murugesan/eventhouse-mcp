from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL
from llm.base import BaseLLM

class OpenAIClient(BaseLLM):
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()