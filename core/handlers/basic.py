import requests
import string
from aiogram.filters import CommandObject
from aiogram.types import Message


async def get_start(message: Message, command: CommandObject):
    code_param = command.args

    if code_param:
        await set_code(message, code_param)
    else:
        await message.answer("Добро пожаловать! Введите код для привязки аккаунта")


async def set_code(message: Message, code_param=None):
    code = code_param if code_param else message.text
    chars = string.ascii_uppercase + string.digits

    if len(code) == 8 and all(c in chars for c in code):
        telegram_id = message.from_user.id

        response = requests.post('http://127.0.0.1:8000/api/account/set-telegram-id/',
                                 data={'code': code, 'telegram_id': telegram_id})

        await message.answer(text=response.json().get('message'))
        return

    await message.answer(text='Проверьте правильность ввода кода')
