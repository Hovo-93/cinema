from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import sync_session
from app.models.schedule import Schedule


class SeatService:

    @classmethod
    async def get_seat_map_by_schedule_id(cls, schedule_id: int):
        """
        Get seats for a specific show with movie and theater information
        """
        with sync_session() as session:
            stmt = (
                select(Schedule)
                .where(Schedule.id == schedule_id)
                .options(
                    selectinload(Schedule.seats),
                    selectinload(Schedule.movie),
                    selectinload(Schedule.room)
                )
            )
            result = session.execute(stmt)
            schedule = result.scalar_one_or_none()
            return schedule
