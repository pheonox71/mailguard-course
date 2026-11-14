# MailGuard Admin — Vite + Vue starter

Minimal Vue 3 + TypeScript SPA scaffold for Module 08.

## Setup

```bash
cd 08-mailguard-admin/starter
npm install
npm run typecheck   # vue-tsc --noEmit (strict)
npm run dev         # http://localhost:5173
```

## Why this shape

- **Vite** for fast local reloads while you wire forms to the Module 07 API.
- **`strict: true`** so illegal decision strings fail at compile time.
- **No secrets** in the browser bundle — call a backend or short-lived session.

Next: implement `katas/rule_form.ts`, then replace the mock hold rows with `fetch` to `/holds`.
