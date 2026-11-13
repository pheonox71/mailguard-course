# Course setup — tools for the MailGuard path

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

- Windows: [Git for Windows](https://git-scm.com/download/win)
- macOS: [Git downloads](https://git-scm.com/download/mac) or `xcode-select --install`
- Linux: distro packages — e.g. `sudo apt install git` (Debian/Ubuntu)

**Check:** `git --version`

### 2. Python 3.11+ (or current stable 3.x)

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

(Expect failing tests until you implement katas — the important part is that `pytest` runs.)

**Check:** `pytest --version`

### 4. Code editor

Any editor is fine (VS Code, Cursor, Neovim, etc.). Install a Python extension if you use VS Code/Cursor.

### 5. PDF reader for quizzes

Use a reader that can fill AcroForm PDFs (many browsers work; Preview / Adobe Reader / Okular also fine). Save finished PDFs under `my-work/quizzes/`.

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

Then mark Module 00 complete in the site progress UI and start Module 01.
