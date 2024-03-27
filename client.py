from discord import Bot
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json


def load_settings():
    with open("settings.json") as f:
        return json.load(f)


class LunaClient(Bot):
    def __init__(self, description=None, *args, **options):
        self.settings = load_settings()

        self.engine = create_engine(self.settings["postgres"])

        self.session = sessionmaker(bind=self.engine)

        super().__init__(description, *args, **options)
