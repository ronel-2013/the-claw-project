import requests

class OllamaClient:
    def __init__(self, model_name="deepseek-coder:latest", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url

    def ask(self, prompt):
        resp = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model_name, "prompt": prompt, "stream": False}
        )
        resp.raise_for_status()
        return resp.json().get("response", "").strip()
