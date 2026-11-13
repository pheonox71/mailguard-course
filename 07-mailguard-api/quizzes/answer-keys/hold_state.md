# Answer key — Hold state

1. held → approved → released; held → rejected. Illegal: held → released (skips human decision). Also typically no released → held without a new hold.
2. Approve records the human policy decision; release is the send-onward side effect. Collapsing them loses audit of “who decided” vs “what left.”
3. Error / 409 (illegal transition). Silent 200 makes operators think mail left (or was reviewed) when state never changed — missend and false confidence.
4. Skips human approve; mail can leave without review — classic elevation / process bypass.
5. Auditable intent; easier policy and least privilege (who may attach BCC); avoids surprise PII copies on every allow.
6. **Alembic** — versions schema with the app so deploys are repeatable; hand-edits drift environments and break rollbacks.
