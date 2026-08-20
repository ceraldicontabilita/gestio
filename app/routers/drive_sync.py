from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import drive_sync as drive_sync_service

router = APIRouter(prefix="/api/drive-sync", tags=["drive-sync"])


class DriveSyncOut(BaseModel):
    trovati: int
    importati: int
    gia_presenti: int
    errori: list[str]


@router.post("/corrispettivi", response_model=DriveSyncOut)
def sync_corrispettivi(db: Session = Depends(get_db)):
    try:
        result = drive_sync_service.sync_corrispettivi(db)
    except drive_sync_service.DriveSyncNotConfigured as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except drive_sync_service.DriveSyncError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return result
