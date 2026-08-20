# Tutti gli endpoint

Implementare solo `active`; `quarantine` è un decision log, non va esposto.

Totale: **1140** — attivi: **737** — quarantena: **403**.

## Legenda quarantena

- `verificare` — nessun riferimento noto (FE/scheduler/chat/test): verificare prima di deprecare
- `admin-only` — endpoint di migrazione/manutenzione one-shot: tenere ma Admin-only, disabilitabile, documentato, non esposto a lungo (§7)

## `accounting.bilancio`

- **active / tenere** — `GET /api/bilancio/conto-economico` — in uso: FE
- **active / tenere** — `GET /api/bilancio/export-pdf` — in uso: FE
- **active / tenere** — `GET /api/bilancio/export/pdf/confronto` — in uso: FE
- **active / tenere** — `GET /api/bilancio/riepilogo` — in uso: chat
- **active / tenere** — `GET /api/bilancio/stato-patrimoniale` — in uso: FE
- **quarantine / verificare** — `GET /api/bilancio/confronto-annuale`, `GET /api/bilancio/conto-economico-dettagliato`

## `accounting.centri_costo`

- **active / tenere** — `GET /api/centri-costo` — in uso: FE
- **active / tenere** — `POST /api/centri-costo` — in uso: FE
- **active / tenere** — `GET /api/centri-costo/utile-obiettivo` — in uso: FE
- **active / tenere** — `POST /api/centri-costo/utile-obiettivo` — in uso: FE
- **active / tenere** — `GET /api/centri-costo/utile-obiettivo/per-cdc` — in uso: FE
- **active / tenere** — `GET /api/centri-costo/utile-obiettivo/suggerimenti` — in uso: FE
- **quarantine / verificare** — `POST /api/centri-costo/assegna-cdc-fatture`, `GET /api/centri-costo/mapping-categorie`, `POST /api/centri-costo/ribaltamento/calcola`, `POST /api/centri-costo/ribaltamento/quote-ricavo`

## `accounting.contabilita_avanzata`

- **active / tenere** — `GET /api/contabilita/aliquote-irap` — in uso: FE
- **active / tenere** — `GET /api/contabilita/bilancio-dettagliato` — in uso: FE
- **active / tenere** — `GET /api/contabilita/calcolo-imposte` — in uso: FE
- **active / tenere** — `GET /api/contabilita/export/pdf-dichiarazione` — in uso: FE
- **active / tenere** — `POST /api/contabilita/ricategorizza-fatture` — in uso: FE
- **active / tenere** — `GET /api/contabilita/statistiche-categorizzazione` — in uso: FE
- **quarantine / verificare** — `GET /api/contabilita/categorizzazione-preview`, `GET /api/contabilita/piano-conti-esteso`
- **quarantine / admin-only** — `POST /api/contabilita/inizializza-piano-esteso`

## `accounting.contabilita_gestionale`

- **active / tenere** — `GET /api/contabilita-gestionale/bilancio-verifica` — in uso: FE
- **active / tenere** — `POST /api/contabilita-gestionale/budget` — in uso: FE
- **active / tenere** — `GET /api/contabilita-gestionale/budget-vs-consuntivo/{anno}` — in uso: FE
- **active / tenere** — `POST /api/contabilita-gestionale/budget/duplica/{anno_origine}/{anno_destinazione}` — in uso: FE
- **active / tenere** — `GET /api/contabilita-gestionale/budget/{anno}` — in uso: FE
- **active / tenere** — `DELETE /api/contabilita-gestionale/budget/{anno}/{voce}` — in uso: FE
- **active / tenere** — `GET /api/contabilita-gestionale/libro-giornale` — in uso: FE
- **active / tenere** — `GET /api/contabilita-gestionale/libro-giornale/controllo-60-giorni` — in uso: FE
- **active / tenere** — `GET /api/contabilita-gestionale/libro-giornale/export` — in uso: FE
- **active / tenere** — `POST /api/contabilita-gestionale/libro-giornale/import` — in uso: FE
- **active / tenere** — `GET /api/contabilita-gestionale/libro-mastro` — in uso: FE
- **quarantine / verificare** — `GET /api/contabilita-gestionale/partitario/clienti`, `GET /api/contabilita-gestionale/partitario/fornitori`, `GET /api/contabilita-gestionale/partitario/fornitori/{piva}`

## `accounting.piano_conti`

- **active / tenere** — `GET /api/piano-conti/` — in uso: FE
- **active / tenere** — `POST /api/piano-conti/` — in uso: FE
- **active / tenere** — `GET /api/piano-conti/bilancio` — in uso: FE
- **active / tenere** — `GET /api/piano-conti/conto/{codice}/movimenti` — in uso: FE
- **active / tenere** — `GET /api/piano-conti/movimenti` — in uso: FE
- **active / tenere** — `POST /api/piano-conti/registra-corrispettivi` — in uso: FE
- **active / tenere** — `POST /api/piano-conti/registra-fattura` — in uso: FE
- **active / tenere** — `POST /api/piano-conti/registra-tutte-fatture` — in uso: FE
- **active / tenere** — `GET /api/piano-conti/regole` — in uso: FE
- **active / tenere** — `POST /api/piano-conti/regole` — in uso: FE
- **active / tenere** — `DELETE /api/piano-conti/{conto_id}` — in uso: FE
- **active / tenere** — `PUT /api/piano-conti/{conto_id}` — in uso: FE

## `accounting.prima_nota_salari`

