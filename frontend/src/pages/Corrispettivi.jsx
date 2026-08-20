import { useCallback, useEffect, useState } from 'react'
import { getCorrispettivi, importaCorrispettivo } from '../api.js'

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

  return (
    <main style={{ maxWidth: 720, margin: '0 auto', padding: 24, fontFamily: 'system-ui, sans-serif' }}>
      <h1>Corrispettivi</h1>

      <label style={{ display: 'inline-block', marginBottom: 24 }}>
        <span style={{ marginRight: 8 }}>Importa XML corrispettivi RT:</span>
        <input type="file" accept=".xml" onChange={onFileSelezionato} disabled={caricamento} />
      </label>

      {errore && <p style={{ color: 'crimson' }}>Errore: {errore}</p>}
      {loading && <p>Caricamento…</p>}
      {!loading && giornate.length === 0 && <p>Nessuna giornata importata.</p>}

      {giornate.map((g) => (
        <section
          key={g.id}
          style={{ border: '1px solid #ddd', borderRadius: 8, padding: 12, marginBottom: 12 }}
        >
          <header style={{ display: 'flex', justifyContent: 'space-between', fontWeight: 'bold' }}>
            <span>{formatData(g.data_rilevazione)} — {g.id_dispositivo}</span>
            <span>{g.numero_doc_commerciali} documenti</span>
          </header>
          <ul style={{ listStyle: 'none', padding: 0, marginTop: 8 }}>
            <li>Contanti (Cassa): <strong>{formatEuro(g.pagato_contanti)}</strong></li>
            <li>Elettronico (POS atteso in Banca): <strong>{formatEuro(g.pagato_elettronico)}</strong></li>
          </ul>
        </section>
      ))}
    </main>
  )
}
