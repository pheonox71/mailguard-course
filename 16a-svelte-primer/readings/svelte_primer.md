# Svelte primer

**Why this matters.** Optional Module 17 (Phish Lite) uses **Svelte / SvelteKit** for a small learning UI. You need just enough framework literacy to follow the assignment — and a hard ethical boundary: simulations never capture real credentials.

**How it works.** Svelte compiles components at build time (less runtime framework overhead than some SPA approaches). SvelteKit adds routing and project structure. Node.js + npm remain the toolchain (same install family as the Vue primer).

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

```bash
# Why: confirm Node before scaffolding a Kit app in Module 17
node -e "console.log('svelte primer: node ok', process.version)"
```

Optional later (Module 17): follow the official `npm create svelte@latest` flow in a **scratch directory**, not inside unrelated modules.

## Official docs

1. [Svelte tutorial](https://svelte.dev/tutorial)
2. [SvelteKit introduction](https://kit.svelte.dev/docs/introduction)
3. [Node.js downloads](https://nodejs.org/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`17-phish-lite`).

This primer has **no** assignment, quiz, or download pack.
