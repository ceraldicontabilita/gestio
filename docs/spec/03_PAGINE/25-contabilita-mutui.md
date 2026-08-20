# 25 — Mutui

## Contratto della schermata

- Route: `/contabilita/mutui`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/Mutui.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Mappa macchina: [`MAPPE_JSON/contabilita-mutui.json`](MAPPE_JSON/contabilita-mutui.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Mutui, rate, quota capitale/interessi, banca e residuo riconciliato.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/mutui/` — `tenere` — sorgente: frontend/src/pages/Mutui.jsx
- `GET /api/mutui/statistiche/dashboard` — `tenere` — sorgente: frontend/src/pages/Mutui.jsx
- `POST /api/mutui/riconcilia` — `tenere` — sorgente: frontend/src/pages/Mutui.jsx
- `GET /api/mutui` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `error`
- `expandedMutuo`
- `lastRiconciliazione`
- `loading`
- `mutui`
- `riconciliaLoading`
- `stats`
- `visitedTabs`

### Handler e operazioni

- `handleTabChange`
- `loadData`

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

- `frontend/src/pages/Mutui.jsx — SHA-256 `1b428ba967b8b0ac6a307a0135c5f6abafbb1748b7273126a114b1bae903b9bf` — 572 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `tests/test_mappa_categoria_estratto_conto.py`
- `tests/test_mutui_document_import.py`

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
