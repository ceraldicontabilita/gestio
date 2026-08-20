from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import get_settings

settings = get_settings()

# Render (e in generale i provider Postgres) forniscono DATABASE_URL con lo
# schema generico postgres://|postgresql://. SQLAlchemy in quel caso sceglie
# di default il driver psycopg2, che non installiamo: forziamo psycopg (v3),
# il driver presente in backend/requirements.txt.
url = make_url(settings.database_url)
if url.drivername in ("postgres", "postgresql"):
    url = url.set(drivername="postgresql+psycopg")

connect_args = {"check_same_thread": False} if url.drivername.startswith("sqlite") else {}
engine = create_engine(url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
