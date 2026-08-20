import { useCallback, useEffect, useState } from 'react'
import { getMovimenti, registraVersamento } from '../api.js'

const CONTI = [
  { valore: 'cassa', etichetta: 'Cassa' },
  { valore: 'banca', etichetta: 'Banca' },
]

function formatEuro(valore) {
  return new Intl.NumberFormat('it-IT', { style: 'currency', currency: 'EUR' }).format(valore)
}

function formatData(valore) {
  const [anno, mese, giorno] = valore.split('-')
  return `${giorno}/${mese}/${anno}`
}

export default function PrimaNota() {
  const [conto, setConto] = useState('cassa')
  const [giorni, setGiorni] = useState([])
  const [loading, setLoading] = useState(true)
  const [errore, setErrore] = useState(null)
  const [form, setForm] = useState({ importo: '', data: '', descrizione: '' })
  const [salvataggio, setSalvataggio] = useState(false)

  const carica = useCallback(async (target) => {
    setLoading(true)
    setErrore(null)
    try {
      const dati = await getMovimenti(target)
      setGiorni(dati)
    } catch (err) {
      setErrore(err.message)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    carica(conto)
  }, [conto, carica])

  async function inviaVersamento(event) {
    event.preventDefault()
    setSalvataggio(true)
    setErrore(null)
    try {
      await registraVersamento({
        importo: form.importo,
        data: form.data,
        descrizione: form.descrizione || undefined,
      })
      setForm({ importo: '', data: '', descrizione: '' })
      await carica(conto)
    } catch (err) {
      setErrore(err.message)
    } finally {
      setSalvataggio(false)
    }
  }

  return (
    <main className="page">
      <h1 className="page-title">Prima Nota</h1>
      <p className="page-subtitle">Registro cassa e banca, con versamenti e riconciliazioni.</p>

      <div className="tabs">
        {CONTI.map((c) => (
          <button
            key={c.valore}
            className={c.valore === conto ? 'active' : ''}
            onClick={() => setConto(c.valore)}
          >
            {c.etichetta}
          </button>
        ))}
      </div>

      <form onSubmit={inviaVersamento} className="toolbar">
        <input
          type="date"
          required
          value={form.data}
          onChange={(e) => setForm({ ...form, data: e.target.value })}
        />
        <input
          type="number"
          step="0.01"
          min="0.01"
          required
          placeholder="Importo"
          value={form.importo}
          onChange={(e) => setForm({ ...form, importo: e.target.value })}
        />
        <input
          type="text"
          placeholder="Descrizione (opzionale)"
          value={form.descrizione}
          onChange={(e) => setForm({ ...form, descrizione: e.target.value })}
        />
        <button type="submit" className="btn" disabled={salvataggio}>
          {salvataggio ? 'Salvataggio…' : 'Registra versamento in banca'}
        </button>
      </form>

      {errore && <p className="alert alert-error">Errore: {errore}</p>}
      {loading && <p className="state-message">Caricamento…</p>}
      {!loading && giorni.length === 0 && <p className="state-message">Nessun movimento.</p>}

      {giorni.map((giorno) => (
        <section key={giorno.data} className="card">
          <header className="card-header">
            <span>{formatData(giorno.data)}</span>
            <span className="muted">Saldo: {formatEuro(giorno.saldo_progressivo)}</span>
          </header>
          <ul className="movement-list">
            {giorno.movimenti.map((m) => (
              <li key={m.id}>
                <span>
                  {m.descrizione}
                  {m.stato === 'attesa' && <span className="badge">in attesa</span>}
                </span>
                <span className={m.tipo === 'entrata' ? 'amount-in' : 'amount-out'}>
                  {m.tipo === 'entrata' ? '+' : '-'}
                  {formatEuro(m.importo)}
                </span>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </main>
  )
}
