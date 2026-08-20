# 65 — Situazione fiscale

## Contratto della schermata

- Route: `/situazione-fiscale`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/SituazioneFiscale.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Contratto logico macchina: [`LOGICA_JSON/65-situazione-fiscale.json`](LOGICA_JSON/65-situazione-fiscale.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Situazione fiscale unificata con F24, dichiarazioni, quietanze e anomalie.

## Fonti e registri letti

- F24/righe tributo
- dichiarazioni
- quietanze
- movimenti banca
- scadenze/anomalie
- indice documentale (database applicativo)

## Scritture ed effetti consentiti

- Nessuna scrittura fiscale primaria; note/stato verifica e relazioni tramite servizi di dominio

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Costruire quadro per anno/tributo da fonti distinte, indicando presenza e stato di F24, dichiarazione, quietanza e banca.
2. Mostrare totali solo quando semanticamente sommabili e permettere drill-down fino a riga tributo e PDF.
3. Evidenziare documenti mancanti, crediti, differenze e relazioni ambigue con liste navigabili.
4. Dichiarare la freschezza dell'indice e non nascondere una fonte indisponibile dietro uno zero.

## Automazioni previste

- Aggiornamento derivato dopo indicizzazione/import/riconciliazione e notifiche su anomalie persistenti.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Tributo ↔ F24/PDF ↔ dichiarazione ↔ quietanza ↔ banca ↔ scadenza e documento (storage file).

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- F24, dichiarazione, quietanza e pagamento bancario non sono intercambiabili; nessuna associazione per importo solo.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ricerca per anno/codice raggiunge tutte le prove; ogni anomalia ha lista e tutte le somme quadrano alle righe origine.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/documenti/indice/index/document/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `GET /api/fiscal/documents/{param}/content` — `verificare contratto dinamico` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `GET /api/fiscal/review` — `tenere` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `GET /api/fiscal/summary` — `tenere` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `POST /api/documenti-fiscali/upload` — `tenere` — sorgente: frontend/src/pages/SituazioneFiscale.jsx
- `/api/documenti/indice/index/document/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/documenti/tax-codes` — `tenere` — in uso: FE
- `GET /api/fiscal/ader-snapshots` — `tenere` — in uso: FE
- `GET /api/fiscal/collections` — `tenere` — in uso: FE
- `GET /api/fiscal/crosswalk` — `tenere` — in uso: FE
- `GET /api/fiscal/declarations` — `tenere` — in uso: FE
- `/api/fiscal/documents/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/fiscal/dossier.pdf` — `tenere` — in uso: FE
- `GET /api/fiscal/evidence-package.zip` — `tenere` — in uso: FE
- `GET /api/fiscal/f24-rows` — `tenere` — in uso: FE
- `GET /api/fiscal/obligations` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `aderRelated`
- `declarationType`
- `declarationYear`
- `f24CreditsOnly`
- `f24TaxCode`
- `f24Year`
- `items`
- `loading`
- `review`
- `selected`
- `summary`
- `tabMeta`
- `tabSources`
- `taxCodeContext`
- `taxCodeFilters`
- `taxCodeMeta`
- `taxCodeOptions`
- `taxCodeQuery`
- `taxCodeType`
- `uploadCategory`
- `uploading`

### Handler e operazioni

- `openDocument`
- `openDriveDocument`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/LinkedEvidencePanel`
- `../components/PageLayout`
- `../components/ds`
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
- `frontend/src/pages/SituazioneFiscale.jsx — SHA-256 `ef9a13bfc46548b4fbd540d9e7269b070e8e198220314d3414b4c98c7dffac7e` — 328 righe`

## Test collegati

- `frontend/src/pages/SituazioneFiscale.test.jsx`

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
