# 60 — Gestione IVA

## Contratto della schermata

- Route: `/iva`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/GestioneIVA.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/iva.json`](MAPPE_JSON/iva.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

IVA, liquidazioni, fatture, corrispettivi, F24, periodi e quadrature.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/corrispettivi?data_da={param}&data_a={param}&limit=5000` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/iva/anomalie?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/iva/dashboard/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/iva/liquidazioni/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/iva/riepilogo-annuale/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/scadenze/iva-mensile/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/verifica-coerenza/confronto-iva-completo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `POST /api/iva/liquidazioni/calcola?periodo={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `POST /api/iva/liquidazioni/{param}/conferma` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `POST /api/iva/liquidazioni/{param}/riapri?motivo=Riapertura+manuale+confermata` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `POST /api/iva/ricalcola-attribuzione{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneIVA.jsx
- `GET /api/corrispettivi` — `tenere` — in uso: FE
- `GET /api/iva/anomalie` — `tenere` — in uso: FE
- `/api/iva/dashboard/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/iva/fatture` — `tenere` — in uso: FE, scheduler
- `POST /api/iva/liquidazioni/calcola` — `tenere` — in uso: FE
- `/api/iva/liquidazioni/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/iva/liquidazioni/{param}/conferma` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/iva/liquidazioni/{param}/riapri` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/iva/ricalcola-attribuzione{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/iva/riepilogo-annuale/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/scadenze/iva-mensile/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verifica-coerenza/confronto-iva-completo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `anomalie`
- `busyLiq`
- `confrontoCommercialista`
- `controlliError`
- `controlliLoading`
- `corrispettivi`
- `dashboard`
- `dati`
- `liquidazione`
- `loading`
- `mese`
- `msg`
- `ricalcolo`
- `riepilogo`
- `scadenzeMensili`
- `vistaAnnuale`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../lib/utils`
- `./App.jsx`
- `./components/ErrorBoundary.jsx`
- `./components/ui/ConfirmDialog.jsx`
- `./components/ui/sonner.jsx`
- `./contexts/AnnoContext.jsx`
- `./contexts/AuthContext.jsx`
- `./iva/IvaAuditSections`
- `./lib/queryClient.js`
- `./lib/utils.js`
- `./pages/Login.jsx`

## Fonti tecniche verificate

- `frontend/src/main.jsx — SHA-256 `43867ec02c33b70634aab8e04e98f996c845971cc1ff88239a980f9d9af12089` — 145 righe`
- `frontend/src/pages/GestioneIVA.jsx — SHA-256 `bede87b4601cfbdbf04c6f9747a27e50832076cebe0989baf9b454953ce7bfb7` — 818 righe`

## Test collegati

- `frontend/src/pages/GestioneIVA.periods.test.jsx`
- `tests/test_frontend_route_consolidation.py`

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
