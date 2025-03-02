target: clean quick

clean:
	-tmp /tmp/snoop
	
token:
	PYTHONPATH=../common pytest -s -vv test_tokenize.py

dbg:
	-rm /tmp/snoop.txt
	-PYTHONPATH=../common pytest -s -vv 'test_solution.py::test_solution[wrong 2]'
	bat /tmp/snoop.txt

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
