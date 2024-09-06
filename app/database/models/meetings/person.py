from beanie import Document


class Person(Document):
    full_name: str
    post: str

    class Settings:
        name = "persons"