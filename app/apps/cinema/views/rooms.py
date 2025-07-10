from fastapi import APIRouter
from starlette import status

from app.apps.cinema.schemas.models.room import RoomResponseSchema
from app.apps.cinema.schemas.models.schedule import ScheduleReadSchema
from app.apps.cinema.schemas.models.seats import ScheduleSeatMap

from app.apps.cinema.services.buisness_services.get_room import get_room
from app.apps.cinema.services.buisness_services.get_scheduled import get_room_scheduled
from app.apps.cinema.services.buisness_services.get_seats import get_seats_for_schedule

router = APIRouter()


@router.get("/room",
            response_model=RoomResponseSchema,
            status_code=status.HTTP_200_OK
            )
async def get_room_view(

):
    """
    Get room information
    """
    response = await get_room()
    return response


@router.get("/rooms/{room_id}/schedules",
            response_model=list[ScheduleReadSchema]
            )
async def get_room_schedules_view(
        room_id: int,
):
    """
    Retrieve a list of movie sessions (schedules) for a specific room (room_id),
    including movie information and start time.
    """
    response = await get_room_scheduled(room_id=room_id)
    return response


@router.get("/schedules/{schedule_id}/seats", response_model=ScheduleSeatMap)
async def get_seats_for_schedule_view(
        schedule_id: int
):
    """
    Retrieve seat map for a specific schedule,
    including seat positions and booking status.
    """
    response = await get_seats_for_schedule(schedule_id=schedule_id)
    return response
