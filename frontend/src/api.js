// In sviluppo locale il proxy di Vite instrada /api verso il backend
// (vite.config.js). In produzione (static site) non c'è proxy: serve
// l'URL assoluto del backend, passato a build time.
const BASE_URL = `${import.meta.env.VITE_API_BASE_URL ?? ''}/api`

async function raiseForStatus(response) {
  const body = await response.text()
  try {
    const parsed = JSON.parse(body)
    throw new Error(parsed.detail ?? body)
  } catch (err) {
    if (err instanceof SyntaxError) throw new Error(body || `Errore ${response.status}`)
    throw err
  }
}

async function request(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!response.ok) await raiseForStatus(response)
  return response.json()
}

export function getMovimenti(conto) {
  return request(`/prima-nota/${conto}`)
}

export function registraVersamento(payload) {
  return request('/prima-nota/versamento', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}

export function getCorrispettivi() {
  return request('/corrispettivi')
}

export function sincronizzaDriveCorrispettivi() {
  return request('/drive-sync/corrispettivi', { method: 'POST' })
}

export async function importaCorrispettivo(file) {
  const formData = new FormData()
  formData.append('file', file)
  const response = await fetch(`${BASE_URL}/corrispettivi/import`, {
    method: 'POST',
    body: formData,
  })
  if (!response.ok) await raiseForStatus(response)
  return response.json()
}
