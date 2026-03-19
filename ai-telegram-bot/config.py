from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    telegram_api_id: int
    telegram_api_hash: str
    telegram_session: str
    telegram_target_chat: str
    openai_api_key: str
    openai_model: str = "gpt-4.1-mini"
    max_message_length: int = 3500
    min_delay_seconds: float = 1.0
    max_delay_seconds: float = 2.5
    reply_style_prefix: str = "✨ "

    @staticmethod
    def from_env() -> "Settings":
        api_id = os.environ.get("API_ID") or os.environ.get("TG_API_ID")
        api_hash = os.environ.get("API_HASH") or os.environ.get("TG_API_HASH")

        if not api_id or not api_hash:
            raise ValueError("Set API_ID and API_HASH environment variables.")

        return Settings(
            telegram_api_id=int(api_id),
            telegram_api_hash=api_hash,
            telegram_session=os.environ.get("TG_SESSION", "bot.session"),
            telegram_target_chat=os.environ["TG_TARGET_CHAT"],
            openai_api_key=os.environ["OPENAI_API_KEY"],
            openai_model=os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"),
            max_message_length=int(os.environ.get("MAX_MESSAGE_LENGTH", "3500")),
            min_delay_seconds=float(os.environ.get("MIN_DELAY_SECONDS", "1.0")),
            max_delay_seconds=float(os.environ.get("MAX_DELAY_SECONDS", "2.5")),
            reply_style_prefix=os.environ.get("REPLY_STYLE_PREFIX", "✨ "),
        )
