from mistralai.client import MistralClient  # API officielle
from mistralai.models.chat_completion import ChatMessage

class IAAssistant:
    def __init__(self, api_key=None, local=False):
        self.local = local
        if not local:
            self.client = MistralClient(api_key=api_key)
        # Note: Pour Ollama, on utilise directement `requests`

    def generate_payload(self, techno, vuln_type):
        prompt = f"Génère un payload {vuln_type} pour {techno} (contournement de WAF)"
        if self.local:
            import requests
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "mistral", "prompt": prompt}
            )
            return response.json()["response"]
        else:
            response = self.client.chat(
                model="mistral-tiny",
                messages=[ChatMessage(role="user", content=prompt)]
            )
            return response.choices[0].message.content