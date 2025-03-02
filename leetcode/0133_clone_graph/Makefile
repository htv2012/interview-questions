test: lint
	PYTHONPATH=../common pytest -s -vv

lint:
	ruff check --select I --fix . ../common
	ruff check . --fix . ../common

sandbox:
	PYTHONPATH=../common python -i sandbox.py
