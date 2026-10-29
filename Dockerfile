
# ---------- build stage ----------
FROM python:3.11.9-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- runtime stage ----------
FROM python:3.11.9-slim

# Security: run as non-root
RUN groupadd -r vulntrack && useradd -r -g vulntrack -s /usr/sbin/nologin vulntrack

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY app/ .

# Own the workdir so the app can create the SQLite file
RUN chown -R vulntrack:vulntrack /app

USER vulntrack

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]