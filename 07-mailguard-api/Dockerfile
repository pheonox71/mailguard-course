# Local/demo image for Module 13 Compose (`mailguard-api:local`).
# Build from this module directory:
#   docker build -t mailguard-api:local .
#
# Default target (`base`) ships katas/ only — solutions/ never enter image layers.
# For demos before the kata is implemented, build the solutions stage:
#   docker build --target with-solutions -t mailguard-api:local .
FROM python:3.12-slim AS base

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY starter ./starter
COPY katas ./katas

ENV MAILGUARD_USE_SOLUTIONS=0
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "starter.app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Explicit opt-in stage: solutions/ exist only in this target's layers.
FROM base AS with-solutions
COPY solutions ./solutions
ENV MAILGUARD_USE_SOLUTIONS=1

# Default build target = student image without solutions.
FROM base
