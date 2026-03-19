from __future__ import annotations

from ai.gpt import GPTClient
from ai.style import add_style
from config import Settings
from telegram.client import TelegramGateway
from utils.delay import random_delay
from utils.splitter import split_message


class MessageHandler:
    def __init__(self, settings: Settings, telegram: TelegramGateway, gpt: GPTClient) -> None:
        self._settings = settings
        self._telegram = telegram
        self._gpt = gpt

    async def process(self, incoming_text: str) -> None:
        # 1) Отримав повідомлення
        # 2) Передав в GPT
        reply = self._gpt.reply(incoming_text)

        # 3) Отримав відповідь
        # 4) Розбив на частини
        chunks = split_message(reply, self._settings.max_message_length)

        for chunk in chunks:
            # 5) Додав стиль
            styled = add_style(chunk, self._settings.reply_style_prefix)

            # 6) Затримка
            await random_delay(self._settings.min_delay_seconds, self._settings.max_delay_seconds)

            # 7) Відправив
            await self._telegram.send_text(self._settings.telegram_target_chat, styled)
