# 65 — Situazione fiscale

## Contratto della schermata

- Route: `/situazione-fiscale`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/SituazioneFiscale.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/situazione-fiscale.json`](MAPPE_JSON/situazione-fiscale.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Situazione fiscale unificata con F24, dichiarazioni, quietanze e anomalie.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/indice/index/document/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `GET /api/fiscal/documents/{param}/content` — `verificare contratto dinamico` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `GET /api/fiscal/review` — `tenere` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `GET /api/fiscal/summary` — `tenere` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `POST /api/documenti-fiscali/upload` — `tenere` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `/api/documenti/indice/index/document/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/documenti/tax-codes` — `tenere` — in uso: FE
- `GET /api/fiscal/ader-snapshots` — `tenere` — in uso: FE
- `GET /api/fiscal/collections` — `tenere` — in uso: FE
- `GET /api/fiscal/crosswalk` — `tenere` — in uso: FE
- `GET /api/fiscal/declarations` — `tenere` — in uso: FE
- `/api/fiscal/documents/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/fiscal/dossier.pdf` — `tenere` — in uso: FE
- `GET /api/fiscal/evidence-package.zip` — `tenere` — in uso: FE
- `GET /api/fiscal/f24-rows` — `tenere` — in uso: FE
- `GET /api/fiscal/obligations` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `aderRelated`
- `declarationType`
- `declarationYear`
- `f24CreditsOnly`
- `f24TaxCode`
- `f24Year`
- `items`
- `loading`
- `review`
- `selected`
- `summary`
- `tabMeta`
- `tabSources`
- `taxCodeContext`
- `taxCodeFilters`
- `taxCodeMeta`
- `taxCodeOptions`
- `taxCodeQuery`
- `taxCodeType`
- `uploadCategory`
- `uploading`

### Handler e operazioni

- `openDocument`
- `openDriveDocument`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/LinkedEvidencePanel`
- `../components/PageLayout`
- `../components/ds`
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
- `frontend/src/pages/SituazioneFiscale.jsx — SHA-256 `ef9a13bfc46548b4fbd540d9e7269b070e8e198220314d3414b4c98c7dffac7e` — 328 righe`

## Test collegati

- `frontend/src/pages/SituazioneFiscale.test.jsx`

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
