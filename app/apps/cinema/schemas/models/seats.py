from pydantic import BaseModel
from datetime import datetime
from typing import List


class SeatReadSchema(BaseModel):
    """Info about a seat"""
    row: int
    column: int
    is_booked: bool

    class Config:
        from_attributes = True


class ScheduleSeatMap(BaseModel):
    """Response: info schedule + list of seats"""
    schedule_id: int
    room_name: str
    movie_title: str
    start_time: datetime
    seats: List[SeatReadSchema]
