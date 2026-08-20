# 07 — Fornitori

## Contratto della schermata

- Route: `/fornitori`
- Accesso: `authenticated`
- Modulo: `fornitori`
- Componente corrente: `frontend/src/pages/Fornitori.jsx`
- Entrypoint/router: `frontend/src/pages/hub/FornitoriHub.jsx`
- Mappa macchina: [`MAPPE_JSON/fornitori.json`](MAPPE_JSON/fornitori.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Anagrafica fornitori univoca, fatture, residui, IBAN, metodo e merge controllato.

## Flusso obbligatorio

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/fatture/{param}{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `GET /api/openapi-imprese/info/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `GET /api/suppliers/filtered?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `GET /api/suppliers/search-piva/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `GET /api/suppliers/{param}/fatturato?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `GET /api/suppliers/{param}/fatture${anno?` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `GET /api/suppliers/{param}/fatture?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `POST /api/anagrafica-fornitori/popola-fornitore/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `POST /api/anagrafica-fornitori/popola-tutti` — `tenere` — sorgente: frontend/src/pages/Fornitori.jsx
- `POST /api/fatture-ricevute/paga-manuale` — `tenere` — sorgente: frontend/src/pages/Fornitori.jsx
- `POST /api/suppliers` — `tenere` — sorgente: frontend/src/pages/Fornitori.jsx
- `PUT /api/suppliers/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Fornitori.jsx
- `/api/admin` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/agenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/ai-parser` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/alerts` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/anagrafica-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/anagrafica-fornitori/popola-fornitore/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/archivio-bonifici` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `/api/fatture/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `/api/openapi-imprese/info/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `/api/rapido` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/regole` — `tenere` — in uso: FE
- `GET /api/ritenute` — `tenere` — in uso: FE
- `/api/scadenzario-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/scadenze` — `tenere` — in uso: FE
- `GET /api/settings` — `tenere` — in uso: FE
- `PUT /api/settings` — `tenere` — in uso: FE
- `/api/sumup` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/suppliers` — `tenere` — in uso: FE
- `GET /api/suppliers/filtered` — `tenere` — in uso: FE
- `/api/suppliers/search-piva/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/suppliers/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/tfr` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-noleggio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verbali-riconciliazione` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/verifica-coerenza` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/voci-bilancio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/whatsapp` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `currentSupplier`
- `debouncedValue`
- `estrattoModal`
- `fatturaView`
- `fatturatoModal`
- `filterAnzianita`
- `filterIncomplete`
- `filterSenzaMetodo`
- `filtroProdotto`
- `form`
- `giorniNuovo`
- `loading`
- `loadingFatturato`
- `loadingOpenAPI`
- `loadingXML`
- `menuPosition`
- `modalOpen`
- `mostraCessati`
- `openAPIError`
- `popolandoTutti`
- `saving`
- `searching`
- `showMetodoMenu`
- `suppliers`
- `totaliFiltrati`
- `updating`
- `xmlMsg`

### Handler e operazioni

- `fetchData`
- `handleChange`
- `handleChangeMetodo`
- `handleDelete`
- `handleLoadFromOpenAPI`
- `handleMetodoChange`
- `handlePopolaDaXml`
- `handlePopolaTuttiXml`
- `handleSave`
- `handleSearchPiva`
- `handleShowFatturato`
- `handleSubmit`
- `handleToggleCessato`
- `handleToggleEsclude`
- `handleViewInvoices`
- `handleViewInvoicesModal`
- `openMenu`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../api`
- `../components/CopyLinkButton`
- `../components/ModalFattura`
- `../components/PageLayout`
- `../components/Portal`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../domain/suppliers`
- `../hooks/useHashState`

## Fonti tecniche verificate

- `frontend/src/pages/Fornitori.jsx — SHA-256 `fdd340ea57ad99b354fd0cd0b61f1ce8e65381a0b3f328e3ead328d643f54ab7` — 3599 righe`
- `frontend/src/pages/hub/FornitoriHub.jsx — SHA-256 `2c55e4cb57ff951fe6459210c4c3907a08fd23a547602e38f989ed34a5b77075` — 13 righe`

## Test collegati

- `frontend/src/pages/Fornitori.compact.test.jsx`
- `tests/test_anagrafica_fornitori_xml_bulk.py`
- `tests/test_assegni_fornitori_esclusi.py`
- `tests/test_bank_evidence_operativa.py`
- `tests/test_export_commercialista_completo.py`
- `tests/test_import_ec_non_riversa_in_prima_nota.py`
- `tests/test_mappa_categoria_estratto_conto.py`
- `tests/test_p1_fornitori.py`
- `tests/test_p1_mapping_piano_conti.py`
- `tests/test_prima_nota_banca_solo_agganciati.py`
- `tests/test_unifica_categorie_prima_nota.py`

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
