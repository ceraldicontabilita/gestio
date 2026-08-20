# 10 — Cedolini e salari

## Contratto della schermata

- Route: `/salari`
- Accesso: `authenticated`
- Modulo: `personale`
- Componente corrente: `frontend/src/pages/CedoliniSalari.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Contratto logico macchina: [`LOGICA_JSON/10-salari.json`](LOGICA_JSON/10-salari.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Dipendenti, cedolini, periodi e pagamenti con regola temporale del giorno 25.

## Fonti e registri letti

- Dipendenti
- Cedolini
- Bonifici
- Movimenti bancari
- documenti paghe

## Scritture ed effetti consentiti

- periodo cedolino
- note/descrizione persistenti
- relazioni pagamento e Prima Nota salari

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Conservare ogni cedolino come documento distinto anche se dipendente, mese e tipo coincidono.
2. Per un bonifico effettuato prima del giorno 25 proporre il mese precedente; dal giorno 25 proporre il mese corrente, senza confermare se il cedolino non esiste.
3. Mostrare per dipendente cedolini, bonifici, residui e documenti; il campo descrizione deve sopravvivere a refresh e filtri.
4. Confermare l'associazione con identità dipendente/IBAN, periodo, importo e provenienza; i candidati multipli richiedono scelta.

## Automazioni previste

- Import paghe/bonifici idempotente e proposta automatica del periodo secondo la regola del giorno 25.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Cedolino ↔ dipendente ↔ bonifico ↔ movimento banca ↔ Prima Nota salari, tutti navigabili.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Importo uguale non basta; non scartare cedolini legittimi dello stesso mese; il periodo proposto non è conferma.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Dopo refresh restano periodo, nota e collegamenti; la somma riconciliata per dipendente coincide con i bonifici confermati.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/prima-nota-salari/export-appdipendenti/download` — `tenere` — sorgente: frontend/src/pages/CedoliniSalari.jsx
- `GET /api/prima-nota-salari/salari` — `tenere` — sorgente: frontend/src/pages/CedoliniSalari.jsx
- `GET /api/prima-nota-salari/salari/{param}/{param}-pdf` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CedoliniSalari.jsx
- `/api/prima-nota-salari/salari/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `annoFiltro`
- `documentoInApertura`
- `exportInCorso`
- `loading`
- `ricerca`
- `righe`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../lib/utils`
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
- `frontend/src/pages/CedoliniSalari.jsx — SHA-256 `637119cf977a3e3a94bf263123418f8299b8ff7a650760eee5c8c1618fce4832` — 281 righe`

## Test collegati

- `frontend/src/pages/CedoliniSalari.test.jsx`

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
