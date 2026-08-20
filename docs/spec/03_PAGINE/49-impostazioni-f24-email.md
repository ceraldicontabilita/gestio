# 49 — Impostazioni F24 email

## Contratto della schermata

- Route: `/impostazioni-f24-email`
- Accesso: `authenticated`
- Modulo: `integrazioni`
- Componente corrente: `frontend/src/pages/ImpostazioniF24Email.jsx`
- Entrypoint/router: `frontend/src/main.jsx`
- Contratto logico macchina: [`LOGICA_JSON/49-impostazioni-f24-email.json`](LOGICA_JSON/49-impostazioni-f24-email.json)
- Stato della prova corrente: `unverified`; una mappa statica o HTTP 200 non sono prova end-to-end.

## Scopo da preservare

Configurazione ingest email F24, query, mittenti, test e ultima scansione.

## Fonti e registri letti

- configurazione query/mittenti F24
- stato connessione Gmail
- ultimo watermark/run

## Scritture ed effetti consentiti

- query e mittenti validati
- configurazione scheduler non segreta

Ogni effetto passa dal servizio/writer canonico del dominio, usa idempotency key
e conserva `canonical_id`, `operation_id`, fonte, attore e audit prima/dopo.

## Logica operativa specifica

1. Configurare ricerca in:anywhere, alias/wrapper PEC e tipi allegato attesi senza esporre credenziali.
2. Testare in sola lettura mostrando messaggi trovati, pagine percorse e potenziali allegati senza importarli.
3. Salvare configurazione versionata e mostrare ultimo run, watermark, nuovi/duplicati/errori.

## Automazioni previste

- Controllo giornaliero Europe/Rome con paginazione, Gmail IDs, SHA-256, lock e retry.

Le automazioni ordinarie non richiedono una plancia di pulsanti. Un errore deve
creare un caso visibile e ripetibile; non deve duplicare dati o mascherarsi da
esito riuscito.

## Collegamenti con le altre pagine

- Configurazione ↔ run Gmail ↔ documenti F24/quietanze importati ↔ audit.

I collegamenti sono reciproci: se A mostra B, B deve mostrare A usando la stessa
`relation_id`/`operation_id` e deve aprire il record esatto, non una ricerca generica.

## Divieti e protezioni specifiche

- Mai spostare/eliminare/segnare lette le email; nessuna password/token restituita alla UI.

## Regole comuni obbligatorie

1. Caricare identità, autorizzazioni e anno globale prima dei dati di dominio.
2. Leggere i registri sul database applicativo tramite servizi/API canonici; mai interrogare file o archivi paralleli dalla UI.
3. Mostrare caricamento, errore reale, vuoto utile e dati popolati senza trasformare errori in zero.
4. Eseguire azioni idempotenti; le associazioni certe sono automatiche, quelle ambigue mostrano candidati e motivazione.
5. Aggiornare tutte le viste collegate tramite `operation_id`/relazioni e rendere la navigazione bidirezionale.
6. Conservare fonte, hash, identificatore esterno, timestamp e stato di ogni prova.

## Criteri specifici di completamento

- Test trova gli stessi messaggi della query completa; secondo run senza novità importa zero allegati.

Questi criteri vanno provati con test unitari, integrazione e almeno un percorso
browser end-to-end basato su fixture documentali verificabili.

## API rilevate dalla pagina e dalle sue mappe

- `DELETE /api/f24-email-settings/rimuovi-mittente/{param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `GET /api/f24-email-settings/impostazioni` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `GET /api/f24-email-settings/log-scansioni?limit=10` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `GET /api/f24-email-settings/stato-sistema` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `POST /api/f24-email-settings/aggiungi-mittente` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `POST /api/f24-email-settings/impostazioni` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `POST /api/f24-email-settings/scan-manuale` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `POST /api/f24-email-settings/toggle-auto-scan?attivo={param}` — `verificare contratto dinamico` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `POST /api/settings/gmail` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `POST /api/settings/gmail/test` — `tenere` — sorgente: frontend/src/pages/ImpostazioniF24Email.jsx
- `GET /api/f24-email-settings/log-scansioni` — `tenere` — in uso: FE
- `/api/f24-email-settings/rimuovi-mittente/{param}` — endpoint rilevato nella mappa; metodo/contratto da verificare
- `POST /api/f24-email-settings/toggle-auto-scan` — `tenere` — in uso: FE
- `GET /api/settings/gmail` — `tenere` — in uso: FE

## Stato e azioni UI rilevati

### Stato locale

- `cfg`
- `form`
- `loading`
- `logs`
- `msg`
- `newKeyword`
- `newMittente`
- `saving`
- `scanning`
- `settings`
- `showAddMittente`
- `showPass`
- `stato`
- `testing`

### Handler e operazioni

- `fetchData`
- `saveSettings`

### Destinazioni di navigazione

- `/documenti/import`

### Componenti/import locali

- `../api`
- `../components/PageLayout`
- `../components/ds`
- `../components/ui/ConfirmDialog`
- `../lib/utils`
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
- `frontend/src/pages/ImpostazioniF24Email.jsx — SHA-256 `589360b6910c5f400b015ce0210896aa20b4b48ec3b1a10c23cfb4613f76942a` — 903 righe`

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
