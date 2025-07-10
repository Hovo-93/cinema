from fastapi import APIRouter

from app.apps.cinema.views.router import cinema_module_router, booking_module_router

router = APIRouter()

router.include_router(cinema_module_router)
router.include_router(booking_module_router)
