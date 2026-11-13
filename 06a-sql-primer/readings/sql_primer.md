# SQL primer

**Why this matters.** Hold/release queues need **durable** state: who held a message, when, and whether it was released. In-memory demos lose that story on restart; SQL is how most SaaS APIs persist it.

**How it works.** You model entities as **tables** (rows + columns), identify rows with **keys**, and change data with declarative statements (`SELECT` / `INSERT` / `UPDATE`). The MailGuard API module starts in-memory, then asks you to *sketch* a Postgres-shaped design — this primer is that vocabulary.

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
| NOT NULL / constraints | Reject impossible states early |
| `SELECT` / `INSERT` / `UPDATE` | Read and mutate hold rows |
| Migrations (awareness) | Schema changes ship with app versions (Alembic later) |

## Install and run

You do **not** need a live database for this primer. Optional: install [PostgreSQL](https://www.postgresql.org/download/) or use SQLite for experiments. Module 07 keeps the kata in-memory; persistence is a stretch with SQLAlchemy/Alembic links in readings.

## Tiny hands-on example

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
```

**How:** `CREATE TABLE` defines the shape; `INSERT` records a hold; `SELECT` filters — the same questions operators ask in an admin UI.

## Official docs

1. [PostgreSQL documentation](https://www.postgresql.org/docs/current/)
2. [SQLAlchemy ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html) (stretch after Module 07)
3. [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`07-mailguard-api`).

This primer has **no** assignment, quiz, or download pack.
