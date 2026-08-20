# Gestio

Specifica di ricostruzione per **Gestio**, il gestionale contabile interno
(ex "GestionaleCloud / Ceraldi ERP"): documenti, fatture, fornitori, Prima
Nota, riconciliazioni, fisco, personale e flotta in un unico grafo operativo.

Il repository contiene la **documentazione di specifica** (`docs/spec/`),
adattata da un kit di ricostruzione più ampio, e il **codice applicativo**
(backend FastAPI, frontend React), costruito modulo verticale per modulo
verticale a partire da questa specifica.

## Stato del codice

Due moduli verticali completi.

**Prima Nota** (Cassa/Banca):

- Schema dati e motore unico di scrittura (`app/services/scritture_contabili.py`):
  nessun altro punto del codice può creare movimenti di Prima Nota.
- Versamento contanti → coppia collegata Cassa/Banca con lo stesso
  `operation_id`, idempotente, riconciliabile con l'estratto conto.
- API REST (`app/routers/prima_nota.py`) e pagina React collegata
  (`frontend/src/pages/PrimaNota.jsx`) con saldo progressivo per giorno.

**Corrispettivi RT** (import XML ufficiale Agenzia Entrate, schema COR10):

- Parser (`app/parsers/corrispettivi_rt.py`) verificato sulla struttura reale
  dei file del cliente (ricognizione su Google Drive, radice
  `1tmVu6fl7qhJbLcGCHT3wEQzrvFAElc9h`).
- Import idempotente per dispositivo/data (`app/services/corrispettivi.py`):
  quota contanti → Prima Nota Cassa (confermato); quota elettronico → Prima
  Nota Banca come credito POS "in attesa" (la riconciliazione con
  l'accredito reale del gestore è il prossimo modulo, Coerenza POS).
- API REST (`app/routers/corrispettivi.py`) e pagina React
  (`frontend/src/pages/Corrispettivi.jsx`) con upload XML.

Entrambi: test automatici sul servizio e sull'API (`tests/`, girano su
SQLite in-memory per velocità) — **verificati anche dal vivo su Postgres
reale** (server locale, non l'istanza Render): schema, scritture,
idempotenza, poi l'intera API con `curl`. Verificati anche dal vivo in
browser (backend + frontend avviati, upload/form compilato, risultato
visibile).

Tutti gli altri moduli descritti in `docs/spec/03_PAGINE/` sono ancora da
costruire, uno alla volta, con lo stesso schema: schema → servizio → API →
pagina → test.

### Avvio locale

```bash
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
.venv/bin/python -m pytest -q
.venv/bin/python -m uvicorn app.main:app --reload   # http://localhost:8000

cd frontend
npm install --include=dev   # necessario se l'ambiente forza NODE_ENV=production
npm run dev                 # http://localhost:5173, proxy verso l'API su :8000
```

Il database è **PostgreSQL**, provisionato su Render (istanza `gestio-db`,
piano free — vedi nota sotto). In locale, se `DATABASE_URL` non è
impostata, l'app usa un file SQLite (`gestio.db`, escluso da git) solo per
comodità di sviluppo: non è il database di destinazione. Le variabili sono
in `docs/spec/06_CONFIG/ENV_TEMPLATE.example`.

> **Nota**: l'istanza Render Postgres `gestio-db` (piano free) **scade il
> 19/09/2026** — è un limite del piano gratuito, non una scelta di design.
> Prima di quella data va portata su un piano a pagamento o ricreata.
> La stringa di connessione con la password non è recuperabile dagli
> strumenti usati per crearla (per sicurezza): va copiata dalla dashboard
> Render → `https://dashboard.render.com/d/dpg-da3fue37uimc73ajcai0-a` →
> "Connect", e impostata come `DATABASE_URL` nell'ambiente locale/di deploy.

## Scelte architetturali per questo repository

Rispetto al kit di origine sono stati esclusi:

- **MongoDB** — nessun backend Mongo, né transitorio né di fallback.
- **Google Sheets** come registro — nessun archivio dati su fogli.
- I nomi storici del prodotto (GestionaleCloud, Gestionale Cloud, ecc.) sono
  stati sostituiti con **Gestio**.

Al loro posto, il target è un **unico database PostgreSQL**, attivo dal
primo avvio (nessuna migrazione o cutover da gestire), con **storage file
locale** per gli originali (fatture, F24, verbali, estratti conto...),
indicizzato per hash e provenienza nel database.

**Google Drive** resta ammesso, ma con un ruolo diverso da quello del kit
originale: non è l'archivio dell'applicazione, è una **fonte esterna da cui
importare** (come Gmail) — cartelle configurate, lette in sola lettura,
i cui documenti vengono acquisiti e indicizzati nel database Postgres. La
struttura reale delle cartelle del cliente (radice
`1tmVu6fl7qhJbLcGCHT3wEQzrvFAElc9h` su Drive) è mappata via via che si
costruiscono i moduli di import.

## Pulizia del kit

Oltre a Mongo/Drive, sono state rimosse le parti morte o ridondanti del kit
di origine, per tenere una sola versione canonica di ogni informazione:

- **60 variabili** Mongo/Google Drive/Sheets tolte dall'inventario
  (`06_CONFIG/VARIABLES.*`, `PROMPT_MASTER.md`) — restano 164.
- **`03_PAGINE/MAPPE_JSON/`** eliminata: era la mappa tecnica grezza da cui
  erano generate le 65 schede pagina, ormai ridondante con le schede stesse
  e con i nuovi contratti `03_PAGINE/LOGICA_JSON/*.json` (uno per pagina,
  con fonti, scritture, logica operativa, automazioni e criteri di
  accettazione).
- **`03_PAGINE/QUARANTENA_MAPPE/`** eliminata (mappe sperimentali inutilizzate).
- **`05_API/ENDPOINTS.*`** compattato: i 403 endpoint in quarantena erano
  quasi tutti ripetizioni della stessa motivazione riga per riga; ora c'è
  una legenda unica e un elenco per router, senza perdere l'informazione.
- **`08_RIFERIMENTI_CONTESTO/`** ridotta da 24 file (audit di codice morto,
  mappe endpoint duplicate, gap-analysis del vecchio codice Mongo) a 5:
  restano solo i riferimenti fiscali di dominio riutilizzabili (piano dei
  conti CEE, IVA, F24/cedolini/IRES/IRAP, libro mastro, regola fornitori).

## Da dove iniziare

Leggere `docs/spec/00_START_HERE.md`, poi
`docs/spec/01_MASTER/PROMPT_MASTER.md` (specifica normativa unica). La
regola di autorità è: il Prompt Master prevale sempre; le schede pagina e
gli inventari tecnici (`03_PAGINE`, `05_API`, `06_CONFIG`,
`09_MACHINE_READABLE`) sono completezza tecnica; i riferimenti in
`08_RIFERIMENTI_CONTESTO` sono subordinati (riferimento fiscale di dominio).

```text
docs/spec/
├── 00_START_HERE.md                punto di ingresso
├── 00_PROMPT_DA_INCOLLARE.txt      istruzioni sintetiche per un agente
├── 01_MASTER/                      Prompt Master e documenti di prodotto
├── 02_ARCHITETTURA/                architettura, sicurezza, Gmail, MCP
├── 03_PAGINE/                      65 schede pagina + LOGICA_JSON/ (contratti)
├── 04_POPUP/                       i popup dell'applicazione
├── 05_API/                         catalogo endpoint (attivi/quarantena)
├── 06_CONFIG/                      variabili di configurazione
├── 07_TEST_E_ACCETTAZIONE/         gate di accettazione e runbook
├── 08_RIFERIMENTI_CONTESTO/        riferimenti fiscali di dominio
└── 09_MACHINE_READABLE/            inventari macchina (JSON)
```
