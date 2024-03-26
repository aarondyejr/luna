from asyncio import AbstractEventLoop
from typing import Any
from discord import Bot
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class LunaClient(Bot):
    def __init__(self, description=None, *args, **options):

        self.engine = create_engine("postgresql://misty:579001aJ!110504@localhost:5432/luna")

        self.session = sessionmaker(bind=self.engine)

        super().__init__(description, *args, **options)