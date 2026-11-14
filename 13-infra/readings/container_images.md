# Reading — Building MailGuard images for Compose

## Learning objectives

1. Build local Docker images for the API (`07`) and worker (`09`).
2. Wire those tags into Module 13’s Compose story (`mailguard-api:local`).
3. Keep secrets out of image layers.

**Why this matters.** Compose referencing `mailguard-api:local` fails until you build that tag. Without a Dockerfile, “compose up demos the MailGuard story” stays aspirational. On the job, the same habit — pin tags, pass secrets at runtime — is how email/identity services move from laptop demos to CI.

**How it works.**

1. Build the API image from Module 07’s Dockerfile.
2. Build the worker image from Module 09’s Dockerfile.
3. Point Compose `image:` fields at those local tags (or `build:` contexts).
4. Confirm `/healthz` on the API container.
5. Never bake cloud keys into `ENV` layers — use Compose `environment` / secrets mounts.

```text
docker build (07) → mailguard-api:local
docker build (09) → mailguard-worker:local
compose up → api + db (+ optional queue) → curl /healthz
```

### Worked example

```bash
# From repo root
docker build -t mailguard-api:local ./07-mailguard-api
docker build -t mailguard-worker:local ./09-mailguard-worker
cd 13-infra/starter && docker compose up -d
curl -s http://127.0.0.1:8000/healthz
# → {"status":"ok"}
```

### Common misconceptions / what goes wrong

- **“Compose will pull `mailguard-api:local` from a registry.”** `:local` is a laptop tag — you must build it.
- **“Put AWS keys in the Dockerfile for convenience.”** Layers leak; use runtime env / IAM roles instead.
- **“Worker image must call cloud SQS on first boot.”** Local queue (LocalStack/ElasticMQ) is enough for the demo path.


## Videos (verified)

1. **[Docker Tutorial for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)**  
   Why it helps: build tags used by Compose.

## Read these (verified)

1. [Docker — Build images](https://docs.docker.com/build/)
2. Module 11a Docker primer
3. [`../starter/docker-compose.yml`](../starter/docker-compose.yml)

## Next step

Build both images, then continue the IAM / Terraform assignment.
