run: lint
	uv run pytest -s -vv

lint:
	uv run ruff check . --fix
	uv run ruff format . 
	uv run ruff check --select I --fix . 

