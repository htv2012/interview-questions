test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff check . --fix

format:
	black *.py
	isort .

sandbox:
	PYTHONPATH=../common python -i sandbox.py
