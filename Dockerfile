############################
# 1️⃣ Builder Stage
############################
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        gcc \
        libpq-dev \
        make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


############################
# 2️⃣ Runtime Stage
############################
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        gettext \
        libpq5 \
        make \
    && rm -rf /var/lib/apt/lists/*

# Install jprq
RUN curl -fsSL https://jprq.io/install.sh | bash

# Install Python dependencies
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy project
COPY . .

# Ensure scripts executable
RUN chmod +x entrypoint.sh start.sh

# Optional static collection
RUN python manage.py collectstatic --noinput || true

EXPOSE 1034

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]
CMD ["bash", "start.sh"]
