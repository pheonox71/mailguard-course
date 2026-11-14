# SQL primer

**Why this matters.** Hold/release queues need **durable** state: who held a message, when, and whether it was released. In-memory demos lose that story on restart; without a queryable store you cannot prove “who released this hold?” after an incident. Document stores or logs alone rarely give the same transactional constraints for account/rule/audit rows — SQL remains the default for that shape of SaaS data.

**How it works.**

1. Model entities as **tables** (rows + columns) with constraints (`NOT NULL`, keys).
2. Identify rows with **primary keys** so holds/rules stay addressable across restarts.
3. Change data with declarative statements (`SELECT` / `INSERT` / `UPDATE`) — the engine plans how, you declare what.
4. Evolve schema with **migrations** (Alembic later) so deploys do not hand-edit production tables.
5. The MailGuard API module starts in-memory, then asks you to *sketch* a Postgres-shaped design — this primer is that vocabulary. On the job, the same pattern backs email-security and identity APIs: durable holds, rules, and audit trails operators can query.

### Worked example

Sketch that answers “what is held?” without an app server:

```sql
-- Why: one table can answer "what is held?" without an app server
CREATE TABLE holds (
  id          TEXT PRIMARY KEY,
  state       TEXT NOT NULL,  -- held | released | rejected
  created_at  TEXT NOT NULL,
  actor       TEXT NOT NULL
);

INSERT INTO holds (id, state, created_at, actor)
VALUES ('msg-1', 'held', '2026-11-13T12:00:00Z', 'api');

SELECT id, state FROM holds WHERE state = 'held';
-- → msg-1 | held
```

This primer has no assignment, quiz, or download pack.

---

## What SQL is

**SQL** (Structured Query Language) is the standard language for relational databases (PostgreSQL, MySQL, SQLite, and cloud variants).

## Why industry uses it

Relational stores give strong consistency for account, rule, and audit data. Security products lean on queryable audit trails — “who released this hold?” — which tables express well.

## Key concepts for Module 07

| Concept | Why you care |
|---------|----------------|
| Primary key | Stable id for a held message |
| Foreign keys | Rules/holds point at real accounts — orphan rows break audits |
| `CHECK` constraints | Reject impossible `state` values early |
| Indexes | Fast lookup by state / created_at for operator queues |
| Transactions | Approve+audit insert commits together or not at all |
| Parameterized queries | Stop SQL injection from operator/search input |
| Migrations (awareness) | Schema changes ship with app versions (Alembic later) |

## Parameterized queries (SQL injection)

**Why:** String-concatenating user input into SQL lets an attacker change the query (classic injection). **How:** pass values as bound parameters:

```sql
-- Bad (never): "SELECT * FROM holds WHERE id = '" + user_id + "'"
-- Good (shape):
SELECT id, state FROM holds WHERE id = ?;   -- SQLite-style placeholder
-- or $1 / %(id)s depending on the driver
```

## Transactions

```sql
BEGIN;
UPDATE holds SET state = 'released' WHERE id = ? AND state = 'approved';
INSERT INTO audit(hold_id, actor, action) VALUES (?, ?, 'release');
COMMIT;
-- On error: ROLLBACK so you never release without an audit row (or the reverse)
```

## CHECK, foreign keys, indexes

```sql
CREATE TABLE accounts (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE
);

CREATE TABLE holds (
  id          TEXT PRIMARY KEY,
  account_id  TEXT NOT NULL REFERENCES accounts(id),
  state       TEXT NOT NULL CHECK (state IN ('held', 'approved', 'released', 'rejected')),
  created_at  TEXT NOT NULL
);

CREATE INDEX holds_state_idx ON holds (state);
```

Why FKs: deleting an account should not leave holds that point nowhere (or should cascade deliberately). Why CHECK: typos like `relased` fail closed. Why index: operator UIs filter `WHERE state = 'held'` constantly.

## Install and run

You do **not** need a live database for this primer — the vocabulary above is enough to start Module 07. Optional (why: muscle memory for `psql` / SQLite before the stretch persistence lab): install [PostgreSQL](https://www.postgresql.org/download/) or use SQLite for experiments. Module 07 keeps the kata in-memory; persistence is a stretch with SQLAlchemy/Alembic links in readings.

## Tiny hands-on example

Use the SQL sketch in **Worked example** above (`CREATE` → `INSERT` → `SELECT`). **How:** `CREATE TABLE` defines the shape; `INSERT` records a hold; `SELECT` filters — the same questions operators ask in an admin UI.

### Common misconceptions / what goes wrong

- **“Logs are enough for audit.”** Append-only logs help forensics, but hold/release needs queryable current state with constraints — tables answer “is this still held?” in one row.
- **“In-memory is fine until launch.”** Restarts wipe holds; multi-instance APIs disagree on state. Sketch SQL early even if the kata stays in-memory.
- **“Any string in `state` is fine.”** Without CHECK constraints, typos (`relased`) become silent bugs; treat legal states as part of the schema design.
- **“Escaping by hand is as good as parameters.”** Drivers’ bound parameters are the reliable fix; hand escaping misses encodings.
- **“Indexes are free.”** They speed reads and slow writes — index the filter columns operators actually use.


## Videos (verified)

1. **[SQL Tutorial - Full Database Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY)**  
   Why it helps: tables/constraints before MailGuard persistence sketches.

## Official docs

1. [PostgreSQL documentation](https://www.postgresql.org/docs/current/)
2. [SQLAlchemy ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) (stretch after Module 07)
3. [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`07-mailguard-api`).

This primer has **no** assignment, quiz, or download pack.
