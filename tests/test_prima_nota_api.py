from fastapi.testclient import TestClient

from app.database import get_db
from app.main import app


def test_versamento_endpoint_crea_coppia_collegata(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    try:
        client = TestClient(app)

        response = client.post(
            "/api/prima-nota/versamento",
            json={"importo": "200.00", "data": "2026-02-01", "descrizione": "Versamento cassa"},
        )
        assert response.status_code == 200
        body = response.json()
        assert len(body) == 2
        assert body[0]["conto"] == "cassa"
        assert body[1]["conto"] == "banca"
        assert body[0]["operation_id"] == body[1]["operation_id"]

        elenco_cassa = client.get("/api/prima-nota/cassa")
        assert elenco_cassa.status_code == 200
        giorni = elenco_cassa.json()
        assert len(giorni) == 1
        assert giorni[0]["saldo_progressivo"] == "-200.00"
    finally:
        app.dependency_overrides.clear()


def test_movimento_manuale_e_conto_non_valido(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    try:
        client = TestClient(app)

        response = client.post(
            "/api/prima-nota/cassa",
            json={"tipo": "entrata", "importo": "50.00", "data": "2026-02-02", "descrizione": "Incasso"},
        )
        assert response.status_code == 200
        assert response.json()["conto"] == "cassa"

        response_invalido = client.get("/api/prima-nota/non-esiste")
        assert response_invalido.status_code == 422
    finally:
        app.dependency_overrides.clear()


def test_health():
    client = TestClient(app)
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
