from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.menu import main_keyboard

router = Router()

@router.message(Command(commands=["start"]))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Приветствую! Я многофункциональный ИИ-Ассистент, готов помочь вам в решении различных задач. "
        "Используйте меню ниже, чтобы выбрать команду или введите команду /help для получения справки.",
        reply_markup=main_keyboard
    )