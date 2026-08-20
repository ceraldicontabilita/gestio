# 30 — Scadenze

## Contratto della schermata

- Route: `/scadenze`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/Scadenze.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Mappa macchina: [`MAPPE_JSON/scadenze.json`](MAPPE_JSON/scadenze.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Scadenziario fornitori con residui, parziali, prove e alert navigabili.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/scadenze/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Scadenze.jsx
- `GET /api/email-scanner/statistiche` — `tenere` — sorgente: frontend/src/pages/Scadenze.jsx
- `GET /api/scadenze/dashboard-widget` — `tenere` — sorgente: frontend/src/pages/Scadenze.jsx
- `GET /api/scadenze/tutte?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Scadenze.jsx
- `POST /api/email-scanner/associa` — `tenere` — sorgente: frontend/src/pages/Scadenze.jsx
- `POST /api/fatture-ricevute/paga-manuale` — `tenere` — sorgente: frontend/src/pages/Scadenze.jsx
- `POST /api/scadenze/crea` — `tenere` — sorgente: frontend/src/pages/Scadenze.jsx
- `PUT /api/scadenze/completa/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Scadenze.jsx
- `/api/scadenze/completa/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/scadenze/tutte` — `tenere` — in uso: FE
- `/api/scadenze/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `alertWidget`
- `documentiRiconciliare`
- `filtroTipo`
- `includePassate`
- `loading`
- `nuovaScadenza`
- `pagaModal`
- `paidIds`
- `processing`
- `scadenze`
- `showModal`
- `viewingInvoice`

### Handler e operazioni

- `handleCompleta`
- `handleCreaScadenza`
- `handleElimina`
- `handlePagaScadenza`
- `loadData`

### Destinazioni di navigazione

- `/contabilita/calendario`
- `/documenti/import`
- `/noleggio`

### Componenti/import locali

- `../api`
- `../components/ModalFattura`
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
- `./lib/queryClient.js`
- `./lib/utils.js`
- `./pages/Login.jsx`

## Fonti tecniche verificate

- `frontend/src/main.jsx — SHA-256 `43867ec02c33b70634aab8e04e98f996c845971cc1ff88239a980f9d9af12089` — 145 righe`
- `frontend/src/pages/Scadenze.jsx — SHA-256 `53bd766173706c08d1b5281af00f14d417bbcacd12a9a60444623deedc5a4995` — 972 righe`

## Test collegati

- `frontend/src/pages/iva/IvaAuditSections.test.jsx`
- `tests/test_contabilita_read_only_guards.py`
- `tests/test_frontend_route_consolidation.py`
- `tests/test_import_f24_bridge_canonico.py`
- `tests/test_scadenze_iva_motore_ufficiale.py`

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
