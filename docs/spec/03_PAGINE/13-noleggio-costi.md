# 13 — Costi noleggio

## Contratto della schermata

- Route: `/noleggio/costi`
- Accesso: `authenticated`
- Modulo: `noleggio`
- Componente corrente: `frontend/src/pages/hub/VeicoliHub.jsx`
- Entrypoint/router: `frontend/src/pages/hub/VeicoliHub.jsx`
- Mappa macchina: [`MAPPE_JSON/noleggio-costi.json`](MAPPE_JSON/noleggio-costi.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Costi noleggio per veicolo: canoni, pedaggi, verbali, bollo e riparazioni.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/noleggio/export-pdf-costi` — `tenere` — in uso: FE
- `GET /api/noleggio/veicoli` — `tenere` — in uso: FE
- `POST /api/noleggio/veicoli` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `loadedTabs`

### Handler e operazioni

- `handleTabChange`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/hub/VeicoliHub.jsx — SHA-256 `95227192a674b44ceaf89aa5577292c55e8762af00a9cf7a500ff96a707c2ba7` — 373 righe`

## Test collegati

- `frontend/src/pages/hub/VeicoliHub.test.jsx`

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
