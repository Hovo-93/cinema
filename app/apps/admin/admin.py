from sqladmin import ModelView
from app.models.room import Room
from app.models.movie import Movie
from app.models.seat import Seat
from app.models.booking import Booking
from app.models.schedule import Schedule


class RoomAdmin(ModelView, model=Room):
    name = "Room"
    name_plural = "Rooms"
    icon = "fas fa-door-open"
    column_list = [Room.id, Room.name]
    column_searchable_list = [Room.name]
    column_sortable_list = [Room.id, Room.name]
    can_create = True
    can_edit = True
    can_delete = True


class ScheduleAdmin(ModelView, model=Schedule):
    name = "Schedule"
    name_plural = "Schedules"
    icon = "fas fa-calendar-alt"

    column_list = [Schedule.id, Schedule.room_id, Schedule.movie_id, Schedule.start_time]
    column_sortable_list = [Schedule.id, Schedule.start_time]

    can_create = True
    can_edit = True
    can_delete = True


class SeatAdmin(ModelView, model=Seat):
    name = "Seat"
    name_plural = "Seats"
    icon = "fas fa-chair"

    column_list = [Seat.id, Seat.schedule_id, Seat.row, Seat.column, Seat.is_booked]
    column_sortable_list = [Seat.id, Seat.row, Seat.column]
    column_filters = [Seat.is_booked]

    can_create = True
    can_edit = True
    can_delete = True


class BookingAdmin(ModelView, model=Booking):
    name = "Booking"
    name_plural = "Bookings"
    icon = "fas fa-ticket-alt"

    column_list = [Booking.id, Booking.seat_id, Booking.booked_at]
    column_sortable_list = [Booking.id, Booking.booked_at]

    can_create = True
    can_edit = False
    can_delete = True


class MovieAdmin(ModelView, model=Movie):
    name = "Movie"
    name_plural = "Movies"
    icon = "fas fa-film"

    column_list = [Movie.id, Movie.title]
    column_searchable_list = [Movie.title]
    column_sortable_list = [Movie.id, Movie.title]

    can_create = True
    can_edit = True
    can_delete = True
