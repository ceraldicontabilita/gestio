# 54 — Admin sistema

## Contratto della schermata

- Route: `/admin`
- Accesso: `admin`
- Modulo: `admin`
- Componente corrente: `frontend/src/pages/Admin.jsx`
- Entrypoint/router: `frontend/src/pages/hub/AdminHub.jsx`
- Mappa macchina: [`MAPPE_JSON/admin.json`](MAPPE_JSON/admin.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Admin con salute, job, errori, configurazione non sensibile e azioni protette.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

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
