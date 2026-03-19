from __future__ import annotations

from openai import OpenAI


class GPTClient:
    def __init__(self, api_key: str, model: str) -> None:
        self._model = model
        self._client = OpenAI(api_key=api_key)

    def reply(self, user_message: str) -> str:
        response = self._client.responses.create(
            model=self._model,
            input=[
                {
                    "role": "system",
                    "content": "You are a concise assistant for Telegram chats.",
                },
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
        )
        return response.output_text.strip()
