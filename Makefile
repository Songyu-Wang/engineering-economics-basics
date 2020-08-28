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

doc-update:
	rm -f DOCS.md
	pdoc --pdf eng_econ > DOCS.md

build: test doc-update
	poetry build