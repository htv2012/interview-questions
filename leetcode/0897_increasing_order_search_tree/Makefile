quick: lint
	PYTHONPATH=../common pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=../common pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=../common pytest -s -vv . ../common

lint: format
	ruff check . ../common --fix

format:
	ruff format . ../common
	ruff check --select I --fix . ../common

cp:
	grep --color=never -E -v 'from (nary_tree|tree|list_node) import' solution.py | xsel -b