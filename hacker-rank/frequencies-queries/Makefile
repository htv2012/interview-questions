.PHONY: all test run lint py clean watch

### Default target(s)
all: test

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	uv run main.py

### Run unit tests
test: lint
	uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .

### Start a Python shell
py:
	uv run ipython

### Watch for source changes and runt tests
watch:
	uv run ptw -v
