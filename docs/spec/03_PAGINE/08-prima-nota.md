# 08 — Prima Nota

## Contratto della schermata

- Route: `/prima-nota`
- Accesso: `authenticated`
- Modulo: `prima-nota`
- Componente corrente: `frontend/src/pages/PrimaNota.jsx`
- Entrypoint/router: `frontend/src/pages/hub/PrimaNotaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/08-prima-nota.json`](LOGICA_JSON/08-prima-nota.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Prima Nota Cassa/Banca/SumUp/Soci come viste coerenti del ledger, raggruppate per giorno.

## Fonti e registri letti

- Prima Nota Cassa
- Prima Nota Banca
- SumUp/POS
- finanziamenti soci
- fatture e movimenti bancari

## Scritture ed effetti consentiti

- scritture tramite writer unico
- trasferimenti Cassa-Banca
- relazioni e correzioni tracciate

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Mostrare Cassa, Banca, SumUp e Soci come conti distinti dello stesso ledger, raggruppando tutte le operazioni in card giornaliere.
2. Calcolare saldi progressivi dal riporto iniziale e dalle righe ordinate; ogni giorno espone numero operazioni e totale netto.
3. Un versamento contanti crea uscita Cassa ed entrata Banca attesa con lo stesso operation_id; il movimento di estratto conto la riconcilia senza crearne una terza.
4. Le vendite POS generano crediti attesi; accredito provider, commissione e movimento banca restano fatti separati ma collegati.
5. Spostare una fattura tra Cassa e Banca corregge la scrittura esistente, conserva audit e aggiorna tutte le viste.

## Automazioni previste

- Import estratto conto idempotente; generazione automatica di attesi POS/versamenti; associazioni certe e coda dei dubbi.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Ogni riga apre fattura/documento/prova; operation_id consente di passare tra Cassa, Banca, SumUp, PayPal e riconciliazione.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non inserire movimenti bancari reali in Cassa; non usare saldi hardcoded; non marcare pagato senza prova coerente.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Saldo per conto ricalcolabile al centesimo; versamento e POS risultano nelle sezioni corrette dopo refresh senza duplicati.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/nexi/stato?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/provvisori?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/sumup?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/{param}?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/attendi-banca` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma-divisione` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma-multipla` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/da-decidere` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/segnala-dubbio` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `PUT /api/prima-nota/saldo-iniziale` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `PUT /api/prima-nota/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/corrispettivi/view-by-filename` — `tenere` — in uso: FE
- `/api/corrispettivi/{param}/view` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/nexi/stato` — `tenere` — in uso: FE
- `GET /api/prima-nota/provvisori` — `tenere` — in uso: FE
- `GET /api/prima-nota/saldo-iniziale` — `tenere` — in uso: FE
- `GET /api/prima-nota/sumup` — `tenere` — in uso: FE
- `/api/prima-nota/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/prima-nota/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `associaFattura`
- `attesaBanca`
- `banca`
- `busy`
- `busyMultiplo`
- `cassa`
- `cerca`
- `completezzaProvvisori`
- `documentView`
- `editing`
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
- `form`
- `importoCassa`
- `loadError`
- `loading`
- `modalitaRapida`
- `nuovo`
- `pagina`
- `paginaDaLavorare`
- `paginaTutte`
- `parziale`
- `provvisori`
- `riportoErr`
- `riportoInput`
- `riportoModal`
- `riportoSaving`
- `saving`
- `selezionate`
- `stato`
- `sumup`
- `tutteFatture`
- `visitedPrimaNota`
- `visitedPulizia`
- `vista`

### Handler e operazioni

Nessuno rilevato staticamente.

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/AssociaAssegnoFattura`
- `../components/AssociaMovimentoBanca`
- `../components/DocumentImportLink`
- `../components/DocumentViewerModal`
- `../components/InAttesaDocumento`
- `../components/ModalFattura`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../hooks/useHashState`
- `../lib/utils`
- `./FinanziamentoSoci`

## Fonti tecniche verificate

- `frontend/src/pages/PrimaNota.jsx — SHA-256 `f80dc2200d66fa126602b6a87aeee77cfdc24764afa23c4ad71dd3c931931cfa` — 2245 righe`
- `frontend/src/pages/hub/PrimaNotaHub.jsx — SHA-256 `daa3325581cd0a60ff90dff5a79782c5acfb0272788a9299eddf00f9c2e0ff0a` — 44 righe`

## Test collegati

- `frontend/src/pages/PrimaNota.test.jsx`
- `tests/test_corrispettivi_pulizia_pos_manuale.py`
- `tests/test_frontend_route_consolidation.py`

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
