# Assignment — Hold state + rule actions

1. Draw the state diagram: held / approved / released / rejected. Annotate **why** each arrow exists (decision vs side effect).
2. **Why** must release require prior approve?
3. Give one abuse case for auto-bcc without access control — **how** does the attacker benefit?
4. **Scenario:** when is delete-on-condition safer than reject-with-bounce, and what trade-off do you accept?
5. Sketch a Postgres table for holds (id, state, created_at, actor). **Why** each column (what audit question it answers)?
6. **Why** must concurrent approve use `UPDATE … WHERE state='held'` and check `rowcount == 1` instead of read-then-write? What should the losing caller see?
