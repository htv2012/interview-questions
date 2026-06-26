.PHONY: all lab lint py test

### Default target(s)
all: test

### Perform static analysis
lint:
	PYTHONPATH=../common uv run ruff check --select I --fix . --quiet
	PYTHONPATH=../common uv run ruff format . --quiet
	PYTHONPATH=../common uv run ruff check . --fix --quiet


### Run unit tests
test: lint
	PYTHONPATH=../common uv run pytest -s -v

### Start a Python interpreter
py:
	PYTHONPATH=../common uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab

