# Python primer

**Why this matters.** MailGuard’s identity, email-auth, API, and capstone labs are Python-first. Without a working interpreter, venv, and pytest habit, Challenge Gym cannot prove the “how” behind TOTP, holds, and rules. On the job, the same loop — isolate deps, let tests define the contract — is how teams ship auth and email-security glue without “works on my machine.”

**How it works.**

1. Confirm a Python 3.11+ (or current stable 3.x) interpreter.
2. Create and activate a **virtual environment** so deps stay off the system Python.
3. Install from `requirements.txt` with `pip`.
4. Read the failing pytest for a kata stub under `katas/`.
5. Implement until the test passes; re-run often. That loop (read test → write code → re-run) is the course’s core practice: fail first, then make the stub match the spec.

### Worked example

```bash
python3 -m venv /tmp/mg-py-primer && source /tmp/mg-py-primer/bin/activate
python - <<'PY'
def hold_reason(score: int) -> str:
    return "hold" if score >= 80 else "allow"
print(hold_reason(90))  # → hold
PY
```

A pure function returning a decision string is the same shape as later hold-rule katas, without frameworks yet.

### Common misconceptions / what goes wrong

- **“I’ll install packages globally to save time.”** Global site-packages drift from CI and classmates; always use a venv for course work.
- **“Green means I understand the crypto/auth.”** Tests are the contract for the stub — still read the Why/How in each module so you can explain the mechanism in an interview.
- **“Type hints are optional fluff.”** Light hints in kata stubs document the expected shapes; ignoring them often causes the first confusing pytest failures.

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


## Videos (verified)

1. **[Python for Beginners – Full Course](https://www.youtube.com/watch?v=eWRfhZAVOY8)**  
   Why it helps: venv/functions mindset before pytest katas.

## Official docs

1. [Python 3 tutorial](https://docs.python.org/3/tutorial/)
2. [venv docs](https://docs.python.org/3/library/venv.html)
3. [pytest documentation](https://docs.pytest.org/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`01-challenge-gym`).

This primer has **no** assignment, quiz, or download pack.
