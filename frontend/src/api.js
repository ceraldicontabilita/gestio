const BASE_URL = '/api'

async function request(path, options = {}) {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!response.ok) {
    const body = await response.text()
    throw new Error(`${response.status} ${body}`)
  }
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

export async function importaCorrispettivo(file) {
  const formData = new FormData()
  formData.append('file', file)
  const response = await fetch(`${BASE_URL}/corrispettivi/import`, {
    method: 'POST',
    body: formData,
  })
  if (!response.ok) {
    const body = await response.text()
    throw new Error(`${response.status} ${body}`)
  }
  return response.json()
}
