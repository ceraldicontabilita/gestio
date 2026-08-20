# Gestio — Ceraldi ERP

<!-- gestio-doc
status: current
reviewed_at: 2026-08-20
storage_architecture: database-sql-postgres
-->

ERP interno di Ceraldi Group S.R.L. per documenti, fatture, fornitori, Prima
Nota, riconciliazioni, fisco, personale e flotta.

La specifica normativa unica, completa e atomica è [`PROMPT_MASTER.md`](PROMPT_MASTER.md).
Gli altri documenti sono guide di lettura, riferimenti di dominio o mappe generate.

- Produzione: [impresasemplice.online](https://impresasemplice.online)
- Repository: `ceraldicontabilita/gestio`
- Branch operativo: `main`
- Catalogo UI: 65 schermate in `page_catalog.json`

## Stato aggiornato al 20/08/2026

La produzione usa un unico database PostgreSQL (gestito su Render) attivo
fin dal primo avvio. Non esiste un backend transitorio né un cutover da
completare: `DATA_BACKEND=sql` è l'unica configurazione supportata.

Il registro applicativo organizza i dati secondo questa struttura logica:

```text
REGISTRO DATI/
PARTENOPAY/
CODICI TRIBUTO/
QUIETANZE/
DICHIARAZIONI/
```

## Architettura

```text
Browser React/Vite
  -> API FastAPI same-origin
     -> servizi di dominio e motore unico Prima Nota
        -> database applicativo PostgreSQL (DATA_BACKEND=sql)

Gmail autorizzato / banche / POS / PayPal / PagoPA / import manuale
  -> import, parser, deduplica, identità canonica
     -> fatture, F24, quietanze, banca, PartenoPay, cedolini
```

### Stack

- Backend: Python 3.12, FastAPI, SQLAlchemy (async), APScheduler.
- Frontend: React 18, Vite 5, React Router 6, TanStack Query, Zustand.
- Persistenza: database applicativo PostgreSQL (gestito su Render); storage
  file locale per gli originali, indicizzato per hash e provenienza.
- Deploy: un servizio Render avviato con `python -m app.process_supervisor`.
- CI: pytest, Vitest, build Vite, audit statici, runtime smoke ed E2E isolato.

## Avvio locale

Prerequisiti: Python 3.12, Node.js e Yarn.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
yarn --cwd frontend install --frozen-lockfile
```

Configurare le variabili in un ambiente locale non versionato. Per una prova
isolata non usare credenziali o dati di produzione.

```powershell
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
yarn --cwd frontend dev
```

Se l'entrypoint applicativo cambia, il riferimento definitivo è il comando di
avvio in `render.yaml` e il lifecycle importato dai test correnti.

## Configurazione essenziale

### Applicazione

- `ENVIRONMENT`
- `SECRET_KEY`
- `CORS_ALLOWED_ORIGINS`
- `DATA_BACKEND=sql`

### Database applicativo

- `DATABASE_URL` (stringa di connessione PostgreSQL, es. istanza Render)
- `DOCUMENT_STORAGE_PATH` (percorso/volume per gli originali indicizzati)

### Gmail (ingestione email autorizzata)

- credenziali OAuth del canale Gmail configurato
- mittenti/etichette autorizzati per canale (F24, quietanze, cedolini, verbali)

Le credenziali restano nel secret store di Render. Non inserire JSON di
service account, token o password nel repository.

## Backup e ripristino

1. backup periodico del database PostgreSQL (gestiti da Render) e dello
   storage file;
2. verifica di integrità (conteggi, hash) dopo ogni ripristino;
3. verifica live del commit in produzione dopo un deploy.

## Albero del repository

```text
app/
├── routers/                    API FastAPI per dominio
├── services/                   logica condivisa e riconciliazioni
├── parsers/                    XML, PDF, CSV e formati fiscali
├── knowledge/                  base di conoscenza della chat
├── config.py                   configurazione e feature flag
└── database.py                 connessione e sessione al database PostgreSQL
backend/
└── requirements.txt
frontend/
├── src/main.jsx                router principale
├── src/pages/                  schermate
├── src/pages/hub/              alberi di navigazione per modulo
├── src/components/             modali e componenti condivisi
└── package.json
gestionale_mcp/                 gateway AI di sola lettura
scripts/                        audit, mappe e manutenzione verificabile
tests/                          test backend e guardie architetturali
memoria/                        specifiche e mappe tecniche
page_catalog.json               catalogo macchina delle 65 pagine
CLAUDE.md                       istruzioni operative per gli agenti
PRODUCT.md                      obiettivi e confini del prodotto
```

## Moduli applicativi

- Dashboard e inserimento rapido
- Fatture, corrispettivi e fornitori
- Prima Nota Cassa/Banca, salari e ritenute
- Flotta, verbali e costi noleggio
- Contabilità, bilancio, IVA, F24 e situazione fiscale
- Riconciliazione banca, bonifici, assegni, PayPal, PagoPA e POS
- Import, archivio e indice documentale
- Strumenti, integrazioni, agenti e amministrazione

L'elenco completo e verificabile delle route è in `page_catalog.json`.

## Regole dati fondamentali

1. `canonical_id` identifica l'entità; `operation_id` collega le prove della
   stessa operazione.
2. Stesso hash/identità non crea un duplicato.
3. L'importo da solo non autorizza un'associazione.
4. Fattura, quietanza e movimento bancario restano entità distinte.
5. I ricavi provengono dai corrispettivi, non dagli accrediti POS.
6. Le scritture di Prima Nota passano da
   `app/services/scritture_contabili.py`.
7. I documenti originali sono immutabili e tracciati con fonte e hash.

## Test

```powershell
python -m pytest -q
yarn --cwd frontend test
yarn --cwd frontend build
python scripts\audit_static.py
git diff --check
```

Test mirati del catalogo e del registro dati:

```powershell
python -m pytest tests\test_page_catalog.py -q
python -m pytest tests\test_ledger.py tests\test_database.py -q
```

## Deploy

`render.yaml` documenta il servizio Render con auto-deploy da `main`. Prima
di considerare pubblicata una modifica:

1. CI verde;
2. `HEAD == origin/main`;
3. `/api/health` deve riportare il commit atteso;
4. controllo live del flusso interessato.

## Documentazione

- `PROMPT_MASTER.md` — unica autorità normativa: prodotto, dati, Gmail,
  variabili, pagine, router, endpoint, divieti e gate.
- `CLAUDE.md` — regole vincolanti per lavorare nel repository.
- `PRODUCT.md` — visione, flussi e albero funzionale.
- `LOGICA_FUNZIONAMENTO.md` — comportamento operativo per gli utenti.
- `page_catalog.json` — route/componenti/accessi/stato audit.
- `memoria/JSON_INVENTORY.json` — inventario e politica dei file JSON.
- `memoria/pagine/*.json` — mappe tecniche delle pagine.
- `memoria/popup/*.json` — mappe tecniche dei popup.

### Kit completo per la ricostruzione pulita

Per generare un unico ZIP autosufficiente con Prompt Master, architettura,
logica delle 65 pagine, 36 popup, contratti API, variabili senza segreti,
modello dati e matrice di accettazione:

```powershell
python scripts\genera_kit_ricostruzione.py
```

Il comando crea in `Documents`:

- `Gestio_REBUILD_KIT_2026-08-20.zip`;
- `Gestio_REBUILD_KIT_2026-08-20.zip.sha256`.

Il generatore verifica una sola cartella radice, manifest e hash interni,
conteggi canonici e firme compatibili con credenziali. Lo ZIP non viene
versionato: non contiene dati aziendali, allegati, segreti o una copia del
codice applicativo; viene rigenerato dalle fonti correnti del repository.

## Licenza

Uso interno Ceraldi Group S.R.L. Tutti i diritti riservati.
