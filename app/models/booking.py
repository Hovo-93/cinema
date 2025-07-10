from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database import Base
from app.models.timestamp_mixin import intpk, created_at


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[intpk]
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id", ondelete="CASCADE"), unique=True)
    booked_at: Mapped[created_at]

    seat: Mapped["Seat"] = relationship(back_populates="booking")
