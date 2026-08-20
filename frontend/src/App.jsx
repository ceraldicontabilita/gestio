import { useState } from 'react'
import PrimaNota from './pages/PrimaNota.jsx'
import Corrispettivi from './pages/Corrispettivi.jsx'

const PAGINE = {
  'prima-nota': { etichetta: 'Prima Nota', Componente: PrimaNota },
  corrispettivi: { etichetta: 'Corrispettivi', Componente: Corrispettivi },
}

export default function App() {
  const [pagina, setPagina] = useState('prima-nota')
  const { Componente } = PAGINE[pagina]

  return (
    <div>
      <nav style={{ display: 'flex', gap: 8, padding: '12px 24px', borderBottom: '1px solid #ddd' }}>
        {Object.entries(PAGINE).map(([chiave, { etichetta }]) => (
          <button
            key={chiave}
            onClick={() => setPagina(chiave)}
            style={{ fontWeight: chiave === pagina ? 'bold' : 'normal' }}
          >
            {etichetta}
          </button>
        ))}
      </nav>
      <Componente />
    </div>
  )
}
