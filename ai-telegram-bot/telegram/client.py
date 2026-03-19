from __future__ import annotations

from telethon import TelegramClient


class TelegramGateway:
    def __init__(self, session: str, api_id: int, api_hash: str) -> None:
        self.client = TelegramClient(session, api_id, api_hash)

    async def start(self) -> None:
        await self.client.start()

    async def send_text(self, chat: str, text: str) -> None:
        await self.client.send_message(chat, text)
