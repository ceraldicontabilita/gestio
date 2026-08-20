# 06 — Corrispettivi

## Contratto della schermata

- Route: `/fatture/corrispettivi`
- Accesso: `authenticated`
- Modulo: `fatture`
- Componente corrente: `frontend/src/pages/Corrispettivi.jsx`
- Entrypoint/router: `frontend/src/pages/hub/FattureHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/06-corrispettivi.json`](LOGICA_JSON/06-corrispettivi.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Corrispettivi giornalieri, aliquote, mezzi di pagamento e scritture Cassa/POS senza duplicati.

## Fonti e registri letti

- XML/ZIP corrispettivi
- Corrispettivi
- chiusure POS
- Prima Nota Cassa
- accrediti provider/banca

## Scritture ed effetti consentiti

- giornata corrispettivi deduplicata
- scrittura vendite Cassa
- crediti POS attesi separati

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Validare firma/schema e ricavare data, imponibili, IVA e mezzi di pagamento dalla fonte RT.
2. Creare una giornata canonica per dispositivo/data e ripartire contanti, carte e altri mezzi senza inventare valori mancanti.
3. Registrare vendite/contanti in Cassa e crediti POS attesi come fatti distinti; l'accredito bancario resta prova successiva.
4. Mostrare differenze tra RT, chiusura terminale e accredito con lista delle righe interessate.

## Automazioni previste

- Secondo import identico nuovi=0; sincronizzazione idempotente verso Prima Nota.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Giornata verso documento RT, Prima Nota Cassa, Coerenza POS e accrediti riconciliati.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non trasformare una chiusura POS in vendita aggiuntiva; non confondere importo lordo, netto e commissioni.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Totali aliquote e mezzi quadrano con il documento; una nuova giornata compare automaticamente in Cassa una sola volta.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `GET /api/corrispettivi?anno={param}&limit=2500` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Corrispettivi.jsx
- `GET /api/fatture-ricevute/archivio?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/fatture-ricevute/fattura/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/fatture-ricevute/fornitori?con_fatture=true&limit=500` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/fatture-ricevute/statistiche{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `GET /api/nexi/stato?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/pos-corrispettivi/controllo-due-fasi?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/riepilogo-mensile?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/pos-corrispettivi/verifica-coerenza?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `GET /api/prima-nota/provvisori?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/sumup?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/prima-nota/{param}?{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `GET /api/sumup/riepilogo?anno={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/corrispettivi/manuale` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/fatture-ricevute/export-selezione` — `tenere` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `POST /api/pos-corrispettivi/chiusure-giornaliere/batch` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `POST /api/prima-nota/provvisori/attendi-banca` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma-divisione` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/conferma-multipla` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/da-decidere` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/provvisori/segnala-dubbio` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `POST /api/prima-nota/sposta-movimento` — `tenere` — sorgente: frontend/src/pages/ArchivioFattureRicevute.jsx
- `POST /api/prima-nota/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `PUT /api/pos-corrispettivi/chiusura-giornaliera` — `tenere` — sorgente: frontend/src/pages/CoerenzaPOSCorrispettivi.jsx
- `PUT /api/prima-nota/saldo-iniziale` — `tenere` — sorgente: frontend/src/pages/PrimaNota.jsx
- `PUT /api/prima-nota/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/PrimaNota.jsx
- `/api/admin` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/agenti` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/ai-parser` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/alerts` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/anagrafica-fornitori` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `GET /api/fatture-ricevute/archivio` — `tenere` — in uso: FE
- `/api/fatture-ricevute/fattura/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `GET /api/fatture-ricevute/fornitori` — `tenere` — in uso: FE
- `/api/fatture-ricevute/statistiche{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
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
- `GET /api/pos-corrispettivi/controllo-due-fasi` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/riepilogo-mensile` — `tenere` — in uso: FE
- `GET /api/pos-corrispettivi/verifica-coerenza` — `tenere` — in uso: FE
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
- `GET /api/sumup/riepilogo` — `tenere` — in uso: FE
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

- `associaFattura`
- `attesaBanca`
- `banca`
- `busy`
- `busyMultiplo`
- `cassa`
- `cerca`
- `completezzaProvvisori`
- `corrispettivi`
- `dataForm`
- `dati`
- `debouncedSearch`
- `dettaglioBancaAperto`
- `documentView`
- `dueFasi`
- `editing`
- `err`
- `errore`
- `erroreRiga`
- `esitiMultipli`
- `esito`
- `espansa`
- `exportInCorso`
- `fCategoria`
- `fDataFattura`
- `fFornitore`
- `fNumeroDdt`
- `fNumeroFattura`
- `fTipo`
- `fatturaView`
- `fatture`
- `filtroStato`
- `form`
- `fornitori`
- `highlightedId`
- `importAperto`
- `importoCassa`
- `importoSalvato`
- `invoiceNotFoundWarning`
- `loadError`
- `loading`
- `modalAperta`
- `modalitaRapida`
- `note`
- `nuovo`
- `pagina`
- `paginaDaLavorare`
- `paginaTutte`
- `parziale`
- `posReale`
- `provvisori`
- `ricercaFornitore`
- `riepilogoMensile`
- `riportoErr`
- `riportoInput`
- `riportoModal`
- `riportoSaving`
- `salvando`
- `saving`
- `selezionate`
- `spostamentoInCorso`
- `statistiche`
- `stato`
- `sumup`
- `tab`
- `testo`
- `totale`
- `tutteFatture`
- `valore`
- `visitedArchivio`
- `visitedCorresp`
- `vista`

### Handler e operazioni

- `fetchFatture`
- `fetchFornitori`
- `fetchStatistiche`
- `loadCorrispettivi`
- `loadDati`
- `openDetail`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

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
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../hooks/useHashState`
- `../lib/utils`
- `./FinanziamentoSoci`

## Fonti tecniche verificate

- `frontend/src/pages/ArchivioFattureRicevute.jsx — SHA-256 `695118c3d2c163fa167dc9b8c4bfd8b9c40010469a71a3d6b0539340fc25e89d` — 1080 righe`
- `frontend/src/pages/CoerenzaPOSCorrispettivi.jsx — SHA-256 `cdc0d4614328f05f04c0ae206fced2f9c672a51b9bca84efd56bd240b81b5aa6` — 1545 righe`
- `frontend/src/pages/Corrispettivi.jsx — SHA-256 `1bf4341559a2350686d42ac6593c80ac18861825bcb59e3d6950c337667f1ddf` — 430 righe`
- `frontend/src/pages/PrimaNota.jsx — SHA-256 `f80dc2200d66fa126602b6a87aeee77cfdc24764afa23c4ad71dd3c931931cfa` — 2245 righe`
- `frontend/src/pages/hub/FattureHub.jsx — SHA-256 `c192e87798860d2d4ed123eda8aa798266d32c8b7f9d94c927aedfcd40d10547` — 56 righe`

## Test collegati

- `frontend/src/pages/CoerenzaPOSCorrispettivi.test.jsx`
- `frontend/src/pages/ControlloMensile.test.jsx`
- `frontend/src/pages/ImportDocumenti.test.jsx`
- `tests/test_audit_iva_corrispettivi_paypal.py`
- `tests/test_bonifica_pos_xml.py`
- `tests/test_concorrenza_registra_corrispettivo.py`
- `tests/test_corrispettivi_dedup_per_dispositivo.py`
- `tests/test_corrispettivi_duplicate_repairs_prima_nota.py`
- `tests/test_corrispettivi_idempotenza_writer.py`
- `tests/test_corrispettivi_prima_nota_regola_contabile.py`
- `tests/test_corrispettivi_pulizia_pos_manuale.py`
- `tests/test_corrispettivi_service_prima_nota_unificata.py`
- `tests/test_documenti_upload_corrispettivo_duplicato.py`
- `tests/test_export_commercialista_completo.py`
- `tests/test_finanziaria_semantica.py`
- `tests/test_motore_unico_scritture.py`
- `tests/test_p1_cash_adapter.py`
- `tests/test_p1_saldo_prima_nota.py`
- `tests/test_pos_multi_gestore.py`
- `tests/test_pos_reale_manuale_prima_nota.py`
- `tests/test_rebuild_prima_nota_purge_completo.py`
- `tests/test_rebuild_prima_nota_senza_campo_totale.py`
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
