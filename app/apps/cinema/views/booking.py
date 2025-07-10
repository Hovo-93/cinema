from fastapi import APIRouter
from app.apps.cinema.schemas.models.booking import BookingCreateSchema, BookingResponseSchema
from app.apps.cinema.services.buisness_services.create_booking import booking_seat

router = APIRouter()


@router.post("/", response_model=BookingResponseSchema)
async def booking_seat_view(
        data: BookingCreateSchema,
):
    """
    Create a booking for a given seat (row/column) on a schedule.
    """
    response = await booking_seat(
       data=data
    )
    return response
