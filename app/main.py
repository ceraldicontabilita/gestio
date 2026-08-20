import logging

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import Base, SessionLocal, engine
from app.routers import corrispettivi, drive_sync, prima_nota
from app.services import drive_sync as drive_sync_service

logger = logging.getLogger("gestio.drive_sync")

settings = get_settings()

app = FastAPI(title="Gestio")

# MVP: crea le tabelle direttamente dai modelli all'avvio. Da sostituire con
# migrazioni Alembic prima della produzione (vedi docs/spec/07_TEST_E_ACCETTAZIONE/
# per i gate su migrazioni idempotenti).
Base.metadata.create_all(bind=engine)

if settings.cors_allowed_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[o.strip() for o in settings.cors_allowed_origins.split(",") if o.strip()],
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(prima_nota.router)
app.include_router(corrispettivi.router)
app.include_router(drive_sync.router)


def _run_scheduled_drive_sync() -> None:
    db = SessionLocal()
    try:
        result = drive_sync_service.sync_corrispettivi(db)
        if result.importati or result.errori:
            logger.info(
                "Drive sync corrispettivi: %s importati, %s già presenti, %s errori",
                result.importati,
                result.gia_presenti,
                len(result.errori),
            )
    except drive_sync_service.DriveSyncNotConfigured:
        pass
    except drive_sync_service.DriveSyncError as exc:
        logger.warning("Drive sync corrispettivi fallita: %s", exc)
    finally:
        db.close()


if settings.google_service_account_json and settings.drive_sync_interval_minutes > 0:
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        _run_scheduled_drive_sync,
        "interval",
        minutes=settings.drive_sync_interval_minutes,
    )
    scheduler.start()


@app.get("/api/health")
def health():
    return {"status": "ok"}
