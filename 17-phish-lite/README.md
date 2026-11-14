# 17 — Phish Lite *(optional)*

**Language:** Svelte / SvelteKit. Est. 8-10h.

Optional phishing-awareness quiz UI for **learning honesty** practice. Clearly label simulations; never capture real credentials.

## Workflow

1. [`readings/phish_lite.md`](./readings/phish_lite.md)
2. Assignment → implement scoring kata
3. Optional SvelteKit UI under [`starter/`](./starter/) (consent + **SIMULATION** label; Vitest + Playwright smoke)
4. Required quiz

## Starter (SvelteKit-shaped)

```bash
cd 17-phish-lite/starter
npm install
npm test
npm run dev
```

**Done when:** quiz → results chart path exists; README states learning-purpose honesty; ethics tests green.

## Trade-offs / harden next

- Ethical simulation only — consent, no credential harvesting.
