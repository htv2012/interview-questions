.PHONY: all test run lint

test: lint
	uv run pytest -vv -s

lint:
	#uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix

edit:
	nvim -p *.py
	$(MAKE) test
