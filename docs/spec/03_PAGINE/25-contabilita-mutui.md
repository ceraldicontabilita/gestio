# 25 — Mutui

## Contratto della schermata

- Route: `/contabilita/mutui`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/Mutui.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/25-contabilita-mutui.json`](LOGICA_JSON/25-contabilita-mutui.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Mutui, rate, quota capitale/interessi, banca e residuo riconciliato.

## Fonti e registri letti

- contratti mutuo/PDF
- mutui
- piano rate
- movimenti bancari
- giornale

## Scritture ed effetti consentiti

- mutuo e rate
- relazione rata-movimento
- scritture capitale/interessi

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Importare o inserire contratto con banca, capitale, tasso, decorrenza e piano verificabile.
2. Per ogni rata separare quota capitale, interessi, spese e residuo; mostrare scadenza e stato.
3. Riconciliare il movimento bancario alla rata usando riferimento, data e importo, poi generare la scrittura tramite writer unico.

## Automazioni previste

- Proposta automatica di rata candidata e aggiornamento residuo dopo conferma.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Mutuo ↔ contratto/PDF ↔ rata ↔ banca ↔ giornale ↔ posizione finanziaria.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Importo uguale non basta; non contabilizzare l'intera rata come costo; nessun pagamento automatico.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Somma capitale rimborsato più residuo coincide col capitale; rata riconciliata apre il movimento esatto.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/mutui/` — `tenere` — sorgente: frontend/src/pages/Mutui.jsx
- `GET /api/mutui/statistiche/dashboard` — `tenere` — sorgente: frontend/src/pages/Mutui.jsx
- `POST /api/mutui/riconcilia` — `tenere` — sorgente: frontend/src/pages/Mutui.jsx
- `GET /api/mutui` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `error`
- `expandedMutuo`
- `lastRiconciliazione`
- `loading`
- `mutui`
- `riconciliaLoading`
- `stats`
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
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/Mutui.jsx — SHA-256 `1b428ba967b8b0ac6a307a0135c5f6abafbb1748b7273126a114b1bae903b9bf` — 572 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `tests/test_mappa_categoria_estratto_conto.py`
- `tests/test_mutui_document_import.py`

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
