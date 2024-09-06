from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.utils.utils import mock_data

router = Router()

@router.message(Command(commands=["status"]))
async def status_handler(message: Message):
    for i in range(1):
        await mock_data(message)
    else:
        await message.answer("Успешно")