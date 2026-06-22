.PHONY: all lab lint py test run

### Default target(s)
all: test run

### Perform static analysis
lint:
	uv run ruff check --select I --fix . --quiet
	uv run ruff format . --quiet
	uv run ruff check . --fix --quiet


### Run unit tests
test: lint
	uv run pytest -s -v

### Run sandbox, if available
run: lint
	uv run ipython -i solution.py
	
### Start a Python interpreter
py:
	uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab

