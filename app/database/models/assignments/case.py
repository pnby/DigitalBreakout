from datetime import datetime
from typing import List

import pytz
from pydantic import BaseModel

from app.database.models.assignments.contractor import Contractor


class Case(BaseModel):
    text: str
    deadline: datetime
    contractors: List[Contractor]
    created_at: datetime = datetime.now(pytz.timezone('Europe/Moscow'))

    class Settings:
        name = "assignments"