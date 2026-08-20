# Gestio

Specifica di ricostruzione per **Gestio**, il gestionale contabile interno
(ex "GestionaleCloud / Ceraldi ERP"): documenti, fatture, fornitori, Prima
Nota, riconciliazioni, fisco, personale e flotta in un unico grafo operativo.

Questo repository contiene per ora la **documentazione di specifica**
(`docs/spec/`), adattata da un kit di ricostruzione più ampio. Il codice
applicativo (backend FastAPI, frontend React) non è ancora stato scritto:
si costruisce modulo per modulo a partire da questa specifica.

## Scelte architetturali per questo repository

Rispetto al kit di origine sono stati esclusi:

- **MongoDB** — nessun backend Mongo, né transitorio né di fallback.
- **Google Drive / Google Sheets** come persistenza — nessun registro su
  fogli, nessun archivio originali su Drive.
- I nomi storici del prodotto (GestionaleCloud, Gestionale Cloud, ecc.) sono
  stati sostituiti con **Gestio**.

Al loro posto, il target è un **unico database SQL monoutente (SQLite)**,
attivo dal primo avvio (nessuna migrazione o cutover da gestire), con
**storage file locale** per gli originali (fatture, F24, verbali, estratti
conto...), indicizzato per hash e provenienza nel database stesso.

## Da dove iniziare

Leggere `docs/spec/00_START_HERE.md`, poi
`docs/spec/01_MASTER/PROMPT_MASTER.md` (specifica normativa unica). La
regola di autorità è: il Prompt Master prevale sempre; le schede pagina e
gli inventari tecnici (`03_PAGINE`, `05_API`, `06_CONFIG`,
`09_MACHINE_READABLE`) sono completezza tecnica; i riferimenti in
`08_RIFERIMENTI_CONTESTO` sono subordinati e documentano in parte il
codice legacy (Mongo/Drive inclusi) solo come cronaca storica, mai come
target da riprodurre.

```text
docs/spec/
├── 00_START_HERE.md                punto di ingresso
├── 00_PROMPT_DA_INCOLLARE.txt      istruzioni sintetiche per un agente
├── 01_MASTER/                      Prompt Master e documenti di prodotto
├── 02_ARCHITETTURA/                architettura, sicurezza, Gmail, MCP
├── 03_PAGINE/                      le pagine dell'applicazione
├── 04_POPUP/                       i popup dell'applicazione
├── 05_API/                         catalogo endpoint (attivi/quarantena)
├── 06_CONFIG/                      variabili di configurazione
├── 07_TEST_E_ACCETTAZIONE/         gate di accettazione e runbook
├── 08_RIFERIMENTI_CONTESTO/        materiale di contesto, subordinato
└── 09_MACHINE_READABLE/            inventari macchina (JSON)
```
