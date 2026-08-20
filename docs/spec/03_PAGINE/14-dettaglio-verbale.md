# 14 — Dettaglio verbale

## Contratto della schermata

- Route: `/verbali-noleggio/:identificativo`
- Accesso: `authenticated`
- Modulo: `noleggio`
- Componente corrente: `frontend/src/pages/DettaglioVerbale.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/dettaglio-verbale.json`](MAPPE_JSON/dettaglio-verbale.json)
- Stato della prova corrente: `verified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Fascicolo del verbale con PDF, importo, targa, trasgressore, driver e prove.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/dipendenti` — `tenere` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `GET /api/verbali-noleggio/dettaglio/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `GET /api/verbali-noleggio/pdf/{param}?indice={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/associa-pdf/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/correggi-importo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/correggi-trasgressore/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/ricalcola-pdf/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/auto-repair/collega-targa-driver` — `tenere` — in uso: FE, scheduler
- `POST /api/auto-repair/inferisci-targa-driver-da-fatture` — `tenere` — in uso: FE, scheduler
- `POST /api/dipendenti` — `tenere` — in uso: FE
- `/api/verbali-noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/associa-pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/correggi-importo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/correggi-trasgressore/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/dettaglio/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/ricalcola-pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `correctedAmount`
- `drivers`
- `error`
- `linkingDriver`
- `loading`
- `openingPdf`
- `pdfUploading`
- `pdfViewer`
- `recalculating`
- `savingAmount`
- `savingTrasgressore`
- `selectedDriver`
- `trasgressore`
- `verbale`

### Handler e operazioni

- `openPdf`
- `saveCorrectedAmount`
- `saveTrasgressore`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/DocumentViewerModal`
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
- `frontend/src/pages/DettaglioVerbale.jsx — SHA-256 `89e12f9b5ab69485c880045158443f292f1ada74882a9aedbd04ad01c2e47354` — 380 righe`

## Test collegati

- `frontend/src/pages/DettaglioVerbale.test.jsx`

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
