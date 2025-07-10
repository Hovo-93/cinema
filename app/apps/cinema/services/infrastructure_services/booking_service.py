from sqlalchemy import select
from app.database import sync_session
from app.models.seat import Seat
from app.models.booking import Booking
from fastapi import HTTPException
from datetime import datetime


class BookingService:
    @classmethod
    async def book_seat(cls, schedule_id: int, row: int, column: int) -> Booking:
        """
        Book seats for session
        """
        with sync_session() as session:
            with session.begin():
                stmt = select(Seat).where(
                    Seat.schedule_id == schedule_id,
                    Seat.row == row,
                    Seat.column == column
                ).limit(1)
                result = await session.execute(stmt)
                seat = result.scalar_one_or_none()

                if not seat:
                    raise HTTPException(status_code=404, detail="Seat not found")

                if seat.is_booked:
                    raise HTTPException(status_code=400, detail="Seat already booked")

                seat.is_booked = True
                booking = Booking(seat_id=seat.id, booked_at=datetime.now())
                session.add(booking)

                await session.commit()
                await session.refresh(booking)
                return booking
