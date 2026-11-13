# Quiz — Hold state

1. **How:** Draw (or list) legal transitions among held / approved / released / rejected. Which single jump is illegal and **why**?
2. **Why:** Why must **release** require a prior **approve** instead of releasing straight from held?
3. **Scenario:** An operator clicks release on a still-held item. What should the API return, and what goes wrong if it silently no-ops with 200?
4. **Spot the bug:** `if action == "release": state = "released"` with no prior-state check. Abuse story?
5. **Why:** Why keep auto-bcc as an explicit action kind rather than a silent side effect of allow?
6. **How / why:** Which tool manages schema migrations for SQLAlchemy apps, and why not hand-edit production tables?
