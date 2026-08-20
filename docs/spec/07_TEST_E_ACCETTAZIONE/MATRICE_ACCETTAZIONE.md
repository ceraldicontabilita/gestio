# Strategia di test e definizione di completato

## Per ogni pagina

- route/accesso, anno globale, loading/error/empty/populated;
- calcoli, centesimi, segni, filtri e paginazione;
- mobile, tablet, desktop, tastiera e focus;
- relazioni bidirezionali e apertura del documento originale;
- secondo ingest identico senza nuove righe;
- candidati ambigui senza mutazione definitiva.

## Per ogni endpoint

- auth/RBAC, schema request/response, errori strutturati, idempotency key;
- limite/paginazione, retry/rate limit, timeout e concorrenza;
- nessuna scrittura fuori dal servizio canonico;
- test unitario, integrazione repository/adapter e contratto OpenAPI.

## Gate di release

Backend e frontend completi, build produzione, audit statico/dead-code,
contratto MCP/OpenAPI, generatori senza diff, manifest del kit valido e CI
verde. In produzione: health con commit corretto e controlli read-only dei
flussi reali. HTTP 200 da solo non basta.
