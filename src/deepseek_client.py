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
        try:
            resp = requests.post(self.api_url, headers=headers, json=data)
            resp.raise_for_status()
        except requests.HTTPError as err:
            if resp.status_code == 402:
                return "Error: 402 Payment Required from DeepSeek. Check your API key, payment status, or account balance."
            elif resp.status_code == 404:
                return f"Error: Model '{self.model_name}' not found on DeepSeek."
            else:
                return f"DeepSeek HTTP error {resp.status_code}: {resp.text}"
        except requests.ConnectionError:
            return "Error: Could not connect to DeepSeek API."
        except Exception as e:
            return f"DeepSeek unexpected error: {str(e)}"

        completions = resp.json()
        return completions['choices'][0]['message']['content'].strip()