- **active / tenere** — `GET /api/prima-nota-salari/dipendenti-lista` — in uso: FE
- **active / tenere** — `GET /api/prima-nota-salari/export-appdipendenti/download` — in uso: FE
- **active / tenere** — `GET /api/prima-nota-salari/export-appdipendenti/preview` — in uso: FE
- **active / tenere** — `POST /api/prima-nota-salari/import-bonifici` — in uso: FE
- **active / tenere** — `POST /api/prima-nota-salari/import-paghe` — in uso: FE
- **active / tenere** — `POST /api/prima-nota-salari/ricalcola-progressivi` — in uso: FE
- **active / tenere** — `GET /api/prima-nota-salari/salari` — in uso: FE
- **active / tenere** — `POST /api/prima-nota-salari/salari/aggiustamento` — in uso: FE
- **active / tenere** — `GET /api/prima-nota-salari/salari/riepilogo` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota-salari/salari/{record_id}` — in uso: FE
- **active / tenere** — `PUT /api/prima-nota-salari/salari/{record_id}` — in uso: FE
- **active / tenere** — `GET /api/prima-nota-salari/salari/{record_id}/bonifico-pdf` — in uso: FE
- **active / tenere** — `POST /api/prima-nota-salari/salari/{record_id}/bonifico-pdf` — in uso: FE
- **active / tenere** — `GET /api/prima-nota-salari/salari/{record_id}/cedolino-pdf` — in uso: FE
- **active / tenere** — `POST /api/prima-nota-salari/salari/{record_id}/cedolino-pdf` — in uso: FE
- **active / tenere** — `PUT /api/prima-nota-salari/salari/{record_id}/riconcilia` — in uso: FE
- **quarantine / verificare** — `POST /api/prima-nota-salari/consolida-record`, `GET /api/prima-nota-salari/export-excel`, `DELETE /api/prima-nota-salari/pulisci-righe-vuote`
- **quarantine / admin-only** — `DELETE /api/prima-nota-salari/salari/reset`

## `accounting.regole_categorizzazione`

- **active / tenere** — `GET /api/regole` — in uso: FE
- **active / tenere** — `POST /api/regole/categorie` — in uso: FE
- **active / tenere** — `POST /api/regole/descrizione` — in uso: FE
- **active / tenere** — `GET /api/regole/download-regole` — in uso: FE
- **active / tenere** — `DELETE /api/regole/elimina/{tipo}/{pattern}` — in uso: FE
- **active / tenere** — `POST /api/regole/fornitore` — in uso: FE
- **active / tenere** — `POST /api/regole/upload-regole` — in uso: FE

## `admin`

- **active / tenere** — `GET /api/admin/bank-supplier-rules` — in uso: FE
- **active / tenere** — `POST /api/admin/bank-supplier-rules` — in uso: FE
- **active / tenere** — `POST /api/admin/bank-supplier-rules/reprocess/{year}` — in uso: FE
- **active / tenere** — `DELETE /api/admin/bank-supplier-rules/{rule_id}` — in uso: FE
- **active / tenere** — `GET /api/admin/dashboard-summary` — in uso: FE
- **active / tenere** — `GET /api/admin/registro-dati/config` — in uso: FE
- **active / tenere** — `POST /api/admin/registro-dati/config` — in uso: FE
- **active / tenere** — `GET /api/admin/registro-dati/duplicate-audit` — in uso: FE
- **active / tenere** — `POST /api/admin/registro-dati/duplicate-audit-folders` — in uso: FE
- **active / tenere** — `POST /api/admin/registro-dati/jobs/{action}` — in uso: FE
- **active / tenere** — `GET /api/admin/registro-dati/jobs/{job_id}` — in uso: FE
- **active / tenere** — `GET /api/admin/registro-dati/manifest` — in uso: FE
- **active / tenere** — `POST /api/admin/registro-dati/restore` — in uso: FE
- **active / tenere** — `POST /api/admin/registro-dati/sync` — in uso: FE
- **active / tenere** — `GET /api/admin/stats` — in uso: FE
- **quarantine / admin-only** — `DELETE /api/admin/cleanup-trattenute-disciplinari`, `POST /api/admin/registro-dati/duplicate-cleanup-folders`, `GET /api/admin/registro-dati/migration-audit`, `POST /api/admin/noleggio/backfill-dati-gestionali`, `POST /api/admin/reset-collections`
- **quarantine / verificare** — `GET /api/admin/collections`, `GET /api/admin/year-opening-balances/{year}`, `PUT /api/admin/year-opening-balances/{year}`

## `admin_export`

- **quarantine / verificare** — `GET /api/admin/export`, `GET /api/admin/export/{filename}`

## `admin_rollback`

- **active / tenere** — `POST /api/admin/rollback/fatture-import/conta` — in uso: FE
- **active / tenere** — `POST /api/admin/rollback/fatture-import/elimina` — in uso: FE
- **active / tenere** — `POST /api/admin/rollback/fatture/azzera-tutto` — in uso: FE
- **active / tenere** — `GET /api/admin/rollback/fatture/azzera-tutto/conta` — in uso: FE
- **active / tenere** — `GET /api/admin/rollback/sezioni` — in uso: FE
- **active / tenere** — `DELETE /api/admin/rollback/{sezione}` — in uso: FE
- **active / tenere** — `GET /api/admin/rollback/{sezione}/conta` — in uso: FE

## `agenti`

- **active / tenere** — `POST /api/agenti/automazioni/ferma` — in uso: FE
- **active / tenere** — `POST /api/agenti/automazioni/riprendi` — in uso: FE
- **active / tenere** — `GET /api/agenti/automazioni/stato` — in uso: FE
- **active / tenere** — `GET /api/agenti/cash-flow-13-settimane` — in uso: FE
- **active / tenere** — `GET /api/agenti/decisioni` — in uso: FE
- **active / tenere** — `POST /api/agenti/decisioni/{decision_id}/approva` — in uso: FE
- **active / tenere** — `GET /api/agenti/decisioni/{decision_id}/eventi` — in uso: FE
- **active / tenere** — `POST /api/agenti/decisioni/{decision_id}/rifiuta` — in uso: FE
- **active / tenere** — `GET /api/agenti/pattern-appresi` — in uso: FE
- **active / tenere** — `GET /api/agenti/segnalazioni` — in uso: FE
- **active / tenere** — `GET /api/agenti/segnalazioni/count` — in uso: FE
- **active / tenere** — `GET /api/agenti/segnalazioni/summary` — in uso: FE
- **active / tenere** — `PUT /api/agenti/segnalazioni/{sid}/letta` — in uso: FE
- **active / tenere** — `PUT /api/agenti/segnalazioni/{sid}/risolta` — in uso: FE
- **active / tenere** — `GET /api/agenti/stato` — in uso: FE
- **quarantine / verificare** — `POST /api/agenti/run`

## `ai_parser`

- **active / tenere** — `POST /api/ai-parser/process-email-batch` — in uso: FE
- **quarantine / verificare** — `POST /api/ai-parser/batch-parse`, `GET /api/ai-parser/da-rivedere`, `POST /api/ai-parser/da-rivedere/process-batch`, `PUT /api/ai-parser/da-rivedere/{document_id}/classifica`, `POST /api/ai-parser/parse`, `POST /api/ai-parser/parse-busta-paga`, `POST /api/ai-parser/parse-f24`, `POST /api/ai-parser/parse-fattura`, `GET /api/ai-parser/statistiche`, `GET /api/ai-parser/test`

## `alerts`

- **active / tenere** — `GET /api/alerts/lista` — in uso: FE
- **active / tenere** — `GET /api/alerts/summary` — in uso: FE
- **active / tenere** — `POST /api/alerts/{alert_id}/risolvi` — in uso: scheduler
- **quarantine / verificare** — `GET /api/alerts/fornitori-senza-metodo`, `POST /api/alerts/risolvi-fornitore/{fornitore_piva}`, `DELETE /api/alerts/{alert_id}`, `POST /api/alerts/{alert_id}/segna-letto`

## `anagrafica_fornitori_xml`

- **active / tenere** — `POST /api/anagrafica-fornitori/popola-fornitore/{fornitore_id}` — in uso: FE
- **active / tenere** — `POST /api/anagrafica-fornitori/popola-tutti` — in uso: FE

## `auth`

- **active / tenere** — `POST /api/auth/login` — in uso: FE
- **active / tenere** — `POST /api/auth/logout` — in uso: FE
- **active / tenere** — `GET /api/auth/verify` — in uso: FE

## `auto_repair`

- **active / tenere** — `POST /api/auto-repair/collega-targa-driver` — in uso: FE, scheduler
- **active / tenere** — `POST /api/auto-repair/inferisci-targa-driver-da-fatture` — in uso: FE, scheduler

## `bank.assegni`

- **active / tenere** — `GET /api/assegni` — in uso: FE
- **active / tenere** — `GET /api/assegni/ambigui` — in uso: FE
- **active / tenere** — `POST /api/assegni/associa-beneficiari-robusto` — in uso: FE
- **active / tenere** — `POST /api/assegni/associa-pagamenti-multipli` — in uso: FE
- **active / tenere** — `POST /api/assegni/auto-associa` — in uso: FE
- **active / tenere** — `POST /api/assegni/auto-match` — in uso: FE
- **active / tenere** — `POST /api/assegni/auto-match/conferma` — in uso: FE
- **active / tenere** — `POST /api/assegni/cerca-combinazioni-assegni` — in uso: FE
- **active / tenere** — `DELETE /api/assegni/clear-generated` — in uso: FE
- **active / tenere** — `POST /api/assegni/conferma-proposta/{proposta_id}` — in uso: FE
- **active / tenere** — `PUT /api/assegni/correggi-associazione/{assegno_id}` — in uso: FE
- **active / tenere** — `POST /api/assegni/correggi-numeri` — in uso: FE
- **active / tenere** — `POST /api/assegni/genera` — in uso: FE
- **active / tenere** — `GET /api/assegni/preview-combinazioni` — in uso: FE
- **active / tenere** — `GET /api/assegni/proposte-associazione` — in uso: FE
- **active / tenere** — `POST /api/assegni/pulisci-beneficiari-fittizi` — in uso: FE
- **active / tenere** — `POST /api/assegni/ricostruisci-dati` — in uso: FE
- **active / tenere** — `POST /api/assegni/rifiuta-proposta/{proposta_id}` — in uso: FE
- **active / tenere** — `POST /api/assegni/riprocessa-collegamenti` — in uso: FE
- **active / tenere** — `GET /api/assegni/senza-associazione` — in uso: FE
- **active / tenere** — `GET /api/assegni/stati` — in uso: FE
- **active / tenere** — `GET /api/assegni/stats` — in uso: FE
- **active / tenere** — `GET /api/assegni/supporto/fatture-disponibili` — in uso: FE
- **active / tenere** — `POST /api/assegni/sync-da-estratto-conto` — in uso: FE
- **active / tenere** — `GET /api/assegni/verifica-associazioni` — in uso: FE
- **active / tenere** — `DELETE /api/assegni/{assegno_id}` — in uso: FE
- **active / tenere** — `GET /api/assegni/{assegno_id}` — in uso: FE
- **active / tenere** — `PUT /api/assegni/{assegno_id}` — in uso: FE
- **active / tenere** — `POST /api/assegni/{assegno_id}/annulla` — in uso: FE
- **active / tenere** — `POST /api/assegni/{assegno_id}/emetti` — in uso: FE
- **active / tenere** — `PUT /api/assegni/{assegno_id}/fatture-collegate` — in uso: FE
- **active / tenere** — `POST /api/assegni/{assegno_id}/incassa` — in uso: FE
- **active / tenere** — `POST /api/assegni/{assegno_id}/risolvi-ambiguo` — in uso: FE

## `bank.assegni_learning`

- **active / tenere** — `POST /api/assegni/learning/associa-combinazioni-avanzato` — in uso: FE
- **active / tenere** — `POST /api/assegni/learning/associa-intelligente` — in uso: FE
- **active / tenere** — `POST /api/assegni/learning/learn` — in uso: FE
- **active / tenere** — `GET /api/assegni/learning/stats-avanzate` — in uso: FE
- **active / tenere** — `GET /api/assegni/learning/suggerimenti/{importo}` — in uso: FE
- **quarantine / admin-only** — `POST /api/assegni/learning/pulizia-duplicati`

## `bank.bank_statement_import`

- **active / tenere** — `GET /api/bank-statement/movements` — in uso: FE
- **quarantine / admin-only** — `POST /api/bank-statement/cleanup-duplicati`, `POST /api/bank-statement/cleanup-duplicati-causale`
- **quarantine / verificare** — `GET /api/bank-statement/formati-supportati`, `POST /api/bank-statement/import`, `POST /api/bank-statement/riconcilia-manuale`, `GET /api/bank-statement/stats`

## `bank.bonifici_import_unificato`

- **quarantine / verificare** — `POST /api/archivio-bonifici/jobs/import`

## `bank.estratto_conto`

- **active / tenere** — `POST /api/estratto-conto-movimenti/import` — in uso: FE, scheduler
- **active / tenere** — `POST /api/estratto-conto-movimenti/ricategorizza-batch` — in uso: FE
- **active / tenere** — `GET /api/estratto-conto-movimenti/riepilogo` — in uso: chat
- **active / tenere** — `POST /api/estratto-conto-movimenti/ripara-versamenti-cassa` — in uso: FE
- **quarantine / verificare** — `GET /api/estratto-conto-movimenti/categorie`, `DELETE /api/estratto-conto-movimenti/clear`, `GET /api/estratto-conto-movimenti/export-excel`, `GET /api/estratto-conto-movimenti/fornitori`, `GET /api/estratto-conto-movimenti/movimenti`, `GET /api/estratto-conto-movimenti/movimenti-stipendi`, `POST /api/estratto-conto-movimenti/riconcilia-stipendi`, `DELETE /api/estratto-conto-movimenti/{movimento_id}`
- **quarantine / admin-only** — `POST /api/estratto-conto-movimenti/force-reimport`, `POST /api/estratto-conto-movimenti/pulizia-non-in-csv`, `POST /api/estratto-conto-movimenti/reimport`

## `bank.riconciliazione_f24_banca`

- **quarantine / verificare** — `GET /api/f24-riconciliazione/estratti-conto`, `GET /api/f24-riconciliazione/movimenti-f24-banca`, `POST /api/f24-riconciliazione/riconcilia-f24`, `GET /api/f24-riconciliazione/stato-riconciliazione`, `POST /api/f24-riconciliazione/upload-estratto-bpm`

## `batch_reprocessing`

- **active / tenere** — `POST /api/batch-reprocess/cedolini-only` — in uso: scheduler
- **active / tenere** — `POST /api/batch-reprocess/f24-only` — in uso: scheduler
- **active / tenere** — `GET /api/batch-reprocess/preview` — in uso: FE, scheduler
- **active / tenere** — `POST /api/batch-reprocess/start` — in uso: FE, scheduler
- **active / tenere** — `GET /api/batch-reprocess/status` — in uso: FE, scheduler

## `bonifici_module.associazioni`

- **active / tenere** — `POST /api/archivio-bonifici/associa-fattura` — in uso: FE
- **active / tenere** — `POST /api/archivio-bonifici/associa-salario` — in uso: FE
- **active / tenere** — `DELETE /api/archivio-bonifici/disassocia-fattura/{bonifico_id}` — in uso: FE
- **active / tenere** — `DELETE /api/archivio-bonifici/disassocia-salario/{bonifico_id}` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/fatture-compatibili/{bonifico_id}` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/operazioni-salari/{bonifico_id}` — in uso: FE
- **active / tenere** — `POST /api/archivio-bonifici/sync-iban-anagrafica` — in uso: FE
- **quarantine / verificare** — `GET /api/archivio-bonifici/dipendente/{dipendente_id}`

## `bonifici_module.jobs`

- **quarantine / verificare** — `GET /api/archivio-bonifici/jobs`, `POST /api/archivio-bonifici/jobs`, `GET /api/archivio-bonifici/jobs/{job_id}`, `POST /api/archivio-bonifici/jobs/{job_id}/upload`

## `bonifici_module.riconciliazione`

- **active / tenere** — `POST /api/archivio-bonifici/riconcilia` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/riconcilia/task/{task_id}` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/stato-riconciliazione` — in uso: FE
- **quarantine / verificare** — `POST /api/archivio-bonifici/associa-dipendenti`, `GET /api/archivio-bonifici/dashboard`
- **quarantine / admin-only** — `POST /api/archivio-bonifici/reset-riconciliazione`

## `bonifici_module.transfers`

- **active / tenere** — `GET /api/archivio-bonifici/transfers` — in uso: FE
- **active / tenere** — `DELETE /api/archivio-bonifici/transfers/bulk` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/transfers/count` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/transfers/summary` — in uso: FE
- **active / tenere** — `DELETE /api/archivio-bonifici/transfers/{transfer_id}` — in uso: FE
- **active / tenere** — `PUT /api/archivio-bonifici/transfers/{transfer_id}` — in uso: FE
- **active / tenere** — `GET /api/archivio-bonifici/transfers/{transfer_id}/pdf` — in uso: FE
- **quarantine / verificare** — `GET /api/archivio-bonifici/download-zip/{year}`, `GET /api/archivio-bonifici/export`

## `cash`

- **active / tenere** — `POST /api/cash/corrispettivi` — in uso: FE
- **active / tenere** — `GET /api/cash/corrispettivi/{target_date}` — in uso: FE
- **active / tenere** — `GET /api/cash/export/excel` — in uso: FE
- **active / tenere** — `GET /api/cash/movements` — in uso: FE
- **active / tenere** — `POST /api/cash/movements` — in uso: FE
- **active / tenere** — `DELETE /api/cash/movements/{movement_id}` — in uso: FE
- **active / tenere** — `PUT /api/cash/movements/{movement_id}` — in uso: FE
- **active / tenere** — `GET /api/cash/stats` — in uso: FE

## `cespiti`

- **active / tenere** — `GET /api/cespiti/` — in uso: FE
- **active / tenere** — `POST /api/cespiti/` — in uso: FE
- **active / tenere** — `GET /api/cespiti/calcolo-rateo/{anno}/{mese}` — in uso: FE
- **active / tenere** — `GET /api/cespiti/calcolo/{anno}` — in uso: FE
- **active / tenere** — `GET /api/cespiti/categorie` — in uso: FE
- **active / tenere** — `POST /api/cespiti/dismissione` — in uso: FE
- **active / tenere** — `POST /api/cespiti/registra/{anno}` — in uso: FE
- **active / tenere** — `GET /api/cespiti/riepilogo` — in uso: FE
- **active / tenere** — `POST /api/cespiti/scan-fatture` — in uso: FE
- **active / tenere** — `GET /api/cespiti/verifica/{anno}` — in uso: FE
- **active / tenere** — `DELETE /api/cespiti/{cespite_id}` — in uso: FE
- **active / tenere** — `GET /api/cespiti/{cespite_id}` — in uso: FE
- **active / tenere** — `PUT /api/cespiti/{cespite_id}` — in uso: FE

## `chat_router`

- **active / tenere** — `POST /api/chat/ask` — in uso: FE, chat
- **active / tenere** — `GET /api/chat/health` — in uso: chat
- **active / tenere** — `GET /api/chat/history` — in uso: chat

## `chiusura_esercizio`

- **active / tenere** — `POST /api/chiusura-esercizio/apertura-nuovo-esercizio` — in uso: FE
- **active / tenere** — `GET /api/chiusura-esercizio/bilancino-verifica/{anno}` — in uso: FE
- **active / tenere** — `POST /api/chiusura-esercizio/esegui-chiusura` — in uso: FE
- **active / tenere** — `GET /api/chiusura-esercizio/stato/{anno}` — in uso: FE
- **active / tenere** — `GET /api/chiusura-esercizio/storico` — in uso: FE
- **active / tenere** — `GET /api/chiusura-esercizio/verifica-preliminare/{anno}` — in uso: FE
- **quarantine / verificare** — `GET /api/chiusura-esercizio/saldi-iniziali/{anno}`

## `collaudo`

- **active / tenere** — `POST /api/collaudo/esegui` — in uso: FE
- **active / tenere** — `GET /api/collaudo/storico` — in uso: FE
- **active / tenere** — `GET /api/collaudo/ultimo` — in uso: FE

## `commercialista`

- **active / tenere** — `GET /api/commercialista/alert-status` — in uso: FE
- **active / tenere** — `GET /api/commercialista/config` — in uso: FE
- **active / tenere** — `PUT /api/commercialista/config` — in uso: FE
- **active / tenere** — `GET /api/commercialista/export-completo/{anno}/{mese}` — in uso: FE
- **active / tenere** — `GET /api/commercialista/export-excel/{anno}/{mese}` — in uso: FE
- **active / tenere** — `GET /api/commercialista/fatture-cassa/{anno}/{mese}` — in uso: FE
- **active / tenere** — `POST /api/commercialista/invia-carnet` — in uso: FE
- **active / tenere** — `POST /api/commercialista/invia-fatture-cassa` — in uso: FE
- **active / tenere** — `POST /api/commercialista/invia-prima-nota` — in uso: FE
- **active / tenere** — `GET /api/commercialista/log` — in uso: FE
- **active / tenere** — `GET /api/commercialista/prima-nota-cassa/{anno}/{mese}` — in uso: FE
- **active / tenere** — `GET /api/commercialista/riepilogo/{anno}/{mese}` — in uso: FE
- **active / tenere** — `POST /api/commercialista/segna-inviata` — in uso: FE
- **quarantine / verificare** — `GET /api/commercialista/export-log`, `POST /api/commercialista/schedula-export`

## `config_import`

- **active / tenere** — `GET /api/config-import/anno` — in uso: FE
- **active / tenere** — `PUT /api/config-import/anno` — in uso: FE
- **active / tenere** — `POST /api/config-import/importa-anno` — in uso: FE

## `configurazioni`

- **active / tenere** — `GET /api/config/email-accounts` — in uso: FE
- **active / tenere** — `POST /api/config/email-accounts` — in uso: FE
- **active / tenere** — `DELETE /api/config/email-accounts/{account_id}` — in uso: FE
- **active / tenere** — `PUT /api/config/email-accounts/{account_id}` — in uso: FE
- **active / tenere** — `POST /api/config/email-accounts/{account_id}/test` — in uso: FE
- **active / tenere** — `GET /api/config/parole-chiave` — in uso: FE
- **active / tenere** — `PUT /api/config/parole-chiave` — in uso: FE
- **active / tenere** — `POST /api/config/parole-chiave/aggiungi` — in uso: FE
- **active / tenere** — `DELETE /api/config/parole-chiave/rimuovi` — in uso: FE

## `contabilita_italiana`

- **active / tenere** — `GET /api/contabilita/disponibilita-liquide` — in uso: FE

## `controllo_gestione`

- **active / tenere** — `GET /api/controllo-gestione/costi-ricavi` — in uso: FE
- **active / tenere** — `GET /api/controllo-gestione/trend-mensile` — in uso: chat
- **quarantine / verificare** — `GET /api/controllo-gestione/costi-per-categoria`, `GET /api/controllo-gestione/kpi/{anno}`

## `dati_isa`

- **active / tenere** — `GET /api/dati-isa/riepilogo` — in uso: FE

## `dati_provvisori`

- **active / tenere** — `POST /api/conferma-tutte` — in uso: scheduler
- **active / tenere** — `POST /api/conferma/{proposta_id}` — in uso: scheduler, chat
- **active / tenere** — `POST /api/dati-provvisori/riconcilia-estratto-conto` — in uso: scheduler
- **active / tenere** — `POST /api/genera-proposte` — in uso: scheduler
- **active / tenere** — `GET /api/proposte` — in uso: scheduler
- **active / tenere** — `POST /api/rifiuta/{proposta_id}` — in uso: scheduler

## `document_ai`

- **quarantine / verificare** — `GET /api/document-ai/classified-documents-stats`, `GET /api/document-ai/document-types`, `POST /api/document-ai/extract`, `POST /api/document-ai/extract-base64`, `POST /api/document-ai/extract-text-only`, `GET /api/document-ai/extracted-documents`, `DELETE /api/document-ai/extracted-documents/{doc_id}`, `POST /api/document-ai/process-all-classified`, `POST /api/document-ai/process-classified-email`, `POST /api/document-ai/reprocess-and-save`

## `documenti`

- **active / tenere** — `GET /api/documenti/amministrativi` — in uso: FE
- **active / tenere** — `DELETE /api/documenti/documento/{doc_id}` — in uso: FE
- **active / tenere** — `GET /api/documenti/documento/{doc_id}` — in uso: FE
- **active / tenere** — `POST /api/documenti/documento/{doc_id}/annulla-processamento` — in uso: FE
- **active / tenere** — `POST /api/documenti/documento/{doc_id}/cambia-categoria` — in uso: FE
- **active / tenere** — `GET /api/documenti/documento/{doc_id}/download` — in uso: FE
- **active / tenere** — `POST /api/documenti/documento/{doc_id}/processa` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/catalog` — in uso: FE
- **active / tenere** — `POST /api/documenti/indice/fiscal/discover` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/fiscal/status` — in uso: FE
- **active / tenere** — `POST /api/documenti/indice/fiscal/sync` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/index/declarations` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/index/document/{document_id}` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/index/f24` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/index/overview` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/index/search` — in uso: FE
- **active / tenere** — `GET /api/documenti/indice/index/status` — in uso: FE
- **active / tenere** — `POST /api/documenti/indice/sync` — in uso: FE
- **active / tenere** — `GET /api/documenti/lista` — in uso: FE
- **active / tenere** — `GET /api/documenti/tax-codes` — in uso: FE
- **active / tenere** — `GET /api/documenti/tax-codes/status` — in uso: FE
- **active / tenere** — `POST /api/documenti/tax-codes/sync` — in uso: FE
- **active / tenere** — `POST /api/documenti/upload-auto` — in uso: FE
- **active / tenere** — `POST /api/documenti/upload-auto/preview` — in uso: FE
- **quarantine / verificare** — `GET /api/documenti/cartelle-email`, `GET /api/documenti/categorie`, `POST /api/documenti/elimina-processati`, `POST /api/documenti/fiscal/ingest`, `GET /api/documenti/lock-status`, `POST /api/documenti/monitor/start`, `GET /api/documenti/monitor/status`, `POST /api/documenti/monitor/stop`, `POST /api/documenti/monitor/sync-now`, `POST /api/documenti/processa-f24-scaricati`, `POST /api/documenti/processa-tutti`, `POST /api/documenti/ricategorizza-documenti`, `POST /api/documenti/scarica-da-email`, `GET /api/documenti/statistiche`, `POST /api/documenti/sync-estratti-bnl`, `POST /api/documenti/sync-estratti-conto`, `POST /api/documenti/sync-f24-automatico`, `GET /api/documenti/task/{task_id}`, `GET /api/documenti/telegram/status`, `POST /api/documenti/telegram/test`, `GET /api/documenti/ultimo-sync`
- **quarantine / admin-only** — `POST /api/documenti/reimporta-da-filesystem`

