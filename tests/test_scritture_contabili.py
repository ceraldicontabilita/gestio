from datetime import date
from decimal import Decimal

from sqlalchemy import select

from app.models import Conto, PrimaNotaMovimento, StatoMovimento, TipoMovimento
from app.services import scritture_contabili


def test_versamento_contanti_crea_coppia_collegata(db_session):
    cassa, banca = scritture_contabili.registra_versamento_contanti(
        db_session, importo=Decimal("500.00"), data=date(2026, 1, 10)
    )
    db_session.commit()

    assert cassa.conto == Conto.cassa
    assert cassa.tipo == TipoMovimento.uscita
    assert banca.conto == Conto.banca
    assert banca.tipo == TipoMovimento.entrata
    assert banca.stato == StatoMovimento.attesa
    assert cassa.operation_id == banca.operation_id
    assert cassa.importo == banca.importo == Decimal("500.00")


def test_versamento_contanti_idempotente(db_session):
    scritture_contabili.registra_versamento_contanti(
        db_session,
        importo=Decimal("500.00"),
        data=date(2026, 1, 10),
        source_external_id="ver-001",
    )
    db_session.commit()

    scritture_contabili.registra_versamento_contanti(
        db_session,
        importo=Decimal("500.00"),
        data=date(2026, 1, 10),
        source_external_id="ver-001",
    )
    db_session.commit()

    tutti = db_session.scalars(select(PrimaNotaMovimento)).all()
    assert len(tutti) == 2, "la seconda chiamata con lo stesso source_external_id non deve duplicare"


def test_riconciliazione_entrata_attesa(db_session):
    cassa, banca = scritture_contabili.registra_versamento_contanti(
        db_session, importo=Decimal("300.00"), data=date(2026, 1, 12)
    )
    db_session.commit()

    riconciliata = scritture_contabili.riconcilia_entrata_attesa(
        db_session, operation_id=cassa.operation_id, movimento_bancario_id="ec-123"
    )
    db_session.commit()

    assert riconciliata.id == banca.id
    assert riconciliata.stato == StatoMovimento.riconciliato
    assert riconciliata.movimento_bancario_id == "ec-123"


def test_saldo_progressivo_per_giorno(db_session):
    scritture_contabili.registra_movimento(
        db_session,
        conto=Conto.cassa,
        tipo=TipoMovimento.entrata,
        importo=Decimal("100.00"),
        data=date(2026, 1, 5),
        descrizione="Incasso",
        source="manuale",
    )
    scritture_contabili.registra_movimento(
        db_session,
        conto=Conto.cassa,
        tipo=TipoMovimento.uscita,
        importo=Decimal("30.00"),
        data=date(2026, 1, 5),
        descrizione="Spesa",
        source="manuale",
    )
    scritture_contabili.registra_movimento(
        db_session,
        conto=Conto.cassa,
        tipo=TipoMovimento.entrata,
        importo=Decimal("50.00"),
        data=date(2026, 1, 6),
        descrizione="Incasso",
        source="manuale",
    )
    db_session.commit()

    giorni = scritture_contabili.saldo_progressivo(db_session, conto=Conto.cassa)

    assert len(giorni) == 2
    assert giorni[0]["totale_netto"] == Decimal("70.00")
    assert giorni[0]["saldo_progressivo"] == Decimal("70.00")
    assert giorni[1]["totale_netto"] == Decimal("50.00")
    assert giorni[1]["saldo_progressivo"] == Decimal("120.00")


def test_importo_non_positivo_rifiutato(db_session):
    try:
        scritture_contabili.registra_movimento(
            db_session,
            conto=Conto.cassa,
            tipo=TipoMovimento.entrata,
            importo=Decimal("0.00"),
            data=date(2026, 1, 5),
            descrizione="Non valido",
            source="manuale",
        )
    except ValueError:
        pass
    else:
        raise AssertionError("importo <= 0 deve essere rifiutato")
