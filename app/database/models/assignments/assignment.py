from datetime import datetime
from typing import List
from uuid import UUID

import pytz
from beanie import Document

from app.database.models.assignments.case import Case


class Assignment(Document):
    uuid: UUID
    is_ready: bool
    cases: List[Case]
    created_at: datetime = datetime.now(pytz.timezone('Europe/Moscow'))

    class Settings:
        name = "assignments"