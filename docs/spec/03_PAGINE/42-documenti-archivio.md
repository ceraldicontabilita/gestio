# 42 — Archivio documenti

## Contratto della schermata

- Route: `/documenti/archivio`
- Accesso: `authenticated`
- Modulo: `documenti`
- Componente corrente: `frontend/src/pages/Documenti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/DocumentiHub.jsx`
- Mappa macchina: [`MAPPE_JSON/documenti-archivio.json`](MAPPE_JSON/documenti-archivio.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Archivio documenti indicizzati con metadati, originale, relazioni e viewer.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/documento/{param}/download` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Documenti.jsx
- `GET /api/documenti/indice/catalog` — `tenere` — sorgente: frontend/src/pages/hub/DocumentiHub.jsx
- `GET /api/documenti/lista?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Documenti.jsx
- `/api/documenti/documento/{param}/download` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/documenti/lista` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `byStatus`
- `categories`
- `category`
- `documents`
- `driveCatalog`
- `error`
- `loading`
- `page`
- `search`
- `searchInput`
- `selectedDocument`
- `status`
- `total`
- `visitedTabs`

### Handler e operazioni

- `loadAndSyncDrive`
- `loadData`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../../hooks/useHashState`
- `../api`
- `../components/DocumentViewerModal`
- `../components/PageLayout`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/Documenti.jsx — SHA-256 `c04c3a3a5fe13e8e38f9ba86bb4d77a9d650fe72130a23b47985e76a3cbbe98a` — 506 righe`
- `frontend/src/pages/hub/DocumentiHub.jsx — SHA-256 `298d1dbee393e132a85837d0926387d7082bc4e73a049ac0bac2f10422f3f382` — 160 righe`

## Test collegati

- `frontend/src/components/DriveImportControls.test.jsx`
- `frontend/src/pages/CedoliniSalari.test.jsx`
- `frontend/src/pages/ChiusuraEsercizio.test.jsx`
- `frontend/src/pages/Documenti.test.jsx`
- `frontend/src/pages/ImportDocumenti.test.jsx`
- `frontend/src/pages/PrimaNota.test.jsx`
- `tests/test_documenti_import_fattura_multi_body.py`
- `tests/test_drive_sync_orchestrator.py`
- `tests/test_email_full_download_mittenti_attendibili.py`
- `tests/test_file_tecnici_pec.py`
- `tests/test_import_f24_bridge_canonico.py`
- `tests/test_p1_documenti_classificati.py`
- `tests/test_rielaborazione_documenti.py`

## Usabilità non negoziabile

- Una sola azione primaria per compito; niente plance di manutenzione nell'interfaccia ordinaria.
- Liste per giorno o contesto, filtri persistenti, contatori cliccabili che aprono sempre il dettaglio.
- Modali sopra il contenuto, chiusura visibile, `Esc`, focus intrappolato e ripristinato, layout responsive.
- Pulsanti tecnici solo in area amministrativa; gli ingest ordinari avvengono automaticamente.
- Ogni alert espone l'elenco dei record, il motivo, la fonte e il collegamento alla correzione.

## Criteri di accettazione della pagina

- Route e autorizzazione corrette; nessun fallback a una pagina diversa.
- Dati, conteggi, centesimi, segni, anno e saldi coerenti con i registri canonici.
- Stato visibile in tutte le sezioni interconnesse dopo refresh.
- Seconda importazione identica: `nuovi=0`, nessun duplicato o scrittura aggiuntiva.
- Ambiguità non applicate definitivamente; scelta manuale tracciata.
- Test: caricamento, errore, vuoto, popolato, permessi, mobile/desktop e almeno un flusso end-to-end reale in sola lettura.
