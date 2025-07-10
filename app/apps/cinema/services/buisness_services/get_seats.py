from fastapi import HTTPException,status

from app.apps.cinema.schemas.models.seats import ScheduleSeatMap
from app.apps.cinema.services.infrastructure_services.seat_service import SeatService


async def get_seats_for_schedule(
    schedule_id: int,
    seat_service: SeatService = SeatService()
):

    schedule = await seat_service.get_seat_map_by_schedule_id(schedule_id)

    if not schedule:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")

    return ScheduleSeatMap(
        schedule_id=schedule.id,
        room_name=schedule.room.name,
        movie_title=schedule.movie.title,
        start_time=schedule.start_time,
        seats=schedule.seats
    )