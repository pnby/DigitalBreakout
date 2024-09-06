from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.models.meetings.decision import Decision
from app.database.models.meetings.question import Question
from app.database.models.meetings.user import User
from app.keyboards.menu import main_menu
from app.utils.utils import mock_data

router = Router()

@router.message(Command(commands=["start"]))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Что-то очень интересное", reply_markup=main_menu)