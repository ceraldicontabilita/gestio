# 44 — Movimenti banca

## Contratto della schermata

- Route: `/riconciliazione/movimenti-banca`
- Accesso: `authenticated`
- Modulo: `riconciliazione`
- Componente corrente: `frontend/src/pages/VerificaMovimentiBanca.jsx`
- Entrypoint/router: `frontend/src/pages/hub/RiconciliazioneHub.jsx`
- Mappa macchina: [`MAPPE_JSON/strumenti-movimenti-banca.json`](MAPPE_JSON/strumenti-movimenti-banca.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Movimenti banca con riga fonte, classificazione e stato di associazione.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/paypal-api/status` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `GET /api/prima-nota/indice-operazioni/{param}/candidati?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerificaMovimentiBanca.jsx
- `GET /api/prima-nota/indice-operazioni?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerificaMovimentiBanca.jsx
- `POST /api/paypal-api/sync` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `PUT /api/prima-nota/indice-operazioni/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerificaMovimentiBanca.jsx
- `/api/admin` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/agenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/ai-parser` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/alerts` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/anagrafica-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/assegni` — `tenere` — in uso: FE
- `POST /api/assegni` — `tenere` — in uso: FE
- `/api/assegni/learning` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/auth` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/auth/api/auth/verify` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/auth/login` — `tenere` — in uso: FE
- `GET /api/auth/verify` — `tenere` — in uso: FE
- `/api/auto-repair` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/bank-statement` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/batch-reprocess` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/bilancio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/cash` — `tenere` — in uso: FE
- `POST /api/cash` — `tenere` — in uso: FE
- `/api/cedolini` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/centri-costo` — `tenere` — in uso: FE
- `POST /api/centri-costo` — `tenere` — in uso: FE
- `/api/cespiti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/chiusura-esercizio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/collaudo` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/commercialista` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/config` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/config-import` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita-gestionale` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/controllo-gestione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/corrispettivi` — `tenere` — in uso: FE
- `/api/dashboard` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/dati-isa` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/dipendenti` — `tenere` — in uso: FE
- `POST /api/dipendenti` — `tenere` — in uso: FE
- `/api/dizionario-articoli` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/document-ai` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-fiscali` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-inbox` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-non-associati` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/email-download` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/email-scanner` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/erp/ponte` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/estratto-conto-movimenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/f24` — `tenere` — in uso: FE
- `POST /api/f24` — `tenere` — in uso: FE
- `/api/f24-analisi` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-email` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-email-settings` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-public` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-riconciliazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/f24/quietanze` — `tenere` — in uso: FE
- `/api/fatture` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-estere` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-ricevute` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/finanziamenti-soci` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/finanziaria` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fiscal` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fiscalita` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fornitori-learning` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/gestione-riservata` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/invoices` — `tenere` — in uso: FE
- `GET /api/invoices/emesse` — `tenere` — in uso: FE
- `POST /api/invoices/emesse` — `tenere` — in uso: FE
- `/api/iva` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/learning-machine` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/learning-universal` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/mutui` — `tenere` — in uso: FE
- `/api/nexi` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi-automotive` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi-imprese` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/operazioni-da-confermare` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/pagamenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/pagamenti-buoni` — `verificare` — nessun riferimento noto (FE/scheduler/chat/test): verificare prima di deprecare
- `/api/pagopa` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/paypal-api` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/paypal-statements` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/pianificazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/piano-conti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/previsioni-acquisti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/prima-nota` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/prima-nota-salari` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/prima-nota/indice-operazioni` — `tenere` — in uso: FE
- `/api/prima-nota/indice-operazioni/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/rapido` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/regole` — `tenere` — in uso: FE
- `GET /api/ritenute` — `tenere` — in uso: FE
- `/api/scadenzario-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/scadenze` — `tenere` — in uso: FE
- `GET /api/settings` — `tenere` — in uso: FE
- `PUT /api/settings` — `tenere` — in uso: FE
- `/api/sumup` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/suppliers` — `tenere` — in uso: FE
- `POST /api/suppliers` — `tenere` — in uso: FE
- `/api/tfr` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-riconciliazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verifica-coerenza` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/voci-bilancio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/whatsapp` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `candidates`
- `category`
- `data`
- `error`
- `loading`
- `loadingCandidates`
- `loadingMore`
- `note`
- `paypalRefreshKey`
- `rows`
- `saving`
- `search`
- `selectedRow`
- `statusFilter`
- `targetId`
- `typeFilter`
- `visitedTabs`

### Handler e operazioni

- `handleTabChange`
- `loadCandidates`

### Destinazioni di navigazione

- `/riconciliazione/movimenti-banca`

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/VerificaMovimentiBanca.jsx — SHA-256 `212571b6047d4ced96a99485481d9d4c5a5b0f3a50b3eb32f4c767ace2ee74af` — 303 righe`
- `frontend/src/pages/hub/RiconciliazioneHub.jsx — SHA-256 `f8e30156c58abc97b26bf319e79a6ebc2d5023c40b7650e415206602d5ae2ba4` — 129 righe`
- `frontend/src/pages/hub/StrumentiHub.jsx — SHA-256 `340781812fde424858372c31f0d2f9586035d345be4eeb4756209e88ffcff7f4` — 134 righe`

## Test collegati

- `frontend/src/pages/VerificaMovimentiBanca.test.jsx`
- `tests/test_contabilita_read_only_guards.py`

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
