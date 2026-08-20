from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import Base, engine
from app.routers import corrispettivi, prima_nota

settings = get_settings()

app = FastAPI(title="Gestio")

# MVP: crea le tabelle direttamente dai modelli all'avvio. Da sostituire con
# migrazioni Alembic prima della produzione (vedi docs/spec/07_TEST_E_ACCETTAZIONE/
# per i gate su migrazioni idempotenti).
Base.metadata.create_all(bind=engine)

if settings.cors_allowed_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[o.strip() for o in settings.cors_allowed_origins.split(",") if o.strip()],
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(prima_nota.router)
app.include_router(corrispettivi.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}
