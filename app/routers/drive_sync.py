import logging

from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

from app.database import SessionLocal
from app.services import drive_sync as drive_sync_service

logger = logging.getLogger("gestio.drive_sync")

router = APIRouter(prefix="/api/drive-sync", tags=["drive-sync"])


class DriveSyncAvviatoOut(BaseModel):
    avviato: bool
    messaggio: str


def _sync_in_background() -> None:
    db = SessionLocal()
    try:
        result = drive_sync_service.sync_corrispettivi(db)
        logger.info(
            "Drive sync corrispettivi (manuale): %s trovati, %s importati, %s già presenti, %s errori",
            result.trovati,
            result.importati,
            result.gia_presenti,
            len(result.errori),
        )
    except drive_sync_service.DriveSyncError as exc:
        logger.warning("Drive sync corrispettivi (manuale) fallita: %s", exc)
    finally:
        db.close()


@router.post("/corrispettivi", response_model=DriveSyncAvviatoOut)
def sync_corrispettivi(background_tasks: BackgroundTasks):
    """Avvia la sincronizzazione in background: una cartella con centinaia di
    file supera facilmente i timeout dei proxy (Render/Cloudflare) se
    eseguita dentro la richiesta HTTP. I risultati si vedono aggiornando
    l'elenco corrispettivi dopo qualche secondo/minuto."""
    if not drive_sync_service.is_configured():
        raise HTTPException(
            status_code=409,
            detail="Import da Drive non configurato: manca GOOGLE_SERVICE_ACCOUNT_JSON o "
            "GOOGLE_DRIVE_CORRISPETTIVI_FOLDER_ID.",
        )
    background_tasks.add_task(_sync_in_background)
    return DriveSyncAvviatoOut(avviato=True, messaggio="Sincronizzazione avviata in background.")
