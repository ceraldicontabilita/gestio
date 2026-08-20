# Riferimenti correnti e di contesto

Questi documenti completano il dominio ma non prevalgono sul Prompt Master.
Le descrizioni di implementazioni transitorie servono a evitare regressioni,
non autorizzano a ricreare il database applicativo, pipeline duplicate o
endpoint in quarantena.

Molti di questi file descrivono ancora, come cronaca tecnica del codice
legacy, MongoDB e Google Drive/Sheets come backend attivo o in migrazione.
Per il target `gestio` questi riferimenti sono storici: il backend è un
unico database SQL monoutente (SQLite) con storage file locale per gli
originali, senza MongoDB né Google Drive/Sheets. In caso di conflitto tra
questi appunti e `01_MASTER/PROMPT_MASTER.md`, vince il Prompt Master.
