# TypeScript / Vue primer

**Why this matters.** Operators approve and release held mail in a UI. Untyped form state is where “allow” vs “hold” bugs hide; **TypeScript** makes illegal states harder to represent, and **Vue 3** is how Module 08 structures that admin SPA. Plain JavaScript + ad-hoc DOM updates can work for demos — until a typo ships the wrong decision label into production.

**How it works.**

1. **Node.js** runs the toolchain (`npm` installs packages and scripts).
2. **TypeScript** compiles typed `.ts` to JavaScript the browser (or Node) runs.
3. **Vue 3** binds reactive state to templates so a hold-queue table updates when the API returns new rows.
4. Forms and row models use interfaces/unions so `"hold" | "allow" | "reject"` stays consistent with the API.
5. On the job, the same stack backs many SaaS security admin consoles: typed forms, clear dangerous actions, no cloud secrets in the browser bundle.

### Worked example

A decision union that rejects typos at compile time:

```ts
export type Decision = "hold" | "allow" | "reject";

export function labelFor(d: Decision): string {
  // Why: exhaustive-ish union — typos become compile errors
  return d.toUpperCase();
}

console.log(labelFor("hold")); // → HOLD
// labelFor("hodl") → TypeScript error before a reviewer sees it
```

This primer has no assignment, quiz, or download pack.

---

## What these tools are

- **Node.js** — JavaScript runtime + npm for frontend tooling
- **TypeScript** — JavaScript with types
- **Vue 3** — progressive UI framework (Composition API in modern apps)

## Why industry uses them

Admin consoles for security products need accessible forms, clear dangerous actions (release), and fewer runtime surprises. Typed UI code + component frameworks are a common SaaS choice.

## Key concepts for Module 08

| Concept | Why you care |
|---------|----------------|
| `npm test` / scripts | Kata workflow mirrors Python’s pytest loop |
| Interfaces / types | Rule form fields stay consistent with the API |
| Components | Queue table vs approve button stay separable |
| No secrets in the browser | Tokens come from a backend — never hard-code cloud keys |

## Install and run

1. Install [Node.js LTS](https://nodejs.org/)
2. Check: `node --version` · `npm --version`

```bash
# Why: disposable scratch dir — do not pollute the course repo
mkdir -p /tmp/mg-ts-primer && cd /tmp/mg-ts-primer
# Why: package.json so npm can track the TypeScript toolchain
npm init -y
# Why: local (devDependency) tsc — same pattern Module 08 katas use
npm install typescript --save-dev
npx tsc --init
```

## Tiny hands-on example

```bash
cat > /tmp/mg-ts-primer/decision.ts << 'EOF'
export type Decision = "hold" | "allow" | "reject";

export function labelFor(d: Decision): string {
  // Why: exhaustive-ish union — typos become compile errors
  return d.toUpperCase();
}

console.log(labelFor("hold"));
EOF
cd /tmp/mg-ts-primer && npx tsc decision.ts && node decision.js
```

**How:** A string union documents legal decisions; the compiler rejects `"hodl"`-style mistakes before a reviewer sees them.

## Vue component example (Module 08 shape)

**Why this matters.** A hold-queue table is not a one-off script: operators need reactive rows, typed decision labels, and a clear separation between “display helpers” and “API calls.” Vue’s Composition API (`<script setup>`) keeps that state next to the template without scattering `document.querySelector` calls. Module 08’s [`starter/`](../../08-mailguard-admin/starter/) boots this pattern under Vite.

**How it works.**

1. Declare a **typed** row model (`Decision` union + `HoldRow` interface).
2. Hold rows in a **`ref`** so the table re-renders when data changes.
3. Bind with `v-for` / mustache interpolation — no raw HTML injection for subjects.
4. Keep cloud secrets out of the SFC; fetch through a backend later.

### Worked example

Minimal single-file component (same idea as `08-mailguard-admin/starter/src/App.vue`):

```vue
<script setup lang="ts">
import { ref } from "vue";

type Decision = "hold" | "allow" | "reject";

interface HoldRow {
  id: string;
  subject: string;
  decision: Decision;
}

const rows = ref<HoldRow[]>([
  { id: "msg-1", subject: "Q4 forecast.xlsx", decision: "hold" },
]);

function labelFor(d: Decision): string {
  return d.toUpperCase(); // Why: display helper stays pure / testable
}
</script>

<template>
  <ul>
    <li v-for="row in rows" :key="row.id">
      {{ row.subject }} — {{ labelFor(row.decision) }}
    </li>
  </ul>
</template>
```

```bash
# Why typecheck in CI: catch Decision typos before a reviewer clicks Release
cd 08-mailguard-admin/starter && npm install && npm run typecheck
```

### Common misconceptions / what goes wrong

- **“Types are just documentation.”** Without `strict` (or equivalent), `any` sneaks back in and the union buys nothing.
- **“Vue templates do not need types.”** Form models and API responses still do — that is where allow/hold mix-ups hide.
- **“Put the API key in the SPA for convenience.”** Browser bundles are public; use a **Backend-for-Frontend (BFF)** with HTTP-only session cookies and CSRF defenses ([RFC 10017 — OAuth 2.0 for Browser-Based Apps](https://www.rfc-editor.org/rfc/rfc10017)) instead of tokens in JS storage.
- **“`v-html` is fine for email subjects.”** Subjects are attacker-controlled text; interpolate as text nodes, not HTML.


## Videos (verified)

1. **[Vue.js Course for Beginners](https://www.youtube.com/watch?v=FXpIoQ_rT_c)**  
   Why it helps: Vue 3 mental model before Module 08.

## Official docs

1. [Node.js downloads](https://nodejs.org/)
2. [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
3. [Vue 3 guide](https://vuejs.org/guide/introduction.html)
4. [RFC 10017 — OAuth 2.0 for Browser-Based Apps](https://www.rfc-editor.org/rfc/rfc10017) — BFF + CSRF when the Vue SPA talks to APIs (Module 08).

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`08-mailguard-admin`).

This primer has **no** assignment, quiz, or download pack.
