BAKE_OPTIONS=--no-input

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@echo "bake 	generate project using defaults"
	@echo "watch 	generate project using defaults and watch for changes"
	@echo "replay 	replay last cookiecutter run and watch for changes"

clean: clean-pyc clean-test

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	rm -fr htmlcov/
	rm -fr .pytest_cache

bake:
	poetry run cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake
	poetry run watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/

replay: BAKE_OPTIONS=--replay
replay: watch
	;

lint:
	@poetry run flakehell lint \{\{cookiecutter.project_slug\}\} tests
	@poetry run isort -rc --check-only \{\{cookiecutter.project_slug\}\} tests
	@poetry run black --check \{\{cookiecutter.project_slug\}\} tests

fmt:
	@poetry run isort -rc \{\{cookiecutter.project_slug\}\} tests
	@poetry run black \{\{cookiecutter.project_slug\}\} tests

test:
	@poetry run py.test --verbose tests

coverage:
	@poetry run py.test --verbose --cov-report term --cov-report html --cov=tests tests
	$(BROWSER) htmlcov/index.html

dev: clean
	poetry install
	poetry run pre-commit install

install: clean
	poetry install --no-dev
