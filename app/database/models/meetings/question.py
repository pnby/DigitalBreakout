from typing import Optional, List

from beanie import Document

from app.database.models.meetings.decision import Decision
from app.database.models.meetings.person import Person


class Question(Document):
    title: str
    persons: Optional[List[Person]]
    decision: List[Decision]

    class Settings:
        name = "questions"