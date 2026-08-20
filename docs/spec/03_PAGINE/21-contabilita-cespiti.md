# 21 — Cespiti

## Contratto della schermata

- Route: `/contabilita/cespiti`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/GestioneCespiti.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/21-contabilita-cespiti.json`](LOGICA_JSON/21-contabilita-cespiti.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Cespiti, documento origine, ammortamenti Decimal, dismissioni e storia.

## Fonti e registri letti

- fatture cespitabili
- cespiti
- categorie e aliquote
- documenti origine

## Scritture ed effetti consentiti

- scheda cespite
- piano ammortamento
- dismissione
- scritture collegate

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Proporre cespiti da fatture con criteri espliciti; l'utente conferma categoria, data entrata in funzione e quota detraibile.
2. Calcolare ammortamenti con Decimal, pro-rata e versione delle regole, mostrando piano completo.
3. Registrazione e dismissione generano eventi contabili tramite writer unico e conservano documento/fonte.

## Automazioni previste

- Scansione nuove fatture idempotente e verifica annuale tra piano e scritture.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Cespite ↔ fattura/PDF ↔ piano rate ↔ scritture giornale ↔ bilancio.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non capitalizzare automaticamente per parola/importo; non modificare rate di esercizi chiusi senza rettifica.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Costo storico, fondo, quota e residuo quadrano al centesimo; ogni cespite ha documento e data di entrata in funzione.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/cespiti/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `GET /api/cespiti/calcolo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `GET /api/tfr/situazione/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `POST /api/cespiti/` — `tenere` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `POST /api/cespiti/registra/{param}?conferma=true` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `POST /api/cespiti/scan-fatture?soglia_valore=200&dry_run=false` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `POST /api/cespiti/scan-fatture?soglia_valore=200&dry_run=true` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `PUT /api/cespiti/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/GestioneCespiti.jsx
- `/api/cespiti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/cespiti/calcolo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/cespiti/categorie` — `tenere` — in uso: FE
- `/api/cespiti/registra/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/cespiti/riepilogo` — `tenere` — in uso: FE
- `POST /api/cespiti/scan-fatture` — `tenere` — in uso: FE
- `/api/cespiti/verifica/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/cespiti/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/scadenzario-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/scadenzario-fornitori/urgenti` — `tenere` — in uso: FE
- `GET /api/tfr/riepilogo-aziendale` — `tenere` — in uso: FE
- `/api/tfr/situazione/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `categorie`
- `cespiti`
- `editData`
- `editingCespite`
- `error`
- `errorePagina`
- `loading`
- `nuovoCespite`
- `registroTFRAperto`
- `registroTFRDettaglio`
- `registroTFRLoading`
- `riepilogoCespiti`
- `riepilogoTFR`
- `scadenzario`
- `showForm`
- `urgenti`
- `verificaAmmortamenti`
- `visitedTabs`

### Handler e operazioni

- `handleCalcolaAmm`
- `handleCancelEdit`
- `handleCreaCespite`
- `handleDeleteCespite`
- `handleEditCespite`
- `handleSaveEdit`
- `handleScanFatture`
- `handleTabChange`
- `loadCategorie`
- `loadCespiti`
- `loadScadenzario`
- `loadTFR`

### Destinazioni di navigazione

- `/contabilita/cespiti/${tabId}`

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ui/ConfirmDialog`
- `../components/ui/button`
- `../components/ui/input`
- `../components/ui/tabs`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/GestioneCespiti.jsx — SHA-256 `bfc573ec1e4081880c5c6a79982e3bda7edf005211d05ac585fcb99a57398bf8` — 1141 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/GestioneCespiti.test.jsx`
- `tests/test_bilancio_immobilizzazioni_e_fondo_tfr.py`

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
