test: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	PYTHONPATH=../common ruff check . --fix

format:
	PYTHONPATH=../common black *.py
	PYTHONPATH=../common isort .
