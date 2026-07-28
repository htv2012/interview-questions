test: lint
	PYTHONPATH=../../_common pytest -s -vv

lint: format
	ruff . --fix

format:
	black *.py
	isort .
