# 17 — Verifica Bilancio

## Contratto della schermata

- Route: `/contabilita/verifica`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/BilancioVerifica.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/17-contabilita-verifica.json`](LOGICA_JSON/17-contabilita-verifica.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Verifica bilancio con anomalie spiegate e link alla scrittura origine.

## Fonti e registri letti

- bilancio calcolato
- giornale
- piano conti
- check di quadratura

## Scritture ed effetti consentiti

- stato e nota di risoluzione dell'anomalia, senza alterare direttamente la contabilità

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Eseguire controlli riproducibili: sbilanci, conti mancanti, date fuori periodo, duplicati e saldi incoerenti.
2. Ogni alert mostra severità, regola, elenco righe, differenza e percorso di correzione.
3. La risoluzione viene riconosciuta ricalcolando la regola, non nascondendo manualmente l'alert.

## Automazioni previste

- Ricalcolo dopo modifica di scritture e prima di chiusura esercizio.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Alert ↔ conto ↔ scrittura ↔ documento origine ↔ checklist di chiusura.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Contatori sempre cliccabili; nessuna correzione contabile direttamente dalla card di allerta.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni anomalia è riproducibile e scompare solo quando la condizione non esiste più.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/contabilita-gestionale/bilancio-verifica?anno={param}&dettaglio={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/BilancioVerifica.jsx
- `GET /api/contabilita-gestionale/bilancio-verifica` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `bvError`
- `data`
- `dettaglio`
- `error`
- `expandedConti`
- `filtroTipo`
- `loading`
- `search`
- `showSaldi`
- `visitedTabs`

### Handler e operazioni

- `handleExportCSV`
- `handlePrint`
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

- `frontend/src/pages/BilancioVerifica.jsx — SHA-256 `0fa1d20b282e386c609dd56ac36ede942d693e56c724277dc0631bd27fd46d87` — 709 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/BilancioVerifica.test.jsx`

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
