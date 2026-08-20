# 48 — Agenti AI

## Contratto della schermata

- Route: `/agenti`
- Accesso: `authenticated`
- Modulo: `strumenti`
- Componente corrente: `frontend/src/pages/Agenti.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/agenti.json`](MAPPE_JSON/agenti.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Agenti e automazioni con scopo, permessi, run, log, esito e disattivazione.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/agenti/automazioni/stato` — `tenere` — sorgente: frontend/src/pages/Agenti.jsx
- `GET /api/agenti/cash-flow-13-settimane` — `tenere` — sorgente: frontend/src/pages/Agenti.jsx
- `GET /api/agenti/decisioni?limit=100` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Agenti.jsx
- `GET /api/agenti/pattern-appresi` — `tenere` — sorgente: frontend/src/pages/Agenti.jsx
- `GET /api/agenti/segnalazioni?limit=100` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Agenti.jsx
- `GET /api/agenti/stato` — `tenere` — sorgente: frontend/src/pages/Agenti.jsx
- `POST /api/agenti/automazioni/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Agenti.jsx
- `POST /api/agenti/decisioni/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Agenti.jsx
- `POST /api/agenti/run{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Agenti.jsx
- `PUT /api/agenti/segnalazioni/{param}/risolta` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Agenti.jsx
- `/api/agenti/automazioni/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/agenti/decisioni` — `tenere` — in uso: FE
- `/api/agenti/decisioni/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/agenti/run{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/agenti/segnalazioni` — `tenere` — in uso: FE
- `/api/agenti/segnalazioni/{param}/risolta` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `automazioni`
- `cashFlow`
- `decisioni`
- `loading`
- `msg`
- `pattern`
- `running`
- `segnalazioni`
- `state`
- `stati`

### Handler e operazioni

- `loadAll`
- `loadPattern`
- `onHashChange`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/CopyLinkButton`
- `../components/PageLayout`
- `../components/ui/ConfirmDialog`
- `../contexts/AuthContext`
- `../hooks/useHashState`
- `../lib/utils`
- `./App.jsx`
- `./components/ErrorBoundary.jsx`
- `./components/ui/ConfirmDialog.jsx`
- `./components/ui/sonner.jsx`
- `./contexts/AnnoContext.jsx`
- `./contexts/AuthContext.jsx`
- `./lib/queryClient.js`
- `./lib/utils.js`
- `./pages/Login.jsx`

## Fonti tecniche verificate

- `frontend/src/hooks/useHashState.js — SHA-256 `bf4792c0a4f9a13a7ede59cb26623094b22766af27b77a302d685b9444900ffd` — 110 righe`
- `frontend/src/main.jsx — SHA-256 `43867ec02c33b70634aab8e04e98f996c845971cc1ff88239a980f9d9af12089` — 145 righe`
- `frontend/src/pages/Agenti.jsx — SHA-256 `34286b66f7c37c89936b8ee92a55bcbe9690e396edcdc87e3d88db728d2a5735` — 768 righe`

## Test collegati

- `frontend/src/pages/Agenti.test.jsx`

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
