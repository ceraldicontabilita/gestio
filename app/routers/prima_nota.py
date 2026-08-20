from datetime import date
from decimal import Decimal
from typing import Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Conto
from app.services import scritture_contabili

router = APIRouter(prefix="/api/prima-nota", tags=["prima-nota"])


class MovimentoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    canonical_id: str
    operation_id: str
    conto: str
    tipo: str
    data: date
    importo: Decimal
    valuta: str
    descrizione: str
    stato: str
    documento_id: str | None
    fattura_id: str | None
    movimento_bancario_id: str | None
    source: str


class GiornoOut(BaseModel):
    data: date
    totale_netto: Decimal
    saldo_progressivo: Decimal
    movimenti: list[MovimentoOut]


class MovimentoIn(BaseModel):
    tipo: Literal["entrata", "uscita"]
    importo: Decimal = Field(gt=0)
    data: date
    descrizione: str
    source_external_id: str | None = None


class VersamentoIn(BaseModel):
    importo: Decimal = Field(gt=0)
    data: date
    descrizione: str | None = None
    source_external_id: str | None = None


class RiconciliazioneIn(BaseModel):
    operation_id: str
    movimento_bancario_id: str


@router.post("/versamento", response_model=list[MovimentoOut])
def registra_versamento(payload: VersamentoIn, db: Session = Depends(get_db)):
    cassa, banca = scritture_contabili.registra_versamento_contanti(
        db,
        importo=payload.importo,
        data=payload.data,
        descrizione=payload.descrizione,
        source_external_id=payload.source_external_id,
    )
    db.commit()
    db.refresh(cassa)
    db.refresh(banca)
    return [cassa, banca]


@router.post("/riconciliazione", response_model=MovimentoOut)
def riconcilia(payload: RiconciliazioneIn, db: Session = Depends(get_db)):
    movimento = scritture_contabili.riconcilia_entrata_attesa(
        db,
        operation_id=payload.operation_id,
        movimento_bancario_id=payload.movimento_bancario_id,
    )
    db.commit()
    db.refresh(movimento)
    return movimento


# Le rotte dinamiche /{conto} vanno registrate per ultime: altrimenti
# intercetterebbero "versamento" e "riconciliazione" come se fossero un conto.
@router.get("/{conto}", response_model=list[GiornoOut])
def elenco_movimenti(conto: Conto, db: Session = Depends(get_db)):
    return scritture_contabili.saldo_progressivo(db, conto=conto)


@router.post("/{conto}", response_model=MovimentoOut)
def registra_movimento_manuale(conto: Conto, payload: MovimentoIn, db: Session = Depends(get_db)):
    movimento = scritture_contabili.registra_movimento(
        db,
        conto=conto,
        tipo=payload.tipo,
        importo=payload.importo,
        data=payload.data,
        descrizione=payload.descrizione,
        source="manuale",
        source_external_id=payload.source_external_id,
    )
    db.commit()
    db.refresh(movimento)
    return movimento
