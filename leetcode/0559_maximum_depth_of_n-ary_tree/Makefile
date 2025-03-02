quick: lint
	PYTHONPATH=../common pytest -s -vv -m 'not slow' . ../common

slow: lint
	PYTHONPATH=../common pytest -s -vv -m 'slow' . ../common

all: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff check . ../common --fix

format:
	ruff format . ../common
	ruff check --select I --fix . ../common
