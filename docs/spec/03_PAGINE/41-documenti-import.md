# 41 — Import documenti

## Contratto della schermata

- Route: `/documenti/import`
- Accesso: `authenticated`
- Modulo: `documenti`
- Componente corrente: `frontend/src/pages/ImportDocumenti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/DocumentiHub.jsx`
- Mappa macchina: [`MAPPE_JSON/documenti-import.json`](MAPPE_JSON/documenti-import.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Import documenti/ZIP con validazione, salvataggio reale, hash e report.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/indice/catalog` — `tenere` — sorgente: frontend/src/pages/hub/DocumentiHub.jsx
- `POST /api/documenti/upload-auto` — `tenere` — sorgente: frontend/src/pages/ImportDocumenti.jsx
- `POST /api/documenti/upload-auto/preview` — `tenere` — sorgente: frontend/src/pages/ImportDocumenti.jsx
- `POST /api/documenti-inbox/auto-classify` — `tenere` — in uso: FE
- `POST /api/documenti-inbox/import-dipendenti-from-cu` — `tenere` — in uso: FE
- `POST /api/documenti-inbox/import-f24-from-inbox` — `tenere` — in uso: FE
- `GET /api/fatture-estere/da-verificare` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `dragOver`
- `driveCatalog`
- `files`
- `previewComplete`
- `results`
- `uploadProgress`
- `uploading`
- `visitedTabs`

### Handler e operazioni

- `handleDragLeave`
- `handleDragOver`
- `handleDrop`
- `handleFileSelect`
- `handlePreview`
- `handleReset`
- `handleUpload`
- `handleZipSelect`
- `loadAndSyncDrive`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../../hooks/useHashState`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/ImportDocumenti.jsx — SHA-256 `0ccb0cad845be08ed6698e1bc5c192489e36a739ed499d3e7202bcbb796e1617` — 923 righe`
- `frontend/src/pages/hub/DocumentiHub.jsx — SHA-256 `298d1dbee393e132a85837d0926387d7082bc4e73a049ac0bac2f10422f3f382` — 160 righe`

## Test collegati

- `frontend/src/pages/ImportDocumenti.test.jsx`

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
