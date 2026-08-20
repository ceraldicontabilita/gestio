# 11 — Flotta noleggio

## Contratto della schermata

- Route: `/noleggio`
- Accesso: `authenticated`
- Modulo: `noleggio`
- Componente corrente: `frontend/src/pages/NoleggioAuto.jsx`
- Entrypoint/router: `frontend/src/pages/hub/VeicoliHub.jsx`
- Mappa macchina: [`MAPPE_JSON/noleggio-flotta.json`](MAPPE_JSON/noleggio-flotta.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Flotta ricostruita da fatture di noleggio, contratti, targhe e storico driver.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/noleggio/veicoli/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/noleggio/drivers` — `tenere` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/noleggio/fatture-non-associate{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/noleggio/fornitori` — `tenere` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/noleggio/riepilogo-controlli{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/noleggio/veicoli?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/openapi-automotive/info/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `POST /api/noleggio/associa-fornitore` — `tenere` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `POST /api/noleggio/fatture/{param}/associa-veicolo` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `POST /api/openapi-automotive/aggiorna-veicolo` — `tenere` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `PUT /api/noleggio/veicoli/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/NoleggioAuto.jsx
- `GET /api/noleggio/export-pdf-costi` — `tenere` — in uso: FE
- `/api/noleggio/fatture-non-associate{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/noleggio/fatture/{param}/associa-veicolo` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/noleggio/riepilogo-controlli{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/noleggio/veicoli` — `tenere` — in uso: FE
- `POST /api/noleggio/veicoli` — `tenere` — in uso: FE
- `/api/noleggio/veicoli/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/openapi-automotive/info/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `controlli`
- `controlloAperto`
- `drivers`
- `editingVeicolo`
- `err`
- `expandedSection`
- `fatturaInAssociazione`
- `fatturaView`
- `fornitori`
- `loadedTabs`
- `loading`
- `lookupLoading`
- `lookupResult`
- `modalFattureNonAssociate`
- `nuovoVeicolo`
- `selectedVeicolo`
- `showAddVeicolo`
- `statistiche`
- `veicoli`
- `veicoloSceltoPerFattura`

### Handler e operazioni

- `fetchControlli`
- `fetchVeicoli`
- `handleAddVeicolo`
- `handleAssociaFatturaVeicolo`
- `handleDelete`
- `handleLookupVeicolo`
- `handleSaveVeicolo`
- `handleTabChange`
- `handleUpdateFromOpenAPI`
- `openFattureNonAssociate`

### Destinazioni di navigazione

- `/noleggio/verbali`

### Componenti/import locali

- `../../api`
- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/ModalFattura`
- `../components/PageLayout`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`

## Fonti tecniche verificate

- `frontend/src/pages/NoleggioAuto.jsx — SHA-256 `3f465206630df8a78854d324161b40628fe1a22ff23b5b9f271a28aaa4d835e9` — 1926 righe`
- `frontend/src/pages/hub/VeicoliHub.jsx — SHA-256 `95227192a674b44ceaf89aa5577292c55e8762af00a9cf7a500ff96a707c2ba7` — 373 righe`

## Test collegati

- `frontend/src/pages/NoleggioAuto.architecture.test.jsx`

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
