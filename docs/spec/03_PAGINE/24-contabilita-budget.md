# 24 — Budget

## Contratto della schermata

- Route: `/contabilita/budget`
- Accesso: `authenticated`
- Modulo: `contabilita`
- Componente corrente: `frontend/src/pages/BudgetPrevisionale.jsx`
- Entrypoint/router: `frontend/src/pages/hub/ContabilitaHub.jsx`
- Contratto logico macchina: [`LOGICA_JSON/24-contabilita-budget.json`](LOGICA_JSON/24-contabilita-budget.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Budget versionato e confronto consuntivo per mese, conto e centro.

## Fonti e registri letti

- budget versionato
- piano conti/centri
- consuntivo giornale
- anno globale

## Scritture ed effetti consentiti

- versione budget, righe mensili, note e stato approvazione

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Creare scenari separati per anno/versione senza sovrascrivere quello approvato.
2. Inserire importi per mese, conto/voce e centro; mostrare totale e controlli di coerenza.
3. Confrontare consuntivo omogeneo con budget e aprire il dettaglio dello scostamento.

## Automazioni previste

- Duplicazione anno crea una bozza distinta e conserva provenienza/versione.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Budget ↔ conto/centro ↔ consuntivo giornale ↔ utile obiettivo/previsioni.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Budget e simulazioni non generano scritture reali; una versione approvata non si modifica in silenzio.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Totali mensili/annuali coerenti e scostamento uguale a consuntivo meno budget al centesimo.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/contabilita-gestionale/budget/{param}/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/BudgetPrevisionale.jsx
- `GET /api/contabilita-gestionale/budget-vs-consuntivo/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/BudgetPrevisionale.jsx
- `GET /api/contabilita-gestionale/budget/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/BudgetPrevisionale.jsx
- `POST /api/contabilita-gestionale/budget` — `tenere` — sorgente: frontend/src/pages/BudgetPrevisionale.jsx
- `POST /api/contabilita-gestionale/budget/duplica/{param}/{param}?variazione_pct={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/BudgetPrevisionale.jsx
- `/api/contabilita-gestionale/budget-vs-consuntivo/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita-gestionale/budget/duplica/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita-gestionale/budget/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `/api/contabilita-gestionale/budget/{param}/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare

## Stato e azioni UI rilevati

### Stato locale

- `activeTab`
- `annoDestinazione`
- `budget`
- `confronto`
- `editingVoce`
- `error`
- `formCategoria`
- `formImporto`
- `formMensili`
- `formNote`
- `formVoce`
- `loading`
- `meseConfronto`
- `saving`
- `showDuplica`
- `showForm`
- `variazionePct`
- `visitedTabs`

### Handler e operazioni

- `handleDelete`
- `handleDuplica`
- `handleMeseChange`
- `handleSave`
- `handleTabChange`
- `loadAll`
- `loadConfronto`

### Destinazioni di navigazione

Nessuno rilevato staticamente.

### Componenti/import locali

- `../../components/ds`
- `../../contexts/AnnoContext`
- `../api`
- `../components/PageLayout`
- `../components/ui/ConfirmDialog`
- `../contexts/AnnoContext`
- `../lib/utils`

## Fonti tecniche verificate

- `frontend/src/pages/BudgetPrevisionale.jsx — SHA-256 `71b811d31681c8c28ed172bfd7eec328f64e85e578c586fb84d12b602035a4d3` — 1032 righe`
- `frontend/src/pages/hub/ContabilitaHub.jsx — SHA-256 `197c8673b46d7a8dd853768cedab5845d5e3231c64441df399821e96639282f0` — 194 righe`

## Test collegati

Nessun test nominale rilevato: nella riscrittura aggiungere test unitario, integrazione e browser E2E.

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
