from typing import List, Optional

from beanie import Document, Link


class User(Document):
    telegram_id: int
    full_name: str
    protocols: Optional[List[Link["Protocol"]]] # noqa

    class Settings:
        name = "users"