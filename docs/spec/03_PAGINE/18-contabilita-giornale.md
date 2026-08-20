# 18 — Libro Giornale

## Contratto della schermata

- Route: `/contabilita/giornale`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/LibroGiornale.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Mappa macchina: [`MAPPE_JSON/contabilita-giornale.json`](MAPPE_JSON/contabilita-giornale.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Libro giornale progressivo, bilanciato, filtrabile, esportabile e auditabile.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/contabilita-gestionale/libro-giornale/export?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LibroGiornale.jsx
- `GET /api/contabilita-gestionale/libro-giornale?{param}&limit=2000` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LibroGiornale.jsx
- `GET /api/contabilita-gestionale/libro-mastro?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LibroGiornale.jsx
- `GET /api/contabilita-gestionale/libro-giornale` — `tenere` — in uso: FE
- `GET /api/contabilita-gestionale/libro-giornale/controllo-60-giorni` — `tenere` — in uso: FE
- `GET /api/contabilita-gestionale/libro-giornale/export` — `tenere` — in uso: FE
- `GET /api/contabilita-gestionale/libro-mastro` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `controllo60`
- `error`
- `espansa`
- `giornale`
- `loading`
- `mastro`
- `registerError`
- `visitedTabs`
- `vista`

### Handler e operazioni

- `handleTabChange`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../contexts/AnnoContext`
- `../lib/utils.js`

## Fonti tecniche verificate

- `frontend/src/pages/LibroGiornale.jsx — SHA-256 `c53f97245011792c245e2e41cc27be1ed121f9423504365a4b72d7ad3e26daf0` — 396 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/LibroGiornale.test.jsx`

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
