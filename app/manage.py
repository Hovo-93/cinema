import logging
import os
import sys
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sqladmin import Admin

from app.apps.admin.admin import RoomAdmin, MovieAdmin, ScheduleAdmin, SeatAdmin, BookingAdmin
from app.apps.router import router
from app.database import engine
from app.utils.fake_data import seed_data
from app.utils.migrations import run_migrations

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Run app...")

    try:
        logging.info("Run Alembic migration...")
        run_migrations()
        if os.getenv("SEED_FAKE_DATA", "false").lower() == "true":
            logging.info("🌱 Seeding fake data...")
            await seed_data()

        yield
    except Exception as e:
        logging.error(f"Error for run app: {e}")
        raise
    finally:
        logging.info("Shutting down app...")


def init():
    app = FastAPI(
        title="Cinema",
        version="1.0.0",
        lifespan=lifespan,
    )
    app.include_router(prefix="/v1", router=router)
    admin = Admin(app, engine, title='Cinema')
    admin.add_view(RoomAdmin)
    admin.add_view(MovieAdmin)
    admin.add_view(ScheduleAdmin)
    admin.add_view(SeatAdmin)
    admin.add_view(BookingAdmin)

    logging.info("Run FastAPI server...")
    return app



if __name__ == "__main__":
    app = init()
    uvicorn.run(app, host='0.0.0.0', port=38046)


app = init()
