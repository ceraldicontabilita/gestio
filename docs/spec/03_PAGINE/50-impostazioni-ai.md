# 50 — Impostazioni AI

## Contratto della schermata

- Route: `/impostazioni-ai`
- Accesso: `admin`
- Modulo: `integrazioni`
- Componente corrente: `frontend/src/pages/ImpostazioniAI.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/impostazioni-ai.json`](MAPPE_JSON/impostazioni-ai.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Configurazione AI tramite riferimenti a segreti, modello, limiti e health.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `POST /api/settings/openai` — `tenere` — sorgente: frontend/src/pages/ImpostazioniAI.jsx
- `POST /api/settings/openai/test` — `tenere` — sorgente: frontend/src/pages/ImpostazioniAI.jsx
- `GET /api/settings/openai` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `apiKey`
- `cfg`
- `modello`
- `msg`
- `saving`
- `showKey`
- `testing`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/PageLayout`
- `../components/ds`
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
- `frontend/src/pages/ImpostazioniAI.jsx — SHA-256 `a75aad4aeac36573e54f5f7a1dc48acc4041201b2e4d233cb4d636f2cedbe3a2` — 194 righe`

## Test collegati

Nessun test nominale rilevato: nella riscrittura aggiungere test unitario, integrazione e browser E2E.

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
