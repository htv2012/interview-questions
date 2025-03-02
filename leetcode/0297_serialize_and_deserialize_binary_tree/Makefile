test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff check . --fix

format:
	black *.py
	isort .

sandbox:
	PYTHONPATH=../common python3 -i sandbox.py