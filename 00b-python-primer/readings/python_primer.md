# Python primer

**Why this matters.** MailGuard’s identity, email-auth, API, and capstone labs are Python-first. Without a working interpreter, venv, and pytest habit, Challenge Gym cannot prove the “how” behind TOTP, holds, and rules. On the job, the same loop — isolate deps, let tests define the contract — is how teams ship auth and email-security glue without “works on my machine.”

**How it works.** You isolate deps in a **virtual environment**, install from `requirements.txt`, implement stubs under `katas/`, and let **pytest** define the contract. That loop (read test → write code → re-run) is the course’s core practice: fail first, then make the stub match the spec.

This primer has no assignment, quiz, or download pack.

---

## What Python is

**Python** is a high-level language widely used for APIs, automation, and security tooling. This course targets **Python 3.11+** (or current stable 3.x).

## Why industry uses it

Teams choose Python for fast iteration on auth, data, and glue code: readable modules, rich libraries (`cryptography`, web frameworks), and excellent test ergonomics. Cloud-security prototypes often start here before hardening.

## Key concepts for Module 01+

| Concept | Why you care |
|---------|----------------|
| `venv` | Keeps course deps from fighting system Python |
| `pip install -r requirements.txt` | Reproducible lab installs |
| functions + type hints (light) | Clear kata stubs |
| `pytest` | Tests are the spec — fail first, then implement |

## Install and run

Follow Module 00 if needed, then:

```bash
# Why: confirm 3.x, then isolate this primer’s deps from system site-packages
python3 --version   # Windows: py -3 --version
python3 -m venv /tmp/mg-py-primer && source /tmp/mg-py-primer/bin/activate
# Windows PowerShell: py -3 -m venv .venv ; .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Official install: [python.org downloads](https://www.python.org/downloads/).

## Tiny hands-on example

```bash
cat > /tmp/mg_hello.py << 'EOF'
def hold_reason(score: int) -> str:
    # Why: small pure function — easy to unit test later
    return "hold" if score >= 80 else "allow"

if __name__ == "__main__":
    print(hold_reason(90))
EOF
python /tmp/mg_hello.py
```

**How:** A pure function returns a decision string — the same shape as later hold-rule katas, without frameworks yet.

## Official docs

1. [Python 3 tutorial](https://docs.python.org/3/tutorial/)
2. [venv docs](https://docs.python.org/3/library/venv.html)
3. [pytest documentation](https://docs.pytest.org/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`01-challenge-gym`).

This primer has **no** assignment, quiz, or download pack.
