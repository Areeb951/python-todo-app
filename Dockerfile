# ---------- Stage 1: Build & Test ----------
FROM python:3.10-slim AS test

WORKDIR /app

# Install app dependencies + test dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt pytest

COPY . .

# Run tests when explicitly executed
CMD ["pytest", "test_api.py"]

# ---------- Stage 2: Production ----------
FROM python:3.10-slim AS prod

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
