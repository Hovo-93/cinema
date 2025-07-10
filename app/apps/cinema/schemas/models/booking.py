from pydantic import BaseModel
from datetime import datetime


class BookingCreateSchema(BaseModel):
    schedule_id: int
    row: int
    column: int


class BookingResponseSchema(BaseModel):
    seat_id: int
    booked_at: datetime

    class Config:
        from_attributes = True
