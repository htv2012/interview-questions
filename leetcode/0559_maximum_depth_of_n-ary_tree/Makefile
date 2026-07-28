quick: lint
	PYTHONPATH=../../_common pytest -s -vv -m 'not slow' . ../../_common

slow: lint
	PYTHONPATH=../../_common pytest -s -vv -m 'slow' . ../../_common

all: lint
	PYTHONPATH=../../_common pytest -s -vv

lint: format
	ruff check . ../.._common --fix

format:
	ruff format . ../.._common
	ruff check --select I --fix . ../../_common
