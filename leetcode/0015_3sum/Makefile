test: lint
	pytest -vs

lint: format
	ruff . --fix

format:
	black *.py
	isort .

