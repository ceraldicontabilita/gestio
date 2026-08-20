"""Motore unico Prima Nota.

Nessun router o import deve scrivere scritture contabili al di fuori di
questo modulo (docs/spec/01_MASTER/PROMPT_MASTER.md §10 e
docs/spec/01_MASTER/ISTRUZIONI_AGENTI.md - regole contabili vincolanti).
"""

import uuid
from datetime import date as date_
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Conto, PrimaNotaMovimento, StatoMovimento, TipoMovimento


def _new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


def registra_movimento(
    db: Session,
    *,
    conto: Conto,
    tipo: TipoMovimento,
    importo: Decimal,
    data: date_,
    descrizione: str,
    source: str,
    operation_id: str | None = None,
    canonical_id: str | None = None,
    source_external_id: str | None = None,
    stato: StatoMovimento = StatoMovimento.confermato,
    documento_id: str | None = None,
    fattura_id: str | None = None,
    movimento_bancario_id: str | None = None,
    valuta: str = "EUR",
) -> PrimaNotaMovimento:
    """Scrive una riga di Prima Nota. Idempotente su (source, source_external_id):
    una seconda chiamata con la stessa coppia restituisce la riga già scritta
    invece di duplicarla."""
    if importo <= 0:
        raise ValueError("importo deve essere positivo")

    if source_external_id is not None:
        existing = db.scalar(
            select(PrimaNotaMovimento).where(
                PrimaNotaMovimento.source == source,
                PrimaNotaMovimento.source_external_id == source_external_id,
            )
        )
        if existing is not None:
            return existing

    movimento = PrimaNotaMovimento(
        canonical_id=canonical_id or _new_id("mov"),
        operation_id=operation_id or _new_id("op"),
        conto=conto,
        tipo=tipo,
        data=data,
        anno=data.year,
        importo=importo,
        valuta=valuta,
        descrizione=descrizione,
        stato=stato,
        documento_id=documento_id,
        fattura_id=fattura_id,
        movimento_bancario_id=movimento_bancario_id,
        source=source,
        source_external_id=source_external_id,
    )
    db.add(movimento)
    db.flush()
    return movimento


def registra_versamento_contanti(
    db: Session,
    *,
    importo: Decimal,
    data: date_,
    source: str = "manuale",
    source_external_id: str | None = None,
    descrizione: str | None = None,
) -> tuple[PrimaNotaMovimento, PrimaNotaMovimento]:
    """Un versamento contanti genera uscita Cassa ed entrata Banca attesa con lo
    stesso operation_id; il movimento di estratto conto riconcilia l'attesa senza
    crearne una terza (docs/spec/01_MASTER/PROMPT_MASTER.md §10)."""
    if source_external_id is not None:
        existing_cassa = db.scalar(
            select(PrimaNotaMovimento).where(
                PrimaNotaMovimento.source == source,
                PrimaNotaMovimento.source_external_id == source_external_id,
                PrimaNotaMovimento.conto == Conto.cassa,
            )
        )
        if existing_cassa is not None:
            existing_banca = db.scalar(
                select(PrimaNotaMovimento).where(
                    PrimaNotaMovimento.operation_id == existing_cassa.operation_id,
                    PrimaNotaMovimento.conto == Conto.banca,
                )
            )
            return existing_cassa, existing_banca

    operation_id = _new_id("op")
    uscita_cassa = registra_movimento(
        db,
        conto=Conto.cassa,
        tipo=TipoMovimento.uscita,
        importo=importo,
        data=data,
        descrizione=descrizione or "Versamento in banca",
        source=source,
        operation_id=operation_id,
        source_external_id=source_external_id,
        stato=StatoMovimento.confermato,
    )
    entrata_banca = registra_movimento(
        db,
        conto=Conto.banca,
        tipo=TipoMovimento.entrata,
        importo=importo,
        data=data,
        descrizione=descrizione or "Versamento da Cassa",
        source=source,
        operation_id=operation_id,
        stato=StatoMovimento.attesa,
    )
    return uscita_cassa, entrata_banca


def riconcilia_entrata_attesa(
    db: Session, *, operation_id: str, movimento_bancario_id: str
) -> PrimaNotaMovimento:
    """Riconcilia l'entrata Banca attesa di un'operazione quando il movimento
    compare nell'estratto conto importato."""
    entrata = db.scalar(
        select(PrimaNotaMovimento).where(
            PrimaNotaMovimento.operation_id == operation_id,
            PrimaNotaMovimento.conto == Conto.banca,
            PrimaNotaMovimento.stato == StatoMovimento.attesa,
        )
    )
    if entrata is None:
        raise ValueError(f"nessuna entrata attesa per operation_id={operation_id}")
    entrata.stato = StatoMovimento.riconciliato
    entrata.movimento_bancario_id = movimento_bancario_id
    db.flush()
    return entrata


def saldo_progressivo(
    db: Session, *, conto: Conto, saldo_iniziale: Decimal = Decimal("0")
) -> list[dict]:
    """Movimenti di un conto raggruppati per giorno con saldo progressivo, come
    richiesto dalla scheda pagina Prima Nota: 'Calcolare saldi progressivi dal
    riporto iniziale e dalle righe ordinate; ogni giorno espone numero
    operazioni e totale netto.'"""
    movimenti = db.scalars(
        select(PrimaNotaMovimento)
        .where(PrimaNotaMovimento.conto == conto)
        .order_by(PrimaNotaMovimento.data, PrimaNotaMovimento.id)
    ).all()

    saldo = saldo_iniziale
    giorni: dict[date_, dict] = {}
    for movimento in movimenti:
        segno = 1 if movimento.tipo == TipoMovimento.entrata else -1
        saldo += segno * movimento.importo
        giorno = giorni.setdefault(
            movimento.data,
            {"data": movimento.data, "movimenti": [], "totale_netto": Decimal("0")},
        )
        giorno["movimenti"].append(movimento)
        giorno["totale_netto"] += segno * movimento.importo
        giorno["saldo_progressivo"] = saldo
    return list(giorni.values())
