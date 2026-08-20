# 15 — Piano dei Conti

## Contratto della schermata

- Route: `/contabilita`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/PianoDeiConti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Mappa macchina: [`MAPPE_JSON/contabilita-piano-conti.json`](MAPPE_JSON/contabilita-piano-conti.json)
- Stato della prova corrente: `verified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Piano dei conti gerarchico, regole versionate e movimenti collegati.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/piano-conti/?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `GET /api/piano-conti/conto/{param}/movimenti?limit=40&anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `GET /api/piano-conti/regole` — `tenere` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `POST /api/dizionario-articoli/riclassifica-completo?limite_ai=500` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `POST /api/piano-conti/` — `tenere` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `POST /api/piano-conti/regole` — `tenere` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `PUT /api/dizionario-articoli/articolo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `/api/dizionario-articoli/articolo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/dizionario-articoli/riclassifica-completo` — `tenere` — in uso: FE
- `/api/piano-conti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/piano-conti/conto/{param}/movimenti` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `_conti`
- `activeTab`
- `bilancio`
- `contoDetail`
- `error`
- `expandedCategories`
- `grouped`
- `loading`
- `loadingDetail`
- `newConto`
- `newRegola`
- `regole`
- `riclassificaResult`
- `riclassificando`
- `selectedConto`
- `showNewConto`
- `showNewRegola`
- `spostandoRiga`
- `visitedTabs`

### Handler e operazioni

- `closeDrawer`
- `handleCreateConto`
- `handleCreateRegola`
- `handleRiclassificaAI`
- `handleSpostaRigaConto`
- `handleTabChange`
- `loadData`
- `openContoDetail`

### Destinazioni di navigazione

- `/contabilita/piano-conti/${tabId}`

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/PianoDeiConti.jsx — SHA-256 `78b1406af2e4044396f03338b290c5979aba9e084b52b74b3e14a25455687ac9` — 1129 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/PianoDeiConti.test.jsx`
- `tests/test_piano_conti_performance_guard.py`

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
