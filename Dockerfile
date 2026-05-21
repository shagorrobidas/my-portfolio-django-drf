# =========================
# 1. BUILDER STAGE
# =========================
FROM python:3.12-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps ONLY for build
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    pkg-config \
    libcairo2-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies in venv-style isolation
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# =========================
# 2. RUNTIME STAGE
# =========================
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Runtime dependencies ONLY (lighter)
RUN apt-get update && apt-get install -y \
    libpq5 \
    libcairo2 \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy wheels and install
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy project
COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]