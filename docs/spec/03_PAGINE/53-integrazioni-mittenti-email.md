# 53 — Mittenti Email attendibili

## Contratto della schermata

- Route: `/integrazioni/mittenti-email`
- Accesso: `authenticated`
- Modulo: `integrazioni`
- Componente corrente: `frontend/src/pages/MittentiEmail.jsx`
- Entrypoint/router: `frontend/src/pages/hub/IntegrazioniHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/53-integrazioni-mittenti-email.json`](LOGICA_JSON/53-integrazioni-mittenti-email.json)
- Stato della prova corrente: `verified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Mittenti email attendibili con canale, documento atteso, priorita e audit.

## Fonti e registri letti

- mittenti/alias configurati
- tipi documento
- statistiche/errori ingest

## Scritture ed effetti consentiti

- regola mittente-canale-documento, priorità e audit

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Registrare indirizzo/dominio, alias PEC, canale, documenti attesi e livello di affidabilità.
2. Testare la regola su esempi esistenti in sola lettura e mostrare corrispondenze/conflitti.
3. Versionare modifiche e permettere disattivazione senza perdere lo storico dei documenti già importati.

## Automazioni previste

- Le regole alimentano classificazione Gmail ma non sostituiscono hash e validazione del documento.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Mittente ↔ run Gmail ↔ documenti classificati ↔ errori/audit.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Mittente noto non rende vero ogni allegato; wrapper PEC e alias vanno conservati come provenienza.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Regola attiva classifica solo il perimetro previsto e il test mostra esattamente i messaggi coinvolti.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/email-download/mittenti/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/MittentiEmail.jsx
- `GET /api/email-download/mittenti` — `tenere` — sorgente: frontend/src/pages/MittentiEmail.jsx
- `POST /api/email-download/mittenti` — `tenere` — sorgente: frontend/src/pages/MittentiEmail.jsx
- `PUT /api/email-download/mittenti/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/MittentiEmail.jsx
- `/api/email-download/mittenti/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `form`
- `loading`
- `mittenti`
- `salvando`
- `visitedTabs`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/fatture-estere-verifica`
- `/riconciliazione/pagopa`

### Componenti/import locali

- `../../components/ds`
- `../api`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/MittentiEmail.jsx — SHA-256 `5adb0b8ed4c89d6ce6228de666df634c91d7960b468bc122a98cfd726f16389d` — 241 righe`
- `frontend/src/pages/hub/IntegrazioniHub.jsx — SHA-256 `07205fd2aed68fbf982c878ee39ad5a74aa68e362c5d106ba9be90d8593792ec` — 50 righe`

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
