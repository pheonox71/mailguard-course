# 08 — MailGuard Admin

**Language:** Vue 3 + TypeScript. Est. 8-10h.

Operator UI for rules and the hold queue. This module ships a TypeScript rule-form helper with tests, plus a reading/assignment track for building a Vue admin against the Module 07 API.

## What this teaches

- TypeScript strict typing for rule forms and hold-queue rows
- Accessible approve/release actions (literacy + small helpers)
- How the admin talks to the API without embedding secrets

## Workflow

1. [`readings/mailguard_admin.md`](./readings/mailguard_admin.md)
2. Assignment → implement `katas/` (TypeScript) until tests pass
3. Optional: run the Vue SPA under [`starter/`](./starter/) and wire it to the Module 07 API
4. Required quiz PDF, then separate answer key

## Starter (Vite + Vue)

A minimal Vue 3 + TypeScript scaffold lives in [`starter/`](./starter/) (`strict` `tsconfig`, `npm run typecheck` via `vue-tsc`).

```bash
cd 08-mailguard-admin/starter
npm install
npm run typecheck
npm run dev
```

## How to run katas

```bash
cd 08-mailguard-admin
npm test
```

**Done when:** rules + hold queue usable end-to-end against the API (or documented curl/operator script); TypeScript strict; a few tests green.

## Trade-offs / harden next

- Kata focuses on form/queue helpers; the Vite starter is the SPA stretch build.
- Production admin needs authn, CSRF protections, and audit of operator actions.
