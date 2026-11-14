# Answer key — Hold state

1. held → approved → released; held → rejected. Illegal: held → released (skips human decision). Also typically no released → held without a new hold.
2. Approve records the human policy decision; release is the send-onward side effect. Collapsing them loses audit of “who decided” vs “what left.”
3. **409 Conflict** for illegal FSM (held → release). Not 412 (that is If-Match / version mismatch) and not an Idempotency-Key replay (same key+body returns the stored prior result). Silent 200 makes operators think mail left when state never changed.
4. Skips human approve; mail can leave without review — classic elevation / process bypass.
5. Auditable intent; easier policy and least privilege (who may attach BCC); avoids surprise PII copies on every allow.
6. **Alembic** — versions schema with the app so deploys are repeatable; hand-edits drift environments and break rollbacks.
7. **412** when If-Match / ETag / row version is stale (optimistic concurrency). **Idempotency-Key** dedupes client retries of the same mutating request (replay stored response; no second side effect) — it does not replace FSM checks or ETags.
8. Read-then-write lets both callers see `held` and both “succeed,” duplicating approve events and breaking audit. Atomic `UPDATE … WHERE state='held'` yields `rowcount` 1 for the winner and 0 for the loser (return 409/412); exactly one transition wins.
