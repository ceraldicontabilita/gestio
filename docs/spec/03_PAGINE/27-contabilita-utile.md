# 27 — Utile obiettivo

## Contratto della schermata

- Route: `/contabilita/utile`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/UtileObiettivo.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/27-contabilita-utile.json`](LOGICA_JSON/27-contabilita-utile.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Simulazione utile obiettivo separata dai consuntivi e senza scritture reali.

## Fonti e registri letti

- consuntivi
- budget
- costi/ricavi ricorrenti
- parametri utente

## Scritture ed effetti consentiti

- scenario di simulazione separato, mai scritture o budget approvati

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Partire da un periodo/base dichiarato e permettere ipotesi su ricavi, margini, costi e imposte.
2. Calcolare il fatturato/margine necessario all'utile obiettivo con formule e sensibilità visibili.
3. Salvare o confrontare scenari nominati senza mescolarli ai consuntivi.

## Automazioni previste

- Aggiornamento immediato della simulazione nel browser o servizio read-only.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Scenario ↔ budget/consuntivo usato come base, con link ma senza relazione contabile.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessuna scrittura, ordine o pagamento; risultati sono simulazioni e devono essere etichettati.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Stessi input producono stesso risultato; esportazione riporta tutte le ipotesi e la data base.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/centri-costo/utile-obiettivo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/UtileObiettivo.jsx
- `POST /api/centri-costo/utile-obiettivo` — `tenere` — sorgente: frontend/src/pages/UtileObiettivo.jsx
- `GET /api/centri-costo/utile-obiettivo` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `error`
- `loading`
- `saving`
- `settings`
- `status`
- `visitedTabs`

### Handler e operazioni

- `handleTabChange`
- `loadStatus`
- `saveTarget`

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

- `frontend/src/pages/UtileObiettivo.jsx — SHA-256 `204b2a1aa85e0346476a217337be53ef07355a4b2c51aa2ae79b97b37de8b66e` — 290 righe`
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
