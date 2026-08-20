from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    # Target: PostgreSQL (istanza gestita su Render). Il default SQLite
    # vale solo per sviluppo locale senza DATABASE_URL configurata.
    database_url: str = "sqlite:///./gestio.db"
    document_storage_path: str = "./storage"
    secret_key: str = "dev-secret-change-me"
    # Origini frontend ammesse per CORS (separate da virgola); vuoto = CORS disattivato.
    cors_allowed_origins: str = ""

    # Import automatico da Google Drive (fonte esterna, non persistenza: vedi
    # README.md "Google Drive resta ammesso..."). Vuoto = sync disattivata.
    # JSON completo della chiave dell'account di servizio Google (scope Drive
    # readonly). La cartella va condivisa con la sua email come Visualizzatore.
    google_service_account_json: str = ""
    # ID della cartella Drive contenente gli XML dei corrispettivi RT.
    google_drive_corrispettivi_folder_id: str = ""
    # Intervallo minuti tra un sync automatico e l'altro (0 = solo manuale via API).
    drive_sync_interval_minutes: int = 15

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
