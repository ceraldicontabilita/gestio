# 12 — Verbali noleggio

## Contratto della schermata

- Route: `/noleggio/verbali`
- Accesso: `authenticated`
- Modulo: `noleggio`
- Componente corrente: `frontend/src/pages/VerbaliRiconciliazione.jsx`
- Entrypoint/router: `frontend/src/pages/hub/VeicoliHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/12-noleggio-verbali.json`](LOGICA_JSON/12-noleggio-verbali.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Riconciliazione verbali, veicoli, driver, pagamenti, quietanze e documenti.

## Fonti e registri letti

- Verbali PartenoPay/Gmail
- veicoli
- storico driver
- pagamenti
- quietanze

## Scritture ed effetti consentiti

- verbale canonico
- associazione veicolo/driver
- stato pagamento
- attesa quietanza

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Importare e leggere il PDF originale, estraendo numero, data/ora infrazione, targa, ente, trasgressore, scadenza e importo esatto.
2. Associare automaticamente il veicolo per targa e il driver solo se l'assegnazione copre data/ora del verbale; altrimenti mostrare candidati.
3. Accettare Ceraldi Group S.r.l. come trasgressore quando risulta dal documento, senza inventare un driver.
4. Dopo prova di pagamento usare PAGATO - ATTESA QUIETANZA; collegare la quietanza quando arriva e mantenere distinta la prova bancaria.

## Automazioni previste

- Controllo Gmail giornaliero idempotente e promemoria su scadenze/quietanze mancanti.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Verbale ↔ PDF ↔ targa ↔ driver storico ↔ pagamento ↔ quietanza ↔ movimento banca.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Mai associare driver per importo; mai chiamare fattura la quietanza; originali Gmail e file non vengono spostati o eliminati.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Importo mostrato coincide col PDF; casi certi si completano da soli, ambigui restano nella lista con candidati e motivo.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/dipendenti` — `tenere` — sorgente: frontend/src/pages/DettaglioVerbale.jsx, frontend/src/pages/VerbaliRiconciliazione.jsx
- `GET /api/verbali-noleggio/dettaglio/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `GET /api/verbali-noleggio/pdf/{param}?indice={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `GET /api/verbali-riconciliazione/dashboard` — `tenere` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/auto-repair/collega-targa-driver?targa={param}&driver_id={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-noleggio/associa-pdf/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/correggi-importo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/correggi-trasgressore/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-noleggio/ricalcola-pdf/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/DettaglioVerbale.jsx
- `POST /api/verbali-riconciliazione/collega-driver-massivo` — `tenere` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/migra-attesa-quietanza` — `admin-only` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/pulisci-duplicati?dry_run=false` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/pulisci-duplicati?dry_run=true` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/riconcilia/{param}?dry_run=false` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/riconcilia/{param}?dry_run=true` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/scan-email?days_back=30` — `verificare contratto dinamico` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/verbali-riconciliazione/scan-fatture-verbali` — `tenere` — sorgente: frontend/src/pages/VerbaliRiconciliazione.jsx
- `POST /api/auto-repair/collega-targa-driver` — `tenere` — in uso: FE, scheduler
- `POST /api/auto-repair/inferisci-targa-driver-da-fatture` — `tenere` — in uso: FE, scheduler
- `POST /api/dipendenti` — `tenere` — in uso: FE
- `GET /api/noleggio/export-pdf-costi` — `tenere` — in uso: FE
- `GET /api/noleggio/veicoli` — `tenere` — in uso: FE
- `POST /api/noleggio/veicoli` — `tenere` — in uso: FE
- `/api/verbali-noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/associa-pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/correggi-importo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/correggi-trasgressore/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/dettaglio/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio/ricalcola-pdf/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/verbali-riconciliazione/lista` — `tenere` — in uso: FE, scheduler
- `POST /api/verbali-riconciliazione/pulisci-duplicati` — `tenere` — in uso: FE, scheduler
- `/api/verbali-riconciliazione/riconcilia/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/verbali-riconciliazione/scan-email` — `tenere` — in uso: FE, scheduler

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `associating`
- `checkingEmail`
- `collegandoDriver`
- `correctedAmount`
- `dashboard`
- `dipendenti`
- `drivers`
- `error`
- `filtroStato`
- `filtroTarga`
- `linkingDriver`
- `loadedTabs`
- `loading`
- `migratingQuietanze`
- `openingPdf`
- `ordinamento`
- `pdfUploading`
- `pdfViewer`
- `pulendoDuplicati`
- `recalculating`
- `savingAmount`
- `savingTrasgressore`
- `scanning`
- `selectedDriver`
- `selectedDriverId`
- `selectedTargaForAssoc`
- `selectedVerbale`
- `showAssociaModal`
- `soloRiconciliare`
- `successMsg`
- `trasgressore`
- `verbale`
- `verbali`

### Handler e operazioni

- `handleAssociaTargaDriver`
- `handleCheckEmail`
- `handleCollegaDriver`
- `handleMigraQuietanze`
- `handlePulisciDuplicati`
- `handleRiconcilia`
- `handleScanFatture`
- `handleTabChange`
- `loadDashboard`
- `loadDipendenti`
- `loadVerbali`
- `openPdf`
- `saveCorrectedAmount`
- `saveTrasgressore`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/DocumentViewerModal`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/DettaglioVerbale.jsx — SHA-256 `89e12f9b5ab69485c880045158443f292f1ada74882a9aedbd04ad01c2e47354` — 380 righe`
- `frontend/src/pages/VerbaliRiconciliazione.jsx — SHA-256 `718794d95fce5f908b363dad8d36e0de77f478a5eb0a8bc570e03472ea827c78` — 1001 righe`
- `frontend/src/pages/hub/VeicoliHub.jsx — SHA-256 `95227192a674b44ceaf89aa5577292c55e8762af00a9cf7a500ff96a707c2ba7` — 373 righe`

## Test collegati

- `frontend/src/pages/VerbaliRiconciliazione.safety.test.jsx`

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
