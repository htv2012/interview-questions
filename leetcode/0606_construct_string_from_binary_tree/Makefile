test: lint
	PYTHONPATH=../../_common uv run pytest -s -vv 

lint: format
	uv run ruff check . ../.._common --fix

format:
	uv run ruff format . ../.._common
	uv run ruff check --select I --fix . ../../_common

cp:
	grep --color=never -E -v 'from (common|nary_tree|tree|list_node) import' solution.py | xsel -b
