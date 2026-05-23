quick: lint
	PYTHONPATH=.. pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=.. pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=.. pytest -s -vv . ../common

lint: format
	ruff check . ../common --fix

format:
	ruff format . ../common
	ruff check --select I --fix . ../common

cp:
	grep --color=never -E -v '^from (common|nary_tree|tree|list_node)' solution.py | xsel -b
