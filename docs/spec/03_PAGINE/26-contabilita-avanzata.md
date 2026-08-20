# 26 — Contabilita avanzata

## Contratto della schermata

- Route: `/contabilita/avanzata`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/ContabilitaAvanzata.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/26-contabilita-avanzata.json`](LOGICA_JSON/26-contabilita-avanzata.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Analisi contabili avanzate come viste derivate, con formule e drill-down.

## Fonti e registri letti

- viste contabili derivate
- giornale
- piano conti
- periodi e dimensioni

## Scritture ed effetti consentiti

- Nessuna scrittura; preferenze/report eventualmente salvati.

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Presentare analisi per conto, mese, fornitore e centro usando formule documentate.
2. Applicare gli stessi filtri canonici del bilancio e indicare dati esclusi o incompleti.
3. Ogni grafico/tabella offre drill-down alle righe contabili e export con metadati del filtro.

## Automazioni previste

- Ricalcolo read-only; cache con data/fingerprint e invalidazione esplicita.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Analisi ↔ giornale ↔ conto ↔ documento origine.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessun indicatore senza formula; errore fonte non diventa zero; niente scritture dalla vista analitica.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Totali delle analisi coincidono con il giornale filtrato e ogni dato è spiegabile.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/contabilita/aliquote-irap` — `tenere` — sorgente: frontend/src/pages/ContabilitaAvanzata.jsx
- `GET /api/contabilita/export/pdf-dichiarazione?anno={param}&regione={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ContabilitaAvanzata.jsx
- `POST /api/contabilita/inizializza-piano-esteso` — `admin-only` — sorgente: frontend/src/pages/ContabilitaAvanzata.jsx
- `POST /api/contabilita/ricategorizza-fatture` — `tenere` — sorgente: frontend/src/pages/ContabilitaAvanzata.jsx
- `GET /api/contabilita/bilancio-dettagliato` — `tenere` — in uso: FE
- `GET /api/contabilita/calcolo-imposte` — `tenere` — in uso: FE
- `GET /api/contabilita/disponibilita-liquide` — `tenere` — in uso: FE
- `GET /api/contabilita/export/pdf-dichiarazione` — `tenere` — in uso: FE
- `GET /api/contabilita/statistiche-categorizzazione` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `aliquoteIrap`
- `bilancio`
- `disponibilita`
- `error`
- `erroriBlocchi`
- `imposte`
- `loading`
- `message`
- `processing`
- `regione`
- `statistiche`
- `visitedTabs`

### Handler e operazioni

- `fetchData`
- `handleDownloadPDF`
- `handleInizializzaPiano`
- `handleRicategorizza`
- `handleTabChange`

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

- `frontend/src/pages/ContabilitaAvanzata.jsx — SHA-256 `f5898bb5efe8525939b37838f83e8b30c073fd5dcad079653e3f8e87d258c50e` — 909 righe`
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
