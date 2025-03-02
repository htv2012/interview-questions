test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff . --fix

format:
	black *.py
	isort .
