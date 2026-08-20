# Architettura pulita da ricostruire

## Obiettivo

Un monolite modulare semplice: frontend React, API FastAPI, servizi di dominio,
adapter per Gmail/banche/provider e un unico database SQL monoutente. Ogni
funzione ha un solo writer canonico e un solo contratto pubblico.

```text
Fonti esterne (Gmail, banche, POS, PayPal, PagoPA)
        ↓ ingest idempotente + hash + source_external_id
Originali immutabili su storage file (tracciati per hash e provenienza)
        ↓ parser versionato
Database applicativo (SQLite) + entity_relations
        ↓ servizi di dominio / writer contabile unico
API autenticate e versionate
        ↓
65 pagine semplici + popup accessibili + audit/notifiche
```

## Confini

- UI: presentazione, filtri, conferme e scelta dei candidati; niente regole contabili duplicate.
- Router: validazione, auth/RBAC e contratto HTTP; niente query dirette sparse.
- Servizi: regole di dominio, idempotenza, matching e scritture atomiche.
- Adapter: Gmail, banche/provider e file di import; retry, rate limit, watermark e lock.
- Archivio: originali su storage file locale; registri e indici sul database SQL applicativo,
  unico e definitivo dal primo avvio (nessun Mongo, nessun Google Drive/Sheets nel target).
- Osservabilità: `run_id`, contatori, errori strutturati, durata, watermark e audit trail.

## Regole di dipendenza

Frontend → API → servizi → repository/adapter. Sono vietati bypass, doppie
pipeline e import che scrivono direttamente in registri contabili.
