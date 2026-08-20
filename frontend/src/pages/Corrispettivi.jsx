import { useCallback, useEffect, useState } from 'react'
import { getCorrispettivi, importaCorrispettivo, sincronizzaDriveCorrispettivi } from '../api.js'

function formatEuro(valore) {
  return new Intl.NumberFormat('it-IT', { style: 'currency', currency: 'EUR' }).format(valore)
}

function formatData(valore) {
  const [anno, mese, giorno] = valore.split('-')
  return `${giorno}/${mese}/${anno}`
}

export default function Corrispettivi() {
  const [giornate, setGiornate] = useState([])
  const [loading, setLoading] = useState(true)
  const [errore, setErrore] = useState(null)
  const [caricamento, setCaricamento] = useState(false)
  const [sync, setSync] = useState({ stato: 'inattivo', messaggio: null })

  const carica = useCallback(async () => {
    setLoading(true)
    setErrore(null)
    try {
      setGiornate(await getCorrispettivi())
    } catch (err) {
      setErrore(err.message)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    carica()
  }, [carica])

  async function onFileSelezionato(event) {
    const file = event.target.files?.[0]
    if (!file) return
    setCaricamento(true)
    setErrore(null)
    try {
      await importaCorrispettivo(file)
      await carica()
    } catch (err) {
      setErrore(err.message)
    } finally {
      setCaricamento(false)
      event.target.value = ''
    }
  }

  async function sincronizza() {
    setSync({ stato: 'in-corso', messaggio: null })
    try {
      const risultato = await sincronizzaDriveCorrispettivi()
      setSync({
        stato: 'ok',
        messaggio: `${risultato.importati} nuovi, ${risultato.gia_presenti} già presenti su ${risultato.trovati} file trovati su Drive.`,
      })
      await carica()
    } catch (err) {
      setSync({ stato: 'non-configurato', messaggio: err.message })
    }
  }

  return (
    <main className="page">
      <h1 className="page-title">Corrispettivi</h1>
      <p className="page-subtitle">
        Giornate RT (Agenzia delle Entrate): quota contanti in Cassa, quota elettronica come credito
        POS atteso in Banca.
      </p>

      <div className="sync-panel">
        <div>
          <strong>Import automatico da Google Drive</strong>
          <div className="sync-info">
            {sync.stato === 'non-configurato'
              ? sync.messaggio
              : sync.messaggio ?? 'Legge la cartella Drive condivisa e importa gli XML nuovi.'}
          </div>
        </div>
        <button className="btn btn-secondary" onClick={sincronizza} disabled={sync.stato === 'in-corso'}>
          {sync.stato === 'in-corso' ? 'Sincronizzazione…' : 'Sincronizza ora'}
        </button>
      </div>

      <label className="file-input-label">
        <span>Oppure importa manualmente un XML corrispettivi RT</span>
        <input type="file" accept=".xml" onChange={onFileSelezionato} disabled={caricamento} />
      </label>

      {errore && <p className="alert alert-error">Errore: {errore}</p>}
      {loading && <p className="state-message">Caricamento…</p>}
      {!loading && giornate.length === 0 && <p className="state-message">Nessuna giornata importata.</p>}

      {giornate.map((g) => (
        <section key={g.id} className="card">
          <header className="card-header">
            <span>
              {formatData(g.data_rilevazione)} — {g.id_dispositivo}
            </span>
            <span className="muted">{g.numero_doc_commerciali} documenti</span>
          </header>
          <ul className="movement-list">
            <li>
              <span>Contanti (Cassa)</span>
              <span className="amount-in">{formatEuro(g.pagato_contanti)}</span>
            </li>
            <li>
              <span>
                Elettronico (POS atteso in Banca)<span className="badge">in attesa</span>
              </span>
              <span className="amount-in">{formatEuro(g.pagato_elettronico)}</span>
            </li>
          </ul>
        </section>
      ))}
    </main>
  )
}
