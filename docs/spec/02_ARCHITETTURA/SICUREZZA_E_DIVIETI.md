# Sicurezza, divieti e confini operativi

- Auth fail-closed, cookie sicuri, CSRF quando necessario, RBAC per ruolo e
  rate limit; endpoint amministrativi mai accessibili per semplice login.
- Segreti soltanto nel secret store; log, ZIP, fogli e API non li restituiscono.
- Non eseguire pagamenti automatici.
- Non eliminare/spostare email o documenti originali senza conferma esplicita.
- Non applicare associazioni definitive quando identità o provenienza sono ambigue.
- Non introdurre MongoDB o Google Drive/Sheets come backend applicativo.
- Non deduplicare per solo importo, data, nome file o fornitore.
- Non mostrare errori come dati zero e non dichiarare riuscito un flusso per HTTP 200.
- Ogni mutazione conserva attore, timestamp, prima/dopo, motivo e rollback.
