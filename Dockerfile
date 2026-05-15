FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        libcairo2 \
        libffi-dev \
        pngquant \
        shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt requirements-dev.txt ./

RUN pip install --upgrade pip \
    && pip install -r requirements-dev.txt

EXPOSE 8000

CMD ["mkdocs", "serve", "--config-file", "docker.mkdocs.yml", "-a", "0.0.0.0:8000", "--dirty"]
