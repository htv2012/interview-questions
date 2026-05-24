.PHONY: all clean install lab lint py run test

all: test

### Perform static analysis
lint:
	uv run ruff check --select I --fix . --quiet
	uv run ruff format . --quiet
	uv run ruff check . --fix --quiet
# 	uv run ty check .

### Run unit tests
test: lint
	uv run pytest -s -vv

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Start a Python interpreter
py:
	uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab
