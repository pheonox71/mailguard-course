# HTTP primer

**Why this matters.** OIDC redirects, FastAPI routes, admin UIs, and health checks are all HTTP conversations. Without method/status/header literacy, every later “401 vs 403” or CORS failure becomes folklore. On the job, identity and email-security APIs are debugged first at the wire: request line, headers, status, then body.

**How it works.**

1. A client opens a **TLS** (or cleartext lab) connection to a host.
2. It sends a **request line** (method + path + HTTP version) plus **headers** and optional body.
3. The server responds with a **status code**, response headers, and optional body.
4. **Cookies** may store session state the browser sends back on later requests (scope/path/Secure/HttpOnly matter).
5. **CORS** is a browser rule set: servers advertise which origins may read responses from script; curl ignores CORS.
6. APIs document this surface (OpenAPI); browsers and SPAs must still respect same-origin / CORS.

```text
Client --TLS--> Server
  REQUEST: METHOD /path HTTP/1.1 + headers + body?
  RESPONSE: status + headers + body?
```

### Worked example

```bash
# Why: see method + status without a framework
curl -sI https://example.com | head -n 5
# Look for HTTP/2 200 (or 301) and security headers (e.g. Strict-Transport-Security)
```

Idempotent sketch: repeating `GET /healthz` should not change server state; repeating `POST /rules` usually creates another rule unless the API defines idempotency keys.

### Common misconceptions / what goes wrong

- **“401 and 403 are the same.”** 401 = not authenticated (or bad credentials); 403 = authenticated but not allowed — different fixes.
- **“CORS protects the server.”** CORS constrains *browsers*; non-browser clients can still call the API — authz still required.
- **“Cookies are fine without Secure/HttpOnly.”** Lab shortcuts leak sessions on HTTP or to JavaScript XSS.
- **“TLS is optional once we have OAuth.”** Tokens on cleartext HTTP are still stealable in transit.

This primer has no assignment, quiz, or download pack.

---

## Methods and status codes

| Method | Typical use | Safe? | Idempotent? |
|--------|-------------|-------|-------------|
| GET | Read | Yes | Yes |
| HEAD | Headers only | Yes | Yes |
| POST | Create / RPC-style | No | Usually no |
| PUT | Replace | No | Yes |
| PATCH | Partial update | No | Usually no |
| DELETE | Remove | No | Yes |

| Status | Meaning (literacy) |
|--------|--------------------|
| 2xx | Success (`200` OK, `201` Created, `204` No Content) |
| 3xx | Redirect (`301`/`302`/`307`/`308`) |
| 4xx | Client error (`400` bad request, `401` authn, `403` authz, `404` missing, `409` conflict) |
| 5xx | Server error |

## Headers, cookies, CORS, TLS

- **Headers** carry metadata (`Authorization`, `Content-Type`, `Cache-Control`).
- **Cookies** are `Set-Cookie` / `Cookie` pairs; prefer `Secure`, `HttpOnly`, and tight `SameSite` for sessions.
- **CORS** uses `Origin` + `Access-Control-Allow-*` for browser cross-origin reads.
- **TLS** authenticates the server (and optionally the client in mTLS) and encrypts the bytes.

## Tiny hands-on example

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://example.com
# → 200 (or a redirect code if the client does not follow)
```

## Official docs

1. [MDN — HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
2. [MDN — HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
3. [MDN — CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
4. [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)

## Videos (verified)

1. **[HTTP Crash Course & Exploration](https://www.youtube.com/watch?v=iYM2zFP3Zn0)** — Traversy Media  
   Why it helps: methods, status codes, and headers in one pass before OIDC/API labs.

## Done when

You can explain **why** HTTP shows up before OIDC and the MailGuard API and **how** to read a status line. Mark this primer complete on the site, then continue.
