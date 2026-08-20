# 16 — Bilancio

## Contratto della schermata

- Route: `/contabilita/bilancio`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/Bilancio.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/16-contabilita-bilancio.json`](LOGICA_JSON/16-contabilita-bilancio.json)
- Stato della prova corrente: `in_review`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Bilancio calcolato da scritture valide, quadratura e drill-down.

## Fonti e registri letti

- scritture giornale valide
- piano dei conti
- periodo/anno globale

## Scritture ed effetti consentiti

- Nessuna scrittura primaria; eventuale snapshot firmato solo come report.

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Calcolare Stato patrimoniale e Conto economico dalle righe bilanciate e dai conti validi nel periodo.
2. Mostrare saldi iniziali, movimenti, saldi finali e quadratura Dare/Avere con formule esplicite.
3. Ogni riga consente drill-down al conto, alla scrittura e al documento origine.

## Automazioni previste

- Ricalcolo read-only quando cambiano scritture aperte; periodi chiusi usano la versione approvata.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Bilancio ↔ piano conti ↔ giornale ↔ documento/prova origine.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Non usare totali Prima Nota non contabilizzati come bilancio; errore fonte non diventa zero.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Dare uguale Avere e utile/perdita riconciliabile al centesimo con il giornale.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/voci-bilancio/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Bilancio.jsx
- `GET /api/bilancio/conto-economico?anno={param}${mese?` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Bilancio.jsx
- `GET /api/bilancio/stato-patrimoniale?anno={param}${mese?` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Bilancio.jsx
- `GET /api/cespiti/calcolo-rateo/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Bilancio.jsx
- `GET /api/voci-bilancio/codici-disponibili` — `tenere` — sorgente: frontend/src/pages/Bilancio.jsx
- `GET /api/voci-bilancio/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/Bilancio.jsx
- `POST /api/voci-bilancio/` — `tenere` — sorgente: frontend/src/pages/Bilancio.jsx
- `GET /api/bilancio/conto-economico` — `tenere` — in uso: FE
- `GET /api/bilancio/stato-patrimoniale` — `tenere` — in uso: FE
- `/api/cespiti/calcolo-rateo/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/voci-bilancio` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/voci-bilancio/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `codiciDisponibili`
- `contoEconomico`
- `error`
- `loading`
- `mese`
- `nuovaVoce`
- `rateoAmmortamenti`
- `statoPatrimoniale`
- `visitedTabs`
- `vociBilancio`

### Handler e operazioni

- `handleEliminaVoce`
- `handleSalvaVoce`
- `handleTabChange`
- `loadBilancio`
- `loadRateoAmmortamenti`
- `loadVociBilancio`

### Destinazioni di navigazione

- `/contabilita/bilancio/${tabId}`

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/Bilancio.jsx — SHA-256 `9186c714d461fcecb48fa89bedf9cf15ce0b86c8cee971f3ca031a402285f28b` — 817 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

- `frontend/src/pages/Bilancio.test.jsx`
- `frontend/src/pages/BilancioVerifica.test.jsx`
- `tests/test_bilancio_export_coerenza.py`
- `tests/test_categorizzazione_carburante_deducibilita.py`
- `tests/test_voci_bilancio_manuali.py`

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
