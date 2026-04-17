from llm.gemini_client import GeminiClient
from llm.openai_client import OpenAIClient

def get_llm(model_name: str):
    if model_name == "Gemini":
        return GeminiClient()
    elif model_name == "OpenAI":
        return OpenAIClient()
    else:
        raise ValueError("Invalid model selected")