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

### Common misconceptions / what goes wrong

- **“Types are just documentation.”** Without `strict` (or equivalent), `any` sneaks back in and the union buys nothing.
- **“Vue templates do not need types.”** Form models and API responses still do — that is where allow/hold mix-ups hide.
- **“Put the API key in the SPA for convenience.”** Browser bundles are public; use a backend-for-frontend or short-lived session instead.

## Official docs

1. [Node.js downloads](https://nodejs.org/)
2. [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
3. [Vue 3 guide](https://vuejs.org/guide/introduction.html)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`08-mailguard-admin`).

This primer has **no** assignment, quiz, or download pack.
