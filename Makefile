shell:
	poetry shell

install:
	poetry install --no-root

reqs-update:
	poetry update

black: shell
	black .

isort: shell
	isort .

lint: black isort
	autopep8 --in-place --aggressive --aggressive -r .

test: lint
	pytest

docs-update:
	rm -rf docs
	pdoc -o docs eng_econ

build: test doc-update
	poetry build