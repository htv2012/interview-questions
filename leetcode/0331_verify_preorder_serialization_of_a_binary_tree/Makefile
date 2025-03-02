quick: lint
	PYTHONPATH=../lib pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=../lib pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=../lib pytest -s -vv

lint: format
	ruff check . --fix

format:
	ruff format .
	ruff check --select I --fix .
