from ollama_client import OllamaClient
from deepseek_client import DeepSeekClient
from gemini_client import GeminiClient

class ClawAgent:
    def __init__(self, backend="ollama", model_name="deepseek-coder:latest", api_key=None):
        if backend == "ollama":
            self.llm = OllamaClient(model_name)
        elif backend == "deepseek":
            self.llm = DeepSeekClient(model_name, api_key)
        elif backend == "gemini":
            self.llm = GeminiClient(model_name, api_key)
        else:
            raise ValueError("Unknown backend: choose 'ollama', 'deepseek', or 'gemini'.")

    def chat(self, message: str, context=None):
        return self.llm.ask(message)
