from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import sync_session
from app.models.schedule import Schedule


class ScheduleService:

    @classmethod
    async def get_schedules_by_room_id(cls, room_id: int):
        with sync_session() as session:
            stmt = (
                select(Schedule)
                .where(Schedule.room_id == room_id)
                .options(selectinload(Schedule.movie))
                .order_by(Schedule.start_time)
            )
            result = session.execute(stmt)
            return result.scalars().all()
