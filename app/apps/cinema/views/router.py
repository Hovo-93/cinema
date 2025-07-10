from fastapi import APIRouter

from app.apps.cinema.views.rooms import router as cinema_router
from app.apps.cinema.views.booking import router as booking_router

cinema_module_router = APIRouter(
    tags=["Cinema"],
)

cinema_module_router.include_router(
    cinema_router,
)

booking_module_router = APIRouter(tags=["Booking"])
booking_module_router.include_router(booking_router, prefix="/booking")
