# 04 — Inserimento rapido

## Contratto della schermata

- Route: `/rapido`
- Accesso: `authenticated`
- Modulo: `dashboard`
- Componente corrente: `frontend/src/pages/InserimentoRapido.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Contratto logico macchina: [`LOGICA_JSON/04-inserimento-rapido.json`](LOGICA_JSON/04-inserimento-rapido.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Inserimento rapido idempotente di corrispettivi, versamenti, pagamenti, apporti e presenze.

## Fonti e registri letti

- anno globale
- anagrafiche fornitori/dipendenti
- categorie e metodi consentiti

## Scritture ed effetti consentiti

- movimento o documento nel registro canonico scelto tramite il writer di dominio

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. L'utente sceglie prima il tipo: corrispettivo, versamento, pagamento, apporto soci o presenza.
2. Il form cambia campi e controlli in base al tipo, calcola l'anteprima e mostra registro/segno di destinazione.
3. Il backend genera idempotency key e operation_id, salva una sola volta e restituisce il link al risultato.

## Automazioni previste

- Riconoscimento di un invio ripetuto e proposta di valori anagrafici già verificati.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Il risultato apre Prima Nota, Corrispettivi, Soci o Personale sulla riga appena creata.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Mai scrivere direttamente in più registri dal browser; mai assumere Cassa/Banca dal solo importo.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Doppio invio produce un solo record; segno, data, centesimi e registro coincidono con l'anteprima.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `POST /api/rapido/acconto-dipendente` — `tenere` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `POST /api/rapido/apporto-soci` — `tenere` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `POST /api/rapido/corrispettivo` — `tenere` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `POST /api/rapido/paga-fattura?invoice_id={param}&metodo_pagamento={param}&importo={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `POST /api/rapido/presenza` — `tenere` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `POST /api/rapido/versamento-banca` — `tenere` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `PUT /api/pos-corrispettivi/chiusura-giornaliera` — `tenere` — sorgente: frontend/src/pages/InserimentoRapido.jsx
- `GET /api/dipendenti` — `tenere` — in uso: FE
- `POST /api/dipendenti` — `tenere` — in uso: FE
- `GET /api/fatture-ricevute/archivio` — `tenere` — in uso: FE
- `GET /api/invoices` — `tenere` — in uso: FE
- `GET /api/rapido/dipendenti-attivi` — `tenere` — in uso: FE, chat
- `POST /api/rapido/paga-fattura` — `tenere` — in uso: FE
- `GET /api/rapido/ultimi-inserimenti` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `activeSection`
- `dipendenti`
- `fatture`
- `formData`
- `loading`
- `message`
- `ultimiInserimenti`

### Handler e operazioni

- `handlePagaFattura`
- `handleSaveAcconto`
- `handleSaveApporto`
- `handleSaveCorrispettivo`
- `handleSavePos`
- `handleSavePresenza`
- `handleSaveVersamento`
- `loadUltimiInserimenti`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../contexts/AnnoContext`
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
- `frontend/src/pages/InserimentoRapido.jsx — SHA-256 `05126e751572d46034d434d84e65ee3d7418d6b7b6f30ddaa5e4913d336c6303` — 958 righe`

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
