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
	coverage run --source=eng_econ -m pytest

docs-update:
	rm -rf docs
	pdoc --html -o docs eng_econ

coverage: test
	rm -rf htmlcov
	coverage html

build: install coverage docs-update
	poetry build

publish: build
	poetry publish --username __token__ --password $(password)