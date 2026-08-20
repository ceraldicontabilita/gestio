# 37 — Archivio bonifici

## Contratto della schermata

- Route: `/riconciliazione/archivio-bonifici`
- Accesso: `authenticated`
- Modulo: `riconciliazione`
- Componente corrente: `frontend/src/pages/ArchivioBonifici.jsx`
- Entrypoint/router: `frontend/src/pages/hub/RiconciliazioneHub.jsx`
- Mappa macchina: [`MAPPE_JSON/archivio-bonifici.json`](MAPPE_JSON/archivio-bonifici.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Archivio bonifici con CRO/TRN, beneficiario, periodo, descrizione e associazioni persistenti.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/archivio-bonifici/disassocia-fattura/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `DELETE /api/archivio-bonifici/disassocia-salario/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `DELETE /api/archivio-bonifici/transfers/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/fatture-compatibili/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/operazioni-salari/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/riconcilia/task/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/stato-riconciliazione?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/transfers/count?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/transfers/summary?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/archivio-bonifici/transfers?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `GET /api/nexi/stato?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/paypal-api/status` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `GET /api/prima-nota/provvisori?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/sumup?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/{param}?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/archivio-bonifici/associa-fattura?bonifico_id={param}&fattura_id={param}&collection={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `POST /api/archivio-bonifici/associa-salario?bonifico_id={param}&operazione_id={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `POST /api/archivio-bonifici/riconcilia?background=true` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `POST /api/archivio-bonifici/sync-iban-anagrafica` — `tenere` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `POST /api/documenti/upload-auto` — `tenere` — sorgente: frontend/src/pages/ImportDocumenti.jsx
- `POST /api/documenti/upload-auto/preview` — `tenere` — sorgente: frontend/src/pages/ImportDocumenti.jsx
- `POST /api/paypal-api/sync` — `tenere` — sorgente: frontend/src/pages/hub/RiconciliazioneHub.jsx
- `POST /api/prima-nota/provvisori/attendi-banca` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma-divisione` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma-multipla` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/da-decidere` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/segnala-dubbio` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `PUT /api/archivio-bonifici/transfers/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioBonifici.jsx
- `PUT /api/prima-nota/saldo-iniziale` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `PUT /api/prima-nota/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `/api/admin` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/agenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/ai-parser` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/alerts` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/anagrafica-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/archivio-bonifici/associa-fattura` — `tenere` — in uso: FE
- `POST /api/archivio-bonifici/associa-salario` — `tenere` — in uso: FE
- `/api/archivio-bonifici/disassocia-fattura/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici/disassocia-salario/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici/fatture-compatibili/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici/operazioni-salari/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/archivio-bonifici/riconcilia` — `tenere` — in uso: FE
- `/api/archivio-bonifici/riconcilia/task/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/archivio-bonifici/stato-riconciliazione` — `tenere` — in uso: FE
- `GET /api/archivio-bonifici/transfers` — `tenere` — in uso: FE
- `GET /api/archivio-bonifici/transfers/count` — `tenere` — in uso: FE
- `GET /api/archivio-bonifici/transfers/summary` — `tenere` — in uso: FE
- `/api/archivio-bonifici/transfers/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/assegni` — `tenere` — in uso: FE
- `POST /api/assegni` — `tenere` — in uso: FE
- `/api/assegni/learning` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/auth` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/auth/api/auth/verify` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/auth/login` — `tenere` — in uso: FE
- `GET /api/auth/verify` — `tenere` — in uso: FE
- `/api/auto-repair` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/bank-statement` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/batch-reprocess` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/bilancio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/cash` — `tenere` — in uso: FE
- `POST /api/cash` — `tenere` — in uso: FE
- `/api/cedolini` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/centri-costo` — `tenere` — in uso: FE
- `POST /api/centri-costo` — `tenere` — in uso: FE
- `/api/cespiti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/chiusura-esercizio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/collaudo` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/commercialista` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/config` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/config-import` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita-gestionale` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/controllo-gestione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/corrispettivi` — `tenere` — in uso: FE
- `GET /api/corrispettivi/view-by-filename` — `tenere` — in uso: FE
- `/api/corrispettivi/{param}/view` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/dashboard` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/dati-isa` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/dipendenti` — `tenere` — in uso: FE
- `POST /api/dipendenti` — `tenere` — in uso: FE
- `/api/dizionario-articoli` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/document-ai` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-fiscali` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-inbox` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/documenti-inbox/auto-classify` — `tenere` — in uso: FE
- `POST /api/documenti-inbox/import-dipendenti-from-cu` — `tenere` — in uso: FE
- `POST /api/documenti-inbox/import-f24-from-inbox` — `tenere` — in uso: FE
- `/api/documenti-non-associati` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/email-download` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/email-scanner` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/erp/ponte` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/estratto-conto-movimenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/f24` — `tenere` — in uso: FE
- `POST /api/f24` — `tenere` — in uso: FE
- `/api/f24-analisi` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-email` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-email-settings` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-public` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/f24-riconciliazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/f24/quietanze` — `tenere` — in uso: FE
- `/api/fatture` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-estere` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-ricevute` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/finanziamenti-soci` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/finanziaria` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fiscal` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fiscalita` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fornitori-learning` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/gestione-riservata` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/invoices` — `tenere` — in uso: FE
- `GET /api/invoices/emesse` — `tenere` — in uso: FE
- `POST /api/invoices/emesse` — `tenere` — in uso: FE
- `/api/iva` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/learning-machine` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/learning-universal` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/mutui` — `tenere` — in uso: FE
- `/api/nexi` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/nexi/stato` — `tenere` — in uso: FE
- `/api/noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi-automotive` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi-imprese` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/operazioni-da-confermare` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/pagamenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/pagamenti-buoni` — `verificare` — nessun riferimento noto (FE/scheduler/chat/test): verificare prima di deprecare
- `/api/pagopa` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/paypal-api` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/paypal-statements` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/pianificazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/piano-conti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/previsioni-acquisti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/prima-nota` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/prima-nota-salari` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/prima-nota/provvisori` — `tenere` — in uso: FE
- `GET /api/prima-nota/saldo-iniziale` — `tenere` — in uso: FE
- `GET /api/prima-nota/sumup` — `tenere` — in uso: FE
- `/api/prima-nota/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/prima-nota/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/rapido` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/regole` — `tenere` — in uso: FE
- `GET /api/ritenute` — `tenere` — in uso: FE
- `/api/scadenzario-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/scadenze` — `tenere` — in uso: FE
- `GET /api/settings` — `tenere` — in uso: FE
- `PUT /api/settings` — `tenere` — in uso: FE
- `/api/sumup` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/suppliers` — `tenere` — in uso: FE
- `POST /api/suppliers` — `tenere` — in uso: FE
- `/api/tfr` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-riconciliazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verifica-coerenza` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/voci-bilancio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/whatsapp` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `associaDropdown`
- `associaFattura`
- `associaFatturaDropdown`
- `attesaBanca`
- `banca`
- `beneficiarioFilter`
- `busy`
- `busyMultiplo`
- `cassa`
- `cerca`
- `completezzaProvvisori`
- `count`
- `dipendenteIbanMatch`
- `documentView`
- `dragOver`
- `editing`
- `editingNote`
- `errore`
- `erroreRiga`
- `esitiMultipli`
- `esito`
- `fCategoria`
- `fDataFattura`
- `fFornitore`
- `fNumeroDdt`
- `fNumeroFattura`
- `fTipo`
- `fatturaView`
- `fattureCompatibili`
- `files`
- `form`
- `importoCassa`
- `loadError`
- `loading`
- `loadingFatture`
- `loadingOperazioni`
- `modalitaRapida`
- `noteText`
- `nuovo`
- `operazioniCompatibili`
- `ordinanteFilter`
- `pagina`
- `paginaDaLavorare`
- `paginaTutte`
- `parziale`
- `paypalRefreshKey`
- `previewComplete`
- `provvisori`
- `results`
- `riconciliando`
- `riconciliazioneStats`
- `riportoErr`
- `riportoInput`
- `riportoModal`
- `riportoSaving`
- `salaryBlockReason`
- `saving`
- `search`
- `selezionate`
- `stato`
- `summary`
- `sumup`
- `transfers`
- `tutteFatture`
- `uploadProgress`
- `uploading`
- `vista`
- `yearFilter`

### Handler e operazioni

- `handleAssocia`
- `handleAssociaFattura`
- `handleClickOutside`
- `handleDelete`
- `handleDisassocia`
- `handleDisassociaFattura`
- `handleDragLeave`
- `handleDragOver`
- `handleDrop`
- `handleFileSelect`
- `handlePreview`
- `handleReset`
- `handleRiconcilia`
- `handleSaveNote`
- `handleSyncIbanToAnagrafica`
- `handleTabChange`
- `handleUpload`
- `handleZipSelect`
- `loadCount`
- `loadFattureCompatibili`
- `loadOperazioniCompatibili`
- `loadRiconciliazioneStats`
- `loadSummary`
- `loadTransfers`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/AssociaAssegnoFattura`
- `../components/AssociaMovimentoBanca`
- `../components/CopyLinkButton`
- `../components/DocumentImportLink`
- `../components/DocumentViewerModal`
- `../components/InAttesaDocumento`
- `../components/ModalFattura`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../hooks/useHashState`
- `../lib/utils`
- `./App.jsx`
- `./FinanziamentoSoci`
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
- `frontend/src/pages/ArchivioBonifici.jsx — SHA-256 `4f68bf59efba7b553c5683166d244596c0cfacf7c56a8ab6f812e3d967702ff7` — 1499 righe`
- `frontend/src/pages/ImportDocumenti.jsx — SHA-256 `0ccb0cad845be08ed6698e1bc5c192489e36a739ed499d3e7202bcbb796e1617` — 923 righe`
- `frontend/src/pages/PrimaNota.jsx — SHA-256 `f80dc2200d66fa126602b6a87aeee77cfdc24764afa23c4ad71dd3c931931cfa` — 2245 righe`
- `frontend/src/pages/hub/RiconciliazioneHub.jsx — SHA-256 `f8e30156c58abc97b26bf319e79a6ebc2d5023c40b7650e415206602d5ae2ba4` — 129 righe`

## Test collegati

- `frontend/src/pages/ArchivioBonifici.safety.test.jsx`

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
