import asyncio
from typing import final

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import BOT_TOKEN, MONGO_URI
from app.database.models.assignments.assignment import Assignment
from app.database.models.meetings.decision import Decision
from app.database.models.meetings.person import Person
from app.database.models.meetings.protocol import Protocol
from app.database.models.meetings.question import Question
from app.database.models.meetings.user import User
from app.utils.singleton import singleton
from handlers.service import router as service_router
from handlers.start import router as start_router
from handlers.transcription import router as transcription_router


@final
@singleton
class Startup(object):
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    _dp = Dispatcher()

    @staticmethod
    async def _init_database():
        client = AsyncIOMotorClient(MONGO_URI)
        await init_beanie(database=client.db_name, document_models=[User, Question, Protocol, Person, Decision, Assignment])

    async def start_polling(self):
        await self._init_database()
        await self._dp.start_polling(self.bot)

    def register_routers(self):
        self._dp.include_routers(service_router, start_router, transcription_router)


if __name__ == "__main__":
    startup = Startup()
    startup.register_routers()
    asyncio.run(startup.start_polling())