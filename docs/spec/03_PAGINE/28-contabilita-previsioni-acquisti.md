# 28 — Previsioni acquisti

## Contratto della schermata

- Route: `/contabilita/previsioni-acquisti`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/PrevisioniAcquisti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/28-contabilita-previsioni-acquisti.json`](LOGICA_JSON/28-contabilita-previsioni-acquisti.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Previsioni acquisti basate su storico e scadenze, senza ordini automatici.

## Fonti e registri letti

- storico acquisti
- fatture/scadenze
- budget
- fornitori
- parametri previsionali

## Scritture ed effetti consentiti

- scenario/previsione e note, non ordini o scritture

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Costruire la base da fatture confermate e periodicità riconoscibili, escludendo duplicati e storni.
2. Mostrare per fornitore/mese importo previsto, intervallo, motivazione e dati storici utilizzati.
3. Consentire correzioni di scenario e confronto con budget/consuntivo.

## Automazioni previste

- Ricalcolo periodico delle proposte con versione del modello e confidenza.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Previsione ↔ fatture storiche ↔ fornitore ↔ budget e scadenze.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non creare ordini, pagamenti o fatture; valori con storico insufficiente restano non stimati.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni previsione espone la serie origine e la somma per periodo è riproducibile.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/previsioni-acquisti/previsioni?anno_riferimento={param}&settimane_previsione={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrevisioniAcquisti.jsx
- `GET /api/previsioni-acquisti/statistiche?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrevisioniAcquisti.jsx
- `POST /api/previsioni-acquisti/popola-storico` — `tenere` — sorgente: frontend/src/pages/PrevisioniAcquisti.jsx
- `GET /api/previsioni-acquisti/previsioni` — `tenere` — in uso: FE
- `GET /api/previsioni-acquisti/statistiche` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `costoTotale`
- `error`
- `expandedId`
- `loading`
- `popolando`
- `previsioni`
- `searchTerm`
- `settimanePrevisione`
- `statistiche`
- `visitedTabs`

### Handler e operazioni

- `handlePopolaStorico`
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

- `frontend/src/pages/PrevisioniAcquisti.jsx — SHA-256 `01b78dbfae9919c347e5b847183328780056383abce9cee0aa9020ad2668a2f8` — 390 righe`
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
