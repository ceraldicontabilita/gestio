# 64 — Atti amministrativi

## Contratto della schermata

- Route: `/documenti/atti`
- Accesso: `authenticated`
- Modulo: `documenti`
- Componente corrente: `frontend/src/pages/AttiAmministrativi.jsx`
- Entrypoint/router: `frontend/src/pages/hub/DocumentiHub.jsx`
- Mappa macchina: [`MAPPE_JSON/documenti-atti.json`](MAPPE_JSON/documenti-atti.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Atti amministrativi con ente, protocollo, originale, scadenze e notifiche.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/amministrativi` — `tenere` — sorgente: frontend/src/pages/AttiAmministrativi.jsx
- `GET /api/documenti/documento/{param}/download` — `verificare contratto dinamico` — sorgente: frontend/src/pages/AttiAmministrativi.jsx
- `GET /api/documenti/indice/catalog` — `tenere` — sorgente: frontend/src/pages/hub/DocumentiHub.jsx
- `/api/documenti/documento/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `area`
- `driveCatalog`
- `loading`
- `payload`
- `search`
- `selectedYear`
- `visitedTabs`

### Handler e operazioni

- `loadAndSyncDrive`
- `openDocument`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../../hooks/useHashState`
- `../api`
- `../components/ds`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/AttiAmministrativi.jsx — SHA-256 `56eec79d1dba80695bd7d4d1f1584eb4f62d966dfb2bcdf18abe96e0f3e5c100` — 146 righe`
- `frontend/src/pages/hub/DocumentiHub.jsx — SHA-256 `298d1dbee393e132a85837d0926387d7082bc4e73a049ac0bac2f10422f3f382` — 160 righe`

## Test collegati

- `frontend/src/pages/AttiAmministrativi.test.jsx`

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
