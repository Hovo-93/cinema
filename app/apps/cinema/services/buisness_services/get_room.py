from fastapi import HTTPException, status

from app.apps.cinema.schemas.models.room import RoomResponseSchema
from app.apps.cinema.services.infrastructure_services.room_service import RoomService


async def get_room(
        room_service: RoomService = RoomService()

):
    try:
        rooms = await room_service.get_rooms()
        return [
            RoomResponseSchema(
                id=room.id,
                name=room.name
            ) for room in rooms
        ]
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Something went wrong") from e
