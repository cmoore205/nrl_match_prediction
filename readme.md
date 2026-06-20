# NRL Match Prediction (Work in Progress)

A service that predicts the outcome of NRL (National Rugby League) matches. The goal is to 
include testing, observability, CI/CD functionality and for the app to eventually be deployed
on an AWS EC2 instance.

## Stack (so far)
FastAPI - PostgreSQL - SQLAlchemy/Alembic - Docker Compose

## Architecture 
TODO: Create architecture diagram

## Prerequisites
- Docker + Docker Compose
- Python 3.12+ and [uv](https:github.com/astral-sh/uv)

## Run locally
```bash
cp .env.example .env
make up
curl http://localhost:8000/health
```

## API Docs
Documentation is automatically generated with FastAPI.
Navigate to http://localhost:8000/docs

## Common Commands
| Command      | What it does                        |
|--------------|-------------------------------------|  
| `make up`    | build + start the stack             |
| `make down`  | stop the stack                      |
| `make logs`  | tail API logs                       |
| `make test`  | run tests (Not yet implemented)     |
| `make lint`  | ruff + mypy                         |