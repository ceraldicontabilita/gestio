# 09 — Pulizia Prima Nota

## Contratto della schermata

- Route: `/prima-nota/pulizia`
- Accesso: `authenticated`
- Modulo: `prima-nota`
- Componente corrente: `frontend/src/pages/PuliziaPrimaNota.jsx`
- Entrypoint/router: `frontend/src/pages/hub/PrimaNotaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/09-prima-nota-pulizia.json`](LOGICA_JSON/09-prima-nota-pulizia.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Audit Prima Nota con liste esatte, dry-run, correzione deterministica e rollback.

## Fonti e registri letti

- Prima Nota Cassa/Banca
- chiavi canoniche
- hash/import run
- audit delle correzioni

## Scritture ed effetti consentiti

- marcatura recuperabile di copie esatte
- report di correzione e rollback

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Eseguire diagnosi read-only e mostrare sempre l'elenco completo dei gruppi, non solo un contatore.
2. Distinguere copie certe, casi simili ma legittimi e incoerenze di relazione; assegni o rate ricorrenti non sono duplicati per importo.
3. Applicare automaticamente solo la copia esatta secondo source_external_id/hash/fingerprint, conservando il record più completo.
4. Registrare prima/dopo, motivo e comando di rollback; i casi dubbi restano visibili senza modifica.

## Automazioni previste

- La prevenzione duplicati agisce già in import; la pagina serve per audit e recupero, non per manutenzione ordinaria.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Ogni elemento della lista apre direttamente le righe nella Prima Nota filtrata.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessuna cancellazione fisica; nessuna deduplica per importo o fattura_id condiviso quando le date/strumenti sono diversi.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Anteprima e applicazione restituiscono gli stessi target; secondo passaggio trova zero copie certe e rollback ripristina la visibilità.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/prima-nota/diagnostica-corrispettivi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `GET /api/prima-nota/diagnostica-metodi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/corrispettivi/sync/quadratura` — `tenere` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/corrispettivi/rebuild-prima-nota?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/estratto-conto-movimenti/ripara-versamenti-cassa?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/prima-nota/cassa/sync-corrispettivi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/prima-nota/dedup-fatture?applica=false&auto_risolvi_certi=true&ripristina_regola_errata=true&anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/prima-nota/provvisori/auto-conferma-per-metodo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/prima-nota/sposta-scrittura` — `tenere` — sorgente: frontend/src/pages/PuliziaPrimaNota.jsx
- `POST /api/corrispettivi/rebuild-prima-nota` — `tenere` — in uso: FE
- `POST /api/estratto-conto-movimenti/ripara-versamenti-cassa` — `tenere` — in uso: FE
- `POST /api/prima-nota/cassa/sync-corrispettivi` — `tenere` — in uso: FE
- `POST /api/prima-nota/dedup-fatture` — `tenere` — in uso: FE
- `GET /api/prima-nota/diagnostica-corrispettivi` — `tenere` — in uso: FE
- `GET /api/prima-nota/diagnostica-metodi` — `tenere` — in uso: FE
- `POST /api/prima-nota/provvisori/auto-conferma-per-metodo` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `anteprima`
- `diagnosi`
- `discordanti`
- `errore`
- `loading`
- `risultatoAutoConferma`
- `risultatoPulizia`
- `risultatoQuadratura`
- `risultatoRicostruzione`
- `risultatoSync`
- `risultatoVersamenti`
- `spostandoId`
- `visitedPrimaNota`
- `visitedPulizia`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/PuliziaPrimaNota.jsx — SHA-256 `15d70c7e55f90272ed5aac845e4bc4a8613502a7ed7e2758c3dec75836908059` — 799 righe`
- `frontend/src/pages/hub/PrimaNotaHub.jsx — SHA-256 `daa3325581cd0a60ff90dff5a79782c5acfb0272788a9299eddf00f9c2e0ff0a` — 44 righe`

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