## `documenti_fiscali`

- **active / tenere** — `POST /api/documenti-fiscali/upload` — in uso: FE
- **quarantine / verificare** — `GET /api/documenti-fiscali/lista`

## `documenti_non_associati`

- **active / tenere** — `POST /api/documenti-non-associati/associa` — in uso: FE
- **active / tenere** — `GET /api/documenti-non-associati/associati-di-recente` — in uso: FE
- **active / tenere** — `GET /api/documenti-non-associati/collezioni-disponibili` — in uso: FE
- **active / tenere** — `POST /api/documenti-non-associati/de-associa` — in uso: FE
- **active / tenere** — `GET /api/documenti-non-associati/lista` — in uso: FE
- **active / tenere** — `GET /api/documenti-non-associati/pdf/{documento_id}` — in uso: FE
- **active / tenere** — `GET /api/documenti-non-associati/statistiche` — in uso: FE
- **quarantine / verificare** — `GET /api/documenti-non-associati/categorie-mittente`, `DELETE /api/documenti-non-associati/{documento_id}`

## `documents_inbox_classify`

- **active / tenere** — `POST /api/documenti-inbox/auto-classify` — in uso: FE
- **active / tenere** — `POST /api/documenti-inbox/import-dipendenti-from-cu` — in uso: FE
- **active / tenere** — `POST /api/documenti-inbox/import-f24-from-inbox` — in uso: FE
- **quarantine / verificare** — `GET /api/documenti-inbox/cross-check-f24`, `GET /api/documenti-inbox/statistics`

## `cedolini_sync`

- **active / tenere** — `GET /api/cedolini/sync/quadratura-completa` — in uso: scheduler
- **active / tenere** — `GET /api/cedolini/sync/status` — in uso: scheduler
- **active / tenere** — `POST /api/cedolini/sync/sync` — in uso: scheduler

