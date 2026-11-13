# Svelte primer

**Why this matters.** Optional Module 17 (Phish Lite) uses **Svelte / SvelteKit** for a small learning UI. You need just enough framework literacy to follow the assignment — and a hard ethical boundary: simulations never capture real credentials. On the job, security-awareness UIs fail when honesty and metrics are an afterthought; the framework is secondary to that boundary.

**How it works.**

1. Install/reuse **Node.js** + npm (same toolchain family as the Vue primer).
2. **Svelte** compiles components at build time (less runtime framework overhead than some SPA approaches).
3. **SvelteKit** adds routing and project structure for pages like consent → scenario → results.
4. In Module 17, label learning purpose clearly and never harvest credentials — the framework only hosts that UI.

```text
node/npm → scaffold Kit app → components + routes → build/dev server
```

This primer has no assignment, quiz, or download pack.

---

## What Svelte is

**Svelte** is a UI framework; **SvelteKit** is its full-stack application framework. Module 17’s language chip is Svelte — Vue was Module 08.

## Why industry uses it

Teams pick Svelte for small, fast interactive apps and teaching demos. In security-awareness work, clear UI copy matters as much as the framework — honesty about simulation purpose is mandatory.

## Key concepts for Module 17

| Concept | Why you care |
|---------|----------------|
| Components + reactive assignments | Score/results UI |
| SvelteKit project layout | Where routes and static assets live |
| Learning-purpose labeling | Never phish real users; no credential harvest |
| Reuse Node from earlier | Same `node` / `npm` checks as Module 08 |

## Install and run

1. Node.js LTS — [nodejs.org](https://nodejs.org/) (reuse from TypeScript/Vue primer)
2. Official scaffold when Module 17 asks: [SvelteKit docs](https://kit.svelte.dev/docs/introduction)

**Check:** `node --version` · `npm --version`

## Tiny hands-on example

### Worked example

Confirm the toolchain before Module 17 scaffolding:

```bash
# Why: confirm Node before scaffolding a Kit app in Module 17
node -e "console.log('svelte primer: node ok', process.version)"
```

Optional later (Module 17): follow the official `npm create svelte@latest` flow in a **scratch directory**, not inside unrelated modules.

### Common misconceptions / what goes wrong

- **“The framework choice is the security model.”** Consent labels and no-password forms matter more than Svelte vs Vue for awareness UIs.
- **“Scaffold inside every course module.”** Keep Kit apps in a scratch directory so unrelated packages do not tangle Module 08/17 trees.
- **“Skip Node checks.”** Kit needs a working `node`/`npm` — confirm versions before debugging route errors.

## Official docs

1. [Svelte tutorial](https://svelte.dev/tutorial)
2. [SvelteKit introduction](https://kit.svelte.dev/docs/introduction)
3. [Node.js downloads](https://nodejs.org/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`17-phish-lite`).

This primer has **no** assignment, quiz, or download pack.
