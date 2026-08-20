# Indice delle 65 pagine

Ogni pagina ha una scheda Markdown leggibile e un contratto JSON macchina con la stessa logica.

| # | Pagina | Route | Modulo | Accesso | Scheda | JSON |
|---:|---|---|---|---|---|---|
| 1 | Login | `/login` | `accesso` | `public` | [01-login.md](01-login.md) | [01-login.json](LOGICA_JSON/01-login.json) |
| 2 | Gestione riservata | `/gestione-riservata` | `accesso` | `reserved` | [02-gestione-riservata.md](02-gestione-riservata.md) | [02-gestione-riservata.json](LOGICA_JSON/02-gestione-riservata.json) |
| 3 | Dashboard | `/` | `dashboard` | `authenticated` | [03-dashboard.md](03-dashboard.md) | [03-dashboard.json](LOGICA_JSON/03-dashboard.json) |
| 4 | Inserimento rapido | `/rapido` | `dashboard` | `authenticated` | [04-inserimento-rapido.md](04-inserimento-rapido.md) | [04-inserimento-rapido.json](LOGICA_JSON/04-inserimento-rapido.json) |
| 5 | Archivio fatture | `/fatture` | `fatture` | `authenticated` | [05-fatture.md](05-fatture.md) | [05-fatture.json](LOGICA_JSON/05-fatture.json) |
| 6 | Corrispettivi | `/fatture/corrispettivi` | `fatture` | `authenticated` | [06-corrispettivi.md](06-corrispettivi.md) | [06-corrispettivi.json](LOGICA_JSON/06-corrispettivi.json) |
| 7 | Fornitori | `/fornitori` | `fornitori` | `authenticated` | [07-fornitori.md](07-fornitori.md) | [07-fornitori.json](LOGICA_JSON/07-fornitori.json) |
| 8 | Prima Nota | `/prima-nota` | `prima-nota` | `authenticated` | [08-prima-nota.md](08-prima-nota.md) | [08-prima-nota.json](LOGICA_JSON/08-prima-nota.json) |
| 9 | Pulizia Prima Nota | `/prima-nota/pulizia` | `prima-nota` | `authenticated` | [09-prima-nota-pulizia.md](09-prima-nota-pulizia.md) | [09-prima-nota-pulizia.json](LOGICA_JSON/09-prima-nota-pulizia.json) |
| 10 | Cedolini e salari | `/salari` | `personale` | `authenticated` | [10-salari.md](10-salari.md) | [10-salari.json](LOGICA_JSON/10-salari.json) |
| 11 | Flotta noleggio | `/noleggio` | `noleggio` | `authenticated` | [11-noleggio-flotta.md](11-noleggio-flotta.md) | [11-noleggio-flotta.json](LOGICA_JSON/11-noleggio-flotta.json) |
| 12 | Verbali noleggio | `/noleggio/verbali` | `noleggio` | `authenticated` | [12-noleggio-verbali.md](12-noleggio-verbali.md) | [12-noleggio-verbali.json](LOGICA_JSON/12-noleggio-verbali.json) |
| 13 | Costi noleggio | `/noleggio/costi` | `noleggio` | `authenticated` | [13-noleggio-costi.md](13-noleggio-costi.md) | [13-noleggio-costi.json](LOGICA_JSON/13-noleggio-costi.json) |
| 14 | Dettaglio verbale | `/verbali-noleggio/:identificativo` | `noleggio` | `authenticated` | [14-dettaglio-verbale.md](14-dettaglio-verbale.md) | [14-dettaglio-verbale.json](LOGICA_JSON/14-dettaglio-verbale.json) |
| 15 | Piano dei Conti | `/contabilita` | `contabilita` | `authenticated` | [15-contabilita-piano-conti.md](15-contabilita-piano-conti.md) | [15-contabilita-piano-conti.json](LOGICA_JSON/15-contabilita-piano-conti.json) |
| 16 | Bilancio | `/contabilita/bilancio` | `contabilita` | `authenticated` | [16-contabilita-bilancio.md](16-contabilita-bilancio.md) | [16-contabilita-bilancio.json](LOGICA_JSON/16-contabilita-bilancio.json) |
| 17 | Verifica Bilancio | `/contabilita/verifica` | `contabilita` | `authenticated` | [17-contabilita-verifica.md](17-contabilita-verifica.md) | [17-contabilita-verifica.json](LOGICA_JSON/17-contabilita-verifica.json) |
| 18 | Libro Giornale | `/contabilita/giornale` | `contabilita` | `authenticated` | [18-contabilita-giornale.md](18-contabilita-giornale.md) | [18-contabilita-giornale.json](LOGICA_JSON/18-contabilita-giornale.json) |
| 19 | Controllo mensile | `/contabilita/controllo` | `contabilita` | `authenticated` | [19-contabilita-controllo.md](19-contabilita-controllo.md) | [19-contabilita-controllo.json](LOGICA_JSON/19-contabilita-controllo.json) |
| 20 | Calendario fiscale | `/contabilita/calendario` | `contabilita` | `authenticated` | [20-contabilita-calendario.md](20-contabilita-calendario.md) | [20-contabilita-calendario.json](LOGICA_JSON/20-contabilita-calendario.json) |
| 21 | Cespiti | `/contabilita/cespiti` | `contabilita` | `authenticated` | [21-contabilita-cespiti.md](21-contabilita-cespiti.md) | [21-contabilita-cespiti.json](LOGICA_JSON/21-contabilita-cespiti.json) |
| 22 | Finanziaria | `/contabilita/finanziaria` | `contabilita` | `authenticated` | [22-contabilita-finanziaria.md](22-contabilita-finanziaria.md) | [22-contabilita-finanziaria.json](LOGICA_JSON/22-contabilita-finanziaria.json) |
| 23 | Chiusura esercizio | `/contabilita/chiusura` | `contabilita` | `authenticated` | [23-contabilita-chiusura.md](23-contabilita-chiusura.md) | [23-contabilita-chiusura.json](LOGICA_JSON/23-contabilita-chiusura.json) |
| 24 | Budget | `/contabilita/budget` | `contabilita` | `authenticated` | [24-contabilita-budget.md](24-contabilita-budget.md) | [24-contabilita-budget.json](LOGICA_JSON/24-contabilita-budget.json) |
| 25 | Mutui | `/contabilita/mutui` | `contabilita` | `authenticated` | [25-contabilita-mutui.md](25-contabilita-mutui.md) | [25-contabilita-mutui.json](LOGICA_JSON/25-contabilita-mutui.json) |
| 26 | Contabilita avanzata | `/contabilita/avanzata` | `contabilita` | `authenticated` | [26-contabilita-avanzata.md](26-contabilita-avanzata.md) | [26-contabilita-avanzata.json](LOGICA_JSON/26-contabilita-avanzata.json) |
| 27 | Utile obiettivo | `/contabilita/utile` | `contabilita` | `authenticated` | [27-contabilita-utile.md](27-contabilita-utile.md) | [27-contabilita-utile.json](LOGICA_JSON/27-contabilita-utile.json) |
| 28 | Previsioni acquisti | `/contabilita/previsioni-acquisti` | `contabilita` | `authenticated` | [28-contabilita-previsioni-acquisti.md](28-contabilita-previsioni-acquisti.md) | [28-contabilita-previsioni-acquisti.json](LOGICA_JSON/28-contabilita-previsioni-acquisti.json) |
| 29 | Learning Machine | `/learning-machine` | `strumenti` | `authenticated` | [29-learning-machine.md](29-learning-machine.md) | [29-learning-machine.json](LOGICA_JSON/29-learning-machine.json) |
| 30 | Scadenze | `/scadenze` | `contabilita` | `authenticated` | [30-scadenze.md](30-scadenze.md) | [30-scadenze.json](LOGICA_JSON/30-scadenze.json) |
| 31 | Ritenute | `/ritenute` | `personale` | `authenticated` | [31-ritenute.md](31-ritenute.md) | [31-ritenute.json](LOGICA_JSON/31-ritenute.json) |
| 32 | Riconciliazione dashboard | `/riconciliazione` | `riconciliazione` | `authenticated` | [32-riconciliazione-bancaria.md](32-riconciliazione-bancaria.md) | [32-riconciliazione-bancaria.json](LOGICA_JSON/32-riconciliazione-bancaria.json) |
| 33 | Riconciliazione banca | `/riconciliazione/banca` | `riconciliazione` | `authenticated` | [33-riconciliazione-banca.md](33-riconciliazione-banca.md) | [33-riconciliazione-banca.json](LOGICA_JSON/33-riconciliazione-banca.json) |
| 34 | Riconciliazione F24 | `/riconciliazione/f24` | `riconciliazione` | `authenticated` | [34-riconciliazione-f24.md](34-riconciliazione-f24.md) | [34-riconciliazione-f24.json](LOGICA_JSON/34-riconciliazione-f24.json) |
| 35 | Riconciliazione stipendi | `/riconciliazione/stipendi` | `riconciliazione` | `authenticated` | [35-riconciliazione-stipendi.md](35-riconciliazione-stipendi.md) | [35-riconciliazione-stipendi.json](LOGICA_JSON/35-riconciliazione-stipendi.json) |
| 36 | Riconciliazione documenti | `/riconciliazione/documenti` | `riconciliazione` | `authenticated` | [36-riconciliazione-documenti.md](36-riconciliazione-documenti.md) | [36-riconciliazione-documenti.json](LOGICA_JSON/36-riconciliazione-documenti.json) |
| 37 | Archivio bonifici | `/riconciliazione/archivio-bonifici` | `riconciliazione` | `authenticated` | [37-archivio-bonifici.md](37-archivio-bonifici.md) | [37-archivio-bonifici.json](LOGICA_JSON/37-archivio-bonifici.json) |
| 38 | Assegni | `/riconciliazione/assegni` | `riconciliazione` | `authenticated` | [38-assegni.md](38-assegni.md) | [38-assegni.json](LOGICA_JSON/38-assegni.json) |
| 39 | PayPal | `/riconciliazione/paypal` | `riconciliazione` | `authenticated` | [39-riconciliazione-paypal.md](39-riconciliazione-paypal.md) | [39-riconciliazione-paypal.json](LOGICA_JSON/39-riconciliazione-paypal.json) |
| 40 | Coerenza POS | `/riconciliazione/coerenza-pos` | `riconciliazione` | `authenticated` | [40-coerenza-pos.md](40-coerenza-pos.md) | [40-coerenza-pos.json](LOGICA_JSON/40-coerenza-pos.json) |
| 41 | Import documenti | `/documenti/import` | `documenti` | `authenticated` | [41-documenti-import.md](41-documenti-import.md) | [41-documenti-import.json](LOGICA_JSON/41-documenti-import.json) |
| 42 | Archivio documenti | `/documenti/archivio` | `documenti` | `authenticated` | [42-documenti-archivio.md](42-documenti-archivio.md) | [42-documenti-archivio.json](LOGICA_JSON/42-documenti-archivio.json) |
| 43 | Verifica coerenza | `/strumenti` | `strumenti` | `authenticated` | [43-strumenti-verifica.md](43-strumenti-verifica.md) | [43-strumenti-verifica.json](LOGICA_JSON/43-strumenti-verifica.json) |
| 44 | Movimenti banca | `/riconciliazione/movimenti-banca` | `riconciliazione` | `authenticated` | [44-strumenti-movimenti-banca.md](44-strumenti-movimenti-banca.md) | [44-strumenti-movimenti-banca.json](LOGICA_JSON/44-strumenti-movimenti-banca.json) |
| 45 | Commercialista | `/strumenti/commercialista` | `strumenti` | `authenticated` | [45-strumenti-commercialista.md](45-strumenti-commercialista.md) | [45-strumenti-commercialista.json](LOGICA_JSON/45-strumenti-commercialista.json) |
| 46 | Pianificazione | `/strumenti/pianificazione` | `strumenti` | `authenticated` | [46-strumenti-pianificazione.md](46-strumenti-pianificazione.md) | [46-strumenti-pianificazione.json](LOGICA_JSON/46-strumenti-pianificazione.json) |
| 47 | Visure | `/strumenti/visure` | `strumenti` | `authenticated` | [47-strumenti-visure.md](47-strumenti-visure.md) | [47-strumenti-visure.json](LOGICA_JSON/47-strumenti-visure.json) |
| 48 | Agenti AI | `/agenti` | `strumenti` | `authenticated` | [48-agenti.md](48-agenti.md) | [48-agenti.json](LOGICA_JSON/48-agenti.json) |
| 49 | Impostazioni F24 email | `/impostazioni-f24-email` | `integrazioni` | `authenticated` | [49-impostazioni-f24-email.md](49-impostazioni-f24-email.md) | [49-impostazioni-f24-email.json](LOGICA_JSON/49-impostazioni-f24-email.json) |
| 50 | Impostazioni AI | `/impostazioni-ai` | `integrazioni` | `admin` | [50-impostazioni-ai.md](50-impostazioni-ai.md) | [50-impostazioni-ai.json](LOGICA_JSON/50-impostazioni-ai.json) |
| 51 | Integrazione OpenAPI | `/integrazioni` | `integrazioni` | `authenticated` | [51-integrazioni-openapi.md](51-integrazioni-openapi.md) | [51-integrazioni-openapi.json](LOGICA_JSON/51-integrazioni-openapi.json) |
| 52 | Riconciliazione PagoPA | `/riconciliazione/pagopa` | `riconciliazione` | `authenticated` | [52-integrazioni-pagopa.md](52-integrazioni-pagopa.md) | [52-integrazioni-pagopa.json](LOGICA_JSON/52-integrazioni-pagopa.json) |
| 53 | Mittenti Email attendibili | `/integrazioni/mittenti-email` | `integrazioni` | `authenticated` | [53-integrazioni-mittenti-email.md](53-integrazioni-mittenti-email.md) | [53-integrazioni-mittenti-email.json](LOGICA_JSON/53-integrazioni-mittenti-email.json) |
| 54 | Admin sistema | `/admin` | `admin` | `admin` | [54-admin.md](54-admin.md) | [54-admin.json](LOGICA_JSON/54-admin.json) |
| 55 | Admin MFA | `/admin/mfa` | `admin` | `admin` | [55-admin-mfa.md](55-admin-mfa.md) | [55-admin-mfa.json](LOGICA_JSON/55-admin-mfa.json) |
| 56 | Elaborazioni amministrative | `/admin/elaborazioni` | `admin` | `admin` | [56-admin-batch-reprocessing.md](56-admin-batch-reprocessing.md) | [56-admin-batch-reprocessing.json](LOGICA_JSON/56-admin-batch-reprocessing.json) |
| 57 | Elaborazioni legacy | `/admin/batch-processor` | `admin` | `admin` | [57-admin-batch-processor.md](57-admin-batch-processor.md) | [57-admin-batch-processor.json](LOGICA_JSON/57-admin-batch-processor.json) |
| 58 | Utenti | `/utenti` | `admin` | `admin` | [58-utenti.md](58-utenti.md) | [58-utenti.json](LOGICA_JSON/58-utenti.json) |
| 59 | Mappa gestionale | `/mappa-gestionale` | `strumenti` | `authenticated` | [59-mappa-gestionale.md](59-mappa-gestionale.md) | [59-mappa-gestionale.json](LOGICA_JSON/59-mappa-gestionale.json) |
| 60 | Gestione IVA | `/iva` | `contabilita` | `authenticated` | [60-iva.md](60-iva.md) | [60-iva.json](LOGICA_JSON/60-iva.json) |
| 61 | Verifica fatture estere | `/fatture-estere-verifica` | `fatture` | `authenticated` | [61-fatture-estere-verifica.md](61-fatture-estere-verifica.md) | [61-fatture-estere-verifica.json](LOGICA_JSON/61-fatture-estere-verifica.json) |
| 62 | Dati ISA | `/contabilita/dati-isa` | `contabilita` | `authenticated` | [62-contabilita-dati-isa.md](62-contabilita-dati-isa.md) | [62-contabilita-dati-isa.json](LOGICA_JSON/62-contabilita-dati-isa.json) |
| 63 | Indice documentale | `/documenti/indice` | `documenti` | `authenticated` | [63-documenti-indice.md](63-documenti-indice.md) | [63-documenti-indice.json](LOGICA_JSON/63-documenti-indice.json) |
| 64 | Atti amministrativi | `/documenti/atti` | `documenti` | `authenticated` | [64-documenti-atti.md](64-documenti-atti.md) | [64-documenti-atti.json](LOGICA_JSON/64-documenti-atti.json) |
| 65 | Situazione fiscale | `/situazione-fiscale` | `contabilita` | `authenticated` | [65-situazione-fiscale.md](65-situazione-fiscale.md) | [65-situazione-fiscale.json](LOGICA_JSON/65-situazione-fiscale.json) |
