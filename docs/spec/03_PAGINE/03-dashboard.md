# 03 — Dashboard

## Contratto della schermata

- Route: `/`
- Accesso: `authenticated`
- Modulo: `dashboard`
- Componente corrente: `frontend/src/pages/Dashboard.jsx`
- Entrypoint/router: `frontend/src/pages/hub/DashboardHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/03-dashboard.json`](LOGICA_JSON/03-dashboard.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Dashboard derivata dai registri, con indicatori cliccabili e nessun saldo hardcoded.

## Fonti e registri letti

- viste aggregate dei registri canonici
- stato importazioni e riconciliazioni
- anno globale

## Scritture ed effetti consentiti

- Nessuna scrittura contabile; solo preferenze di visualizzazione non sensibili.

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Caricare anno e permessi, poi KPI calcolati dai registri e non da valori salvati nella pagina.
2. Ogni KPI deve dichiarare formula, periodo, ultimo aggiornamento e stato della fonte.
3. Il clic su una card apre la lista esatta che compone il numero, con gli stessi filtri.

## Automazioni previste

- Aggiornamento periodico read-only e invalidazione quando termina un'importazione.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- KPI verso Fatture, Prima Nota, Riconciliazioni, Scadenze e anomalie filtrate.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Errore o fonte indisponibile non diventano zero; totali di documenti, pagamenti e saldi restano semanticamente distinti.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Somma delle righe di drill-down uguale alla card al centesimo; cambio anno aggiorna card e destinazione.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/bank/statements?skip={param}&limit={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/cash?skip={param}&limit={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/dashboard/fascia-energia` — `tenere` — sorgente: frontend/src/pages/Dashboard.jsx
- `GET /api/dashboard/summary{param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/exports/{param}?format={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/f24?skip={param}&limit={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/health` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/invoices?skip={param}&limit={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/suppliers?skip={param}&limit={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `GET /api/verifica-coerenza/iva/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Dashboard.jsx
- `GET /api/warehouse/products?skip={param}&limit={param}` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `POST /api/cash` — `tenere` — sorgente: frontend/src/api.js
- `POST /api/invoices` — `verificare contratto dinamico` — sorgente: frontend/src/api.js
- `POST /api/suppliers` — `tenere` — sorgente: frontend/src/api.js
- `POST /api/warehouse/products` — `tenere` — sorgente: frontend/src/api.js
- `GET /api/bank/statements` — `tenere` — in uso: FE
- `POST /api/bank/statements` — `tenere` — in uso: FE
- `GET /api/cash` — `tenere` — in uso: FE
- `GET /api/controllo-gestione/costi-ricavi` — `tenere` — in uso: FE
- `/api/dashboard/summary{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/dashboard/trend-mensile` — `tenere` — in uso: FE, chat
- `/api/exports/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/f24` — `tenere` — in uso: FE
- `POST /api/f24` — `tenere` — in uso: FE
- `/api/health` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/invoices` — `tenere` — in uso: FE
- `GET /api/prima-nota/stats` — `tenere` — in uso: FE
- `GET /api/scadenze` — `tenere` — in uso: FE
- `GET /api/suppliers` — `tenere` — in uso: FE
- `/api/verifica-coerenza/confronto-iva-completo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verifica-coerenza/iva/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/warehouse/products` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `costiRicavi`
- `domanda`
- `energia`
- `erroreEnergia`
- `erroriApi`
- `iva`
- `loading`
- `mese`
- `primaNota`
- `scadenze`
- `trend`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../api`
- `../components/PageLayout`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/api.js — SHA-256 `de0debaa931793f20ecde82e564d07fefdf4f9e0e88eb6334049b71cb637b2fd` — 168 righe`
- `frontend/src/pages/Dashboard.jsx — SHA-256 `157b3059ba39d2508b7d767b3ea497193112c5db4ae4fb49ee1460ca8d0fdecc` — 801 righe`
- `frontend/src/pages/hub/DashboardHub.jsx — SHA-256 `b6b4d404c0c0d727f21267bc405678c0f81cae05616364d447fedd36e7615f69` — 13 righe`

## Test collegati

- `frontend/src/pages/Dashboard.test.jsx`
- `tests/test_sicurezza_auth.py`

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
