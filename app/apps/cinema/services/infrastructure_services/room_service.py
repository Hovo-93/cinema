from sqlalchemy import select

from app.database import sync_session
from app.models.room import Room


class RoomService:
    @classmethod
    async def get_rooms(cls):
        """
        Get all rooms.
        """
        with sync_session() as session:
            result = await session.execute(select(Room))
            return result.scalars().all()
