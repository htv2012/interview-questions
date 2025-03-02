test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff check . --fix

format:
	ruff format .
	ruff check --select I --fix .

sandbox:
	PYTHONPATH=../common python -i sandbox.py
