# 57 — Elaborazioni legacy

## Contratto della schermata

- Route: `/admin/batch-processor`
- Accesso: `admin`
- Modulo: `admin`
- Componente corrente: `frontend/src/pages/hub/AdminElaborazioni.jsx`
- Entrypoint/router: `frontend/src/pages/hub/AdminHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/57-admin-batch-processor.json`](LOGICA_JSON/57-admin-batch-processor.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Alias legacy temporaneo verso elaborazioni, senza componente o router duplicato.

## Fonti e registri letti

- route legacy e mappa di redirect
- permessi utente

## Scritture ed effetti consentiti

- Nessuna scrittura; solo audit del redirect se necessario.

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Risolvere la route legacy verso /admin/batch-reprocessing mantenendo parametri sicuri supportati.
2. Mostrare un avviso di percorso aggiornato solo se utile, poi usare lo stesso componente e gli stessi endpoint canonici.

## Automazioni previste

- Telemetry del traffico legacy per decidere la rimozione futura.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Route legacy → pagina elaborazioni canonica, senza duplicare stato o logica.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessun componente, router o writer duplicato; parametri sconosciuti vengono scartati.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Stesso contenuto e autorizzazioni della pagina canonica; nessuna chiamata a endpoint legacy paralleli.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `POST /api/ai-parser/process-email-batch` — `tenere` — in uso: FE
- `POST /api/email-download/auto-associa` — `tenere` — in uso: FE
- `POST /api/email-download/start-full-download` — `tenere` — in uso: FE
- `POST /api/estratto-conto-movimenti/ricategorizza-batch` — `tenere` — in uso: FE
- `POST /api/f24-riconciliazione/riconcilia-tutto` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `autoMode`
- `currentTask`
- `isRunning`
- `logs`
- `progress`
- `stats`
- `taskResults`
- `visited`
- `visitedAdmin`
- `visitedElaborazioni`
- `visitedMfa`

### Handler e operazioni

- `handleSelect`

### Destinazioni di navigazione

- `/admin/elaborazioni`

### Componenti/import locali

- `../../components/ds`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/BatchProcessor.jsx — SHA-256 `591e5df3ab9ad8e833d90e7564a57fff933d13ca36290e98e360b73a7ddd4518` — 602 righe`
- `frontend/src/pages/hub/AdminElaborazioni.jsx — SHA-256 `a6d36feacc680ae40246e5515336d08299456e65793d093e8802b44da6dadec8` — 42 righe`
- `frontend/src/pages/hub/AdminHub.jsx — SHA-256 `4bcbb943b2ca87e7b91e4928ff69d9cec3225fb0d1c65d20140a52a336bb2cdd` — 63 righe`

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
