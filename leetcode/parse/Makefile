sample := sample0957.txt

run: lint
	@echo "-----"
	cat $(sample)
	@echo "-----"
	python3 make_testcases.py $(sample) | bat -l python

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

sandbox: lint
	python -i sandbox.py