from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.utils.utils import mock_data

router = Router()

@router.message(Command(commands=["status"]))
async def status_handler(message: Message):
    for i in range(30):
        await mock_data(message)
    else:
        await message.answer("Успешно")

@router.message(Command(commands=["help"]))
async def help_handler(message: Message):
    await message.answer(
        "Привет! Я ваш помощник для работы с протоколами и транскрипциями. Вот список команд, которые вам могут пригодиться:\n\n"
        "1. /start - Начать работу с ботом.\n"
        "2. /status - Проверить статус и сгенерировать тестовые данные.\n"
        "3. /help - Показать это сообщение о помощи.\n\n"
        "Доступные действия для работы с транскрипциями:\n"
        "- Загрузка транскрипции: просто загрузите mp3 файл после выбора соответствующего действия.\n"
        "- Просмотр транскрипций: выберите из списка сохранённых транскрипций.\n\n"
        "Для работы с транскрипциями используйте интерактивные кнопки, которые будут предложены после выбора соответствующего действия.\n\n"
    )
