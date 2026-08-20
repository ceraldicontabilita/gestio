# 55 — Admin MFA

## Contratto della schermata

- Route: `/admin/mfa`
- Accesso: `admin`
- Modulo: `admin`
- Componente corrente: `frontend/src/pages/MFAAdmin.jsx`
- Entrypoint/router: `frontend/src/pages/hub/AdminHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/55-admin-mfa.json`](LOGICA_JSON/55-admin-mfa.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

MFA amministrativa, enrollment, revoca, recovery e step-up authentication.

## Fonti e registri letti

- utente amministratore
- stato enrollment MFA
- recovery policy
- audit

## Scritture ed effetti consentiti

- enrollment/revoca MFA nel provider
- recovery code hash
- audit step-up

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Richiedere step-up prima di enrollment, rigenerazione recovery o revoca.
2. Mostrare QR/secret soltanto nella fase di enrollment e confermare con codice valido.
3. Recovery code mostrati una volta, conservati solo come hash e invalidati dopo uso/rigenerazione.

## Automazioni previste

- Revoca sessioni esistenti dopo operazioni sensibili e notifica all'amministratore.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Enrollment ↔ utente ↔ sessioni revocate ↔ audit sicurezza.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Secret MFA mai nei log/fogli/ZIP; nessuna disattivazione senza step-up e motivo.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Codice errato non attiva MFA; dopo attivazione il login richiede secondo fattore e revoca è auditata.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/auth/mfa/status` — `tenere` — sorgente: frontend/src/pages/MFAAdmin.jsx
- `POST /api/auth/mfa/disable` — `tenere` — sorgente: frontend/src/pages/MFAAdmin.jsx
- `POST /api/auth/mfa/setup/confirm` — `tenere` — sorgente: frontend/src/pages/MFAAdmin.jsx
- `POST /api/auth/mfa/setup/start?regenerate={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/MFAAdmin.jsx
- `POST /api/auth/mfa/step-up` — `tenere` — sorgente: frontend/src/pages/MFAAdmin.jsx
- `POST /api/auth/mfa/setup/start` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `busy`
- `code`
- `message`
- `recoveryCodes`
- `setup`
- `status`
- `visitedAdmin`
- `visitedElaborazioni`
- `visitedMfa`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

- `/admin/elaborazioni`

### Componenti/import locali

- `../../components/ds`
- `../api`
- `../components/CopiaTesto`
- `../contexts/AuthContext`

## Fonti tecniche verificate

- `frontend/src/pages/MFAAdmin.jsx — SHA-256 `9a7aa9948045bcb0cd4999881acd8322607498eacb600fa00679c605630f84d5` — 188 righe`
- `frontend/src/pages/hub/AdminHub.jsx — SHA-256 `4bcbb943b2ca87e7b91e4928ff69d9cec3225fb0d1c65d20140a52a336bb2cdd` — 63 righe`

## Test collegati

- `frontend/src/pages/MFAAdmin.test.jsx`

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
