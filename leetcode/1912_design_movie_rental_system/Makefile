targets: clean quick

clean:
	-rm /tmp/movie.sqlite3

quick: lint
	pytest -s -vv -m 'not slow'

slow: lint
	pytest -s -vv -m 'slow'

all: lint
	pytest -s -vv

lint: format
	ruff check . --fix

format:
	ruff format .
	ruff check --select I --fix .
