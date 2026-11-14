# Local/demo image for Module 13 Compose / Module 14 kind (`mailguard-api:local-dev`).
# Build from this module directory:
#   docker build -t mailguard-api:local-dev .
#
# Default target (`base`) ships katas/ only — solutions/ never enter image layers.
# For demos before the kata is implemented, build the solutions stage:
#   docker build --target with-solutions -t mailguard-api:local-dev .
FROM python:3.12-slim AS base

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY starter ./starter
COPY katas ./katas

# Non-root for Pod Security Standards restricted (Module 14 runAsUser 10001).
RUN useradd -u 10001 -r -s /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app
USER 10001

ENV MAILGUARD_USE_SOLUTIONS=0
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "starter.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Explicit opt-in stage: solutions/ exist only in this target's layers.
FROM base AS with-solutions
USER root
COPY solutions ./solutions
RUN chown -R appuser:appuser /app/solutions
USER 10001
ENV MAILGUARD_USE_SOLUTIONS=1

# Default build target = student image without solutions.
FROM base
