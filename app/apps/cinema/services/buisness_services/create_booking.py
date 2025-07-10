from app.apps.cinema.schemas.models.booking import BookingCreateSchema
from app.apps.cinema.services.infrastructure_services.booking_service import BookingService


async def booking_seat(

        data: BookingCreateSchema,
        booking_service: BookingService = BookingService()

):
    booking = await booking_service.book_seat(
        schedule_id=data.schedule_id,
        row=data.row,
        column=data.column
    )
    return booking
