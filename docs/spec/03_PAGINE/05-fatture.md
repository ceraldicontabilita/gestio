# 05 — Archivio fatture

## Contratto della schermata

- Route: `/fatture`
- Accesso: `authenticated`
- Modulo: `fatture`
- Componente corrente: `frontend/src/pages/ArchivioFattureRicevute.jsx`
- Entrypoint/router: `frontend/src/pages/hub/FattureHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/05-fatture.json`](LOGICA_JSON/05-fatture.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Archivio unico fatture ricevute, PDF/XML, provenienza, pagamento e spostamento Cassa/Banca.

## Fonti e registri letti

- Documenti
- Fatture ricevute
- Fornitori
- Relazioni
- Prima Nota e movimenti bancari

## Scritture ed effetti consentiti

- stato e classificazione fattura
- relazioni di pagamento
- eventuale destinazione Cassa/Banca richiesta

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Indicizzare XML/PDF con chiave fattura composta da cedente, numero, data e tipo, conservando l'originale sullo storage file.
2. Mostrare imponibile, IVA esposta, totale, scadenza, residuo, metodo previsto e prove collegate.
3. Segnare pagata solo con relazione confermata a pagamento/prova coerente; altrimenti mostrare prevista, candidata o da verificare.
4. I comandi Cassa/Banca spostano o correggono la scrittura tramite operation_id senza duplicare la fattura.

## Automazioni previste

- Matching certo con banca/PayPal/assegno solo usando identità, centesimi, data e provenienza; aggiornamento residui.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Viewer originale; link bidirezionali a fornitore, Prima Nota, banca, PayPal, assegno e documento.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non dedurre il pagamento dal metodo previsto; non usare l'importo da solo; IVA esposta non equivale a IVA detraibile.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Ogni fattura appare una volta, apre l'originale e mostra la stessa relazione/stato da tutte le pagine collegate.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/assegni/{param}?force={param}` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `DELETE /api/corrispettivi/{param}?force={param}` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `DELETE /api/fatture/{param}?force={param}` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `GET /api/assegni` — `tenere` — sorgente: frontend/src/hooks/useData.js
- `GET /api/corrispettivi?anno={param}&limit=2500` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Corrispettivi.jsx
- `GET /api/corrispettivi?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `GET /api/fatture-ricevute/archivio?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/fatture-ricevute/fattura/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/fatture-ricevute/fattura/{param}/documenti-pagamento` — `verificare contratto dinamico` — sorgente: frontend/src/components/ModalFattura.jsx
- `GET /api/fatture-ricevute/fattura/{param}/xml-originale` — `verificare contratto dinamico` — sorgente: frontend/src/components/ModalFattura.jsx
- `GET /api/fatture-ricevute/fornitori?con_fatture=true&limit=500` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/fatture-ricevute/statistiche{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/invoices?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `GET /api/suppliers?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `POST /api/fatture-ricevute/export-selezione` — `tenere` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `POST /api/prima-nota/sposta-movimento` — `tenere` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `PUT /api/fatture/{param}/paga` — `verificare contratto dinamico` — sorgente: frontend/src/hooks/useData.js
- `/api/admin` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/agenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/ai-parser` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/alerts` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/anagrafica-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/assegni` — `tenere` — in uso: FE
- `/api/assegni/learning` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/assegni/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `/api/corrispettivi/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/dashboard` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/dati-isa` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/dipendenti` — `tenere` — in uso: FE
- `POST /api/dipendenti` — `tenere` — in uso: FE
- `/api/dizionario-articoli` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/document-ai` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-fiscali` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/documenti-inbox` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `GET /api/fatture-estere/da-verificare` — `tenere` — in uso: FE
- `/api/fatture-ricevute` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/fatture-ricevute/archivio` — `tenere` — in uso: FE
- `/api/fatture-ricevute/fattura/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-ricevute/fattura/{param}/documenti-pagamento` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-ricevute/fattura/{param}/view-assoinvoice` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture-ricevute/fattura/{param}/xml-originale` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/fatture-ricevute/fornitori` — `tenere` — in uso: FE
- `POST /api/fatture-ricevute/paga-manuale` — `tenere` — in uso: FE
- `/api/fatture-ricevute/statistiche{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/fatture/{param}/paga` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `GET /api/prima-nota/banca` — `tenere` — in uso: FE
- `POST /api/prima-nota/banca` — `tenere` — in uso: FE
- `/api/prima-nota/banca/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/prima-nota/cassa` — `tenere` — in uso: FE
- `POST /api/prima-nota/cassa` — `tenere` — in uso: FE
- `/api/prima-nota/cassa/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
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

- `assegni`
- `corrispettivi`
- `data`
- `debouncedSearch`
- `debouncedValue`
- `dialog`
- `documentiPagamento`
- `err`
- `error`
- `exportInCorso`
- `fatturaView`
- `fatture`
- `fornitori`
- `highlightedId`
- `invoiceNotFoundWarning`
- `isMobile`
- `loading`
- `message`
- `movimenti`
- `pagamentoSelezionato`
- `pagina`
- `ricercaFornitore`
- `saldi`
- `selezionate`
- `spostamentoInCorso`
- `statistiche`
- `stats`
- `visitedArchivio`
- `visitedCorresp`

### Handler e operazioni

- `fetchData`
- `fetchFatture`
- `fetchFornitori`
- `fetchStatistiche`
- `handleResize`
- `loadAssegni`
- `loadCorrispettivi`
- `loadFatture`
- `loadFornitori`
- `loadMovimenti`
- `openDetail`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/AssociaAssegnoFattura`
- `../components/CopyLinkButton`
- `../components/ModalFattura`
- `../contexts/AnnoContext`
- `../hooks/useHashState`
- `./DocumentViewerModal`

## Fonti tecniche verificate

- `frontend/src/components/ModalFattura.jsx — SHA-256 `7fcbaf4b27eb2b7f206c334009e2ecccc1e94e6ac84c3420abd04151b13bf21b` — 91 righe`
- `frontend/src/hooks/useData.js — SHA-256 `8c09aca245282be790a82d1850fea9c18f01cbac2fd2061b51e6b6b119646c77` — 522 righe`
- `frontend/src/pages/ArchivioFattureRicevute.jsx — SHA-256 `695118c3d2c163fa167dc9b8c4bfd8b9c40010469a71a3d6b0539340fc25e89d` — 1080 righe`
- `frontend/src/pages/Corrispettivi.jsx — SHA-256 `1bf4341559a2350686d42ac6593c80ac18861825bcb59e3d6950c337667f1ddf` — 430 righe`
- `frontend/src/pages/hub/FattureHub.jsx — SHA-256 `c192e87798860d2d4ed123eda8aa798266d32c8b7f9d94c927aedfcd40d10547` — 56 righe`

## Test collegati

- `frontend/src/pages/ArchivioFattureRicevute.test.jsx`

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
