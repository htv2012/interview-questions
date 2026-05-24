.PHONY: all clean install lab lint py run test

all: test

### Run unit tests
test: lint
	uv run pytest -s -vv

### Perform static analysis
lint:
	uv run ruff check . --fix
	uv run ruff format . 
	uv run ruff check --select I --fix . 
	uv run ty check .


### Start a Python interpreter
py:
	uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab

