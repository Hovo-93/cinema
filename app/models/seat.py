from sqlalchemy import UniqueConstraint, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.timestamp_mixin import intpk


class Seat(Base):
    __tablename__ = "seats"
    __table_args__ = (UniqueConstraint("schedule_id", "row", "column", name="uix_schedule_seat"),)

    id: Mapped[intpk]
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedules.id", ondelete="CASCADE"))
    row: Mapped[int] = mapped_column(Integer)
    column: Mapped[int] = mapped_column(Integer)
    is_booked: Mapped[bool] = mapped_column(Boolean, default=False)

    schedule: Mapped["Schedule"] = relationship(back_populates="seats")
    booking: Mapped["Booking"] = relationship(back_populates="seat", uselist=False)
