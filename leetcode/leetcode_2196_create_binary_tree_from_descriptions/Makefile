.PHONY: all lab lint py test

### Default target(s)
all: test

### Perform static analysis
lint:
	PYTHONPATH=../../_common uv run ruff check --select I --fix . --quiet
	PYTHONPATH=../../_common uv run ruff format . --quiet
	PYTHONPATH=../../_common uv run ruff check . --fix --quiet


### Run unit tests
test: lint
	PYTHONPATH=../../_common uv run pytest -s -v

### Start a Python interpreter
py:
	PYTHONPATH=../../_common uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab

