import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src import container as cont
from src.bot.handlers.commands import commands_router

dp = Dispatcher()
dp.include_router(commands_router)


async def main() -> None:
    """
    Telegram bot polling start
    """
    bot = Bot(
        token=cont.settings.telegram_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=cont.settings.log_level, stream=sys.stdout)
    asyncio.run(main())
