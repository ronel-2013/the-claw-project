import requests

class OllamaClient:
    def __init__(self, model_name="deepseek-coder:latest", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url

    def ask(self, prompt):
        try:
            resp = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": self.model_name, "prompt": prompt, "stream": False}
            )
            resp.raise_for_status()
        except requests.HTTPError as err:
            if resp.status_code == 404:
                return f"Error: Model '{self.model_name}' not found in Ollama. Use `ollama pull {self.model_name}` to install it."
            else:
                return f"Ollama HTTP error {resp.status_code}: {resp.text}"
        except requests.ConnectionError:
            return "Error: Could not connect to Ollama server. Ensure Ollama is running."
        except Exception as e:
            return f"Ollama unexpected error: {str(e)}"

        return resp.json().get("response", "").strip()
