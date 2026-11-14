# Reading — Hold / approve / release

## Learning objectives

1. Model a first-class hold queue with explicit state transitions.
2. Separate **approve** (human decision) from **release** (send onward).
3. Reject illegal transitions instead of silently no-oping.

**Why this matters.** Collapsing “approve” and “release” into one click is how held mail leaves without a recorded human decision — or how a bug silently no-ops and operators think work finished. Illegal transitions that return 200 hide missends. Explicit states (`held` → `approved` → `released`, or `rejected`) exist so audits answer “who decided?” separately from “did it leave?”

**How it works.**

1. A hold starts in state **held** (message parked for review).
2. An operator **approves** (policy OK) or **rejects** (do not send).
3. Only **approved** items may **release** to the next hop (MTA / downstream).
4. The API rejects illegal jumps (e.g. held → released) with a client error (often **409 Conflict**), not a silent 200.
5. Stretch: persist rows in Postgres via SQLAlchemy; **Alembic** migrations version the schema so deploys do not hand-edit production tables ([Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)).
6. Auto-bcc / delete-on-condition are explicit **action kinds**, not silent side effects of allow — so least privilege and audit stay possible.

```
held --approve--> approved --release--> released
  \--reject--> rejected
```

### Worked example

State transition table (illegal cells must error):

| From \ Action | approve | reject | release |
|---------------|---------|--------|---------|
| held | → approved | → rejected | **409** (must approve first) |
| approved | **409** | → rejected (policy: may still reject before release) | → released |
| rejected | **409** | **409** | **409** |
| released | **409** | **409** | **409** |

This course’s `hold_state` kata treats **approved → reject** as legal so operators can stop a previously approved item before release. Document any stricter policy in your own lab notes.

```http
POST /holds/msg-1/release
→ 409 {"detail": "hold msg-1 is held; approve before release"}
```

**On the job.** Every email-security and DLP review queue uses a similar state machine. Cloud identity/admin tools likewise separate “decision recorded” from “side effect executed.” Being able to draw the diagram and defend illegal-transition errors is day-one literacy for gateway work.

## Short intro

An email-security gateway often **holds** outbound mail for review. Operators approve or reject; only approved items are released to the next hop. Keep vocabulary vendor-neutral: hold, approve, release, reject.

Persistence (Postgres + SQLAlchemy/Alembic) belongs in your stretch lab — the kata stays a pure state machine you can unit-test.

### Common misconceptions / what goes wrong

- **“Approve and release are the same button.”** Then audits cannot separate human judgment from send — and a UI bug can release without a decision record.
- **“Illegal transitions can no-op with 200.”** Operators and monitors treat 200 as success; use 4xx so clients retry or surface the error.
- **“We’ll add states later; strings are fine.”** Unchecked free-text states drift (`aproved`); model an enum/FSM early and test every edge.
- **“Alembic is optional busywork.”** Hand-edited production schemas diverge across environments; migrations are how schema changes travel with the app.

## Read these (verified)

1. [FastAPI — Path operation configuration](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/)
2. [SQLAlchemy 2.0 — ORM quick start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
3. [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Next step

Continue with the assignment from the downloads on this page (`hold_state` + `rule_actions` katas). The quiz is required after you attempt the assignment and tests.
