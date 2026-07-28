test: lint
	PYTHONPATH=../../_common pytest -s -vv

lint: format
	ruff check . --fix

format:
	black *.py
	isort .

sandbox:
	PYTHONPATH=../../_common python -i sandbox.py
