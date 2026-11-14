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
5. Never bake cloud keys into `ENV` or `ARG` layers — use Compose `environment` / secrets mounts at **runtime**, and BuildKit **`RUN --mount=type=secret`** for any **build-time** credential (private indexes, etc.).

```text
docker build (07) → mailguard-api:local   # Module 14 kind labs also use :local-dev
docker build (09) → mailguard-worker:local
compose up → api + db (+ optional queue) → curl /healthz
```

### Worked example

```bash
# From repo root
# Default API image uses katas/ only (no solutions/ in the image).
# /healthz works either way; /evaluate needs your kata implemented.
docker build -t mailguard-api:local ./07-mailguard-api
docker build -t mailguard-worker:local ./09-mailguard-worker
cd 13-infra/starter && docker compose up -d
curl -s http://127.0.0.1:8000/healthz
# → {"status":"ok"}

# Optional: demo /evaluate before finishing Module 07 — with-solutions stage:
# docker build --target with-solutions -t mailguard-api:local ./07-mailguard-api
```

### Common misconceptions / what goes wrong

- **“Compose will pull `mailguard-api:local` from a registry.”** `:local` is a laptop tag — you must build it.
- **“Put AWS keys in the Dockerfile for convenience.”** Layers leak; use runtime env / IAM roles instead.
- **“`ARG` is safe because it is not `ENV`.”** Build args still leak via history/cache — use BuildKit `--secret` mounts (see Module 11a).
- **“Worker image must call cloud SQS on first boot.”** Local queue (**ElasticMQ** default in Module 09; LocalStack optional) is enough for the demo path.
- **“The default API image includes `solutions/`.”** It does not — Module 07’s Dockerfile uses a multi-stage build so the default target never copies `solutions/` (a `COPY` then `rm` would still leave answers in earlier layers). Use `--target with-solutions` only when you intentionally want the reference rules engine.

### BuildKit secret mount (shape)

```dockerfile
# syntax=docker/dockerfile:1
RUN --mount=type=secret,id=npm_token \
    NPM_TOKEN="$(cat /run/secrets/npm_token)" npm ci
```

```bash
DOCKER_BUILDKIT=1 docker build --secret id=npm_token,src=./.npm_token_local .
# Never commit the secret file; never use ARG/ENV for the same value.
```


## Videos (verified)

1. **[Docker Tutorial for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)**  
   Why it helps: build tags used by Compose.

## Read these (verified)

1. [Docker — Build images](https://docs.docker.com/build/)
2. [BuildKit — Build-time secrets](https://docs.docker.com/build/building/secrets/)
3. Module 11a Docker primer
4. [`../starter/docker-compose.yml`](../starter/docker-compose.yml)

## Next step

Build both images, then continue the IAM / Terraform assignment.
