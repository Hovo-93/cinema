from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.configs import settings

engine = create_engine(
    settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600
)

sync_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


def check_version():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        version = result.scalar_one()
        print(f"Postgres version: {version}")


if __name__ == "__main__":
    check_version()
