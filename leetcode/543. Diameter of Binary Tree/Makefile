quick: lint
	PYTHONPATH=.. uv run pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=.. uv run pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=.. uv run pytest -s -vv . ../common

lint: format
	uv run ruff check . ../common --fix

format:
	uv run ruff format . ../common
	uv run ruff check --select I --fix . ../common

cp:
	grep --color=never -E -v '^from (common|nary_tree|tree|list_node)' solution.py | xsel -b
