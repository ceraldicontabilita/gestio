# 59 — Mappa gestionale

## Contratto della schermata

- Route: `/mappa-gestionale`
- Accesso: `authenticated`
- Modulo: `strumenti`
- Componente corrente: `frontend/src/pages/MappaGestionale.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Contratto logico macchina: [`LOGICA_JSON/59-mappa-gestionale.json`](LOGICA_JSON/59-mappa-gestionale.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Mappa gestionale generata dal catalogo con moduli, route, flussi e health.

## Fonti e registri letti

- page_catalog
- router frontend/backend
- health e stato audit

## Scritture ed effetti consentiti

- Nessuna scrittura applicativa; artefatto generato e fingerprint.

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Generare albero per modulo dalle route canoniche con accesso, componente e stato verifica.
2. Ogni nodo apre la pagina e mostra dipendenze/endpoint principali; alias legacy sono marcati.
3. Separare raggiungibile, testato staticamente e verificato end-to-end.

## Automazioni previste

- Rigenerazione in CI e fallimento se catalogo/router/documentazione divergono.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Nodo pagina ↔ scheda logica ↔ componente ↔ endpoint ↔ test/health.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- HTTP 200 non equivale a funzionamento; nessuna pagina scoperta fuori catalogo.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Catalogo contiene esattamente le route canoniche e ogni link risolve con il ruolo previsto.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

Nessuna chiamata API rilevata staticamente: verificare se la pagina è puramente di navigazione.

## Stato e azioni UI rilevati

### Stato locale

- `activeId`
- `group`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `./App.jsx`
- `./components/ErrorBoundary.jsx`
- `./components/ui/ConfirmDialog.jsx`
- `./components/ui/sonner.jsx`
- `./contexts/AnnoContext.jsx`
- `./contexts/AuthContext.jsx`
- `./lib/queryClient.js`
- `./lib/utils.js`
- `./pages/Login.jsx`

## Fonti tecniche verificate

- `frontend/src/main.jsx — SHA-256 `43867ec02c33b70634aab8e04e98f996c845971cc1ff88239a980f9d9af12089` — 145 righe`
- `frontend/src/pages/MappaGestionale.jsx — SHA-256 `9032ca362e918c595ab8013577baee31938abb1ebc083e3e1aca5e7b4778b561` — 1008 righe`

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
