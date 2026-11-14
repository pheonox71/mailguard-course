# Phish Lite — SvelteKit starter

Minimal SvelteKit-shaped training UI with a visible **SIMULATION** label and consent gate. Never capture credentials.

## Setup

```bash
cd 17-phish-lite/starter
npm install        # generates .svelte-kit/ (gitignored) for tsconfig extends
npm test           # Vitest — ethics + reportRate
npm run dev        # local UI
npx playwright install chromium   # once, for e2e
npm run test:e2e   # Playwright smoke (builds + previews)
```

Ethics helpers live in `src/lib/ethics.js`; the scoring kata in `../katas/score.js` remains the Module 17 graded path.
