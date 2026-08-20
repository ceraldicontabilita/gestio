# 62 — Dati ISA

## Contratto della schermata

- Route: `/contabilita/dati-isa`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/DatiIsa.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/62-contabilita-dati-isa.json`](LOGICA_JSON/62-contabilita-dati-isa.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Dati ISA derivati, tracciabili, quadrati ed esportabili senza valori inventati.

## Fonti e registri letti

- bilancio/giornale
- fatture/corrispettivi
- personale/cespiti
- mappatura campi ISA

## Scritture ed effetti consentiti

- snapshot ISA derivato, mapping/versione e note; nessuna modifica alle fonti

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Mappare ogni campo ISA a formula e conti/registri origine per esercizio.
2. Calcolare valori solo da dati confermati e mostrare mancanti, esclusioni e quadrature.
3. Esportare snapshot versionato con fingerprint delle fonti e drill-down per campo.

## Automazioni previste

- Ricalcolo bozza dopo variazioni; snapshot consegnato resta immutabile.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Campo ISA ↔ formula ↔ conti/righe/documenti origine ↔ snapshot/export.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessun valore inventato o zero al posto di fonte mancante; niente invio automatico.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni valore è tracciabile e la somma delle righe origine coincide; mancanti restano espliciti.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/dashboard/fascia-energia` — `tenere` — sorgente: frontend/src/pages/DatiIsa.jsx
- `GET /api/dati-isa/riepilogo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DatiIsa.jsx
- `GET /api/dati-isa/riepilogo` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `data`
- `error`
- `errore`
- `fasce`
- `loading`
- `visitedTabs`

### Handler e operazioni

- `handleTabChange`

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

- `frontend/src/pages/DatiIsa.jsx — SHA-256 `0d515a06f2bbb8e2fecffcbfaff0e81fa062c53c30b1bbf05b3f8ff5e629754d` — 124 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/DatiIsa.test.jsx`

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
