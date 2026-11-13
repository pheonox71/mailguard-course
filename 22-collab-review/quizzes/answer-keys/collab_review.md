# Answer key — Collab review

1. feat, fix, docs (or chore/test/ci/refactor). Types make intent scannable and improve bisect/changelog signal.
2. Split into reviewable PRs; isolate auth changes so reviewers can focus on authz/secrets without noise.
3. Secret material in git — block merge; if real, rotate credentials and treat as incident, not only “delete the file.”
4. CODEOWNERS — ensures people who own identity/mail paths must approve before merge.
5. Faster, safer review; easier revert; auth mistakes are harder to hide in a focused diff.
6. No — do not history-rewrite course main for practice; it breaks clones, CI history, and shared references.
