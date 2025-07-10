from fastapi import HTTPException,status

from app.apps.cinema.schemas.models.schedule import ScheduleReadSchema
from app.apps.cinema.services.infrastructure_services.schedule_service import ScheduleService


async def get_room_scheduled(
        room_id: int,
        schedule_service: ScheduleService = ScheduleService()

):
    schedules = await schedule_service.get_schedules_by_room_id(room_id)
    if not schedules:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No schedules found for this room")

    return [
        ScheduleReadSchema(
            schedule_id=schedule.id,
            start_time=schedule.start_time,
            movie=schedule.movie
        ) for schedule in schedules
    ]