## `corrispettivi_sync`

- **active / tenere** — `POST /api/corrispettivi/sync/quadratura` — in uso: FE
- **active / tenere** — `GET /api/corrispettivi/sync/status` — in uso: FE, scheduler
- **active / tenere** — `POST /api/corrispettivi/sync/sync` — in uso: FE, scheduler

## `quietanze_sync`

- **active / tenere** — `POST /api/f24/quietanze/sync/quadratura` — in uso: FE
- **active / tenere** — `GET /api/f24/quietanze/sync/status` — in uso: FE, scheduler
- **active / tenere** — `POST /api/f24/quietanze/sync/sync` — in uso: FE, scheduler

## `email_download`

- **active / tenere** — `POST /api/email-download/auto-associa` — in uso: FE
- **active / tenere** — `GET /api/email-download/mittenti` — in uso: FE
- **active / tenere** — `POST /api/email-download/mittenti` — in uso: FE
- **active / tenere** — `GET /api/email-download/mittenti/check` — in uso: FE
- **active / tenere** — `DELETE /api/email-download/mittenti/{mittente_id}` — in uso: FE
- **active / tenere** — `PUT /api/email-download/mittenti/{mittente_id}` — in uso: FE
- **active / tenere** — `DELETE /api/email-download/pulisci-duplicati` — in uso: scheduler
- **active / tenere** — `POST /api/email-download/start-full-download` — in uso: FE
- **quarantine / verificare** — `POST /api/email-download/associa-documento`, `POST /api/email-download/associa-f24-filesystem`, `POST /api/email-download/auto-associa-v2`, `GET /api/email-download/confronto-pos`, `GET /api/email-download/dizionario-email`, `GET /api/email-download/documenti-non-associati`, `GET /api/email-download/documents-inbox-stats`, `POST /api/email-download/download-single-day`, `POST /api/email-download/estrai-importi-verbali`, `POST /api/email-download/fix-numeri-verbali`, `GET /api/email-download/inbox-documents`, `POST /api/email-download/parse-f24-llm`, `POST /api/email-download/parse-verbali-llm`, `GET /api/email-download/paypal-transazioni`, `GET /api/email-download/pdf/{collection}/{pdf_id}`, `POST /api/email-download/popola-pdf-payslips`, `POST /api/email-download/processa-cedolini`, `POST /api/email-download/processa-fatture-email`, `POST /api/email-download/processa-fatture-email/batch`, `GET /api/email-download/processa-fatture-email/status`, `POST /api/email-download/processa-pipeline`, `POST /api/email-download/riconcilia-paypal`, `POST /api/email-download/riconcilia-verbali`, `POST /api/email-download/riconcilia-verbali-avanzato`, `POST /api/email-download/riconciliazione-completa`, `POST /api/email-download/scarica-pdf-verbali-mancanti`, `GET /api/email-download/statistiche`, `GET /api/email-download/status`, `POST /api/email-download/sync-email-now`, `POST /api/email-download/sync-filesystem`
- **quarantine / admin-only** — `DELETE /api/email-download/dizionario-email/reset`, `POST /api/email-download/mittenti/migra-legacy`, `POST /api/email-download/pulizia-non-attendibili`

## `email_scanner`

- **active / tenere** — `POST /api/email-scanner/associa` — in uso: FE
- **active / tenere** — `GET /api/email-scanner/statistiche` — in uso: FE, scheduler
- **quarantine / verificare** — `GET /api/email-scanner/cartelle`, `POST /api/email-scanner/scansiona`, `POST /api/email-scanner/scansiona-e-associa`

## `employees.dipendenti`

- **active / tenere** — `GET /api/dipendenti` — in uso: FE
- **active / tenere** — `POST /api/dipendenti` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/bulk-upsert` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/bulk-upsert/preview` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/buste-paga` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/buste-paga` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/buste-paga/dipendente/{dipendente_id}` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/buste-paga/dipendente/{dipendente_id}/import` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/buste-paga/import` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/buste-paga/scan` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/by-google-email` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/duplicati` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/duplicati/auto-merge` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/duplicati/merge` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/invita-multipli` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/mansioni` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/portale/stats` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/report-ferie-permessi-tutti` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/stats` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/sync-iban` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/tipi-turno` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/turni/salva` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/turni/settimana` — in uso: FE
- **active / tenere** — `DELETE /api/dipendenti/{dipendente_id}` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/{dipendente_id}` — in uso: FE
- **active / tenere** — `PUT /api/dipendenti/{dipendente_id}` — in uso: FE
- **active / tenere** — `POST /api/dipendenti/{dipendente_id}/invita-portale` — in uso: FE
- **active / tenere** — `GET /api/dipendenti/{dipendente_id}/report-ferie-permessi` — in uso: FE

## `erp_bridge`

- **quarantine / verificare** — `POST /api/erp/ponte/fattura-ricevuta`, `GET /api/erp/ponte/status`

## `f24.email_f24`

- **quarantine / verificare** — `GET /api/f24-email/allegati`, `GET /api/f24-email/codici-tributo`, `GET /api/f24-email/log-download`, `GET /api/f24-email/mittenti`, `POST /api/f24-email/processa-allegati`, `POST /api/f24-email/scarica-e-processa`, `POST /api/f24-email/scarica-email`

## `f24.f24_main`

- **active / tenere** — `GET /api/f24` — in uso: FE
- **active / tenere** — `POST /api/f24` — in uso: FE
- **active / tenere** — `GET /api/f24/alerts/scadenze` — in uso: FE
- **active / tenere** — `GET /api/f24/codici/all` — in uso: FE
- **active / tenere** — `GET /api/f24/codici/{codice}` — in uso: FE
- **active / tenere** — `GET /api/f24/dashboard/summary` — in uso: FE
- **active / tenere** — `GET /api/f24/documents` — in uso: FE
- **active / tenere** — `DELETE /api/f24/documents/{doc_id}` — in uso: FE
- **active / tenere** — `POST /api/f24/fascicolo/costruisci` — in uso: FE
- **active / tenere** — `GET /api/f24/fascicolo/{codice_fiscale}/{mese}/{anno}` — in uso: FE
- **active / tenere** — `GET /api/f24/quietanze` — in uso: FE
- **active / tenere** — `GET /api/f24/quietanze/statistiche/tributi` — in uso: FE
- **active / tenere** — `POST /api/f24/quietanze/upload` — in uso: FE
- **active / tenere** — `DELETE /api/f24/quietanze/{f24_id}` — in uso: FE
- **active / tenere** — `GET /api/f24/quietanze/{f24_id}` — in uso: FE
- **active / tenere** — `POST /api/f24/riconcilia` — in uso: FE, scheduler
- **active / tenere** — `POST /api/f24/upload` — in uso: FE
- **active / tenere** — `POST /api/f24/upload-multiple` — in uso: FE
- **active / tenere** — `POST /api/f24/upload-pdf` — in uso: FE
- **active / tenere** — `POST /api/f24/upload-zip` — in uso: FE
- **active / tenere** — `DELETE /api/f24/{f24_id}` — in uso: FE
- **active / tenere** — `GET /api/f24/{f24_id}` — in uso: FE
- **active / tenere** — `PUT /api/f24/{f24_id}` — in uso: FE
- **active / tenere** — `POST /api/f24/{f24_id}/mark-paid` — in uso: FE

## `f24.f24_public`

- **quarantine / verificare** — `GET /api/f24-public/models`, `DELETE /api/f24-public/models/{f24_id}`, `PUT /api/f24-public/models/{f24_id}`, `PUT /api/f24-public/models/{f24_id}/pagato`, `GET /api/f24-public/pdf/{f24_id}`, `GET /api/f24-public/scadenze-prossime`, `GET /api/f24-public/test`, `POST /api/f24-public/upload`, `POST /api/f24-public/upload-overwrite`

## `f24.f24_riconciliazione`

- **active / tenere** — `POST /api/f24-riconciliazione/riconcilia-tutto` — in uso: FE
- **quarantine / verificare** — `GET /api/f24-riconciliazione/alerts`, `POST /api/f24-riconciliazione/alerts/{alert_id}/conferma-elimina`, `POST /api/f24-riconciliazione/alerts/{alert_id}/ignora`, `GET /api/f24-riconciliazione/commercialista`, `POST /api/f24-riconciliazione/commercialista/upload`, `DELETE /api/f24-riconciliazione/commercialista/{f24_id}`, `GET /api/f24-riconciliazione/commercialista/{f24_id}`, `PUT /api/f24-riconciliazione/commercialista/{f24_id}`, `PUT /api/f24-riconciliazione/commercialista/{f24_id}/pagato`, `GET /api/f24-riconciliazione/commercialista/{f24_id}/pdf`, `GET /api/f24-riconciliazione/dashboard`, `POST /api/f24-riconciliazione/fix-campo-anno`, `GET /api/f24-riconciliazione/quietanze`, `POST /api/f24-riconciliazione/quietanze/upload-multiplo`, `GET /api/f24-riconciliazione/quietanze/{quietanza_id}`, `POST /api/f24-riconciliazione/riconcilia-quietanza`, `GET /api/f24-riconciliazione/verifica-codice/{codice_tributo}`

## `f24_analisi`

- **active / tenere** — `GET /api/f24-analisi/doppi-pagamenti` — in uso: chat
- **active / tenere** — `GET /api/f24-analisi/{f24_id}/associazione` — in uso: chat
- **quarantine / verificare** — `GET /api/f24-analisi/tabella`, `GET /api/f24-analisi/{f24_id}`

## `f24_email_settings`

- **active / tenere** — `POST /api/f24-email-settings/aggiungi-mittente` — in uso: FE
- **active / tenere** — `GET /api/f24-email-settings/impostazioni` — in uso: FE
- **active / tenere** — `POST /api/f24-email-settings/impostazioni` — in uso: FE
- **active / tenere** — `GET /api/f24-email-settings/log-scansioni` — in uso: FE
- **active / tenere** — `DELETE /api/f24-email-settings/rimuovi-mittente/{email}` — in uso: FE
- **active / tenere** — `POST /api/f24-email-settings/scan-manuale` — in uso: FE
- **active / tenere** — `GET /api/f24-email-settings/stato-sistema` — in uso: FE
- **active / tenere** — `POST /api/f24-email-settings/toggle-auto-scan` — in uso: FE

## `fatture_estera_verifica`

- **active / tenere** — `GET /api/fatture-estere/affidabilita` — in uso: FE
- **active / tenere** — `GET /api/fatture-estere/da-verificare` — in uso: FE
- **quarantine / verificare** — `POST /api/fatture-estere/{fattura_id}/verifica`

## `fatture_module.crud`

- **active / tenere** — `GET /api/fatture-ricevute/archivio` — in uso: FE
- **active / tenere** — `GET /api/fatture-ricevute/fattura/{fattura_id}` — in uso: FE, scheduler
- **active / tenere** — `PUT /api/fatture-ricevute/fattura/{fattura_id}` — in uso: FE, scheduler
- **active / tenere** — `GET /api/fatture-ricevute/fattura/{fattura_id}/documenti-pagamento` — in uso: FE
- **active / tenere** — `GET /api/fatture-ricevute/fattura/{fattura_id}/pdf/{allegato_id}` — in uso: FE
- **active / tenere** — `GET /api/fatture-ricevute/fattura/{fattura_id}/storia` — in uso: FE
- **active / tenere** — `GET /api/fatture-ricevute/fattura/{fattura_id}/view-assoinvoice` — in uso: FE
- **active / tenere** — `GET /api/fatture-ricevute/fattura/{fattura_id}/xml-originale` — in uso: FE
- **active / tenere** — `GET /api/fatture-ricevute/fornitori` — in uso: FE
- **active / tenere** — `POST /api/fatture-ricevute/pulisci-duplicati` — in uso: scheduler
- **quarantine / verificare** — `POST /api/fatture-ricevute/elimina-anni-vecchi`, `POST /api/fatture-ricevute/elimina-gusci-vuoti`, `GET /api/fatture-ricevute/statistiche`

