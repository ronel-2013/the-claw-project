import requests

class GeminiClient:
    def __init__(self, model_name="gemini-pro", api_key=None):
        self.model_name = model_name
        if not api_key:
            raise ValueError("Gemini API key is required")
        self.api_key = api_key
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"

    def ask(self, prompt):
        headers = {"Content-Type": "application/json"}
        params = {"key": self.api_key}
        data = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }
        try:
            resp = requests.post(self.url, headers=headers, params=params, json=data)
            resp.raise_for_status()
        except requests.HTTPError as err:
            if resp.status_code == 401:
                return "Error: Unauthorized. Check your Gemini API key."
            elif resp.status_code == 404:
                return f"Error: Model '{self.model_name}' not found on Gemini."
            else:
                return f"Gemini HTTP error {resp.status_code}: {resp.text}"
        except requests.ConnectionError:
            return "Error: Could not connect to Gemini API."
        except Exception as e:
            return f"Gemini unexpected error: {str(e)}"

        result = resp.json()
        # Handle API errors
        if "candidates" in result and result["candidates"]:
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()
        elif "error" in result:
            return f"Gemini API error: {result['error'].get('message','')}"
        else:
            return "No completion returned by Gemini."
