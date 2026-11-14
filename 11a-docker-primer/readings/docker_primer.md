# Docker primer

**Why this matters.** “Works on my machine” fails CI and demos. **Containers** package an app with its runtime so Module 12 image builds and Module 13 Compose demos look the same on every laptop. VMs can isolate too, but images are the usual unit security teams scan and CI rebuilds — baking secrets into layers is the anti-pattern to avoid.

**How it works.**

1. Write a **Dockerfile**: base image → install deps → copy app → set start command (each instruction is a **layer**).
2. `docker build` produces an **image** (layered filesystem + metadata).
3. `docker run` starts a **container** (running instance of that image).
4. **Compose** declares multi-service stacks (API + DB + mail dependencies) in YAML so `docker compose up` tells a story, not twelve manual steps.
5. Pass secrets at **runtime** (env / secret mounts) — never `ENV AWS_SECRET=…` in a layer. On the job, email/identity services ship as images from laptop → CI → cloud with the same artifact.

### Worked example

Layer idea for a tiny API image (conceptual):

```dockerfile
# Why: slim base keeps scan surface smaller
FROM python:3.12-slim
WORKDIR /app
# Why: copy requirements first so dependency layer caches when only app code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
# Why: secrets stay out of the image — inject at run time
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

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

### Common misconceptions / what goes wrong

- **“Containers are VMs.”** They share the host kernel; isolation model and patching story differ — still scan images.
- **“Bake credentials into the image for easier demos.”** Layers are extractable; use runtime env/secrets.
- **“Compose is only for production orchestration.”** Local Compose approximates topology; production may use other schedulers later (Module 13+).


## Videos (verified)

1. **[Docker Tutorial for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)**  
   Why it helps: images/containers before Compose demos.

## Official docs

1. [Docker overview](https://docs.docker.com/get-started/overview/)
2. [Docker Compose overview](https://docs.docker.com/compose/)
3. [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)

---

## Done when

You can explain **why** this tool shows up on the MailGuard path and **how** to install/run the tiny example. Mark this primer complete on the site, then continue to the next module (`12-ci-aws`).

This primer has **no** assignment, quiz, or download pack.
