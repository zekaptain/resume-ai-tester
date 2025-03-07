# resume_parser/openai_api.py

from openai import OpenAI


class OpenAIAPI:
    def __init__(self, api_key: str, model: str):
        client = OpenAI(api_key=api_key)
        self.model = model
        self.client = client

    def format_text_to_json(self, text: str, json_structure: dict) -> dict:
        system_message = "You are a helpful assistant."
        prompt = f"Extract the following information from the text and format it into the specified JSON" \
                 f" structure:\n\nText: {text}\n\nExpected JSON Structure: {json_structure}"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.5,
            max_tokens=1500
        )

        return response.choices[0].message.content.strip()
