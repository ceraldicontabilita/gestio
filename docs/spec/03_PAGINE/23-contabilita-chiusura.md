# 23 — Chiusura esercizio

## Contratto della schermata

- Route: `/contabilita/chiusura`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/ChiusuraEsercizio.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/23-contabilita-chiusura.json`](LOGICA_JSON/23-contabilita-chiusura.json)
- Stato della prova corrente: `verified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Chiusura esercizio con checklist, anteprima, conferma forte, audit e rollback.

## Fonti e registri letti

- check mensili
- bilancio
- giornale
- IVA/F24
- stato esercizio

## Scritture ed effetti consentiti

- evento di chiusura
- snapshot e hash
- eventuale riapertura/rettifica

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Eseguire una checklist bloccante di quadrature, periodi, documenti e registrazioni mancanti.
2. Mostrare anteprima completa degli effetti e richiedere frase esatta più step-up authentication.
3. La chiusura congela la versione, registra hash/attore/orario e impedisce modifiche dirette al periodo.
4. La riapertura è separata, motivata e auditata; le rettifiche non cancellano lo snapshot precedente.

## Automazioni previste

- Ricalcolo della checklist prima della conferma e invalidazione se i dati cambiano.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Chiusura ↔ bilancio ↔ giornale ↔ controlli ↔ audit e snapshot esportabile.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessuna chiusura automatica o con checklist rossa; nessuna cancellazione di dati originari.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Chiusura impossibile senza conferma forte; esercizio chiuso produce lo stesso snapshot da sorgenti immutate.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/chiusura-esercizio/bilancino-verifica/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ChiusuraEsercizio.jsx
- `GET /api/chiusura-esercizio/stato/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ChiusuraEsercizio.jsx
- `GET /api/chiusura-esercizio/storico` — `tenere` — sorgente: frontend/src/pages/ChiusuraEsercizio.jsx
- `GET /api/chiusura-esercizio/verifica-preliminare/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ChiusuraEsercizio.jsx
- `POST /api/chiusura-esercizio/apertura-nuovo-esercizio` — `tenere` — sorgente: frontend/src/pages/ChiusuraEsercizio.jsx
- `POST /api/chiusura-esercizio/esegui-chiusura` — `tenere` — sorgente: frontend/src/pages/ChiusuraEsercizio.jsx
- `/api/chiusura-esercizio/bilancino-verifica/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/chiusura-esercizio/stato/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/chiusura-esercizio/verifica-preliminare/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeStep`
- `bilancino`
- `confirmationText`
- `error`
- `executing`
- `loading`
- `note`
- `openingConfirmationText`
- `stato`
- `storico`
- `success`
- `verifica`
- `visitedTabs`

### Handler e operazioni

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
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/ChiusuraEsercizio.jsx — SHA-256 `cccb2beccc78daf93b2b5bfdbcbd2475600d7cf8928e7666cc525555e7948078` — 958 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/ChiusuraEsercizio.test.jsx`
- `tests/test_cespiti_chiusura.py`

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
