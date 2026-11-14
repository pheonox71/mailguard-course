# Prerequisites

What you should already have (or be willing to pick up quickly) before Module `01`. Start with Module [`00-setup/`](./00-setup/) for installs and version checks (est. 8-10h), then the Bash and Python **primers** (`00a`, `00b`) before Challenge Gym. Later primers sit before the first module that uses each new language or tool. This course surveys backend, frontend, and platform/infra; it does **not** teach programming from zero.

Student fills assignments and implements stubs. Course content uses AI assistance — verify important facts against linked primary sources.

---

## Required

| Area | Bar |
|------|-----|
| **CS fundamentals** | Comfortable with variables, functions, data structures, basic algorithms, and reading error messages. |
| **Python 3** | Write small modules, use a virtualenv, run scripts from a terminal. Strongest language assumed. |
| **Git** | Clone/commit; read a diff; answer the blank assignments and quiz PDFs already under `my-work/`. |
| **Command line** | `cd`, env vars, pipes, install packages with `pip`. |
| **English technical reading** | RFCs, OWASP cheat sheets, library docs (linked from readings). |

## Strongly recommended before the product-build modules (`07`+)

| Area | Why |
|------|-----|
| **HTTP basics** | Status codes, JSON bodies, headers — for FastAPI and admin UI work. |
| **pytest literacy** | Tests are the contract in Challenge Gym; later APIs keep that habit. |
| **SQL / persistence idea** | Enough to store users, rules, and held messages (exact store varies by module). |

## Needed when you reach that module

| When | Skill |
|------|--------|
| `08` | TypeScript + Vue 3 basics (or willingness to follow the official tutorials while building). |
| `09` | Go tour-level syntax (interfaces, packages, `go test`). |
| `12`–`13` | GitHub account; AWS free-tier or LocalStack/MinIO for local demos; Terraform install. |
| `14`+ | Docker comfort; willingness to run kind/minikube. |
| `03` | High-level OAuth2 / OIDC vocabulary (login redirect, tokens) — glossary helps. |

## Tools to install early

- Python 3.11+ (or current stable), `pip`, `venv`
- Git
- A code editor
- Later: Node.js (for Vue/Svelte), Go toolchain, Docker, Terraform, `kubectl` / kind — install when the module README says so

## Not required

- Prior cloud security job experience
- Prior MFA/OIDC product work
- Production Kubernetes years
- Any particular employer’s internal tools

If a reading acronym is new, expand it once in [GLOSSARY.md](./GLOSSARY.md), then continue.