## `fatture_module.export_selezione`

- **active / tenere** — `POST /api/fatture-ricevute/export-selezione` — in uso: FE

## `fatture_module.pagamento`

- **active / tenere** — `POST /api/fatture-ricevute/paga-manuale` — in uso: FE
- **quarantine / verificare** — `POST /api/fatture-ricevute/aggiorna-metodi-pagamento`, `POST /api/fatture-ricevute/cambia-metodo-pagamento`, `POST /api/fatture-ricevute/import-paypal`, `GET /api/fatture-ricevute/lista-paypal`, `POST /api/fatture-ricevute/riconcilia-con-estratto-conto`, `POST /api/fatture-ricevute/riconcilia-paypal`, `GET /api/fatture-ricevute/verifica-incoerenze-estratto-conto`
- **quarantine / admin-only** — `POST /api/fatture-ricevute/backfill-autoroute`

## `finanziamenti_soci`

- **active / tenere** — `POST /api/finanziamenti-soci/movimento` — in uso: FE
- **active / tenere** — `DELETE /api/finanziamenti-soci/movimento/{movimento_id}` — in uso: FE
- **active / tenere** — `GET /api/finanziamenti-soci/schede` — in uso: FE
- **quarantine / verificare** — `POST /api/finanziamenti-soci/scan`

## `finanziaria`

- **active / tenere** — `GET /api/finanziaria/summary` — in uso: FE
- **quarantine / verificare** — `GET /api/finanziaria/cost-categories`, `GET /api/finanziaria/costi`, `POST /api/finanziaria/costo`

## `fiscal_control`

- **active / tenere** — `GET /api/fiscal/ader-snapshots` — in uso: FE
- **active / tenere** — `POST /api/fiscal/ader-snapshots/dry-run` — in uso: FE
- **active / tenere** — `POST /api/fiscal/ader-snapshots/import` — in uso: FE
- **active / tenere** — `GET /api/fiscal/collections` — in uso: FE
- **active / tenere** — `GET /api/fiscal/collections/{claim_id}` — in uso: FE
- **active / tenere** — `POST /api/fiscal/collections/{claim_id}/events` — in uso: FE
- **active / tenere** — `GET /api/fiscal/crosswalk` — in uso: FE
- **active / tenere** — `GET /api/fiscal/declarations` — in uso: FE
- **active / tenere** — `GET /api/fiscal/documents/{document_id}/content` — in uso: FE
- **active / tenere** — `GET /api/fiscal/dossier.pdf` — in uso: FE
- **active / tenere** — `GET /api/fiscal/evidence-package.zip` — in uso: FE
- **active / tenere** — `GET /api/fiscal/evidence/{entity_type}/{entity_id}` — in uso: FE, scheduler
- **active / tenere** — `GET /api/fiscal/f24-rows` — in uso: FE
- **active / tenere** — `GET /api/fiscal/obligations` — in uso: FE
- **active / tenere** — `GET /api/fiscal/review` — in uso: FE
- **active / tenere** — `GET /api/fiscal/summary` — in uso: FE, chat
- **quarantine / verificare** — `POST /api/fiscal/collection-snapshots/dry-run`, `POST /api/fiscal/collection-snapshots/import`, `GET /api/fiscal/f24-documents`, `POST /api/fiscal/ravvedimento/calculate`, `POST /api/fiscal/vat-credit-chain/rebuild`

## `fiscalita_italiana`

- **active / tenere** — `POST /api/fiscalita/calendario/completa/{scadenza_id}` — in uso: FE
- **active / tenere** — `POST /api/fiscalita/calendario/riapri/{scadenza_id}` — in uso: FE
- **active / tenere** — `GET /api/fiscalita/calendario/scadenze-imminenti` — in uso: FE
- **active / tenere** — `GET /api/fiscalita/calendario/{anno}` — in uso: FE
- **active / tenere** — `GET /api/fiscalita/notifiche-scadenze` — in uso: FE
- **active / tenere** — `POST /api/fiscalita/notifiche-scadenze/invia` — in uso: FE
- **quarantine / verificare** — `GET /api/fiscalita/agevolazioni`, `POST /api/fiscalita/agevolazioni/simula`, `GET /api/fiscalita/agevolazioni/{agevolazione_id}`, `POST /api/fiscalita/f24/registra`, `GET /api/fiscalita/f24/storico`

## `fornitori_learning`

- **active / tenere** — `GET /api/fornitori-learning/centri-costo-disponibili` — in uso: FE
- **active / tenere** — `POST /api/fornitori-learning/classifica-ai` — in uso: FE
- **active / tenere** — `POST /api/fornitori-learning/classifica-da-contenuto` — in uso: FE
- **active / tenere** — `GET /api/fornitori-learning/lista` — in uso: FE
- **active / tenere** — `GET /api/fornitori-learning/non-classificati` — in uso: FE
- **active / tenere** — `POST /api/fornitori-learning/riclassifica-con-keywords` — in uso: FE
- **active / tenere** — `POST /api/fornitori-learning/salva` — in uso: FE
- **active / tenere** — `GET /api/fornitori-learning/stats` — in uso: FE
- **active / tenere** — `GET /api/fornitori-learning/suggerisci-keywords/{fornitore_nome}` — in uso: FE
- **quarantine / verificare** — `POST /api/fornitori-learning/associa-magazzino`, `POST /api/fornitori-learning/classifica-f24`, `GET /api/fornitori-learning/f24-statistiche`, `GET /api/fornitori-learning/giacenze-fornitore/{fornitore_nome}`, `GET /api/fornitori-learning/prodotti-per-fornitore/{fornitore_nome}`, `POST /api/fornitori-learning/riclassifica-f24/{f24_id}`, `DELETE /api/fornitori-learning/{fornitore_id}`

## `gestione_riservata`

- **active / tenere** — `POST /api/gestione-riservata/login` — in uso: FE
- **active / tenere** — `GET /api/gestione-riservata/movimenti` — in uso: FE
- **active / tenere** — `POST /api/gestione-riservata/movimenti` — in uso: FE
- **active / tenere** — `DELETE /api/gestione-riservata/movimenti/{movimento_id}` — in uso: FE
- **active / tenere** — `PUT /api/gestione-riservata/movimenti/{movimento_id}` — in uso: FE
- **active / tenere** — `GET /api/gestione-riservata/riepilogo` — in uso: FE, chat
- **quarantine / verificare** — `GET /api/gestione-riservata/volume-affari-reale`

## `invoices.corrispettivi`

