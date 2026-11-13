# Docker primer

**Why this matters.** “Works on my machine” fails CI and demos. **Containers** package an app with its runtime so Module 12 image builds and Module 13 Compose demos look the same on every laptop. VMs can isolate too, but images are the usual unit security teams scan and CI rebuilds — baking secrets into layers is the anti-pattern to avoid.

**How it works.** An **image** is a layered filesystem + start command. A **container** is a running instance. **Compose** declares multi-service stacks (API + DB + mail dependencies) in YAML so `docker compose up` tells a story, not twelve manual steps. On the job, email/identity services ship as images from laptop → CI → cloud with the same artifact.

This primer has no assignment, quiz, or download pack.

---

## What Docker is

**Docker** is a popular container toolchain (Engine/Desktop + CLI). **Docker Compose** orchestrates multiple containers locally.

## Why industry uses it

Identical artifacts from laptop → CI → cloud; fewer “missing library” incidents; security reviews can scan images. Local stacks approximate cloud topology without full accounts.

## Key concepts for Modules 12–13

| Concept | Why you care |
|---------|----------------|
| Image vs container | Build once, run many |
| Dockerfile (awareness) | CI may build an image for a service you own |
| Compose services | MailGuard demo wiring |
| No secrets in images | Pass env at runtime; never bake cloud keys into layers |

## Install and run

- macOS / Windows: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Linux: [Docker Engine install](https://docs.docker.com/engine/install/)

**Check:** `docker --version` · `docker compose version` — **why:** confirm Engine + Compose plugins before Module 12/13, so “command not found” is not your first CI failure.

## Tiny hands-on example

```bash
# Why: prove the daemon runs without pulling a whole MailGuard stack yet
docker run --rm hello-world
```

**How:** The CLI pulls (if needed) a tiny image, starts a container, prints a confirmation message, and removes it (`--rm`) — the same pull/run lifecycle CI uses.

## Official docs

1. [Docker overview](https://docs.docker.com/get-started/overview/)
2. [Docker Compose overview](https://docs.docker.com/compose/)
3. [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`12-ci-aws`).

This primer has **no** assignment, quiz, or download pack.
