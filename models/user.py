from models.base import Base
from sqlalchemy import Uuid, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    balance: Mapped[int] = mapped_column(BigInteger, server_default="1000")
    guild_id: Mapped[Uuid] = mapped_column(ForeignKey("guild.id"), nullable=True)
    guild = relationship("Guild", back_populates="members")

    def __repr__(self) -> str:
        return (
            f"<User(id='{self.id}',balance='{self.balance},guild_id={self.guild_id}')>"
        )
