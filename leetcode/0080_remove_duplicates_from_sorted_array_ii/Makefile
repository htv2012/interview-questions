quick: lint
	PYTHONPATH=../common pytest -s -vv --strict-markers -m 'not slow'

slow: lint
	PYTHONPATH=../common pytest -s -vv --strict-markers -m slow

all: lint
	PYTHONPATH=../common pytest -s -vv --strict-markers

lint: format
	ruff check . --fix

format:
	ruff format .
	ruff check --select I --fix .