- **active / tenere** — `GET /api/corrispettivi` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/aggiorna-stati-mancanti` — in uso: FE
- **active / tenere** — `DELETE /api/corrispettivi/all` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/auto-ricostruisci-dati` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/elimina-duplicati` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/hard-delete-bulk` — in uso: FE
- **active / tenere** — `DELETE /api/corrispettivi/hard-delete/{corrispettivo_id}` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/import-csv` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/manuale` — in uso: FE
- **active / tenere** — `GET /api/corrispettivi/manuali-senza-xml` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/normalizza-pagamenti` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/rebuild-prima-nota` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/ricalcola-annulli-non-riscosso` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/ricalcola-iva` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/sincronizza-prima-nota` — in uso: FE
- **active / tenere** — `GET /api/corrispettivi/template-csv` — in uso: FE
- **active / tenere** — `GET /api/corrispettivi/totals` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/upload-xml` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/upload-xml-bulk` — in uso: FE
- **active / tenere** — `POST /api/corrispettivi/upload-zip` — in uso: FE
- **active / tenere** — `GET /api/corrispettivi/view-by-filename` — in uso: FE
- **active / tenere** — `DELETE /api/corrispettivi/{corrispettivo_id}` — in uso: FE
- **active / tenere** — `GET /api/corrispettivi/{corrispettivo_id}/view` — in uso: FE
- **quarantine / admin-only** — `POST /api/corrispettivi/cleanup-duplicati-forte`

## `invoices.fatture_sync`

- **active / tenere** — `POST /api/fatture/sync/quadratura` — in uso: FE
- **active / tenere** — `GET /api/fatture/sync/status` — in uso: FE, scheduler
- **active / tenere** — `POST /api/fatture/sync/sync` — in uso: FE, scheduler

## `invoices.fatture_upload`

- **active / tenere** — `DELETE /api/fatture/all` — in uso: scheduler
- **active / tenere** — `POST /api/fatture/categorize-movements` — in uso: scheduler
- **active / tenere** — `POST /api/fatture/recalculate-iva` — in uso: scheduler
- **active / tenere** — `POST /api/fatture/sync-suppliers` — in uso: scheduler
- **active / tenere** — `POST /api/fatture/upload-xml` — in uso: scheduler
- **active / tenere** — `POST /api/fatture/upload-xml-bulk` — in uso: scheduler
- **active / tenere** — `DELETE /api/fatture/{invoice_id}` — in uso: FE, scheduler
- **active / tenere** — `GET /api/fatture/{invoice_id}` — in uso: FE, scheduler
- **active / tenere** — `PUT /api/fatture/{invoice_id}` — in uso: FE, scheduler
- **active / tenere** — `PUT /api/fatture/{invoice_id}/classifica` — in uso: FE, scheduler
- **active / tenere** — `GET /api/fatture/{invoice_id}/entita-correlate` — in uso: FE, scheduler
- **active / tenere** — `PUT /api/fatture/{invoice_id}/paga` — in uso: FE, scheduler

## `invoices.invoices_emesse`

- **active / tenere** — `GET /api/invoices/emesse` — in uso: FE
- **active / tenere** — `POST /api/invoices/emesse` — in uso: FE
- **active / tenere** — `DELETE /api/invoices/emesse/{invoice_id}` — in uso: FE
- **active / tenere** — `GET /api/invoices/emesse/{invoice_id}` — in uso: FE

## `invoices.invoices_main`

- **active / tenere** — `GET /api/invoices` — in uso: FE
- **active / tenere** — `GET /api/invoices/bank-pending` — in uso: FE
- **active / tenere** — `GET /api/invoices/by-month/{year}/{month}` — in uso: FE
- **active / tenere** — `GET /api/invoices/{invoice_id}` — in uso: FE

## `iva`

- **active / tenere** — `GET /api/iva/anomalie` — in uso: FE
- **active / tenere** — `GET /api/iva/dashboard/{anno}/{mese}` — in uso: FE
- **active / tenere** — `GET /api/iva/fatture` — in uso: FE, scheduler
- **active / tenere** — `GET /api/iva/fatture/non-utilizzate` — in uso: FE
- **active / tenere** — `POST /api/iva/fatture/{fid}/correggi-periodo` — in uso: FE
- **active / tenere** — `POST /api/iva/fatture/{fid}/escludi` — in uso: FE
- **active / tenere** — `POST /api/iva/fatture/{fid}/includi` — in uso: FE
- **active / tenere** — `POST /api/iva/fatture/{fid}/indetraibile` — in uso: FE
- **active / tenere** — `POST /api/iva/fatture/{fid}/recupero-annuale` — in uso: FE
- **active / tenere** — `POST /api/iva/fatture/{fid}/rinvia` — in uso: FE
- **active / tenere** — `GET /api/iva/liquidazioni` — in uso: FE
- **active / tenere** — `POST /api/iva/liquidazioni/calcola` — in uso: FE
- **active / tenere** — `POST /api/iva/liquidazioni/{liq_id}/conferma` — in uso: FE
- **active / tenere** — `POST /api/iva/liquidazioni/{liq_id}/rettifica` — in uso: FE
- **active / tenere** — `POST /api/iva/liquidazioni/{liq_id}/riapri` — in uso: FE
- **active / tenere** — `GET /api/iva/liquidazioni/{periodo}` — in uso: FE
- **active / tenere** — `GET /api/iva/riepilogo-annuale/{anno}` — in uso: FE
- **quarantine / verificare** — `POST /api/iva/ricalcola-attribuzione`, `GET /api/iva/ricalcola-attribuzione/ultimo`, `GET /api/iva/versamento/{anno}/{mese}`

## `learning_machine`

- **active / tenere** — `GET /api/learning-machine/dashboard` — in uso: FE
- **active / tenere** — `GET /api/learning-machine/regole-apprese` — in uso: FE
- **quarantine / verificare** — `GET /api/learning-machine/documenti`, `POST /api/learning-machine/feedback`, `POST /api/learning-machine/scan`, `GET /api/learning-machine/statistiche-feedback`
- **quarantine / admin-only** — `DELETE /api/learning-machine/reset-learning`

## `learning_universal`

- **active / tenere** — `GET /api/learning-universal/results` — in uso: FE
- **active / tenere** — `GET /api/learning-universal/status` — in uso: FE
- **active / tenere** — `POST /api/learning-universal/train/all` — in uso: FE
- **quarantine / verificare** — `POST /api/learning-universal/apply-suggestions`, `GET /api/learning-universal/suggestions/{module}`

## `legal_pages`

- **quarantine / verificare** — `GET /api/data-deletion`, `GET /api/privacy`, `GET /api/terms`, `GET /data-deletion`, `GET /privacy`, `GET /terms`

## `mfa`

- **active / tenere** — `POST /api/auth/mfa/disable` — in uso: FE
- **active / tenere** — `POST /api/auth/mfa/setup/confirm` — in uso: FE
- **active / tenere** — `POST /api/auth/mfa/setup/start` — in uso: FE
- **active / tenere** — `GET /api/auth/mfa/status` — in uso: FE
- **active / tenere** — `POST /api/auth/mfa/step-up` — in uso: FE
- **active / tenere** — `POST /api/auth/mfa/verify-login` — in uso: FE

## `multi_pagamento`

- **active / tenere** — `POST /api/pagamenti/registra` — in uso: FE, scheduler
- **quarantine / verificare** — `POST /api/pagamenti/assegno-multi-fatture`, `POST /api/pagamenti/fattura-multi-metodo`, `GET /api/pagamenti/fattura/{fattura_id}`, `GET /api/pagamenti/riepilogo-fornitore/{piva}`, `DELETE /api/pagamenti/{pagamento_id}`

## `mutui`

- **active / tenere** — `GET /api/mutui` — in uso: FE
- **active / tenere** — `GET /api/mutui/` — in uso: FE
- **active / tenere** — `POST /api/mutui/` — in uso: FE
- **active / tenere** — `POST /api/mutui/riconcilia` — in uso: FE
- **active / tenere** — `GET /api/mutui/statistiche/dashboard` — in uso: FE
- **active / tenere** — `DELETE /api/mutui/{mutuo_id}` — in uso: FE
- **active / tenere** — `GET /api/mutui/{mutuo_id}` — in uso: FE
- **active / tenere** — `PUT /api/mutui/{mutuo_id}` — in uso: FE
- **active / tenere** — `GET /api/mutui/{mutuo_id}/rate` — in uso: FE
- **active / tenere** — `PUT /api/mutui/{mutuo_id}/rate/{numero_rata}/riconcilia` — in uso: FE

## `mutui_parser`

- **active / tenere** — `POST /api/mutui/import-pdf` — in uso: FE
- **active / tenere** — `POST /api/mutui/parse-multiple` — in uso: FE
- **active / tenere** — `POST /api/mutui/parse-pdf` — in uso: FE

## `nexi_carta`

- **active / tenere** — `GET /api/nexi/stato` — in uso: FE
- **quarantine / verificare** — `GET /api/nexi/movimenti`, `POST /api/nexi/upload-pdf`, `POST /api/nexi/verifica`

## `noleggio`

- **active / tenere** — `POST /api/noleggio/associa-fornitore` — in uso: FE
- **active / tenere** — `GET /api/noleggio/drivers` — in uso: FE
- **active / tenere** — `GET /api/noleggio/export-pdf-costi` — in uso: FE
- **active / tenere** — `POST /api/noleggio/fatture/{fattura_id}/associa-veicolo` — in uso: FE
- **active / tenere** — `GET /api/noleggio/fornitori` — in uso: FE
- **active / tenere** — `GET /api/noleggio/veicoli` — in uso: FE
- **active / tenere** — `POST /api/noleggio/veicoli` — in uso: FE
- **active / tenere** — `DELETE /api/noleggio/veicoli/{targa}` — in uso: FE
- **active / tenere** — `PUT /api/noleggio/veicoli/{targa}` — in uso: FE
- **active / tenere** — `GET /api/noleggio/veicoli/{targa}/completo` — in uso: FE
- **quarantine / verificare** — `POST /api/noleggio/controllo-canoni`, `GET /api/noleggio/fatture-non-associate`, `GET /api/noleggio/riepilogo-controlli`, `GET /api/noleggio/verbali-dipendente`

## `openapi_automotive`

- **active / tenere** — `POST /api/openapi-automotive/aggiorna-veicolo` — in uso: FE
- **active / tenere** — `GET /api/openapi-automotive/info/{targa}` — in uso: FE
- **quarantine / verificare** — `GET /api/openapi-automotive/assicurazione/{targa}`, `GET /api/openapi-automotive/status`, `GET /api/openapi-automotive/veicoli-da-aggiornare`

## `openapi_imprese`

- **active / tenere** — `POST /api/openapi-imprese/aggiorna-fornitore` — in uso: FE
- **active / tenere** — `GET /api/openapi-imprese/cerca` — in uso: FE
- **active / tenere** — `GET /api/openapi-imprese/info/{partita_iva}` — in uso: FE
- **quarantine / verificare** — `GET /api/openapi-imprese/pec/{partita_iva}`, `GET /api/openapi-imprese/sdi/{partita_iva}`, `GET /api/openapi-imprese/status`

## `openapi_it`

- **active / tenere** — `GET /api/openapi/xbrl/bilancio/{request_id}` — in uso: FE
- **active / tenere** — `GET /api/openapi/xbrl/download/{request_id}` — in uso: FE
- **active / tenere** — `GET /api/openapi/xbrl/download/{request_id}/{tipo}` — in uso: FE
- **active / tenere** — `POST /api/openapi/xbrl/richiedi-bilancio` — in uso: FE
- **active / tenere** — `POST /api/openapi/xbrl/richiedi-riclassificato` — in uso: FE
- **active / tenere** — `GET /api/openapi/xbrl/status` — in uso: FE
- **active / tenere** — `GET /api/openapi/xbrl/storico-richieste` — in uso: FE
- **quarantine / verificare** — `POST /api/openapi/aisp/connetti-conto`, `GET /api/openapi/aisp/movimenti`, `GET /api/openapi/aisp/status`, `POST /api/openapi/visure/richiedi`

## `operazioni_module`

- **active / tenere** — `POST /api/operazioni-da-confermare/smart/ignora` — in uso: FE
- **active / tenere** — `POST /api/operazioni-da-confermare/smart/riconcilia-stipendio` — in uso: FE

## `operazioni_module.smart`

- **active / tenere** — `GET /api/operazioni-da-confermare/smart/analizza` — in uso: FE
- **active / tenere** — `GET /api/operazioni-da-confermare/smart/analizza-anomalie` — in uso: FE
- **active / tenere** — `GET /api/operazioni-da-confermare/smart/banca-veloce` — in uso: FE
- **active / tenere** — `GET /api/operazioni-da-confermare/smart/cerca-f24` — in uso: FE
- **active / tenere** — `GET /api/operazioni-da-confermare/smart/cerca-fatture` — in uso: FE
- **active / tenere** — `GET /api/operazioni-da-confermare/smart/cerca-stipendi` — in uso: FE
- **active / tenere** — `POST /api/operazioni-da-confermare/smart/conferma-f24` — in uso: FE
- **active / tenere** — `GET /api/operazioni-da-confermare/smart/movimento/{movimento_id}` — in uso: FE
- **active / tenere** — `POST /api/operazioni-da-confermare/smart/riconcilia-manuale` — in uso: FE

## `pagamenti_buoni`

- **quarantine / verificare** — `GET /api/pagamenti-buoni`, `POST /api/pagamenti-buoni/import`

## `pagopa`

- **active / tenere** — `POST /api/pagopa/auto-associa` — in uso: FE
- **active / tenere** — `GET /api/pagopa/ricevute` — in uso: FE
- **active / tenere** — `POST /api/pagopa/ricevute/associa-manuale` — in uso: FE
- **active / tenere** — `POST /api/pagopa/ricevute/upload` — in uso: FE
- **active / tenere** — `GET /api/pagopa/ricevute/{ricevuta_id}/pdf` — in uso: FE
- **active / tenere** — `GET /api/pagopa/stats` — in uso: FE
- **quarantine / verificare** — `POST /api/pagopa/cerca-movimenti-pagopa`, `GET /api/pagopa/movimenti-agenzia-entrate`

## `partite_aperte_api`

- **quarantine / verificare** — `GET /api/partite-aperte/lista`, `GET /api/partite-aperte/scadute`, `GET /api/partite-aperte/stats`

## `paypal_api`

- **active / tenere** — `GET /api/paypal-api/status` — in uso: FE, scheduler, chat
- **active / tenere** — `POST /api/paypal-api/sync` — in uso: FE
- **active / tenere** — `POST /api/paypal-api/sync/incremental` — in uso: FE
- **active / tenere** — `POST /api/paypal-api/sync/month` — in uso: FE
- **quarantine / verificare** — `GET /api/paypal-api/account-ids-non-mappati`, `POST /api/paypal-api/account/{paypal_account_id}/cerca-fattura-email`, `POST /api/paypal-api/crea-fornitore-e-mappa`, `POST /api/paypal-api/mappa-fornitore`, `GET /api/paypal-api/ricevuta-pdf/{transaction_id}`, `POST /api/paypal-api/riconcilia`, `POST /api/paypal-api/smappa-fornitore`, `POST /api/paypal-api/webhook`

## `paypal_statements`

- **active / tenere** — `POST /api/paypal-statements/auto-associa` — in uso: scheduler
- **active / tenere** — `GET /api/paypal-statements/bank-movements` — in uso: FE
- **active / tenere** — `GET /api/paypal-statements/dashboard` — in uso: FE
- **active / tenere** — `GET /api/paypal-statements/report` — in uso: FE
- **active / tenere** — `POST /api/paypal-statements/riprocessa` — in uso: FE
- **active / tenere** — `GET /api/paypal-statements/statements` — in uso: FE
- **active / tenere** — `GET /api/paypal-statements/transactions` — in uso: FE
- **active / tenere** — `PUT /api/paypal-statements/transactions/{transaction_id}/descrizione` — in uso: FE
- **quarantine / verificare** — `POST /api/paypal-statements/auto-cerca-gmail`, `POST /api/paypal-statements/import-all-local`, `POST /api/paypal-statements/import-csv`, `POST /api/paypal-statements/import-pdf`, `POST /api/paypal-statements/pulisci-match-solo-importo`, `POST /api/paypal-statements/riconcilia-banca`, `POST /api/paypal-statements/transazione/{transaction_id}/associa`, `GET /api/paypal-statements/transazione/{transaction_id}/cerca-gmail`, `GET /api/paypal-statements/transazione/{transaction_id}/dettaglio`

## `pianificazione`

- **quarantine / verificare** — `GET /api/pianificazione/costi-previsionali`, `POST /api/pianificazione/costi-previsionali`, `DELETE /api/pianificazione/costi-previsionali/{costo_id}`

## `pin_login`

- **active / tenere** — `POST /api/auth/pin-login` — in uso: FE
- **active / tenere** — `GET /api/auth/pin-login/health` — in uso: FE

## `pos_corrispettivi_check`

- **active / tenere** — `PUT /api/pos-corrispettivi/chiusura-giornaliera` — in uso: FE
- **active / tenere** — `GET /api/pos-corrispettivi/chiusura-giornaliera/audit` — in uso: FE
- **active / tenere** — `POST /api/pos-corrispettivi/chiusure-giornaliere/batch` — in uso: FE
- **active / tenere** — `GET /api/pos-corrispettivi/controllo-due-fasi` — in uso: FE
- **active / tenere** — `GET /api/pos-corrispettivi/riepilogo-mensile` — in uso: FE
- **active / tenere** — `GET /api/pos-corrispettivi/verifica-coerenza` — in uso: FE
- **quarantine / verificare** — `GET /api/pos-corrispettivi/alert-oggi`, `GET /api/pos-corrispettivi/anomalie-gravi`, `POST /api/pos-corrispettivi/riconcilia-pos-giorno`

## `previsioni_acquisti`

- **active / tenere** — `POST /api/previsioni-acquisti/popola-storico` — in uso: FE
- **active / tenere** — `GET /api/previsioni-acquisti/previsioni` — in uso: FE
- **active / tenere** — `GET /api/previsioni-acquisti/statistiche` — in uso: FE
- **quarantine / verificare** — `GET /api/previsioni-acquisti/confronto-ordine`, `GET /api/previsioni-acquisti/prodotti`

## `prima_nota_module`

- **active / tenere** — `GET /api/prima-nota/banca/template-csv` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/cassa/template-csv` — in uso: FE

