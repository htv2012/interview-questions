test: lint
	PYTHONPATH=../../_common pytest -s -vv

lint: format
	PYTHONPATH=../../_common ruff check . --fix

format:
	PYTHONPATH=../../_common black *.py
	PYTHONPATH=../../_common isort .
