# 31 — Ritenute

## Contratto della schermata

- Route: `/ritenute`
- Accesso: `authenticated`
- Modulo: `personale`
- Componente corrente: `frontend/src/pages/Ritenute.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/ritenute.json`](MAPPE_JSON/ritenute.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Ritenute per percipiente, periodo, aliquota, F24 e quadratura annuale.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/ritenute?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Ritenute.jsx
- `GET /api/ritenute` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `dati`
- `error`
- `filtroStato`
- `loading`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../contexts/AnnoContext`
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

- `frontend/src/main.jsx — SHA-256 `43867ec02c33b70634aab8e04e98f996c845971cc1ff88239a980f9d9af12089` — 145 righe`
- `frontend/src/pages/Ritenute.jsx — SHA-256 `bc624b4d46b1d171dae10a3a816f3db2f6fb09e89fc448ebdb5307856bf077c1` — 212 righe`

## Test collegati

- `tests/test_tax_code_registry.py`

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