## `prima_nota_module.banca`

- **active / tenere** — `GET /api/prima-nota/banca` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/banca` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/banca/analisi-righe-grezze` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/banca/candidati-per-fattura` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/banca/delete-all` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/banca/delete-by-source/{source}` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/banca/in-attesa-documento` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/banca/{movimento_id}` — in uso: FE
- **active / tenere** — `PUT /api/prima-nota/banca/{movimento_id}` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/banca/{movimento_id}/fattura` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/sumup` — in uso: FE

## `prima_nota_module.cassa`

- **active / tenere** — `GET /api/prima-nota/cassa` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/cassa` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/cassa/analisi-movimenti-bancari-errati` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/cassa/delete-all` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/cassa/delete-by-source/{source}` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/cassa/elimina-movimenti-bancari-errati` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/cassa/{movimento_id}` — in uso: FE
- **active / tenere** — `PUT /api/prima-nota/cassa/{movimento_id}` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/cassa/{movimento_id}/fattura` — in uso: FE

## `prima_nota_module.manutenzione`

- **active / tenere** — `POST /api/prima-nota/cassa/fix-corrispettivi-importo` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/cassa/verifica-entrate-corrispettivi` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/dedup-fatture` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/diagnostica-corrispettivi` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/diagnostica-metodi` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/sposta-movimento` — in uso: FE
- **quarantine / verificare** — `POST /api/prima-nota/annulla-associazione-fattura-banca`, `POST /api/prima-nota/arricchisci-pagamenti-banca`, `POST /api/prima-nota/collega-banca-estratto-conto`, `POST /api/prima-nota/collega-corrispettivi`, `POST /api/prima-nota/dedup-righe-estratto-conto`, `POST /api/prima-nota/fix-categories-and-duplicates`, `POST /api/prima-nota/fix-date-formato-italiano`, `POST /api/prima-nota/fix-tipo-movimento`, `POST /api/prima-nota/fix-versamenti-duplicati`, `GET /api/prima-nota/movimenti-ec-non-in-prima-nota`, `POST /api/prima-nota/recalculate-balances`, `POST /api/prima-nota/regenerate-from-invoices`, `POST /api/prima-nota/ripristina-fatture-movimento-cancellato`, `POST /api/prima-nota/ripristina-provvisori-metodo-errato`, `POST /api/prima-nota/unifica-categorie`, `GET /api/prima-nota/verifica-metodo-fattura/{fattura_id}`
- **quarantine / admin-only** — `POST /api/prima-nota/cleanup-orphan-movements`, `POST /api/prima-nota/migra-pos-accrediti-reali`, `POST /api/prima-nota/migrazione-pulisci-bancari-cassa`, `POST /api/prima-nota/pulizia-pre-anno`

## `prima_nota_module.operation_index`

- **active / tenere** — `GET /api/prima-nota/indice-operazioni` — in uso: FE
- **active / tenere** — `PUT /api/prima-nota/indice-operazioni/{movement_id}` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/indice-operazioni/{movement_id}/candidati` — in uso: FE

## `prima_nota_module.salari`

- **quarantine / verificare** — `GET /api/prima-nota/salari`, `POST /api/prima-nota/salari`, `GET /api/prima-nota/salari/stats`, `DELETE /api/prima-nota/salari/{movimento_id}`

## `prima_nota_module.stats`

- **active / tenere** — `GET /api/prima-nota/saldo-iniziale` — in uso: FE
- **active / tenere** — `PUT /api/prima-nota/saldo-iniziale` — in uso: FE
- **active / tenere** — `DELETE /api/prima-nota/saldo-iniziale/{tipo}/{anno}` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/stats` — in uso: FE
- **quarantine / verificare** — `GET /api/prima-nota/anni-disponibili`, `GET /api/prima-nota/export/excel`, `GET /api/prima-nota/saldi-finanziari`, `GET /api/prima-nota/saldo-finale`

## `prima_nota_module.sync`

- **active / tenere** — `POST /api/prima-nota/banca/sync-estratto-conto` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/cassa/crea-entrata-da-corrispettivo` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/cassa/sync-corrispettivi` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/cassa/sync-fatture-pagate` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/provvisori` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/annulla-auto-conferma` — in uso: FE
- **active / tenere** — `GET /api/prima-nota/provvisori/assegni-proposti` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/associa-assegno` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/attendi-banca` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/auto-conferma-per-metodo` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/conferma` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/conferma-divisione` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/conferma-multipla` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/da-decidere` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/provvisori/segnala-dubbio` — in uso: FE
- **active / tenere** — `POST /api/prima-nota/sposta-scrittura` — in uso: FE
- **quarantine / verificare** — `POST /api/prima-nota/collega-fatture`, `GET /api/prima-nota/corrispettivi-status`, `POST /api/prima-nota/import-batch`, `POST /api/prima-nota/movimento`, `POST /api/prima-nota/registra-fattura`, `POST /api/prima-nota/sposta-cassa-pagate-in-banca`, `POST /api/prima-nota/sync-corrispettivi`

## `public_api`

- **active / tenere** — `POST /api/assegni` — in uso: FE
- **active / tenere** — `GET /api/bank/statements` — in uso: FE
- **active / tenere** — `POST /api/bank/statements` — in uso: FE
- **active / tenere** — `GET /api/cash` — in uso: FE
- **active / tenere** — `POST /api/cash` — in uso: FE
- **active / tenere** — `GET /api/pianificazione/events` — in uso: FE
- **active / tenere** — `POST /api/pianificazione/events` — in uso: FE
- **active / tenere** — `GET /api/suppliers/{supplier_id}/inventory` — in uso: FE
- **active / tenere** — `GET /api/warehouse/products` — in uso: FE
- **active / tenere** — `POST /api/warehouse/products` — in uso: FE
- **active / tenere** — `DELETE /api/warehouse/products/{product_id}` — in uso: FE
- **active / tenere** — `PUT /api/warehouse/products/{product_id}` — in uso: FE
- **quarantine / verificare** — `GET /api/assegni-legacy`, `GET /api/dashboard/stats-legacy`, `GET /api/f24-public/alerts`, `GET /api/f24-public/dashboard`, `POST /api/portal/upload`, `GET /api/ricerca-globale`, `POST /api/suppliers-legacy`, `GET /api/v1/fatture`, `GET /api/v1/keys`, `POST /api/v1/keys/generate`, `GET /api/v1/movimenti`, `GET /api/v1/stats`, `GET /api/warehouse/movements`, `POST /api/warehouse/movements`

## `rapido`

- **active / tenere** — `POST /api/rapido/acconto-dipendente` — in uso: FE
- **active / tenere** — `POST /api/rapido/apporto-soci` — in uso: FE
- **active / tenere** — `POST /api/rapido/corrispettivo` — in uso: FE
- **active / tenere** — `GET /api/rapido/dipendenti-attivi` — in uso: FE, chat
- **active / tenere** — `POST /api/rapido/paga-fattura` — in uso: FE
- **active / tenere** — `POST /api/rapido/presenza` — in uso: FE
- **active / tenere** — `GET /api/rapido/ultimi-inserimenti` — in uso: FE
- **active / tenere** — `POST /api/rapido/versamento-banca` — in uso: FE

## `reports.dashboard`

- **active / tenere** — `GET /api/dashboard/fascia-energia` — in uso: FE
- **active / tenere** — `GET /api/dashboard/trend-mensile` — in uso: FE, chat
- **quarantine / verificare** — `GET /api/dashboard/bilancio-istantaneo`, `GET /api/dashboard/confronto-annuale`, `GET /api/dashboard/kpi`, `GET /api/dashboard/spese-per-categoria`, `GET /api/dashboard/stato-riconciliazione`, `GET /api/dashboard/stats`, `GET /api/dashboard/summary`

## `riconciliazione_stats_api`

- **quarantine / verificare** — `GET /api/riconciliazione/stats`

## `ritenute`

- **active / tenere** — `GET /api/ritenute` — in uso: FE
- **active / tenere** — `GET /api/ritenute/codici-ravvedimento` — in uso: FE
- **active / tenere** — `POST /api/ritenute/scan` — in uso: FE
- **active / tenere** — `GET /api/ritenute/verifica-caso-1040` — in uso: FE

## `scadenzario_fornitori`

- **active / tenere** — `GET /api/scadenzario-fornitori/` — in uso: FE
- **active / tenere** — `PUT /api/scadenzario-fornitori/aggiorna-scadenza` — in uso: FE
- **active / tenere** — `GET /api/scadenzario-fornitori/aging` — in uso: FE
- **active / tenere** — `GET /api/scadenzario-fornitori/cash-flow-previsionale` — in uso: FE
- **active / tenere** — `GET /api/scadenzario-fornitori/scadenze-integrate` — in uso: FE
- **active / tenere** — `GET /api/scadenzario-fornitori/urgenti` — in uso: FE

## `scadenze`

