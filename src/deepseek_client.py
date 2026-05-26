import requests

class DeepSeekClient:
    def __init__(self, model_name="deepseek-coder", api_key=None, api_url="https://api.deepseek.com/v1/chat/completions"):
        self.model_name = model_name
        self.api_key = api_key
        self.api_url = api_url

    def ask(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}]
        }
        resp = requests.post(self.api_url, headers=headers, json=data)
        resp.raise_for_status()
        completions = resp.json()
        return completions['choices'][0]['message']['content'].strip()
