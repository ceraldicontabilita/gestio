# 28 — Previsioni acquisti

## Contratto della schermata

- Route: `/contabilita/previsioni-acquisti`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/PrevisioniAcquisti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Mappa macchina: [`MAPPE_JSON/contabilita-previsioni-acquisti.json`](MAPPE_JSON/contabilita-previsioni-acquisti.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Previsioni acquisti basate su storico e scadenze, senza ordini automatici.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/previsioni-acquisti/previsioni?anno_riferimento={param}&settimane_previsione={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrevisioniAcquisti.jsx
- `GET /api/previsioni-acquisti/statistiche?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrevisioniAcquisti.jsx
- `POST /api/previsioni-acquisti/popola-storico` — `tenere` — sorgente: frontend/src/pages/PrevisioniAcquisti.jsx
- `GET /api/previsioni-acquisti/previsioni` — `tenere` — in uso: FE
- `GET /api/previsioni-acquisti/statistiche` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `costoTotale`
- `error`
- `expandedId`
- `loading`
- `popolando`
- `previsioni`
- `searchTerm`
- `settimanePrevisione`
- `statistiche`
- `visitedTabs`

### Handler e operazioni

- `handlePopolaStorico`
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

- `frontend/src/pages/PrevisioniAcquisti.jsx — SHA-256 `01b78dbfae9919c347e5b847183328780056383abce9cee0aa9020ad2668a2f8` — 390 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

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
