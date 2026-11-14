# Course setup — tools for the MailGuard path

**Why this matters.** Security labs fail for boring reasons: wrong Python, no `venv`, Git missing, or tools installed too late. Without a repeatable machine baseline, every later module becomes “debug the laptop” instead of learning identity, email auth, and cloud access. On the job, the same hygiene — isolate deps, verify versions, defer heavy tooling until needed — keeps shared environments and CI honest.

**How it works.**

1. Install a small **core** set now: Git, Python 3.11+ (or current stable 3.x), `venv`/`pip`, `pytest`, and an editor.
2. Confirm each with a version check (`git --version`, `python3 --version`, `pytest --version`).
3. Create a Challenge Gym `.venv`, install `requirements.txt`, and run `pytest -q` so the toolchain is proven (failing kata tests are expected).
4. Defer Node, Go, Docker, Terraform, kubectl/kind, and cloud CLIs until the module that needs them.
5. Mark Module 00 complete only after the checklist below passes.

That staged path mirrors how teams onboard: unblock day-one work first, then add platform tooling when the workload appears.

### Worked example

```bash
git --version
python3 --version          # Windows: py -3 --version
cd 01-challenge-gym && python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pytest --version
```

You should see version strings for Git/Python/pytest. Kata failures are fine; an import or `venv` error means fix setup before Module 01.

### Common misconceptions / what goes wrong

- **“Install every cloud/K8s tool on day one.”** Unused Docker/Terraform/kubectl stacks rot and fight each other; defer until the module that needs them so core Python labs stay unblocked.
- **“System Python is fine — skip venv.”** Global packages diverge from classmates and CI; a project `.venv` keeps `pyotp`/`cryptography`/pytest on a known graph.
- **“pytest red means setup failed.”** Early red tests prove the runner works; only interpreter/venv/import errors mean the machine baseline is wrong.

This module prepares your machine for the full course: identity / MFA katas, email authentication, Python APIs, TypeScript/Vue admin, Go workers, AWS/CI, Terraform, and local Kubernetes. You do **not** need every tool on day one — install **core** tools now, and the **later** tools when the matching module arrives.

Work through the installs below, then mark Module 00 complete on the site. This module has no assignment, quiz, or download pack.

---

## What the course uses (audit)

| Area | Tools / libraries | First needed |
|------|-------------------|--------------|
| Editor + VCS | Code editor; **Git** | 00 / whole course |
| Python path | **Python 3.11+**, `pip`, `venv`, **pytest**, **pyotp**, **cryptography**; later **FastAPI** | 01, 05, 07, 10 |
| Frontend | **Node.js** + npm/pnpm; **TypeScript**; **Vue 3**; optional **Svelte / SvelteKit** | 08, 17 (also to preview the course site: `cd site && npm start`) |
| Go path | **Go** toolchain (`go test`, modules) | 09 |
| Containers | **Docker** + **Docker Compose** | 12 (image CI step), 13, 14 |
| Cloud / CI | **GitHub** account; **GitHub Actions**; **AWS** account (free tier) or local stand-ins; **AWS CLI** (optional early) | 12+ |
| IaC | **Terraform** | 13 |
| Kubernetes | **kubectl**; **kind** or **minikube**; YAML / Helm or Kustomize; **Argo CD** for GitOps in 16 | 14–16 |
| Course site | Modern browser; Node.js to preview the site locally (`cd site && npm start`); later modules use fillable quiz PDFs | 00 / whole course |
| Sample data | Module fixtures and stubs in-repo (no separate dataset download) | per module |

Official docs linked below. Prefer current stable releases unless a module README pins a version.

---

## Core installs (do these now)

### 1. Git

Why: every module is a git-tracked lab; without Git you cannot pull fixes or keep `my-work/` history separate from course stubs.

