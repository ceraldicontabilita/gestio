# 40 — Coerenza POS

## Contratto della schermata

- Route: `/riconciliazione/coerenza-pos`
- Accesso: `authenticated`
- Modulo: `riconciliazione`
- Componente corrente: `frontend/src/pages/CoerenzaPOSCorrispettivi.jsx`
- Entrypoint/router: `frontend/src/pages/hub/RiconciliazioneHub.jsx`
- Mappa macchina: [`MAPPE_JSON/coerenza-pos.json`](MAPPE_JSON/coerenza-pos.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Coerenza fra corrispettivi, POS, commissioni, giorni di vendita e accrediti.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/paypal-api/status` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/riepilogo-mensile?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/verifica-coerenza?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/sumup/riepilogo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/corrispettivi/manuale` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/paypal-api/sync` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `POST /api/pos-corrispettivi/chiusure-giornaliere/batch` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `PUT /api/pos-corrispettivi/chiusura-giornaliera` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/riepilogo-mensile` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/verifica-coerenza` — `tenere` — in uso: FE
- `GET /api/sumup/riepilogo` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `dataForm`
- `dati`
- `dettaglioBancaAperto`
- `dueFasi`
- `err`
- `errore`
- `espansa`
- `filtroStato`
- `importAperto`
- `importoSalvato`
- `loading`
- `modalAperta`
- `note`
- `paypalRefreshKey`
- `posReale`
- `riepilogoMensile`
- `salvando`
- `sumup`
- `tab`
- `testo`
- `totale`
- `valore`
- `vista`

### Handler e operazioni

- `loadDati`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/ds`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/CoerenzaPOSCorrispettivi.jsx — SHA-256 `cdc0d4614328f05f04c0ae206fced2f9c672a51b9bca84efd56bd240b81b5aa6` — 1545 righe`
- `frontend/src/pages/hub/RiconciliazioneHub.jsx — SHA-256 `f8e30156c58abc97b26bf319e79a6ebc2d5023c40b7650e415206602d5ae2ba4` — 129 righe`

## Test collegati

- `frontend/src/pages/CoerenzaPOSCorrispettivi.test.jsx`

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
