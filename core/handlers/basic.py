from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=str(message.from_user.id))
    await message.answer(text=str(message.from_user.id))
    await message.reply(text=str(message.from_user.id))
