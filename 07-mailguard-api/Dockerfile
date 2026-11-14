# Local/demo image for Module 13 Compose (`mailguard-api:local`).
# Build from this module directory:
#   docker build -t mailguard-api:local .
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY starter ./starter
COPY solutions ./solutions
COPY katas ./katas

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "starter.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
