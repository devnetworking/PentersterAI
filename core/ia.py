# core/ia.py

from mistralai.client import MistralClient
from config import MISTRAL_API_KEY

class IAGenerator:
    def __init__(self):
        self.client = MistralClient(api_key=MISTRAL_API_KEY)

    def generate_payload(self, prompt: str) -> str:
        response = self.client.chat(
            model="mistral-medium",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def generate_report(self, findings: str) -> str:
        prompt = f"Génère un rapport structuré pour ces résultats : {findings}"
        return self.generate_payload(prompt)

