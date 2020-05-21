.PHONY: tests hooks

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

install: clean
	poetry install

hooks:
	poetry run pre-commit install

fmt:
	@poetry run isort -rc {{ cookiecutter.project_slug }} tests
	@poetry run black {{ cookiecutter.project_slug }} tests

lint:
	@poetry run flakehell lint {{ cookiecutter.project_slug }} tests
	@poetry run isort -rc --check-only {{ cookiecutter.project_slug }} tests
	@poetry run black --check {{ cookiecutter.project_slug }} tests
	@poetry export --dev --format=requirements.txt --without-hashes | poetry run safety check --stdin

mypy:
	@poetry run mypy {{ cookiecutter.project_slug }} tests

tests:
	poetry run pytest --verbose tests

coverage:
	poetry run pytest --verbose --cov-report term --cov-report html --cov={{ cookiecutter.project_slug }} tests
