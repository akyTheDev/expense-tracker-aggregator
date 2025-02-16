SHELL=/bin/bash
.DEFAULT_GOAL := default

.PHONY: install
install:
	@echo "Installing production dependencies..."
	pip install poetry
	poetry install --without dev

.PHONY: install-dev
install-dev:
	@echo "Installing dev dependencies..."
	pip install poetry
	poetry install

.PHONY: lint
lint:
	poetry run ruff check . --fix

.PHONY: format
format:
	poetry run ruff format . --check

.PHONY: coverage
coverage:
	@echo "Test coverage."
	bash scripts/test.sh

.PHONY: run
run:
	@echo "Running the application."
	poetry run python src/main.py
