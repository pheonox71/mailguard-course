# Reading — Passkeys / WebAuthn (beside TOTP MFA)

## Learning objectives

1. Explain **Web Authentication (WebAuthn)** as a browser API for public-key credentials scoped to a relying-party **RP ID** (a registrable domain suffix), not exactly the full origin string alone.
2. Contrast phishing risk of **TOTP** (user can type a code into a fake site) vs **passkeys** (origin-bound assertion).
3. Place passkeys next to MailGuard’s TOTP path as a *next* factor — not a rewrite of Challenge Gym.

**Why this matters.** TOTP proves “something you have,” but a convincing phishing page can still harvest the live code and replay it. Without phishing-resistant authenticators, identity and cloud admin portals stay one lookalike domain away from account takeover. On the job, passkeys / WebAuthn are how teams raise assurance beside (or instead of) OTP — without claiming TOTP literacy alone is enough.

TOTP proves “something you have” via a shared secret — but a convincing phishing page can still harvest the live code. Passkeys use WebAuthn: the browser/OS authenticator signs a challenge for *this* origin, so a lookalike domain should not get a usable assertion.

**How it works.**

1. **Registration.** The relying party (RP) sends a challenge; the authenticator creates a public-key credential bound to the **RP ID** (a registrable domain suffix, not merely “whatever string the page typed”).
2. **Storage.** The RP stores the credential id + public key (and related metadata); the private key stays in the authenticator / platform.
3. **Assertion.** At login, the RP sends a new challenge; the browser/OS asks the authenticator to sign only if the request matches that RP ID / origin.
4. **Verify.** The RP verifies the signature with the stored public key and checks challenge, origin/RP ID, and flags per WebAuthn.
5. **Recovery.** Lost device, backup passkey, and IT-assisted reset are operational design problems — plan them before turning off TOTP/recovery codes.

![TOTP code typed into a fake site versus a WebAuthn passkey bound to the relying-party origin](images/passkeys-vs-totp.svg)

*Figure. On the left, a typed TOTP code can be harvested and replayed. On the right, the authenticator signs only for the real relying-party origin — notice a lookalike domain does not get a usable assertion. Original course diagram (CC0).*

### Worked example

```text
RP ID:  example.com
Origin: https://login.example.com

Registration ceremony (shape):
  navigator.credentials.create({ publicKey: {
    rp: { id: "example.com", name: "Example" },
    user: { id: ..., name: "alex@example.com", displayName: "Alex" },
    challenge: <serverBytes>,
    pubKeyCredParams: [{ alg: -7, type: "public-key" }, ...]
  }})

Assertion on https://evil-example.com:
  authenticator should refuse — RP ID / origin binding does not match.
```

A phished TOTP code typed into `evil-example.com` still works at the real site until it expires; a passkey assertion for the wrong RP does not.

### Common misconceptions / what goes wrong

- **“Passkeys are just better passwords in the cloud.”** The private key never goes to the RP; the phishing resistance comes from origin/RP-bound signatures, not from longer secrets.
- **“RP ID equals the full origin including scheme and path.”** Credentials are scoped to a registrable domain suffix (RP ID); misunderstanding that breaks registration or weakens the threat model — see W3C WebAuthn.
- **“Turn off TOTP the day passkeys ship.”** Without recovery (second device, backup passkey, IT reset), lockouts become outages.
- **“This replaces Challenge Gym TOTP work.”** Passkeys sit *beside* TOTP literacy; the course still needs OTP for labs and for estates that have not moved yet.

## Videos (verified)

1. **[Understand passkeys in 4 minutes](https://www.youtube.com/watch?v=2xdV-xut7EQ)** — Google / passkeys overview  
   Why it helps: phishing-resistant passkeys mental model in under five minutes.

2. **[Passkeys: A simpler and more secure way to log in](https://www.youtube.com/watch?v=3BmYR--3z8M)** — Google  
   Why it helps: how passkeys relate to platform authenticators without building an IdP.

Prefer MDN + W3C links below if a video moves.

## Read these (verified)

1. [MDN — Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API) — ceremonies and browser support.
2. [W3C WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/) — **W3C Recommendation** (current). Prefer Level 3 for RP ID / passkey literacy; Level 2 remains the prior Recommendation for older references. Credentials are scoped to the **RP ID** (a registrable domain).
3. [passkeys.dev](https://passkeys.dev/) — practitioner-oriented passkey guidance.
4. [OWASP MFA Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) — factors and phishing-resistant authenticators.
5. [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) (final, 31 Jul 2025; incorporates syncable authenticators / passkeys) — authenticator assurance high-level.

## Quiz (required)
[`../quizzes/passkeys_webauthn.md`](../quizzes/passkeys_webauthn.md)
