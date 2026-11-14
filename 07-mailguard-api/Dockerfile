# Local/demo image for Module 13 Compose (`mailguard-api:local`).
# Build from this module directory:
#   docker build -t mailguard-api:local .
#
# Default image ships katas/ only (student stubs). For demos before the kata
# is implemented, include the reference engine:
#   docker build --build-arg INCLUDE_SOLUTIONS=1 -t mailguard-api:local .
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY starter ./starter
COPY katas ./katas
COPY solutions ./solutions

# Drop solutions/ from the final image unless explicitly requested.
# (Build layers still see the COPY; the running image filesystem will not
# contain /app/solutions when INCLUDE_SOLUTIONS is unset/0.)
ARG INCLUDE_SOLUTIONS=0
RUN if [ "$INCLUDE_SOLUTIONS" != "1" ]; then rm -rf /app/solutions; fi
# "0" keeps the default kata import; only "1" enables solutions fallback.
ENV MAILGUARD_USE_SOLUTIONS=${INCLUDE_SOLUTIONS}

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "starter.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
