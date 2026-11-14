# Answer key — DMARC policy helper

Use only after attempting the quiz questions.

1. Receivers look for `v=DMARC1` as the first tag; without it (or if it is not first) many treat the record as invalid and ignore the policy.
2. `p=` is the policy for the organizational domain; `sp=` is the policy for subdomains. Different values let you harden the apex while still learning on subdomains (or the reverse).
3. Aggregate reports show which senders fail SPF/DKIM alignment so you can fix legitimate mail before reject drops it.
4. `pct` applies the policy to only a percentage of failing mail; operators need to see it so they do not assume 100% enforcement.
5. Version must be first — many receivers ignore the whole record, so `p=reject` never applies.
6. DMARC authenticates domain use on *inbound* paths; outbound hold stops missends/leaks of content that authenticated mail can still carry.
