import enum
from datetime import date as date_
from datetime import datetime
from decimal import Decimal

from sqlalchemy import JSON, Date, DateTime, Enum, Index, Integer, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Conto(str, enum.Enum):
    """Cassa, Banca, SumUp e Soci sono conti distinti dello stesso ledger
    (docs/spec/03_PAGINE/LOGICA_JSON/08-prima-nota.json), non tabelle separate."""

    cassa = "cassa"
    banca = "banca"
    sumup = "sumup"
    soci = "soci"


class TipoMovimento(str, enum.Enum):
    entrata = "entrata"
    uscita = "uscita"


class StatoMovimento(str, enum.Enum):
    confermato = "confermato"
    attesa = "attesa"
    riconciliato = "riconciliato"


class PrimaNotaMovimento(Base):
    """Riga del registro Prima Nota. Colonne allineate a
    docs/spec/01_MASTER/PROMPT_MASTER.md §5 (Architettura dati)."""

    __tablename__ = "prima_nota_movimenti"
    __table_args__ = (
        UniqueConstraint("source", "source_external_id", name="uq_prima_nota_source"),
        Index("ix_prima_nota_conto_data", "conto", "data"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    canonical_id: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    operation_id: Mapped[str] = mapped_column(String(64), index=True)
    conto: Mapped[Conto] = mapped_column(Enum(Conto), nullable=False)
    tipo: Mapped[TipoMovimento] = mapped_column(Enum(TipoMovimento), nullable=False)
    data: Mapped[date_] = mapped_column(Date, nullable=False)
    anno: Mapped[int] = mapped_column(Integer, nullable=False)
    importo: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    valuta: Mapped[str] = mapped_column(String(3), default="EUR", nullable=False)
    descrizione: Mapped[str] = mapped_column(Text, nullable=False)
    stato: Mapped[StatoMovimento] = mapped_column(Enum(StatoMovimento), default=StatoMovimento.confermato, nullable=False)
    documento_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    fattura_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    movimento_bancario_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    source: Mapped[str] = mapped_column(String(64), nullable=False)
    source_external_id: Mapped[str | None] = mapped_column(String(128), nullable=True)
    file_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)
    parser_version: Mapped[str | None] = mapped_column(String(32), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    payload_schema_version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    payload_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
