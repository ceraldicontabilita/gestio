from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    # Target: PostgreSQL (istanza gestita su Render). Il default SQLite
    # vale solo per sviluppo locale senza DATABASE_URL configurata.
    database_url: str = "sqlite:///./gestio.db"
    document_storage_path: str = "./storage"
    secret_key: str = "dev-secret-change-me"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
