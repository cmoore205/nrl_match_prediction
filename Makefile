.PHONY: up down logs test lint fmt train

up:
	docker compose up --build -d

down: 
	docker compose down

build:
	docker compose --profile jobs build

logs:
	docker compose logs -f api

ps:
	docker compose ps -a

shell: ## open shell inside API container
	docker compose exec api bash

ingest:
	docker compose run --rm ingest

predict:
	docker compose run --rm predict

train:
	docker compose run --rm train

score:
	docker compose run --rm score

test:
	uv run pytest

lint:
	uv run ruff check . && uv run mypy src

fmt: 		## auto-format
	uv run ruff format .
