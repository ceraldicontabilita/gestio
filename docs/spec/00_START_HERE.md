# START HERE — Gestio Rebuild Kit

Questo ZIP è il contratto di ricostruzione pulita di Gestio.
Non contiene dati reali, credenziali, allegati fiscali o una copia del vecchio codice.

## Contenuto verificato

- 65 pagine canoniche con logica, API, stato UI, handler, fonti e test;
- 65 contratti logici JSON (`03_PAGINE/LOGICA_JSON/`), uno per pagina;
- 36 popup mappati;
- 1140 endpoint classificati (737 attivi, 403 quarantena come decision log);
- 164 variabili senza valori segreti;
- 22 tabelle/registri canonici del database applicativo;
- fingerprint fonti: `4b6ea6e27c9ce4a487a5847a3312a56ce2ff7e15d6b2b7e83107fa414c521daa`.

Adattamento per il repository `gestio`: rispetto al kit originale sono
esclusi MongoDB e Google Sheets come registro/persistenza. Il target usa un
unico database PostgreSQL (gestito su Render) e storage file locale per gli
originali. Google Drive resta ammesso come *fonte* da cui importare i
documenti (cartelle configurate, sola lettura), non come archivio: vedi
`02_ARCHITETTURA/ARCHITETTURA.md`. Sono state rimosse anche le parti
morte/ridondanti del kit:
60 variabili Mongo/Drive dall'inventario, la mappa tecnica duplicata
`03_PAGINE/MAPPE_JSON/` (assorbita dalle schede pagina e da `LOGICA_JSON/`),
le mappe in quarantena e la documentazione di audit del vecchio repository
in `08_RIFERIMENTI_CONTESTO/` (restano solo i riferimenti fiscali di
dominio: piano dei conti, IVA, F24/cedolini, libro mastro, fornitori).

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
