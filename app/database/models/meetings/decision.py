from beanie import Document


class Decision(Document):
    title: str
    brief_context: str
    elapsed_time: str # mm:ss

    class Settings:
        name = "decisions"