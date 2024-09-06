import os
from typing import cast, List
from uuid import uuid1

from aiogram.types import File, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from beanie import WriteRules
from faker import Faker

from app import logger
from app.database.models.meetings.decision import Decision
from app.database.models.meetings.protocol import Protocol
from app.database.models.meetings.question import Question
from app.database.models.meetings.user import User


async def safe_download(file: File):
    logger.debug(f"Установка файла {file.file_id}")
    directory = "files"

    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, file.file_path.split("/")[-1])
    logger.debug(f"Путь {file_path}")

    await file.bot.download_file(file.file_path, destination=file_path)


async def mock_data(message):
    fake = Faker()
    decision = Decision(title=fake.street_name(), brief_context="123", elapsed_time="01:01")
    user = await User.find_one(User.telegram_id == message.from_user.id)
    if user is None:
        user = User(telegram_id=message.from_user.id, full_name=message.from_user.full_name, protocols=None)
        await User.insert(user)
    question = Question(title=fake.name_female(), persons=None, decision=[decision])


    await Question.insert(question)
    fake = Faker(locale="ru_RU")

    protocol = Protocol(
        uuid=uuid1(),
        user=user,
        title=fake.region(),
        theme="1",
        questions=[question],
        persons=None,
    )
    await Protocol.insert(protocol)

    if user.protocols is None:
        user.protocols = []

    user.protocols = cast(list[Protocol], user.protocols)
    user.protocols.append(protocol)
    await User.save(user)

def create_paginated_keyboard(items: List[str], page: int = 1, items_per_page: int = 5) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_page_items = items[start_idx:end_idx]

    for i in range(0, len(current_page_items), 3):
        row = current_page_items[i:i+3]
        kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=f"item:{item}") for item in row])

    nav_buttons = []
    if page > 1:
        nav_buttons.append(InlineKeyboardButton(text="◀️ Назад", callback_data=f"page:{page - 1}"))
    if end_idx < len(items):
        nav_buttons.append(InlineKeyboardButton(text="Вперед ▶️", callback_data=f"page:{page + 1}"))

    if nav_buttons:
        kb_builder.row(*nav_buttons)

    return kb_builder.as_markup()

