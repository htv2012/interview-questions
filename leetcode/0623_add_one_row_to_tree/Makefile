quick: lint
	PYTHONPATH=.. pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=.. pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=.. pytest -s -vv . ../../_common

lint: format
	ruff check . ../.._common --fix

format:
	ruff format . ../.._common
	ruff check --select I --fix . ../../_common

cp:
	grep --color=never -E -v '^from (common|nary_tree|tree|list_node)' solution.py | xsel -b
