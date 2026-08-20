# 39 — PayPal

## Contratto della schermata

- Route: `/riconciliazione/paypal`
- Accesso: `authenticated`
- Modulo: `riconciliazione`
- Componente corrente: `frontend/src/pages/RiconciliazionePaypal.jsx`
- Entrypoint/router: `frontend/src/pages/hub/RiconciliazioneHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/39-riconciliazione-paypal.json`](LOGICA_JSON/39-riconciliazione-paypal.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

PayPal interconnesso con banca, fatture, Prima Nota e prove tramite operation_id.

## Fonti e registri letti

- transazioni PayPal
- movimenti bancari SDD PayPal
- fatture
- Prima Nota

## Scritture ed effetti consentiti

- relazioni transazione-fattura-banca
- stato riconciliazione
- note

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Importare tutte le transazioni con transaction ID, data, controparte, valuta, lordo, commissione e netto.
2. Collegare fattura usando controparte/numero/data/centesimi e il movimento bancario usando riferimenti SDD PayPal e finestra coerente.
3. Assegnare un operation_id comune a fattura, transazione e banca senza fondere le tre righe.
4. Applicare la stessa logica a tutti i movimenti PayPal; i dubbi mostrano candidati e scelta.

## Automazioni previste

- Sync incrementale idempotente e riprocessamento dei non associati quando arriva fattura o banca.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- PayPal ↔ fattura/PDF ↔ banca ↔ Prima Nota; ogni colonna è un link alla prova.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non confrontare USD ed EUR senza cambio/prova; commissione e acquisto non sono la stessa riga; importo solo non basta.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Un acquisto PayPal con fattura e addebito SDD produce tre record collegati con lo stesso operation_id; il secondo sync non duplica transazioni.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/paypal-api/status` — `tenere` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx, frontend/src/pages/hub/RiconciliazioneHub.jsx
- `GET /api/paypal-statements/bank-movements?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `GET /api/paypal-statements/dashboard?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `GET /api/paypal-statements/report?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `GET /api/paypal-statements/statements?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `GET /api/paypal-statements/transactions?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `POST /api/paypal-api/sync` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `POST /api/paypal-api/sync/incremental` — `tenere` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `POST /api/paypal-statements/riprocessa?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `PUT /api/paypal-statements/transactions/{param}/descrizione` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RiconciliazionePaypal.jsx
- `/api/fatture-ricevute/fattura/{f` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/paypal-statements/bank-movements` — `tenere` — in uso: FE
- `GET /api/paypal-statements/dashboard` — `tenere` — in uso: FE
- `GET /api/paypal-statements/report` — `tenere` — in uso: FE
- `POST /api/paypal-statements/riprocessa` — `tenere` — in uso: FE
- `GET /api/paypal-statements/statements` — `tenere` — in uso: FE
- `GET /api/paypal-statements/transactions` — `tenere` — in uso: FE
- `/api/paypal-statements/transactions/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `dashboard`
- `errore`
- `fonti`
- `loading`
- `movimentiBanca`
- `paypalRefreshKey`
- `ricerca`
- `riepilogoBanca`
- `riprocessamento`
- `saving`
- `sincronizzazione`
- `statoApi`
- `statoCollegamento`
- `tab`
- `transazioni`
- `value`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../contexts/AnnoContext`
- `../hooks/useData`

## Fonti tecniche verificate

- `frontend/src/pages/RiconciliazionePaypal.jsx — SHA-256 `b4070051a114949cdc4c24398fba25cb0441fa599c57eb974a8d9957d04b0ffa` — 335 righe`
- `frontend/src/pages/hub/RiconciliazioneHub.jsx — SHA-256 `f8e30156c58abc97b26bf319e79a6ebc2d5023c40b7650e415206602d5ae2ba4` — 129 righe`

## Test collegati

- `frontend/src/pages/RiconciliazionePaypal.test.jsx`

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
