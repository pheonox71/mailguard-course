import { describe, expect, it } from 'vitest'

function ethicalSimOk({ consent, capturesCredentials }: { consent: boolean; capturesCredentials: boolean }) {
  return Boolean(consent) && capturesCredentials === false
}

describe('ethics gate', () => {
  it('requires consent and forbids credential capture', () => {
    expect(ethicalSimOk({ consent: true, capturesCredentials: false })).toBe(true)
    expect(ethicalSimOk({ consent: true, capturesCredentials: true })).toBe(false)
    expect(ethicalSimOk({ consent: false, capturesCredentials: false })).toBe(false)
  })
})
