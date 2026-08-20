from fastapi import FastAPI

from app.database import Base, engine
from app.routers import prima_nota

app = FastAPI(title="Gestio")

# MVP: crea le tabelle direttamente dai modelli all'avvio. Da sostituire con
# migrazioni Alembic prima della produzione (vedi docs/spec/07_TEST_E_ACCETTAZIONE/
# per i gate su migrazioni idempotenti).
Base.metadata.create_all(bind=engine)

app.include_router(prima_nota.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}
