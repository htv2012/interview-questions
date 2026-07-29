quick: lint
	PYTHONPATH=../../_common pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=../../_common pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=../../_common pytest -s -vv . ../../_common

lint: format
	ruff check . ../.._common --fix

format:
	ruff format . ../.._common
	ruff check --select I --fix . ../../_common
