from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    schedules: Mapped[list["Schedule"]] = relationship(back_populates="room")

