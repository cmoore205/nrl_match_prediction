FROM python:3.12-slim

## Disables buffering so output is written immediately as it happens
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN pip install --no-cache-dir uv

## Installing dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY src ./src
RUN uv sync --frozen --no-dev

EXPOSE 8000
CMD ["uv", "run", "gunicorn", "nrl.api.main:app", \
     "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]