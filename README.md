# 🎬 Cinema  API


Users can:
- View available rooms
- See movie schedules per room
- View available and booked seats per schedule
- Book seats for a selected movie session

Admins can:
- Manage rooms, movies, schedules, seats, and bookings via admin panel (sqladmin)

---

## 🚀 Features

- REST API with FastAPI
- SQLAlchemy 2.0 async support
- PostgreSQL support
- Admin panel with [sqladmin](https://github.com/awtkns/sqladmin)
- Alembic migrations
- Booking with transactional safety (`FOR UPDATE` locking)
- Demo seed data script

---

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy 2.0
- PostgreSQL + asyncpg
- Alembic
- sqladmin

---

## 🚀 How to Run (using Poetry)

### 1. Clone the repository

```bash
git clone https://github.com/Hovo-93/cinema.git
cd cinema
```
```
poetry install
```

Create app/.env and connect your local DB
```dotenv
POSTGRES_USER=user
POSTGRES_PASS=pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_NAME=cinema
SEED_FAKE_DATA=true
```

Run the application
```bash
  python app/manage.py run
```
