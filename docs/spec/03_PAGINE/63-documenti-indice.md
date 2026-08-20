# 63 — Indice documentale

## Contratto della schermata

- Route: `/documenti/indice`
- Accesso: `authenticated`
- Modulo: `documenti`
- Componente corrente: `frontend/src/pages/DocumentIndex.jsx`
- Entrypoint/router: `frontend/src/pages/hub/DocumentiHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/63-documenti-indice.json`](LOGICA_JSON/63-documenti-indice.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Indice autorevole nel database applicativo per metadati, hash, percorso e stato indicizzazione degli originali sullo storage file.

## Fonti e registri letti

- storage file applicativo
- metadati/hash/permessi
- indice Documenti
- watermark scansione

## Scritture ed effetti consentiti

- indice documentale e stato indicizzazione; mai contenuto originale

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Scansionare le cartelle di storage autorizzate con paginazione e conservare ID interno, percorso, MIME, dimensione, checksum e permessi.
2. Mostrare cartelle/documenti con filtri e stato indicizzato/non leggibile/duplicato esatto/da elaborare.
3. Aprire l'originale e il record applicativo; una nuova scansione aggiorna metadati senza creare copie.

## Automazioni previste

- Scan incrementale con watermark, retry e rilevamento spostamenti tramite ID interno.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- File (storage applicativo) ↔ indice Documenti ↔ import run ↔ record di dominio.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Errore permessi è esplicito; nessuna pulizia automatica; hash SHA-256 esatto è requisito minimo per copia certa.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Conteggi verificabili per cartella, file apribili e seconda scansione senza nuovi record se lo storage non cambia.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/indice/catalog` — `tenere` — sorgente: frontend/src/pages/hub/DocumentiHub.jsx
- `GET /api/documenti/indice/index/document/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DocumentIndex.jsx
- `GET /api/documenti/indice/index/overview` — `tenere` — sorgente: frontend/src/pages/DocumentIndex.jsx
- `GET /api/documenti/indice/index/status` — `tenere` — sorgente: frontend/src/pages/DocumentIndex.jsx
- `GET /api/documenti/indice/index/declarations` — `tenere` — in uso: FE
- `/api/documenti/indice/index/document/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/documenti/indice/index/f24` — `tenere` — in uso: FE
- `GET /api/documenti/indice/index/search` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `documentCatalog`
- `error`
- `loading`
- `opening`
- `overview`
- `query`
- `results`
- `selected`
- `status`
- `taxCode`
- `visitedTabs`
- `year`

### Handler e operazioni

- `loadAndSyncIndex`
- `loadDocument`
- `openOriginal`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../../hooks/useHashState`
- `../api`

## Fonti tecniche verificate

- `frontend/src/pages/DocumentIndex.jsx` (ex `DriveDocumentIndex.jsx`) — da ricostruire.
- `frontend/src/pages/hub/DocumentiHub.jsx` — da ricostruire.

## Test collegati

- `frontend/src/pages/DocumentIndex.test.jsx`

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
