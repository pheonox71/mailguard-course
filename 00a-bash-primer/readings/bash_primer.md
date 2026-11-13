# Bash / shell primer

**Why this matters.** Almost every MailGuard lab starts in a terminal: create a venv, run `pytest`, call `go test`, or bring Compose up. Without shell fluency, the “how” of every later module stays blocked behind copy-paste.

**How it works.** A shell reads a line, expands variables/globs, then runs a program. Pipes (`|`) pass stdout of one command to stdin of the next. Environment variables configure tools without hard-coding secrets into files you might commit.

This primer has no assignment, quiz, or download pack — read, try the tiny example, mark complete, then continue.

---

## What Bash is

**Bash** (Bourne Again SHell) is a command language common on Linux/macOS. On Windows, **Git Bash**, **WSL**, or **PowerShell** cover the same lab ideas with slightly different syntax.

## Why industry uses it

Cloud and security work is automation-heavy: CI runners, remote bastions, and container entrypoints are shell-first. Guis help explore; shells make steps repeatable and reviewable in git.

## Key concepts for upcoming labs

| Concept | Why you care |
|---------|----------------|
| `cd` / paths | Every module README assumes you are in the right folder |
| `export VAR=…` | Tokens and API URLs stay out of source when possible |
| pipes / redirects | Compose logs, `pytest -q`, filtering output |
| exit codes | Scripts and CI fail when a command returns non-zero |

## Install / open a shell

- **macOS / Linux:** Terminal.app, iTerm, or your desktop terminal — Bash or zsh both work for this course.
- **Windows:** [Git for Windows](https://git-scm.com/download/win) (Git Bash), [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install), or PowerShell (`py -3`, `python`, etc. as Module 00 notes).

**Check:** `echo $SHELL` (Git Bash/WSL/macOS/Linux) or `$PSVersionTable` in PowerShell.

## Tiny hands-on example

```bash
# Why: confirm the shell runs commands and prints exit status
mkdir -p /tmp/mailguard-shell-demo && cd /tmp/mailguard-shell-demo
echo "hold" > decision.txt
grep -n hold decision.txt && echo "exit was $?"
```

**How:** `mkdir` creates a sandbox, `echo` writes a file, `grep` searches it, `$?` shows the last exit code — the same pattern CI uses to fail a job.

## Official docs

1. [GNU Bash manual](https://www.gnu.org/software/bash/manual/)
2. [Git for Windows](https://gitforwindows.org/)
3. [PowerShell docs](https://learn.microsoft.com/en-us/powershell/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`01-challenge-gym`).

This primer has **no** assignment, quiz, or download pack.
