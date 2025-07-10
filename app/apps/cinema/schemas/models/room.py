from pydantic import BaseModel


class RoomResponseSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
