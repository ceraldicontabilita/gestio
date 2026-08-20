# 41 — Import documenti

## Contratto della schermata

- Route: `/documenti/import`
- Accesso: `authenticated`
- Modulo: `documenti`
- Componente corrente: `frontend/src/pages/ImportDocumenti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/DocumentiHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/41-documenti-import.json`](LOGICA_JSON/41-documenti-import.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Import documenti/ZIP con validazione, salvataggio reale, hash e report.

## Fonti e registri letti

- file/ZIP caricati
- catalogo parser
- storage file e document inbox

## Scritture ed effetti consentiti

- originali (storage file)
- Documenti
- import run
- record di dominio tramite servizi

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Anteprima identifica file, tipo probabile, hash, duplicati certi, parser e problemi senza scrivere.
2. Il comando principale deve caricare e salvare davvero: espandere ZIP in sicurezza, archiviare originali e processare ogni elemento.
3. Instradare F24, quietanze, fatture, corrispettivi, estratti, cedolini e altri tipi ai servizi canonici, mai a writer paralleli.
4. Restituire report per file con nuovo/già presente/elaborato/da verificare/errore e link al risultato.

## Automazioni previste

- Hash e source_external_id rendono ogni reimport idempotente; corrispettivi elaborati sincronizzano Prima Nota Cassa.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Import run ↔ originale sullo storage file ↔ documento inbox ↔ entità creata ↔ eventuale Prima Nota/riconciliazione.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Protezione ZIP traversal/bombe; nessun 'carica senza salvare'; un errore non annulla i file validi né elimina originali.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Reimport dello stesso ZIP: nuovi=0; ogni file ha esito e i corrispettivi validi compaiono una volta in Cassa.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/indice/catalog` — `tenere` — sorgente: frontend/src/pages/hub/DocumentiHub.jsx
- `POST /api/documenti/upload-auto` — `tenere` — sorgente: frontend/src/pages/ImportDocumenti.jsx
- `POST /api/documenti/upload-auto/preview` — `tenere` — sorgente: frontend/src/pages/ImportDocumenti.jsx
- `POST /api/documenti-inbox/auto-classify` — `tenere` — in uso: FE
- `POST /api/documenti-inbox/import-dipendenti-from-cu` — `tenere` — in uso: FE
- `POST /api/documenti-inbox/import-f24-from-inbox` — `tenere` — in uso: FE
- `GET /api/fatture-estere/da-verificare` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `dragOver`
- `driveCatalog`
- `files`
- `previewComplete`
- `results`
- `uploadProgress`
- `uploading`
- `visitedTabs`

### Handler e operazioni

- `handleDragLeave`
- `handleDragOver`
- `handleDrop`
- `handleFileSelect`
- `handlePreview`
- `handleReset`
- `handleUpload`
- `handleZipSelect`
- `loadAndSyncDrive`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../../hooks/useHashState`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/ImportDocumenti.jsx — SHA-256 `0ccb0cad845be08ed6698e1bc5c192489e36a739ed499d3e7202bcbb796e1617` — 923 righe`
- `frontend/src/pages/hub/DocumentiHub.jsx — SHA-256 `298d1dbee393e132a85837d0926387d7082bc4e73a049ac0bac2f10422f3f382` — 160 righe`

## Test collegati

- `frontend/src/pages/ImportDocumenti.test.jsx`

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
