from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.timestamp_mixin import intpk,created_at


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(255))

    schedules: Mapped[list["Schedule"]] = relationship(back_populates="movie")
    created_at: Mapped[created_at]
