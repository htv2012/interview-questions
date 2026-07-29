target: quick

sandbox:
	python -i sandbox.py

quick: lint
	PYTHONPATH=../../_common pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=../../_common pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=../../_common pytest -s -vv

lint: format
	ruff check . --fix

format:
	ruff format .
	ruff check --select I --fix .
