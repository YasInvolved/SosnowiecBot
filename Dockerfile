# FROM python:3.14-slim as base

# WORKDIR /app

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .
# CMD ["python", "main.py"]

FROM python:3.14-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
COPY requirements.txt .

ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.14-slim AS runner
WORKDIR /app

RUN groupadd -g 10001 runnerusr && \
    useradd -u 10001 -g runnerusr -m -s /bin/bash runnerusr

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

USER runnerusr
COPY --chown=runnerusr:runnerusr . .

CMD ["python", "main.py"]