- **active / tenere** — `GET /api/scadenze` — in uso: FE
- **active / tenere** — `GET /api/scadenze/` — in uso: FE
- **active / tenere** — `PUT /api/scadenze/completa/{notifica_id}` — in uso: FE
- **active / tenere** — `POST /api/scadenze/crea` — in uso: FE
- **active / tenere** — `GET /api/scadenze/dashboard-widget` — in uso: FE
- **active / tenere** — `GET /api/scadenze/iva-mensile/{anno}` — in uso: FE
- **active / tenere** — `GET /api/scadenze/prossime` — in uso: FE
- **active / tenere** — `GET /api/scadenze/tutte` — in uso: FE
- **active / tenere** — `DELETE /api/scadenze/{notifica_id}` — in uso: FE

## `settings`

- **active / tenere** — `GET /api/settings` — in uso: FE
- **active / tenere** — `PUT /api/settings` — in uso: FE
- **quarantine / verificare** — `GET /api/settings/logo`, `POST /api/settings/logo`, `GET /api/settings/user-preferences`, `PUT /api/settings/user-preferences`

## `settings_router`

- **active / tenere** — `GET /api/settings/gmail` — in uso: FE
- **active / tenere** — `POST /api/settings/gmail` — in uso: FE
- **active / tenere** — `POST /api/settings/gmail/test` — in uso: FE
- **active / tenere** — `GET /api/settings/openai` — in uso: FE
- **active / tenere** — `POST /api/settings/openai` — in uso: FE
- **active / tenere** — `POST /api/settings/openai/test` — in uso: FE
- **quarantine / verificare** — `GET /api/settings/anthropic`, `POST /api/settings/anthropic`, `POST /api/settings/anthropic/test`

## `sumup`

- **active / tenere** — `GET /api/sumup/riepilogo` — in uso: FE
- **active / tenere** — `GET /api/sumup/stato` — in uso: FE
- **quarantine / verificare** — `POST /api/sumup/bonifica-accrediti-numia`, `GET /api/sumup/bonifica-pos-xml`, `POST /api/sumup/bonifica-pos-xml`, `POST /api/sumup/normalizza-descrizioni-pos`, `POST /api/sumup/sincronizza`

## `suppliers_module.base`

- **active / tenere** — `GET /api/suppliers` — in uso: FE
- **active / tenere** — `POST /api/suppliers` — in uso: FE
- **active / tenere** — `GET /api/suppliers/filtered` — in uso: FE
- **active / tenere** — `GET /api/suppliers/scadenze` — in uso: FE
- **active / tenere** — `GET /api/suppliers/search-piva/{partita_iva}` — in uso: FE
- **active / tenere** — `GET /api/suppliers/stats` — in uso: FE
- **active / tenere** — `DELETE /api/suppliers/{supplier_id}` — in uso: FE
- **active / tenere** — `GET /api/suppliers/{supplier_id}` — in uso: FE
- **active / tenere** — `PUT /api/suppliers/{supplier_id}` — in uso: FE
- **active / tenere** — `GET /api/suppliers/{supplier_id}/dati-da-fatture` — in uso: FE
- **active / tenere** — `GET /api/suppliers/{supplier_id}/fatturato` — in uso: FE
- **active / tenere** — `GET /api/suppliers/{supplier_id}/fatture` — in uso: FE
- **active / tenere** — `GET /api/suppliers/{supplier_id}/iban-from-invoices` — in uso: FE
- **active / tenere** — `PUT /api/suppliers/{supplier_id}/metodo-pagamento` — in uso: FE
- **active / tenere** — `PUT /api/suppliers/{supplier_id}/nome` — in uso: FE
- **active / tenere** — `POST /api/suppliers/{supplier_id}/toggle-active` — in uso: FE

## `suppliers_module.bulk`

- **active / tenere** — `POST /api/suppliers/aggiorna-metodi-bulk` — in uso: FE
- **active / tenere** — `POST /api/suppliers/aggiorna-tutti-bulk` — in uso: FE
- **active / tenere** — `POST /api/suppliers/correggi-nomi-mancanti` — in uso: FE
- **active / tenere** — `POST /api/suppliers/elimina-senza-fatture` — in uso: FE
- **active / tenere** — `POST /api/suppliers/ripara-sconosciuti` — in uso: FE
- **active / tenere** — `POST /api/suppliers/sincronizza-da-fatture` — in uso: FE

## `suppliers_module.iban`

- **active / tenere** — `POST /api/suppliers/ricerca-iban-singolo/{supplier_id}` — in uso: FE
- **active / tenere** — `POST /api/suppliers/ricerca-iban-web` — in uso: FE
- **active / tenere** — `POST /api/suppliers/sync-iban` — in uso: FE

## `suppliers_module.import_export`

- **active / tenere** — `POST /api/suppliers/import-excel` — in uso: FE
- **active / tenere** — `POST /api/suppliers/upload-excel` — in uso: FE

## `suppliers_module.validation`

- **active / tenere** — `POST /api/suppliers/aggiorna-dizionario-metodo` — in uso: FE
- **active / tenere** — `GET /api/suppliers/dizionario-metodi-pagamento` — in uso: FE
- **active / tenere** — `GET /api/suppliers/payment-methods` — in uso: FE
- **active / tenere** — `GET /api/suppliers/payment-terms` — in uso: FE
- **active / tenere** — `GET /api/suppliers/validazione-p0` — in uso: FE

## `sync_relazionale`

- **active / tenere** — `POST /api/sync/match-fatture-banca` — in uso: FE
- **active / tenere** — `POST /api/sync/match-fatture-cassa` — in uso: FE
- **active / tenere** — `GET /api/sync/stato-sincronizzazione` — in uso: FE
- **quarantine / verificare** — `GET /api/sync/fatture-cassa-dettaglio`, `POST /api/sync/sync-all-corrispettivi`, `POST /api/sync/sync-corrispettivo/{corrispettivo_id}`, `POST /api/sync/sync-fattura/{fattura_id}`, `PUT /api/sync/update-fattura-everywhere/{fattura_id}`

## `tfr`

- **active / tenere** — `GET /api/tfr/riepilogo-aziendale` — in uso: FE
- **active / tenere** — `GET /api/tfr/situazione/{dipendente_id}` — in uso: FE
- **quarantine / verificare** — `POST /api/tfr/accantonamento`, `POST /api/tfr/acconti`, `DELETE /api/tfr/acconti/{acconto_id}`, `PUT /api/tfr/acconti/{acconto_id}`, `POST /api/tfr/acconti/{acconto_id}/annulla-riconciliazione-banca`, `GET /api/tfr/acconti/{acconto_id}/candidati-banca`, `POST /api/tfr/acconti/{acconto_id}/riconcilia-banca`, `GET /api/tfr/acconti/{dipendente_id}`, `POST /api/tfr/calcola-batch/{anno}`, `POST /api/tfr/cedolini/{cedolino_id}/annulla-scalatura-acconti`, `GET /api/tfr/cedolini/{cedolino_id}/preview-scalatura-acconti`, `POST /api/tfr/cedolini/{cedolino_id}/scala-acconti`, `POST /api/tfr/liquidazione`, `GET /api/tfr/parse-payslips`, `GET /api/tfr/storico-tfr/{dipendente_id}`

## `utenti`

- **active / tenere** — `GET /api/utenti` — in uso: FE
- **active / tenere** — `POST /api/utenti` — in uso: FE
- **active / tenere** — `DELETE /api/utenti/{utente_id}` — in uso: FE
- **active / tenere** — `PUT /api/utenti/{utente_id}` — in uso: FE

## `verbali_noleggio`

- **active / tenere** — `POST /api/verbali-noleggio/associa-pdf/{numero_verbale:path}` — in uso: FE
- **active / tenere** — `POST /api/verbali-noleggio/correggi-importo/{numero_verbale:path}` — in uso: FE
- **active / tenere** — `POST /api/verbali-noleggio/correggi-trasgressore/{numero_verbale:path}` — in uso: FE
- **active / tenere** — `GET /api/verbali-noleggio/dettaglio/{numero_verbale}` — in uso: FE
- **active / tenere** — `GET /api/verbali-noleggio/pdf/{numero_verbale:path}` — in uso: FE
- **active / tenere** — `POST /api/verbali-noleggio/ricalcola-pdf/{numero_verbale:path}` — in uso: FE
- **active / tenere** — `GET /api/verbali-noleggio/verbali-completi` — in uso: chat

## `verbali_noleggio_api`

- **active / tenere** — `GET /api/verbali-noleggio/dettaglio/{numero_verbale:path}` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-noleggio/{verbale_id}/upload-quietanza` — in uso: scheduler

## `verbali_riconciliazione`

- **active / tenere** — `POST /api/verbali-riconciliazione/collega-driver-massivo` — in uso: FE, scheduler
- **active / tenere** — `GET /api/verbali-riconciliazione/dashboard` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-riconciliazione/import-partenopay` — in uso: scheduler
- **active / tenere** — `GET /api/verbali-riconciliazione/lista` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-riconciliazione/pulisci-duplicati` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-riconciliazione/riconcilia/{numero_verbale}` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-riconciliazione/scan-email` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-riconciliazione/scan-fatture-verbali` — in uso: FE, scheduler
- **active / tenere** — `POST /api/verbali-riconciliazione/scan-gmail-attendibili` — in uso: scheduler
- **quarantine / admin-only** — `POST /api/verbali-riconciliazione/migra-attesa-quietanza`

## `verifica_coerenza`

- **active / tenere** — `GET /api/verifica-coerenza/completa/{anno}` — in uso: FE
- **active / tenere** — `GET /api/verifica-coerenza/confronto-iva-completo/{anno}` — in uso: FE
- **active / tenere** — `GET /api/verifica-coerenza/iva/{anno}/{mese}` — in uso: FE
- **quarantine / verificare** — `GET /api/verifica-coerenza/discrepanze/{anno}`, `GET /api/verifica-coerenza/riepilogo-giornaliero`, `GET /api/verifica-coerenza/verifica-bonifici-vs-banca/{anno}`, `GET /api/verifica-coerenza/widget`

## `voci_bilancio`

- **active / tenere** — `POST /api/voci-bilancio/` — in uso: FE
- **active / tenere** — `GET /api/voci-bilancio/codici-disponibili` — in uso: FE
- **active / tenere** — `GET /api/voci-bilancio/{anno}` — in uso: FE
- **active / tenere** — `DELETE /api/voci-bilancio/{voce_id}` — in uso: FE

## `warehouse.dizionario_articoli`

- **active / tenere** — `PUT /api/dizionario-articoli/articolo/{descrizione_encoded}` — in uso: FE
- **active / tenere** — `POST /api/dizionario-articoli/riclassifica-completo` — in uso: FE
- **quarantine / verificare** — `POST /api/dizionario-articoli/categorizza-ai`, `GET /api/dizionario-articoli/cerca`, `GET /api/dizionario-articoli/dizionario`, `GET /api/dizionario-articoli/estrai-articoli`, `POST /api/dizionario-articoli/genera-dizionario`, `GET /api/dizionario-articoli/non-classificati`, `POST /api/dizionario-articoli/ricategorizza-fatture`, `GET /api/dizionario-articoli/statistiche`
- **quarantine / admin-only** — `DELETE /api/dizionario-articoli/reset-dizionario`

## `whatsapp_webhook`

- **quarantine / verificare** — `POST /api/whatsapp/send`, `POST /api/whatsapp/send-test`, `GET /api/whatsapp/status`, `GET /api/whatsapp/webhook`, `POST /api/whatsapp/webhook`
