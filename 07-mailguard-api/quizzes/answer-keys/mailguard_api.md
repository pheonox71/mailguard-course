# Quiz answer key — MailGuard API

Use only after attempting the quiz questions.

1. Application Programming Interface; Create, Read, Update, Delete.
2. hold, allow, reject.
3. Walk rules in list order; stop at the first match; later matches are ignored.
4. Keeps policy logic unit-testable without HTTP, and reusable from workers/CLIs.
5. reject (Rule 1 matches first).
6. Failures look like success; callers cannot distinguish errors; tests that expect 4xx/5xx never fail for the right reason.
7. Data disappears on restart; no multi-instance consistency; weak audit trail.
