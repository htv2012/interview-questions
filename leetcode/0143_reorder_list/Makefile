target: clean quick

clean:
	-rm /tmp/snoop.txt

quick: lint
	PYTHONPATH=../common pytest -s -vv -m 'not slow'

slow: lint
	PYTHONPATH=../common pytest -s -vv -m 'slow'

all: lint
	PYTHONPATH=../common pytest -s -vv

lint: format
	ruff check . --fix

format:
	ruff format .
	ruff check --select I --fix .
