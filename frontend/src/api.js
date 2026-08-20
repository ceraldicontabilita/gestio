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