- Windows: [Git for Windows](https://git-scm.com/download/win)
- macOS: [Git downloads](https://git-scm.com/download/mac) or `xcode-select --install`
- Linux: distro packages — e.g. `sudo apt install git` (Debian/Ubuntu)

**Check:** `git --version`

### 2. Python 3.11+ (or current stable 3.x)

Why: Challenge Gym and most identity/email katas are Python-first; an old or Store-alias interpreter breaks `venv` and pytest.

- Windows / macOS / source: [python.org downloads](https://www.python.org/downloads/)
- macOS (Homebrew): `brew install python`
- Linux: distro `python3` / `python3-venv` / `python3-pip`

On Windows installer, enable **Add python.exe to PATH**.

**Check:**

```bash
python3 --version   # Windows: py -3 --version  (or python --version)
python3 -m pip --version
```

On Windows use `py -3` (or `python`) instead of `python3`; `python3` may open the Microsoft Store alias.

### 3. Virtualenv + Challenge Gym deps

Why: a project `.venv` keeps course packages (`pyotp`, `cryptography`, pytest) off the system Python so CI and classmates get the same import graph.

From the course repo:

```bash
cd 01-challenge-gym
python3 -m venv .venv
# Windows PowerShell: py -3 -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
#   If activation is blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
# Windows cmd.exe: .venv\Scripts\activate.bat
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

(Expect failing tests until you implement katas — the important part is that `pytest` runs. Why run it now: proves the toolchain, not that solutions exist yet.)

**Check:** `pytest --version`

### 4. Code editor

Any editor is fine (VS Code, Cursor, Neovim, etc.). Install a Python extension if you use VS Code/Cursor.

### 5. PDF reader for quizzes

Use a reader that can fill AcroForm PDFs (many browsers work; Preview / Adobe Reader / Okular also fine). Blank quiz PDFs are already under `my-work/quizzes/` — answer them in place.

---

## Install when you reach that module

### Node.js (Modules 08, 17)

- [Node.js LTS downloads](https://nodejs.org/)

**Check:** `node --version` · `npm --version`

### Go (Module 09)

- [Go install](https://go.dev/doc/install)

**Check:** `go version`

### Docker + Compose (Modules 13–14)

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS) or [Docker Engine](https://docs.docker.com/engine/install/) (Linux)

**Check:** `docker --version` · `docker compose version`

### Terraform (Module 13)

- [HashiCorp Terraform installs](https://developer.hashicorp.com/terraform/install)

**Check:** `terraform version`

### kubectl + kind or minikube (Modules 14–16)

- [kubectl install](https://kubernetes.io/docs/tasks/tools/)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) or [minikube](https://minikube.sigs.k8s.io/docs/start/)

**Check:** `kubectl version --client` · `kind version` or `minikube version`

### GitHub + AWS (Modules 12+)

- [GitHub signup](https://github.com/signup)
- [AWS free tier](https://aws.amazon.com/free/) (or local stand-ins such as LocalStack/MinIO when a module allows)
- Optional: [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) — `aws --version`

Never commit cloud secrets. Module READMEs describe least-privilege demos.

---

## OS tips

| OS | Notes |
|----|--------|
| **Windows** | Prefer PowerShell or Git Bash; WSL2 is excellent for Python/Docker/kind. |
| **macOS** | Homebrew simplifies Git, Python, Go, Terraform, kubectl. |
| **Linux** | Use your distro packages for Git/Python; follow upstream docs for Docker/Terraform/kind. |

---

## Final setup checklist

Confirm each item before marking Module 00 complete:

1. `git --version` works  
2. `python3 --version` (Windows: `py -3 --version`) shows 3.11+ (or current stable 3.x)  
3. `python3 -m venv` (Windows: `py -3 -m venv`) works; Challenge Gym venv installs `requirements.txt`  
4. `pytest --version` works inside that venv  
5. Editor + Git configured; you can commit  
6. Browser opens the course site  
7. You know *when* to add Node, Go, Docker, Terraform, kubectl/kind, GitHub, and AWS  

Then mark Module 00 complete in the site progress UI. Next are short **language/tool primers** (Bash, then Python) before Module 01 — read-only like this setup module. Later primers appear immediately before the first module that uses that tool (SQL, TypeScript/Vue, Go, Docker, GitHub Actions, Terraform, Kubernetes YAML, Svelte).
