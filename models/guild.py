from models.base import Base
from models.user import User
from typing import List
from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4


class Guild(Base):
    __tablename__ = "guild"

    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, nullable=False, default=uuid4()
    )
    name: Mapped[str] = mapped_column(String(length=16), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    members: Mapped[List[User]] = relationship("User", back_populates="guild")

    def __repr__(self) -> str:
        return f"Guild<id={self.id},name={self.name},description={self.description},member={self.member}>"
