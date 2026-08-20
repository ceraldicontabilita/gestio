"""Import automatico dei corrispettivi RT da una cartella Google Drive del
cliente. Drive resta una fonte esterna in sola lettura (README.md), mai
persistenza: ogni file letto viene acquisito nel database Postgres tramite
la stessa logica idempotente dell'upload manuale
(app/services/corrispettivi.py) — un file già importato non genera righe
duplicate in Prima Nota, perché l'idempotenza è per dispositivo/data.

Richiede un account di servizio Google con la cartella Drive condivisa in
sola lettura (scope drive.readonly). Se GOOGLE_SERVICE_ACCOUNT_JSON non è
configurata, la sync è disattivata: le funzioni qui sotto sollevano
DriveSyncNotConfigured, mai un errore generico.
"""

import json
from dataclasses import dataclass

import requests
from google.auth.transport.requests import Request as GoogleAuthRequest
from google.oauth2 import service_account
from sqlalchemy.orm import Session

from app.config import get_settings
from app.models import Corrispettivo
from app.parsers.corrispettivi_rt import CorrispettivoXmlError
from app.services import corrispettivi as corrispettivi_service

DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
DRIVE_API_BASE = "https://www.googleapis.com/drive/v3"


class DriveSyncNotConfigured(RuntimeError):
    pass


class DriveSyncError(RuntimeError):
    pass


@dataclass
class DriveSyncResult:
    trovati: int
    importati: int
    gia_presenti: int
    errori: list[str]


def is_configured() -> bool:
    settings = get_settings()
    return bool(settings.google_service_account_json and settings.google_drive_corrispettivi_folder_id)


def _load_credentials() -> service_account.Credentials:
    settings = get_settings()
    if not settings.google_service_account_json:
        raise DriveSyncNotConfigured(
            "GOOGLE_SERVICE_ACCOUNT_JSON non configurata: import da Drive disattivato."
        )
    try:
        info = json.loads(settings.google_service_account_json)
    except json.JSONDecodeError as exc:
        raise DriveSyncError("GOOGLE_SERVICE_ACCOUNT_JSON non è un JSON valido") from exc
    return service_account.Credentials.from_service_account_info(info, scopes=DRIVE_SCOPES)


def _access_token() -> str:
    creds = _load_credentials()
    creds.refresh(GoogleAuthRequest())
    return creds.token


def _list_xml_files(folder_id: str, access_token: str) -> list[dict]:
    """Elenca tutti gli XML nella cartella, con paginazione: l'API Drive
    limita ogni risposta a un massimo di 100 file, e una cartella con
    centinaia di corrispettivi supera facilmente quel limite."""
    query = f"'{folder_id}' in parents and trashed = false and name contains '.xml'"
    files: list[dict] = []
    page_token: str | None = None
    while True:
        params = {"q": query, "fields": "nextPageToken,files(id,name,modifiedTime)", "pageSize": 100}
        if page_token:
            params["pageToken"] = page_token
        response = requests.get(
            f"{DRIVE_API_BASE}/files",
            params=params,
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=30,
        )
        if not response.ok:
            raise DriveSyncError(f"Drive API files.list fallita: {response.status_code} {response.text}")
        payload = response.json()
        files.extend(payload.get("files", []))
        page_token = payload.get("nextPageToken")
        if not page_token:
            break
    return files


def _download_file(file_id: str, access_token: str) -> bytes:
    response = requests.get(
        f"{DRIVE_API_BASE}/files/{file_id}",
        params={"alt": "media"},
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=60,
    )
    if not response.ok:
        raise DriveSyncError(f"Drive API files.get (media) fallita per {file_id}: {response.status_code}")
    return response.content


def sync_corrispettivi(db: Session, *, folder_id: str | None = None) -> DriveSyncResult:
    """Legge tutti gli XML nella cartella Drive dei corrispettivi e li importa.
    Idempotente: un file già importato (stesso dispositivo/data) non produce
    righe duplicate in Prima Nota."""
    settings = get_settings()
    target_folder = folder_id or settings.google_drive_corrispettivi_folder_id
    if not target_folder:
        raise DriveSyncNotConfigured(
            "GOOGLE_DRIVE_CORRISPETTIVI_FOLDER_ID non configurata: nessuna cartella da leggere."
        )

    access_token = _access_token()
    files = _list_xml_files(target_folder, access_token)

    importati = 0
    gia_presenti = 0
    errori: list[str] = []
    for f in files:
        try:
            xml_bytes = _download_file(f["id"], access_token)
            prima = db.query(Corrispettivo).count()
            corrispettivi_service.importa_corrispettivo_xml(
                db, xml_bytes=xml_bytes, source="google_drive"
            )
            db.commit()
            dopo = db.query(Corrispettivo).count()
            if dopo > prima:
                importati += 1
            else:
                gia_presenti += 1
        except CorrispettivoXmlError as exc:
            db.rollback()
            errori.append(f"{f.get('name', f['id'])}: {exc}")
        except DriveSyncError as exc:
            db.rollback()
            errori.append(f"{f.get('name', f['id'])}: {exc}")

    return DriveSyncResult(
        trovati=len(files), importati=importati, gia_presenti=gia_presenti, errori=errori
    )
