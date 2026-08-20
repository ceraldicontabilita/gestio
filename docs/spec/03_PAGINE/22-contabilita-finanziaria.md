# 22 — Finanziaria

## Contratto della schermata

- Route: `/contabilita/finanziaria`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/Finanziaria.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/22-contabilita-finanziaria.json`](LOGICA_JSON/22-contabilita-finanziaria.json)
- Stato della prova corrente: `verified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Posizione finanziaria, flussi, debiti, crediti e finanziamenti soci non duplicati.

## Fonti e registri letti

- saldi banca/cassa
- crediti/debiti
- mutui
- finanziamenti soci
- scadenze

## Scritture ed effetti consentiti

- Nessuna scrittura primaria; classificazioni finanziarie tracciate quando necessarie.

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Calcolare liquidità, posizione finanziaria netta e flussi da registri confermati con periodo e formula visibili.
2. Separare finanziamenti soci da ricavi e distinguere capitale, interessi, debiti e crediti.
3. Ogni totale apre strumenti e movimenti che lo compongono, senza sommare la stessa operazione su più viste.

## Automazioni previste

- Ricalcolo derivato quando cambiano saldi, rate o relazioni.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Indicatore ↔ banca/Prima Nota ↔ mutuo/socio ↔ documento e scadenza.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Niente saldi inventati o cache non datata; trasferimenti interni non sono flussi economici.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni indicatore è riconciliabile alle fonti e finanziamenti soci non risultano duplicati tra banca e ledger.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/finanziaria/summary?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Finanziaria.jsx
- `GET /api/finanziaria/summary` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `error`
- `loadError`
- `loading`
- `summary`
- `visitedTabs`

### Handler e operazioni

- `handleTabChange`
- `loadSummary`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/ds`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/Finanziaria.jsx — SHA-256 `417b7fc53294c720e09d5084fb6a58ec171d0173b6dc37498b971a889c836300` — 386 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/Finanziaria.test.jsx`
- `tests/test_finanziaria_semantica.py`

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
