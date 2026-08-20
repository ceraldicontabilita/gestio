# 29 — Learning Machine

## Contratto della schermata

- Route: `/learning-machine`
- Accesso: `authenticated`
- Modulo: `strumenti`
- Componente corrente: `frontend/src/pages/LearningMachine.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Contratto logico macchina: [`LOGICA_JSON/29-learning-machine.json`](LOGICA_JSON/29-learning-machine.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Suggerimenti di apprendimento con evidenza, confidenza, approvazione e revoca.

## Fonti e registri letti

- casi riconciliati e rifiutati
- regole approvate
- feature/provenienza del suggerimento

## Scritture ed effetti consentiti

- suggerimento, confidenza, approvazione/revoca e versione regola

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Generare suggerimenti spiegando segnali, esempi, perimetro e confidenza.
2. L'utente approva, rifiuta o limita la regola; l'approvazione non modifica retroattivamente record già chiusi.
3. Ogni applicazione futura registra regola/versione e resta revocabile o correggibile.

## Automazioni previste

- Training solo su decisioni confermate e dati minimizzati; monitoraggio falsi positivi.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Suggerimento ↔ esempi origine ↔ regola ↔ record sui quali è stata applicata.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessun auto-apprendimento da associazioni ambigue; nessuna regola opaca o pagamento automatico.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Regola approvata applicata solo nel perimetro; revoca impedisce nuove applicazioni e mantiene audit storico.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/fornitori-learning/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LearningMachine.jsx
- `DELETE /api/regole/elimina/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/RegoleCategorizzazione.jsx
- `GET /api/assegni/learning/stats-avanzate` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/fornitori-learning/centri-costo-disponibili` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/fornitori-learning/lista` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/fornitori-learning/non-classificati?limit=100` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/fornitori-learning/stats` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/fornitori-learning/suggerisci-keywords/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/learning-machine/dashboard` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/learning-machine/regole-apprese` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `GET /api/learning-universal/results` — `tenere` — sorgente: frontend/src/pages/LearningMachineUniversale.jsx
- `GET /api/learning-universal/status` — `tenere` — sorgente: frontend/src/pages/LearningMachineUniversale.jsx
- `GET /api/regole` — `tenere` — sorgente: frontend/src/pages/RegoleCategorizzazione.jsx
- `GET /api/regole/download-regole` — `tenere` — sorgente: frontend/src/pages/RegoleCategorizzazione.jsx
- `POST /api/assegni/learning/associa-intelligente` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/assegni/learning/learn` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/assegni/learning/pulizia-duplicati?dry_run={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/contabilita/ricategorizza-fatture` — `tenere` — sorgente: frontend/src/pages/RegoleCategorizzazione.jsx
- `POST /api/fornitori-learning/classifica-ai` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/fornitori-learning/classifica-da-contenuto` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/fornitori-learning/riclassifica-con-keywords` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/fornitori-learning/salva` — `tenere` — sorgente: frontend/src/pages/LearningMachine.jsx
- `POST /api/learning-universal/train/all` — `tenere` — sorgente: frontend/src/pages/LearningMachineUniversale.jsx
- `POST /api/regole/fornitore` — `tenere` — sorgente: frontend/src/pages/RegoleCategorizzazione.jsx
- `POST /api/regole/upload-regole` — `tenere` — sorgente: frontend/src/pages/RegoleCategorizzazione.jsx
- `POST /api/assegni/learning/pulizia-duplicati` — `admin-only` — endpoint di migrazione/manutenzione one-shot: tenere ma Admin-only, disabilitabile, documentato, non esposto a lungo (§7)
- `GET /api/fornitori-learning/non-classificati` — `tenere` — in uso: FE
- `/api/fornitori-learning/suggerisci-keywords/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fornitori-learning/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/regole/elimina/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `assegniLoading`
- `assegniStats`
- `centriCosto`
- `centriCostoAmmessi`
- `dashboardLoading`
- `dashboardStats`
- `documentiLoading`
- `documentiStats`
- `editingCategoria`
- `error`
- `fornitoriConfigurati`
- `fornitoriLoading`
- `fornitoriNonClassificati`
- `keywords`
- `keywordsSuggerite`
- `learningResult`
- `loading`
- `message`
- `newRule`
- `puliziaResult`
- `regole`
- `regoleApprese`
- `results`
- `ricategorizzando`
- `saving`
- `searchTerm`
- `selectedFornitore`
- `showAddForm`
- `status`
- `training`
- `uploading`

### Handler e operazioni

- `fetchRegole`
- `handleAddRule`
- `handleAssociaIntelligente`
- `handleDeleteRule`
- `handleDownloadExcel`
- `handleLearnAssegni`
- `handlePuliziaDuplicati`
- `handleRicategorizza`
- `handleUploadExcel`
- `loadAssegniStats`
- `loadDashboardStats`
- `loadData`
- `loadDocumentiStats`
- `loadFornitoriData`

### Destinazioni di navigazione

- `/documenti`
- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/DocumentImportLink`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
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
- `frontend/src/pages/LearningMachine.jsx — SHA-256 `1ccc3fb01eb06a5b1b4aaec1640b098ba9c2bccd977208b9f072fbf671e98475` — 1519 righe`
- `frontend/src/pages/LearningMachineUniversale.jsx — SHA-256 `389ea1247adcaf934394262e658e8b54a7fd50f84547c521fe38b706a222a13a` — 390 righe`
- `frontend/src/pages/RegoleCategorizzazione.jsx — SHA-256 `eba47420fec37efbc088739c12e5d336351c6df983bd7b41075b4c1af5b4e6eb` — 678 righe`

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
