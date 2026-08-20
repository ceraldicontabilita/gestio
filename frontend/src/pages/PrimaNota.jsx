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
    <main style={{ maxWidth: 720, margin: '0 auto', padding: 24, fontFamily: 'system-ui, sans-serif' }}>
      <h1>Prima Nota</h1>

      <nav style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        {CONTI.map((c) => (
          <button
            key={c.valore}
            onClick={() => setConto(c.valore)}
            style={{ fontWeight: c.valore === conto ? 'bold' : 'normal' }}
          >
            {c.etichetta}
          </button>
        ))}
      </nav>

      <form
        onSubmit={inviaVersamento}
        style={{ marginBottom: 24, display: 'flex', gap: 8, flexWrap: 'wrap', alignItems: 'center' }}
      >
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
        <button type="submit" disabled={salvataggio}>
          {salvataggio ? 'Salvataggio…' : 'Registra versamento in banca'}
        </button>
      </form>

      {errore && <p style={{ color: 'crimson' }}>Errore: {errore}</p>}
      {loading && <p>Caricamento…</p>}
      {!loading && giorni.length === 0 && <p>Nessun movimento.</p>}

      {giorni.map((giorno) => (
        <section
          key={giorno.data}
          style={{ border: '1px solid #ddd', borderRadius: 8, padding: 12, marginBottom: 12 }}
        >
          <header style={{ display: 'flex', justifyContent: 'space-between', fontWeight: 'bold' }}>
            <span>{formatData(giorno.data)}</span>
            <span>Saldo: {formatEuro(giorno.saldo_progressivo)}</span>
          </header>
          <ul style={{ listStyle: 'none', padding: 0, marginTop: 8 }}>
            {giorno.movimenti.map((m) => (
              <li key={m.id} style={{ display: 'flex', justifyContent: 'space-between', padding: '4px 0' }}>
                <span>
                  {m.descrizione}
                  {m.stato === 'attesa' && ' (in attesa)'}
                </span>
                <span style={{ color: m.tipo === 'entrata' ? 'green' : 'crimson' }}>
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
