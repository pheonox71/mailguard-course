# Reading — Hold / approve / release

## Learning objectives

1. Model a first-class hold queue with explicit state transitions.
2. Separate **approve** (human decision) from **release** (send onward).
3. Reject illegal transitions instead of silently no-oping.

**Why this matters.** Collapsing “approve” and “release” into one click is how held mail leaves without a recorded human decision — or how a bug silently no-ops and operators think work finished. Illegal transitions that return 200 hide missends. Explicit states (`held` → `approved` → `released`, or `rejected`) exist so audits answer “who decided?” separately from “did it leave?”

**How it works.** A hold starts **held**. An operator **approves** (policy OK) or **rejects**. Only **approved** items may **release** to the next hop. The API rejects jumps (e.g. held → released) with a client error (often 409). Stretch: persist rows in Postgres via SQLAlchemy; **Alembic** migrations version the schema so deploys do not hand-edit production tables. Auto-bcc / delete-on-condition are explicit **action kinds**, not silent side effects of allow — so least privilege and audit stay possible.

```
held --approve--> approved --release--> released
  \--reject--> rejected
```

**On the job.** Every email-security and DLP review queue uses a similar state machine. Cloud identity/admin tools likewise separate “decision recorded” from “side effect executed.” Being able to draw the diagram and defend illegal-transition errors is day-one literacy for gateway work.

## Short intro

An email-security gateway often **holds** outbound mail for review. Operators approve or reject; only approved items are released to the next hop. Keep vocabulary vendor-neutral: hold, approve, release, reject.

Persistence (Postgres + SQLAlchemy/Alembic) belongs in your stretch lab — the kata stays a pure state machine you can unit-test.

## Read these (verified)

1. [FastAPI — Path operations](https://fastapi.tiangolo.com/tutorial/path-operations/)
2. [SQLAlchemy 2.0 — ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
3. [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Next step

Continue with the assignment from the downloads on this page (`hold_state` + `rule_actions` katas). The quiz is required after you attempt the assignment and tests.
