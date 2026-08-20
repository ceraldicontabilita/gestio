# 15 — Piano dei Conti

## Contratto della schermata

- Route: `/contabilita`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/PianoDeiConti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/15-contabilita-piano-conti.json`](LOGICA_JSON/15-contabilita-piano-conti.json)
- Stato della prova corrente: `verified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Piano dei conti gerarchico, regole versionate e movimenti collegati.

## Fonti e registri letti

- piano dei conti versionato
- regole di classificazione
- scritture e righe giornale

## Scritture ed effetti consentiti

- conto/sottoconto
- validità temporale
- regole approvate

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Mostrare la gerarchia con codice stabile, natura Dare/Avere, validità e conti non più utilizzabili separati.
2. Creazione/modifica controlla unicità, cicli gerarchici e impatto sulle regole future.
3. La disattivazione impedisce nuove scritture ma conserva storico e bilanci precedenti.

## Automazioni previste

- Suggerire classificazioni dalle regole approvate senza riclassificare automaticamente periodi chiusi.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Conto ↔ movimenti giornale ↔ documenti/fatture ↔ bilancio e controlli.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Mai cancellare conti usati; nessuna riclassificazione retroattiva silenziosa.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Gerarchia senza cicli; ogni saldo apre le scritture origine e un conto disattivato resta nello storico.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/piano-conti/?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `GET /api/piano-conti/conto/{param}/movimenti?limit=40&anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `GET /api/piano-conti/regole` — `tenere` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `POST /api/dizionario-articoli/riclassifica-completo?limite_ai=500` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `POST /api/piano-conti/` — `tenere` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `POST /api/piano-conti/regole` — `tenere` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `PUT /api/dizionario-articoli/articolo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PianoDeiConti.jsx
- `/api/dizionario-articoli/articolo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/dizionario-articoli/riclassifica-completo` — `tenere` — in uso: FE
- `/api/piano-conti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/piano-conti/conto/{param}/movimenti` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `_conti`
- `activeTab`
- `bilancio`
- `contoDetail`
- `error`
- `expandedCategories`
- `grouped`
- `loading`
- `loadingDetail`
- `newConto`
- `newRegola`
- `regole`
- `riclassificaResult`
- `riclassificando`
- `selectedConto`
- `showNewConto`
- `showNewRegola`
- `spostandoRiga`
- `visitedTabs`

### Handler e operazioni

- `closeDrawer`
- `handleCreateConto`
- `handleCreateRegola`
- `handleRiclassificaAI`
- `handleSpostaRigaConto`
- `handleTabChange`
- `loadData`
- `openContoDetail`

### Destinazioni di navigazione

- `/contabilita/piano-conti/${tabId}`

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/PianoDeiConti.jsx — SHA-256 `78b1406af2e4044396f03338b290c5979aba9e084b52b74b3e14a25455687ac9` — 1129 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/PianoDeiConti.test.jsx`
- `tests/test_piano_conti_performance_guard.py`

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
