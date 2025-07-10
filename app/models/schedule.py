from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.timestamp_mixin import intpk, created_at


class Schedule(Base):
    __tablename__ = "schedules"

    id: Mapped[intpk]
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id", ondelete="CASCADE"))
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id", ondelete="CASCADE"))
    start_time: Mapped[created_at]

    room: Mapped["Room"] = relationship(back_populates="schedules")
    movie: Mapped["Movie"] = relationship(back_populates="schedules")
    seats: Mapped[list["Seat"]] = relationship(back_populates="schedule", cascade="all, delete-orphan")
