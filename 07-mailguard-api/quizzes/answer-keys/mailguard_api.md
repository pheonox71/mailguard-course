# Quiz answer key — MailGuard API

Use only after attempting the quiz questions.

1. Keeps policy unit-testable without HTTP; reusable from workers/CLIs; handlers stay thin transport. Mixing policy into handlers couples every test to the framework and hides edge cases.
2. Walk rules in list order; stop at the first match; later matches are ignored (default applies only if none match).
3. With Rule 1 first → **reject**. With Rule 2 first → **hold** (Rule 1 never runs). Order is an operator-facing contract: reordering changes security outcomes without code deploys.
4. Instance B never saw the new rule → allow/hold drift across nodes. Shared durable store (e.g. Postgres) plus consistent read path fixes multi-instance policy.
5. Failures look like success; callers cannot distinguish errors; tests expecting 4xx/5xx never fail for the right reason; operators get silent wrong allows. Loud errors surface incidents.
6. Gap: data disappears on restart / no multi-instance consistency / weak audit. Start in-memory **why:** prove the evaluate engine fast without infra hiding policy bugs.
7. Login proves identity, not that the caller may touch *this* hold — filter every access by tenant (+ role) or you get cross-tenant BOLA/function bugs. Lifespan owns client lifecycle for tests/shutdown; a transactional outbox (hold + outbox row, then publish) beats “HTTP 200 then hope SQS send worked.”
