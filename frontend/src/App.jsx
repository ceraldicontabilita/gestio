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
    <div className="app-shell">
      <header className="app-header">
        <div className="app-brand">
          Gestio <small>gestionale contabile</small>
        </div>
        <nav className="app-nav">
          {Object.entries(PAGINE).map(([chiave, { etichetta }]) => (
            <button
              key={chiave}
              className={chiave === pagina ? 'active' : ''}
              onClick={() => setPagina(chiave)}
            >
              {etichetta}
            </button>
          ))}
        </nav>
      </header>
      <Componente />
    </div>
  )
}
