FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /workspace

COPY requirements.txt requirements-dev.txt ./

RUN pip install --upgrade pip \
    && pip install -r requirements-dev.txt

EXPOSE 8000

CMD ["zensical", "serve", "--config-file", "docker.mkdocs.yml", "-a", "0.0.0.0:8000"]
