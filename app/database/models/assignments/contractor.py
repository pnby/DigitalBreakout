from datetime import datetime

import pytz
from pydantic import BaseModel


class Contractor(BaseModel):
    director: str
    implementing_organization: str
    created_at: datetime = datetime.now(pytz.timezone('Europe/Moscow'))

    class Settings:
        name = "executors"