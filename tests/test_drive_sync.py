from pathlib import Path

import pytest
from sqlalchemy import select

from app.models import Corrispettivo
from app.services import drive_sync as drive_sync_service

FIXTURE = Path(__file__).parent / "fixtures" / "corrispettivo_esempio.xml"


def test_sync_senza_credenziali_solleva_not_configured(db_session):
    with pytest.raises(drive_sync_service.DriveSyncNotConfigured):
        drive_sync_service.sync_corrispettivi(db_session, folder_id="qualunque")


def test_sync_importa_file_nuovi(db_session, monkeypatch):
    monkeypatch.setattr(drive_sync_service, "_access_token", lambda: "fake-token")
    monkeypatch.setattr(
        drive_sync_service,
        "_list_xml_files",
        lambda folder_id, access_token: [{"id": "file-1", "name": "corrispettivo.xml"}],
    )
    monkeypatch.setattr(
        drive_sync_service, "_download_file", lambda file_id, access_token: FIXTURE.read_bytes()
    )

    result = drive_sync_service.sync_corrispettivi(db_session, folder_id="cartella-test")

    assert result.trovati == 1
    assert result.importati == 1
    assert result.gia_presenti == 0
    assert result.errori == []
    assert db_session.scalar(select(Corrispettivo).limit(1)) is not None


def test_sync_e_idempotente_su_file_gia_importato(db_session, monkeypatch):
    monkeypatch.setattr(drive_sync_service, "_access_token", lambda: "fake-token")
    monkeypatch.setattr(
        drive_sync_service,
        "_list_xml_files",
        lambda folder_id, access_token: [{"id": "file-1", "name": "corrispettivo.xml"}],
    )
    monkeypatch.setattr(
        drive_sync_service, "_download_file", lambda file_id, access_token: FIXTURE.read_bytes()
    )

    drive_sync_service.sync_corrispettivi(db_session, folder_id="cartella-test")
    result = drive_sync_service.sync_corrispettivi(db_session, folder_id="cartella-test")

    assert result.importati == 0
    assert result.gia_presenti == 1
    giornate = db_session.scalars(select(Corrispettivo)).all()
    assert len(giornate) == 1


def test_sync_registra_errori_di_parsing_senza_interrompersi(db_session, monkeypatch):
    monkeypatch.setattr(drive_sync_service, "_access_token", lambda: "fake-token")
    monkeypatch.setattr(
        drive_sync_service,
        "_list_xml_files",
        lambda folder_id, access_token: [{"id": "file-1", "name": "non-valido.xml"}],
    )
    monkeypatch.setattr(
        drive_sync_service, "_download_file", lambda file_id, access_token: b"<non-e-xml/>"
    )

    result = drive_sync_service.sync_corrispettivi(db_session, folder_id="cartella-test")

    assert result.trovati == 1
    assert result.importati == 0
    assert len(result.errori) == 1
    assert "non-valido.xml" in result.errori[0]
