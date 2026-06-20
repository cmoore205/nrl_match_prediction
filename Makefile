.PHONY: up down logs test lint fmt train

up:
	docker compose up --build -d

down: 
	docker compose down

logs:
	docker compose logs -f api

test:
	uv run pytest

lint:
	uv run ruff check . && uv run mypy src

fmt: 		## auto-format
	uv run ruff format .

#train: 		## train the model
	##TODO: add when I actually implement the model