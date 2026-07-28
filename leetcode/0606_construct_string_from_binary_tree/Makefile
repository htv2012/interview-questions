test: lint
	PYTHONPATH=../common uv run pytest -s -vv 

lint: format
	uv run ruff check . ../common --fix

format:
	uv run ruff format . ../common
	uv run ruff check --select I --fix . ../common

cp:
	grep --color=never -E -v 'from (common|nary_tree|tree|list_node) import' solution.py | xsel -b
