from app.database import sync_session
from app.models.movie import Movie
from datetime import datetime, timedelta

from app.models.room import Room
from app.models.schedule import Schedule
from app.models.seat import Seat


async def seed_data():
    with sync_session() as session:
        red = Room(name="Red")
        blue = Room(name="Blue")
        session.add_all([red, blue])
        session.flush()

        movie1 = Movie(title="Inception")
        movie2 = Movie(title="Matrix")
        session.add_all([movie1, movie2])
        session.flush()

        now = datetime.now().replace(minute=0, second=0, microsecond=0)
        schedules = [
            Schedule(room_id=red.id, movie_id=movie1.id, start_time=now + timedelta(hours=2)),
            Schedule(room_id=red.id, movie_id=movie2.id, start_time=now + timedelta(hours=4)),
            Schedule(room_id=blue.id, movie_id=movie1.id, start_time=now + timedelta(hours=1)),
            Schedule(room_id=blue.id, movie_id=movie2.id, start_time=now + timedelta(hours=3)),
        ]
        session.add_all(schedules)
        session.flush()

        for schedule in schedules:
            for row in range(1, 11):
                for column in range(1, 9):
                    seat = Seat(schedule_id=schedule.id, row=row, column=column, is_booked=False)
                    session.add(seat)
                    session.commit()

    print("✅ Fake data successfully seed!.")
