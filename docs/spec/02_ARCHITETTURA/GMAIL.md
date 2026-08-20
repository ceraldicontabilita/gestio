# Gmail — flusso completo

## Gmail

1. Ricerca `in:anywhere`, paginazione completa, alias mittente e wrapper PEC.
2. Conserva Gmail message ID, thread ID, Message-ID RFC, etichette, mittente,
   destinatari, data, oggetto, corpo, raw EML quando autorizzato e allegati.
3. SHA-256 su ogni allegato; doppio ingest idempotente.
4. Scheduler `Europe/Rome`, lock distribuito, watermark e retry con backoff.
5. Non spostare, eliminare, segnare come letta o alterare l'email originale.
6. PartenoPay: targa + data/ora + storico assegnazione; mai importo da solo.
7. Ambiguità: `Scegli driver`, `Scegli verbale`, `Scegli fattura`.

## Archiviazione degli allegati

1. Ogni allegato acquisito viene salvato sullo storage file dell'applicazione
   (percorso locale/volume dedicato) e mai modificato dopo l'acquisizione.
2. Il database applicativo indicizza ogni file per identificativo interno,
   nome, MIME, dimensione, SHA-256 calcolato, percorso e provenienza (Gmail
   message ID/thread ID o canale di import).
3. Duplicato solo con hash binario esatto; nome o dimensione non bastano.
4. Nessuna pulizia dello storage senza anteprima, target esatti e autorizzazione.
5. Eliminazione recuperabile (soft-delete), mai cancellazione permanente automatica.
6. Credenziali e configurazione dei canali stanno nella configurazione, non nel codice.

## Cartelle minime

`REGISTRO DATI`, `PARTENOPAY`, `CODICI TRIBUTO`, `QUIETANZE`, `DICHIARAZIONI`
restano le categorie logiche degli archivi nel database applicativo; non
corrispondono più a cartelle Drive.
