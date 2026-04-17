from llm.gemini_llm import GeminiClient
from llm.openai_llm import AzureOpenAIClient

def get_llm(model_name: str):
    if model_name == "Gemini":
        return GeminiClient()
    elif model_name == "Azure OpenAI":
        return AzureOpenAIClient()
    else:
        raise ValueError("Invalid model selected")