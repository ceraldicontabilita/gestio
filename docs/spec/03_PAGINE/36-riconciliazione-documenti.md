# 36 — Riconciliazione documenti

## Contratto della schermata

- Route: `/riconciliazione/documenti`
- Accesso: `authenticated`
- Modulo: `riconciliazione`
- Componente corrente: `frontend/src/pages/RiconciliazioneUnificata.jsx`
- Entrypoint/router: `frontend/src/pages/hub/RiconciliazioneHub.jsx`
- Mappa macchina: [`MAPPE_JSON/riconciliazione-documenti.json`](MAPPE_JSON/riconciliazione-documenti.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Riconciliazione documenti con originale, classificazione, candidati e provenienza.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/documenti-non-associati/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/documenti-non-associati/associati-di-recente?limit=20` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/documenti-non-associati/collezioni-disponibili` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/f24-analisi/tabella{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/operazioni-da-confermare/smart/analizza-anomalie?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/operazioni-da-confermare/smart/analizza?limit={param}&anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/operazioni-da-confermare/smart/cerca-f24?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `GET /api/paypal-api/status` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `POST /api/assegni/{param}/incassa` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/documenti-non-associati/associa` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/documenti-non-associati/de-associa` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/operazioni-da-confermare/smart/conferma-f24` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/operazioni-da-confermare/smart/ignora` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/operazioni-da-confermare/smart/riconcilia-manuale` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/operazioni-da-confermare/smart/riconcilia-stipendio` — `tenere` — sorgente: frontend/src/pages/RiconciliazioneUnificata.jsx
- `POST /api/paypal-api/sync` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `/api/assegni/{param}/incassa` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/documenti-non-associati/associati-di-recente` — `tenere` — in uso: FE
- `GET /api/documenti-non-associati/lista` — `tenere` — in uso: FE
- `/api/documenti-non-associati/pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/documenti-non-associati/statistiche` — `tenere` — in uso: FE
- `/api/documenti-non-associati/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/download/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-analisi/tabella{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/operazioni-da-confermare/smart/analizza` — `tenere` — in uso: FE
- `GET /api/operazioni-da-confermare/smart/analizza-anomalie` — `tenere` — in uso: FE
- `GET /api/operazioni-da-confermare/smart/banca-veloce` — `tenere` — in uso: FE
- `GET /api/operazioni-da-confermare/smart/cerca-f24` — `tenere` — in uso: FE
- `GET /api/operazioni-da-confermare/smart/cerca-stipendi` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `annullando`
- `anomalyReport`
- `assegni`
- `associazioneForm`
- `collezioni`
- `currentLimit`
- `documentiNonAssociati`
- `documentiStats`
- `errore`
- `f24Loading`
- `f24Pendenti`
- `filters`
- `hasMore`
- `loadError`
- `loading`
- `loadingCollezioni`
- `loadingMore`
- `message`
- `mostraRecenti`
- `movimentiBanca`
- `paypalRefreshKey`
- `pdfViewer`
- `processing`
- `recenti`
- `reconciliationStats`
- `ricercaTributo`
- `righe`
- `salvandoBatch`
- `selectedDoc`
- `selezionati`
- `showFilters`
- `soloAnno`
- `stats`
- `stipendiPendenti`

### Handler e operazioni

- `handleAnalizzaAnomalie`
- `handleAssocia`
- `handleConferma`
- `handleDelete`
- `handleIgnora`
- `handleIncassaAssegno`
- `handleTabChange`
- `handleVediProva`
- `handleViewPdf`
- `loadAllData`
- `loadCollezioni`
- `loadF24OnDemand`
- `loadMore`

### Destinazioni di navigazione

- `/riconciliazione`
- `/riconciliazione/${tabId}`
- `/riconciliazione/banca`
- `/riconciliazione/movimenti-banca`

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/DocumentViewerModal`
- `../components/ExportButton`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/RiconciliazioneUnificata.jsx — SHA-256 `8d56e69724bee22b76b74e7077adbae916e3642ab4310571ccb235a4330a34a4` — 2826 righe`
- `frontend/src/pages/hub/RiconciliazioneHub.jsx — SHA-256 `f8e30156c58abc97b26bf319e79a6ebc2d5023c40b7650e415206602d5ae2ba4` — 129 righe`

## Test collegati

- `frontend/src/pages/RiconciliazioneUnificata.rentalScope.test.jsx`
- `frontend/src/pages/RiconciliazioneUnificata.safety.test.jsx`

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
