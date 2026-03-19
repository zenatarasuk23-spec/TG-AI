from __future__ import annotations

import asyncio

from telethon import events

from ai.gpt import GPTClient
from config import Settings
from telegram.client import TelegramGateway
from telegram.handler import MessageHandler


async def main() -> None:
    settings = Settings.from_env()

    telegram = TelegramGateway(
        session=settings.telegram_session,
        api_id=settings.telegram_api_id,
        api_hash=settings.telegram_api_hash,
    )
    gpt = GPTClient(api_key=settings.openai_api_key, model=settings.openai_model)
    handler = MessageHandler(settings=settings, telegram=telegram, gpt=gpt)

    await telegram.start()

    @telegram.client.on(events.NewMessage(incoming=True))
    async def on_message(event: events.NewMessage.Event) -> None:
        if not event.raw_text:
            return
        await handler.process(event.raw_text)

    print("Bot is running...")
    await telegram.client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
