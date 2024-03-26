from models.base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4


class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    balance: Mapped[int] = mapped_column(Integer, default=1000)

    def __repr__(self) -> str:
        return f"<User(id='{self.id}',balance='{self.balance}')>"
