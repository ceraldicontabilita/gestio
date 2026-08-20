# 40 — Coerenza POS

## Contratto della schermata

- Route: `/riconciliazione/coerenza-pos`
- Accesso: `authenticated`
- Modulo: `riconciliazione`
- Componente corrente: `frontend/src/pages/CoerenzaPOSCorrispettivi.jsx`
- Entrypoint/router: `frontend/src/pages/hub/RiconciliazioneHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/40-coerenza-pos.json`](LOGICA_JSON/40-coerenza-pos.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Coerenza fra corrispettivi, POS, commissioni, giorni di vendita e accrediti.

## Fonti e registri letti

- corrispettivi RT
- chiusure POS
- transazioni/accrediti SumUp
- movimenti banca
- commissioni

## Scritture ed effetti consentiti

- casi di differenza e relazioni confermate
- nessuna nuova vendita

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Confrontare per giorno e terminale: vendite carta RT, chiusura terminale, credito provider atteso e accredito banca.
2. Mostrare lordo, commissioni, netto, date di competenza/accredito e differenza con elenco operazioni.
3. Riconciliare accrediti uno-a-uno o molti-a-uno quando il provider lo documenta, conservando tutti gli ID.

## Automazioni previste

- Aggiornamento giornaliero e riapertura del caso se cambia una fonte.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Giorno POS ↔ corrispettivo ↔ transazioni provider ↔ accredito/commissione banca ↔ Prima Nota.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non creare vendite dalle chiusure o dagli accrediti; data vendita e data accredito non devono coincidere per forza.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni differenza è spiegata; giorni completi quadrano lordo - commissioni = netto accreditato.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/paypal-api/status` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/riepilogo-mensile?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/verifica-coerenza?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/sumup/riepilogo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/corrispettivi/manuale` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/paypal-api/sync` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `POST /api/pos-corrispettivi/chiusure-giornaliere/batch` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `PUT /api/pos-corrispettivi/chiusura-giornaliera` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/riepilogo-mensile` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/verifica-coerenza` — `tenere` — in uso: FE
- `GET /api/sumup/riepilogo` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `dataForm`
- `dati`
- `dettaglioBancaAperto`
- `dueFasi`
- `err`
- `errore`
- `espansa`
- `filtroStato`
- `importAperto`
- `importoSalvato`
- `loading`
- `modalAperta`
- `note`
- `paypalRefreshKey`
- `posReale`
- `riepilogoMensile`
- `salvando`
- `sumup`
- `tab`
- `testo`
- `totale`
- `valore`
- `vista`

### Handler e operazioni

- `loadDati`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/ds`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/CoerenzaPOSCorrispettivi.jsx — SHA-256 `cdc0d4614328f05f04c0ae206fced2f9c672a51b9bca84efd56bd240b81b5aa6` — 1545 righe`
- `frontend/src/pages/hub/RiconciliazioneHub.jsx — SHA-256 `f8e30156c58abc97b26bf319e79a6ebc2d5023c40b7650e415206602d5ae2ba4` — 129 righe`

## Test collegati

- `frontend/src/pages/CoerenzaPOSCorrispettivi.test.jsx`

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
