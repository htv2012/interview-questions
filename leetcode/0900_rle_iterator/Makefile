test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff check . --fix

format:
	black *.py
	isort .

sandbox:
	python -i sandbox.py
