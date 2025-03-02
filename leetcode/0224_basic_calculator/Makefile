test: lint
	# PYTHONPATH=../common pytest -s -vv test_convert.py
	PYTHONPATH=../common pytest -x -s -vv

lint: format
	ruff check . --fix

format:
	black *.py
	isort .
