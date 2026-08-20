# 20 — Calendario fiscale

## Contratto della schermata

- Route: `/contabilita/calendario`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/CalendarioFiscale.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Mappa macchina: [`MAPPE_JSON/contabilita-calendario.json`](MAPPE_JSON/contabilita-calendario.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Calendario fiscale con fonte, scadenza, stato, promemoria e documento collegato.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/fiscalita/calendario/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CalendarioFiscale.jsx
- `GET /api/fiscalita/notifiche-scadenze?anno={param}&giorni=30` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CalendarioFiscale.jsx
- `POST /api/fiscalita/calendario/completa/{param}?anno={param}&note={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CalendarioFiscale.jsx
- `POST /api/fiscalita/calendario/riapri/{param}?anno={param}&motivo={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CalendarioFiscale.jsx
- `POST /api/fiscalita/notifiche-scadenze/invia?scadenza_id={param}&tipo_notifica={param}&anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CalendarioFiscale.jsx
- `/api/fiscalita/calendario/completa/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fiscalita/calendario/riapri/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fiscalita/calendario/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/fiscalita/notifiche-scadenze` — `tenere` — in uso: FE
- `POST /api/fiscalita/notifiche-scadenze/invia` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `calendario`
- `completando`
- `error`
- `filtroMese`
- `filtroStato`
- `inviandoNotifica`
- `loading`
- `notifiche`
- `notificheError`
- `visitedTabs`

### Handler e operazioni

- `handleTabChange`
- `loadCalendario`

### Destinazioni di navigazione

- `/iva`

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/ui/ConfirmDialog`
- `../components/ui/button`
- `../components/ui/card`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/CalendarioFiscale.jsx — SHA-256 `57a92a634dca23309be646cfdf63c2b56efb9066a46683500b3e208011414f15` — 649 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/CalendarioFiscale.test.jsx`

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
