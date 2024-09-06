from datetime import datetime
from typing import List, Optional
from uuid import UUID

import pytz
from beanie import Document, Link

from app.database.models.meetings.person import Person
from app.database.models.meetings.question import Question
from app.database.models.meetings.user import User


class Protocol(Document):
    uuid: UUID
    user: Link[User]
    title: str
    theme: str
    questions: List[Question]
    persons: Optional[List[Person]]
    created_at: datetime = datetime.now(pytz.timezone('Europe/Moscow'))

    class Settings:
        name = "protocols"