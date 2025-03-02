quick: lint
	PYTHONPATH=../common pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=../common pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=../common pytest -s -vv . ../common

lint: format
	ruff check . ../common --fix

format:
	ruff format . ../common
	ruff check --select I --fix . ../common

sandbox: lint
	PYTHONPATH=../common python -i sandbox.py