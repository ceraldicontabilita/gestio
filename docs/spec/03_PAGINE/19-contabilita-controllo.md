# 19 — Controllo mensile

## Contratto della schermata

- Route: `/contabilita/controllo`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/ControlloMensile.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Mappa macchina: [`MAPPE_JSON/contabilita-controllo.json`](MAPPE_JSON/contabilita-controllo.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Controllo mensile con lista per ogni anomalia e stato di risoluzione.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/contabilita-gestionale/bilancio-verifica?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ControlloMensile.jsx
- `GET /api/corrispettivi?data_da={param}&data_a={param}&limit=10000` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ControlloMensile.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ControlloMensile.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi?data_da={param}&data_a={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ControlloMensile.jsx
- `GET /api/prima-nota/cassa?{param}&limit=10000` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ControlloMensile.jsx
- `GET /api/contabilita-gestionale/bilancio-verifica` — `tenere` — in uso: FE
- `GET /api/corrispettivi` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/controllo-due-fasi` — `tenere` — in uso: FE
- `GET /api/prima-nota/cassa` — `tenere` — in uso: FE
- `POST /api/prima-nota/cassa` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `completezzaRegistro`
- `dailyComparison`
- `error`
- `fontiErrore`
- `loading`
- `meseSelezionato`
- `monthlyData`
- `showVersamentiModal`
- `versamentiDettaglio`
- `viewMode`
- `visitedTabs`
- `yearTotals`

### Handler e operazioni

- `handleBackToYear`
- `handleMonthClick`
- `handleTabChange`
- `loadMonthData`
- `loadYearData`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/ControlloMensile.jsx — SHA-256 `e0c5c733ffc8673c487692dc724b6f329a96cba1a905ff55ccab0cd5717db027` — 1424 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/ControlloMensile.test.jsx`

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
