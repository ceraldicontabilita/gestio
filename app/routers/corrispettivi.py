from datetime import date, datetime
from decimal import Decimal

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Corrispettivo
from app.parsers.corrispettivi_rt import CorrispettivoXmlError
from app.services import corrispettivi as corrispettivi_service

router = APIRouter(prefix="/api/corrispettivi", tags=["corrispettivi"])


class RiepilogoIVAOut(BaseModel):
    aliquota_iva: str | None
    natura: str | None
    imposta: str
    ammontare: str
    importo_parziale: str


class CorrispettivoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    canonical_id: str
    operation_id: str
    id_dispositivo: str
    piva_esercente: str
    data_rilevazione: date
    numero_doc_commerciali: int
    pagato_contanti: Decimal
    pagato_elettronico: Decimal
    riepiloghi_iva: list[RiepilogoIVAOut]
    file_hash: str
    created_at: datetime


@router.get("", response_model=list[CorrispettivoOut])
def elenco_corrispettivi(db: Session = Depends(get_db)):
    return db.scalars(
        select(Corrispettivo).order_by(Corrispettivo.data_rilevazione.desc())
    ).all()


@router.post("/import", response_model=CorrispettivoOut)
async def importa_corrispettivo(file: UploadFile = File(...), db: Session = Depends(get_db)):
    xml_bytes = await file.read()
    try:
        corrispettivo = corrispettivi_service.importa_corrispettivo_xml(
            db, xml_bytes=xml_bytes, source="upload_manuale"
        )
    except CorrispettivoXmlError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    db.commit()
    db.refresh(corrispettivo)
    return corrispettivo


@router.delete("/{canonical_id}", status_code=204)
def elimina_corrispettivo(canonical_id: str, db: Session = Depends(get_db)):
    trovato = corrispettivi_service.elimina_corrispettivo(db, canonical_id=canonical_id)
    if not trovato:
        raise HTTPException(status_code=404, detail="Giornata non trovata")
    db.commit()
