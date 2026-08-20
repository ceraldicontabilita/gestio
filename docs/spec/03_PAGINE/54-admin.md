# 54 — Admin sistema

## Contratto della schermata

- Route: `/admin`
- Accesso: `admin`
- Modulo: `admin`
- Componente corrente: `frontend/src/pages/Admin.jsx`
- Entrypoint/router: `frontend/src/pages/hub/AdminHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/54-admin.json`](LOGICA_JSON/54-admin.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Admin con salute, job, errori, configurazione non sensibile e azioni protette.

## Fonti e registri letti

- health servizi/provider
- job/run
- errori
- configurazione non sensibile
- audit

## Scritture ed effetti consentiti

- comandi amministrativi protetti
- retry/cancel controllato
- note operative

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Mostrare stato per servizio con timestamp, versione/commit, dipendenze e ultimo errore strutturato.
2. Ogni contatore apre lista di job/errori; retry è selettivo e idempotente.
3. Azioni distruttive o migrazioni mostrano dry-run, target esatti, conferma forte e rollback.

## Automazioni previste

- Refresh health e alert su errori persistenti, senza tempeste di notifiche.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Servizio/job ↔ run ↔ record coinvolti ↔ log/audit e pagina operativa.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Nessun segreto, stack trace sensibile o pulsante inutilizzabile; admin non significa autorizzazione automatica al pagamento.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni stato è datato e verificabile; retry non duplica record e un errore apre il dettaglio utile.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/admin/bank-supplier-rules/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `DELETE /api/admin/rollback/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `DELETE /api/config/email-accounts/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `DELETE /api/config/parole-chiave/rimuovi?categoria={param}&parola={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/bank-supplier-rules` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/dashboard-summary` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/registro-dati/config` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/registro-dati/duplicate-audit` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/registro-dati/jobs/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/registro-dati/manifest` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/rollback/sezioni` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/rollback/{param}/conta` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/admin/stats` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/collaudo/storico?limit=15` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/collaudo/ultimo` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/config/email-accounts` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/config/parole-chiave` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/health` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/prima-nota/cassa/verifica-entrate-corrispettivi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `GET /api/sync/stato-sincronizzazione` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/bank-supplier-rules` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/bank-supplier-rules/reprocess/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/registro-dati/config` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/registro-dati/duplicate-audit-folders` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/registro-dati/duplicate-cleanup-folders` — `admin-only` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/registro-dati/jobs/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/admin/rollback/fatture-import/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/collaudo/esegui` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/config/email-accounts` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/config/email-accounts/{param}/test` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/config/parole-chiave/aggiungi?categoria={param}&parola={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/estratto-conto-movimenti/import` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/prima-nota/cassa/fix-corrispettivi-importo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/sync/match-fatture-banca` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `POST /api/sync/match-fatture-cassa` — `tenere` — sorgente: frontend/src/pages/Admin.jsx
- `PUT /api/config/email-accounts/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Admin.jsx
- `/api/admin/bank-supplier-rules/reprocess/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/admin/bank-supplier-rules/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/admin/registro-dati/jobs/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/admin/rollback` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/admin/rollback/fatture-import/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/admin/rollback/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/admin/rollback/{param}/conta` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/auth/google/callback` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/collaudo/storico` — `tenere` — in uso: FE
- `/api/config/email-accounts/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/config/email-accounts/{param}/test` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `PUT /api/config/parole-chiave` — `tenere` — in uso: FE
- `POST /api/config/parole-chiave/aggiungi` — `tenere` — in uso: FE
- `DELETE /api/config/parole-chiave/rimuovi` — `tenere` — in uso: FE
- `/api/health` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/prima-nota/cassa/fix-corrispettivi-importo` — `tenere` — in uso: FE
- `GET /api/prima-nota/cassa/verifica-entrate-corrispettivi` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `anni`
- `bankCsvText`
- `bankImportResult`
- `bankReprocessResult`
- `bankRule`
- `bankRules`
- `bankRulesLoading`
- `busy`
- `conferma`
- `config`
- `contaRes`
- `contando`
- `dbStatus`
- `driveFolderLinks`
- `duplicateAudit`
- `editKeywordInput`
- `editingAccount`
- `eliminando`
- `emailAccounts`
- `errore`
- `eseguendo`
- `esito`
- `espanso`
- `folder`
- `initialLoad`
- `loading`
- `loadingEmails`
- `manifest`
- `newAccount`
- `newKeyword`
- `newKeywordInput`
- `paroleChiave`
- `periodi`
- `result`
- `secondiEsecuzione`
- `sezioni`
- `showNewForm`
- `showPassword`
- `stats`
- `storico`
- `syncLoading`
- `syncStatus`
- `testingConnection`
- `triggerLoading`
- `ultimo`
- `verificaCorrispettivi`
- `visitedAdmin`
- `visitedElaborazioni`
- `visitedMfa`

### Handler e operazioni

- `handleTabChange`
- `loadBankRules`
- `loadDashboardSummary`
- `loadEmailAccounts`
- `loadParoleChiave`
- `loadStats`
- `loadSyncStatus`
- `saveBankRule`
- `saveConfig`
- `saveEmailAccount`

### Destinazioni di navigazione

- `/admin/${tabId}`
- `/admin/elaborazioni`

### Componenti/import locali

- `../../components/ds`
- `../api`
- `../components/PageLayout`
- `../components/PannelloSumUp`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../hooks/useHashState`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/Admin.jsx — SHA-256 `d71344d2fbac3e33ebfbe80712d4b167d3bc06ed5a55258befaba6f982f72110` — 1788 righe`
- `frontend/src/pages/hub/AdminHub.jsx — SHA-256 `4bcbb943b2ca87e7b91e4928ff69d9cec3225fb0d1c65d20140a52a336bb2cdd` — 63 righe`

## Test collegati

- `frontend/src/contexts/AuthContext.test.jsx`
- `frontend/src/pages/AdminOperationalBoundary.test.jsx`
- `frontend/src/pages/Agenti.test.jsx`
- `frontend/src/pages/Documenti.test.jsx`
- `frontend/src/pages/MFAAdmin.test.jsx`
- `tests/test_bank_supplier_rules.py`
- `tests/test_importa_anno_da_drive.py`
- `tests/test_mfa_admin.py`

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
