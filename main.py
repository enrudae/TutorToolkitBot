import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from core.handlers.basic import get_start, set_code
from core.settings import settings


async def start_bot(bot: Bot):
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, CommandStart(deep_link=True))
    dp.message.register(set_code)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
