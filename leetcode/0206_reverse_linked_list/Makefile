test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff . --fix

format:
	ruff format .
	ruff check --select I --fix .