from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest
from sqlalchemy import select

from app.models import Conto, Corrispettivo, PrimaNotaMovimento, StatoMovimento
from app.parsers.corrispettivi_rt import CorrispettivoXmlError, parse_corrispettivo_xml
from app.services import corrispettivi as corrispettivi_service

FIXTURE = Path(__file__).parent / "fixtures" / "corrispettivo_esempio.xml"


def test_parse_corrispettivo_xml_reale():
    parsed = parse_corrispettivo_xml(FIXTURE.read_bytes())

    assert parsed.id_dispositivo == "99TEST000001"
    assert parsed.numero_doc_commerciali == 42
    assert parsed.pagato_contanti == Decimal("250.00")
    assert parsed.pagato_elettronico == Decimal("370.00")
    assert len(parsed.riepiloghi_iva) == 3
    aliquote = {r.aliquota_iva for r in parsed.riepiloghi_iva if r.aliquota_iva is not None}
    assert aliquote == {Decimal("10.00"), Decimal("22.00")}
    esente = [r for r in parsed.riepiloghi_iva if r.natura is not None]
    assert esente[0].natura == "N4"


def test_parse_corrispettivo_xml_invalido():
    with pytest.raises(CorrispettivoXmlError):
        parse_corrispettivo_xml(b"<non-e-xml-corrispettivi/>")


def test_importa_corrispettivo_crea_cassa_e_pos_atteso(db_session):
    corrispettivo = corrispettivi_service.importa_corrispettivo_xml(
        db_session, xml_bytes=FIXTURE.read_bytes()
    )
    db_session.commit()

    assert corrispettivo.data_rilevazione == date(2026, 3, 1)
    assert corrispettivo.pagato_contanti == Decimal("250.00")

    movimenti = db_session.scalars(
        select(PrimaNotaMovimento).where(PrimaNotaMovimento.operation_id == corrispettivo.operation_id)
    ).all()
    assert len(movimenti) == 2

    cassa = next(m for m in movimenti if m.conto == Conto.cassa)
    banca = next(m for m in movimenti if m.conto == Conto.banca)

    assert cassa.importo == Decimal("250.00")
    assert cassa.stato == StatoMovimento.confermato
    assert banca.importo == Decimal("370.00")
    assert banca.stato == StatoMovimento.attesa
    assert cassa.documento_id == corrispettivo.canonical_id


def test_elimina_corrispettivo_rimuove_giornata_e_movimenti(db_session):
    corrispettivo = corrispettivi_service.importa_corrispettivo_xml(
        db_session, xml_bytes=FIXTURE.read_bytes()
    )
    db_session.commit()

    rimosso = corrispettivi_service.elimina_corrispettivo(db_session, canonical_id=corrispettivo.canonical_id)
    db_session.commit()

    assert rimosso is True
    assert db_session.scalar(select(Corrispettivo).where(Corrispettivo.canonical_id == corrispettivo.canonical_id)) is None
    movimenti = db_session.scalars(
        select(PrimaNotaMovimento).where(PrimaNotaMovimento.operation_id == corrispettivo.operation_id)
    ).all()
    assert movimenti == []


def test_elimina_corrispettivo_inesistente_ritorna_false(db_session):
    assert corrispettivi_service.elimina_corrispettivo(db_session, canonical_id="non-esiste") is False


def test_importa_corrispettivo_idempotente(db_session):
    corrispettivi_service.importa_corrispettivo_xml(db_session, xml_bytes=FIXTURE.read_bytes())
    db_session.commit()

    corrispettivi_service.importa_corrispettivo_xml(db_session, xml_bytes=FIXTURE.read_bytes())
    db_session.commit()

    giornate = db_session.scalars(select(Corrispettivo)).all()
    assert len(giornate) == 1, "un secondo import dello stesso file non deve creare una seconda giornata"

    movimenti = db_session.scalars(select(PrimaNotaMovimento)).all()
    assert len(movimenti) == 2, "né duplicare le scritture di Prima Nota"
