test: lint
	PYTHONPATH=../leetcode_common pytest -s -vv

lint: format
	ruff . --fix

format:
	black *.py
	isort .

