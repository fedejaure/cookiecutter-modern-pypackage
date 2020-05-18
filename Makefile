BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"
	@echo "watch 	generate project using defaults and watch for changes"
	@echo "replay 	replay last cookiecutter run and watch for changes"

clean: clean-pyc clean-test

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -fr htmlcov/
	@rm -fr .pytest_cache

bake:
	poetry run cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake
	poetry run watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/

replay: BAKE_OPTIONS=--replay
replay: watch
	;

lint:
	@poetry run flakehell lint tests
	@poetry run isort -rc --check-only tests
	@poetry run black --check tests

fmt:
	@poetry run isort -rc tests
	@poetry run black tests

test:
	poetry run py.test --verbose tests

install: clean
	poetry install

hooks:
	poetry run pre-commit install
