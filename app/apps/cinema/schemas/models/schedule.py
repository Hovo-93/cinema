from pydantic import BaseModel
from datetime import datetime


class MovieSchema(BaseModel):
    id: int
    title: str
    poster_url: str

    class Config:
        from_attributes = True


class ScheduleReadSchema(BaseModel):
    schedule_id: int
    start_time: datetime
    movie: MovieSchema
