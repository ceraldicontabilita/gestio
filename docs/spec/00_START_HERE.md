# START HERE — Gestio Rebuild Kit

Questo ZIP è il contratto di ricostruzione pulita di Gestio.
Non contiene dati reali, credenziali, allegati fiscali o una copia del vecchio codice.

## Contenuto verificato

- 65 pagine canoniche con logica, API, stato UI, handler, fonti e test;
- 36 popup mappati;
- 1140 endpoint classificati, inclusi quelli in quarantena;
- 224 variabili senza valori segreti;
- 22 tabelle/registri canonici del database applicativo;
- fingerprint fonti: `0c0fbc2c05f1fcb851823adc2f5d3e914f540a25db0ede76bf8d83933c6bf755`.

Adattamento per il repository `gestio`: rispetto al kit originale sono
esclusi MongoDB e Google Drive/Sheets come persistenza. Il target usa un
unico database SQL monoutente (SQLite) e storage file locale per gli
originali. I riferimenti a Drive/Mongo rimasti in appendici e mappe
tecniche descrivono il codice legacy come inventario storico, non il
target da costruire (vedi nota nelle rispettive appendici).

## Ordine di lettura

1. `00_PROMPT_DA_INCOLLARE.txt`
2. `01_MASTER/PROMPT_MASTER.md`
3. `02_ARCHITETTURA/`
4. `03_PAGINE/INDICE_PAGINE.md` e le schede pagina
5. `04_POPUP/INDICE_POPUP.md`
6. `05_API/ENDPOINTS.md`
7. `06_CONFIG/`
8. `07_TEST_E_ACCETTAZIONE/`

## Regola di autorità

Il Prompt Master è normativo. Le schede pagina e gli inventari macchina sono
completezza tecnica. I riferimenti di contesto sono subordinati e non devono
reintrodurre pipeline, endpoint o persistenze in quarantena, né MongoDB o
Google Drive/Sheets come backend applicativo.
