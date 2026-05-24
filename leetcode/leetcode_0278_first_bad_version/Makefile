.PHONY: all lab lint py run test

### Default target(s)
all: test


### Perform static analysis
lint:
	uv run ruff check --select I --fix . --quiet
	uv run ruff format . --quiet
	uv run ruff check . --fix --quiet
	uv run ty check .

### Run unit tests
test: lint
	uv run pytest -s -vv


### Start a Python interpreter
py:
	uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab

