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
    input_code = code_param if code_param else message.text
    valid_chars = string.ascii_uppercase + string.digits

    if len(input_code) == 9 and all(c in valid_chars for c in input_code) and input_code[0] in ('S', 'T'):
        role_map = {'S': 'student', 'T': 'tutor'}
        role = role_map.get(input_code[0])
        invite_code = input_code[1:]
        telegram_id = message.from_user.id

        response = requests.post('http://127.0.0.1:8000/api/account/set-telegram-id/',
                                 data={'code': invite_code, 'role': role, 'telegram_id': telegram_id})

        await message.answer(text=response.json().get('message'))
        return

    await message.answer(text='Проверьте правильность ввода кода')
